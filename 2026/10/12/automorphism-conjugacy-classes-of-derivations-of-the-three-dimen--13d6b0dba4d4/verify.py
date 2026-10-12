"""Direct finite-field checks for derivation-conjugacy orbit classification.

Run with Python 3: python verify.py
The proof of the infinite-field family is mathematical, not the enumeration.
"""
from itertools import product
from collections import Counter

CASES = {2:(2,(0,1)),3:(3,(0,1)),4:(2,(1,1,1)),5:(5,(0,1)),7:(7,(0,1)),8:(2,(1,1,0,1)),9:(3,(1,0,1))}

class Field:
    def __init__(self,q):
        self.q=q
        self.p,self.mod=CASES[q]
        self.k=len(self.mod)-1
        assert self.p**self.k==q
        self.add=[[self._binary(a,b,False) for b in range(q)] for a in range(q)]
        self.mul=[[self._binary(a,b,True) for b in range(q)] for a in range(q)]
        self.neg=[next(b for b in range(q) if self.add[a][b]==0) for a in range(q)]
        self.inv=[None]+[next(b for b in range(1,q) if self.mul[a][b]==1) for a in range(1,q)]
    def digits(self,n):
        d=[]
        for _ in range(self.k):d.append(n%self.p);n//=self.p
        return d
    def encode(self,d):return sum(z*self.p**i for i,z in enumerate(d))
    def _binary(self,a,b,times):
        x=self.digits(a);y=self.digits(b)
        if not times:return self.encode([(i+j)%self.p for i,j in zip(x,y)])
        out=[0]*(2*self.k-1)
        for i in range(self.k):
            for j in range(self.k):out[i+j]=(out[i+j]+x[i]*y[j])%self.p
        for d in range(2*self.k-2,self.k-1,-1):
            coeff=out[d]
            for j in range(self.k):out[d-self.k+j]=(out[d-self.k+j]-coeff*self.mod[j])%self.p
        return self.encode(out[:self.k])
    def A(self,a,b):return self.add[a][b]
    def N(self,a):return self.neg[a]
    def S(self,a,b):return self.add[a][self.neg[b]]
    def M(self,a,b):return self.mul[a][b]
    def D(self,a,b):return self.mul[a][self.inv[b]]
    def scalar(self,m):return m%self.p


def deriv(F,a,b,c):
    return ((a,0,0),(b,F.M(2%F.p,a),0),(c,b,F.M(3%F.p,a)))


def autom(F,h,t,u):
    return ((h,0,0),(t,F.M(h,h),0),(u,F.M(h,t),F.M(F.M(h,h),h)))


def mm(F,X,Y):
    return tuple(tuple(F.A(F.A(F.M(X[i][0],Y[0][j]),F.M(X[i][1],Y[1][j])),F.M(X[i][2],Y[2][j])) for j in range(3)) for i in range(3))


def det3(F,X):
    terms=[F.M(X[0][j],F.S(F.M(X[1][(j+1)%3],X[2][(j+2)%3]),F.M(X[1][(j+2)%3],X[2][(j+1)%3]))) for j in range(3)]
    # above cyclic minor orientation alternates, use generic permutation sign
    import itertools
    ans=0
    for pp in itertools.permutations(range(3)):
        z=F.M(F.M(X[0][pp[0]],X[1][pp[1]]),X[2][pp[2]])
        if sum(pp[i]>pp[j] for i in range(3) for j in range(i+1,3))%2:z=F.N(z)
        ans=F.A(ans,z)
    return ans


def invmat(F,X):
    rows=[list(X[i])+[int(i==j) for j in range(3)] for i in range(3)]
    for i in range(3):
        pivot=next(j for j in range(i,3) if rows[j][i]!=0)
        rows[pivot],rows[i]=rows[i],rows[pivot]
        z=F.inv[rows[i][i]]
        rows[i]=[F.M(z,v) for v in rows[i]]
        for j in range(3):
            if j!=i:
                z=rows[j][i]
                rows[j]=[F.S(rows[j][k],F.M(z,rows[i][k])) for k in range(6)]
    return tuple(tuple(rows[i][j+3] for j in range(3)) for i in range(3))


def bracket(F,x,y):
    return (0,F.M(x[0],y[0]),F.M(x[0],y[1]))


def vmat(F,X,x):
    return tuple(F.A(F.A(F.M(X[i][0],x[0]),F.M(X[i][1],x[1])),F.M(X[i][2],x[2])) for i in range(3))


def transformed(F,a,b,c,h,t,u):
    # Derived by explicit matrix conjugation, cross-checked against orbit predictions.
    aa=a
    bb=F.S(F.M(h,b),F.D(F.M(a,t),h))
    cc=F.S(F.A(F.M(F.M(h,h),c),F.M(a,F.M(F.D(t,h),F.D(t,h)))),F.D(F.M(F.M(F.scalar(2),a),u),h))
    return (aa,bb,cc)


def canonical(F,a,b,c):
    if a!=0:
        if F.p!=2:return ('nonzero_char',a)
        z=F.A(F.M(a,c),F.M(b,b))
        return ('char2',a,int(z!=0))
    if b!=0:return ('nil_b',F.D(c,F.M(b,b)))
    if c==0:return ('zero',)
    if F.p==2:return ('nil_c',1)
    return ('nil_c',int(c in {F.M(x,x) for x in range(1,F.q)}))


def check(q):
    F=Field(q)
    derivations=list(product(range(q), repeat=3))
    group=list(product(range(1,q),range(q),range(q)))
    expected_orbits=(3*q if F.p==2 else 2*q+2)
    assert len(derivations)==q**3 and len(group)==(q-1)*q*q
    def e(i):return tuple(int(i==j) for j in range(3))
    # Check derivation and automorphism identities on basis pairs.
    for a,b,c in derivations:
        D=deriv(F,a,b,c)
        for i,j in product(range(3),repeat=2):
            left=vmat(F,D,bracket(F,e(i),e(j)))
            right=tuple(F.A(x,y) for x,y in zip(bracket(F,vmat(F,D,e(i)),e(j)),bracket(F,e(i),vmat(F,D,e(j)))))
            assert left==right,(q,'derivation',a,b,c,i,j)
    for h,t,u in group:
        G=autom(F,h,t,u)
        assert det3(F,G)!=0
        for i,j in product(range(3),repeat=2):
            assert vmat(F,G,bracket(F,e(i),e(j)))==bracket(F,vmat(F,G,e(i)),vmat(F,G,e(j)))
    # Direct matrix-conjugation cross-check on complete Cartesian product when q<=4.
    if q<=4:
        for a,b,c in derivations:
            D=deriv(F,a,b,c)
            for h,t,u in group:
                G=autom(F,h,t,u)
                H=mm(F,mm(F,G,D),invmat(F,G))
                assert H==deriv(F,*transformed(F,a,b,c,h,t,u)),(q,'matrix',a,b,c,h,t,u,H)
    labels=Counter(canonical(F,*x) for x in derivations)
    assert len(labels)==expected_orbits,(q,'classes',len(labels),expected_orbits)
    visited=set()
    for a,b,c in derivations:
        if (a,b,c) in visited:continue
        orb={transformed(F,a,b,c,*g) for g in group}
        assert all(canonical(F,*d)==canonical(F,a,b,c) for d in orb)
        assert len(orb)==labels[canonical(F,a,b,c)],(q,'orbit_size',a,b,c,len(orb),labels[canonical(F,a,b,c)])
        assert not orb.intersection(visited)
        visited.update(orb)
    assert len(visited)==q**3
    hist=Counter(labels.values())
    print(f'q={q} derivations={q**3} automorphisms={(q-1)*q*q} orbits={len(labels)} orbit_size_multiplicity={dict(sorted(hist.items()))}')

if __name__=='__main__':
    for q in CASES:check(q)
    print('VERIFY_OK')
