"""Exhaustive finite-field cross-checks for Heisenberg derivation rank counts."""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, q):
        assert q in (2,3,4)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        p=0
        while b:
            if b&1:p^=a
            b>>=1
            a<<=1
            if a&4:a^=7
        return p
    def inv(self,a):
        return next(v for v in range(1,self.q) if self.mul(a,v)==1)
    def sub(self,a,b):return self.add(a,self.neg(b))

def product_matrices(X,Y,F):
    return [[F.add(0, sum_mod((F.mul(X[i][k],Y[k][j]) for k in range(len(Y))),F)) for j in range(len(Y[0]))] for i in range(len(X))]
def sum_mod(it,F):
    r=0
    for a in it:r=F.add(r,a)
    return r

def rank(M,F):
    M=[list(x) for x in M]
    if not M:return 0
    n=len(M); p=len(M[0]); i=0
    for j in range(p):
        piv=next((k for k in range(i,n) if M[k][j]),None)
        if piv is None:continue
        M[piv],M[i]=M[i],M[piv]
        v=F.inv(M[i][j]);M[i]=[F.mul(v,x) for x in M[i]]
        for k in range(n):
            if k!=i and M[k][j]:
                v=M[k][j]
                M[k]=[F.sub(x,F.mul(v,y)) for x,y in zip(M[k],M[i])]
        i+=1
        if i==n:break
    return i

def brute(m,q):
    F=Field(q); d=2*m
    J=[[0]*d for _ in range(d)]
    for i in range(m):J[i][m+i]=1;J[m+i][i]=F.neg(1)
    distribution=Counter()
    accepted_matrices=Counter()
    for entries in product(range(q),repeat=d*d):
        A=[list(entries[i*d:(i+1)*d]) for i in range(d)]
        c=None
        # Independently derive the induced central scalar by the Leibniz identity.
        for c0 in range(q):
            if all(F.add(sum_mod((F.mul(A[k][i],J[k][j]) for k in range(d)),F),
                         sum_mod((F.mul(J[i][k],A[k][j]) for k in range(d)),F))
                   == F.mul(c0,J[i][j]) for i in range(d) for j in range(d)):
                c=c0;break
        if c is None:continue
        if any(product_matrices(A,A,F)[i][j]!=A[i][j] for i in range(d) for j in range(d)):continue
        if F.mul(c,c)!=c:continue
        accepted_matrices[c]+=1
        for phi in product(range(q),repeat=d):
            # Form full (d+1)-square derivation matrix and test composition directly.
            D=[A[i]+[0] for i in range(d)]+[list(phi)+[c]]
            if product_matrices(D,D,F)!=D:continue
            # Recheck Lie Leibniz identity on every pair of generator basis vectors.
            if any(F.add(sum_mod((F.mul(D[k][i],J[k][j]) for k in range(d)),F),
                         sum_mod((F.mul(J[i][k],D[k][j]) for k in range(d)),F))
                   !=F.mul(D[d][d],J[i][j]) for i in range(d) for j in range(d)):
                raise AssertionError('bad derivation')
            distribution[rank(D,F)]+=1
    return dict(sorted(distribution.items())),dict(accepted_matrices)

def sp_order(m,q):
    out=q**(m*m)
    for i in range(1,m+1):out*=q**(2*i)-1
    return out

def expected(m,q):
    R=Counter();
    if q%2==0:
        for r in range(m+1):
            ratio=sp_order(m,q)//(sp_order(r,q)*sp_order(m-r,q))
            assert ratio*sp_order(r,q)*sp_order(m-r,q)==sp_order(m,q)
            R[2*r]+=ratio*q**(2*r)
    else:R[0]=1
    L=1
    for i in range(1,m+1): L*=q**i+1
    R[m+1]+=q**(m*(m+1)//2+m)*L
    return dict(sorted(R.items()))

if __name__=='__main__':
    for m,q in ((1,2),(1,3),(1,4),(2,2)):
        actual,blocks=brute(m,q)
        want=expected(m,q)
        assert actual==want,(m,q,actual,want)
        print(f'H_{2*m+1}(F_{q}): rank_counts={actual}; central_multiplier_matrix_counts={blocks}; total={sum(actual.values())}')
    print('VERIFY_OK')

def orbit_test(q):
    # Direct conjugacy computation for the three-dimensional Heisenberg algebra.
    F=Field(q)
    ds=[]; aut=[]
    for entries in product(range(q),repeat=4):
        P=[list(entries[:2]),list(entries[2:])]
        det=F.sub(F.mul(P[0][0],P[1][1]),F.mul(P[0][1],P[1][0]))
        if det:
            for psi in product(range(q),repeat=2):
                aut.append([P[0]+[0],P[1]+[0],list(psi)+[det]])
        for c in range(q):
            if F.add(P[0][0],P[1][1])!=c:continue
            if product_matrices(P,P,F)!=P or F.mul(c,c)!=c:continue
            for phi in product(range(q),repeat=2):
                d=[P[0]+[0],P[1]+[0],list(phi)+[c]]
                if product_matrices(d,d,F)==d:ds.append(d)
    def inverse(M):
        I=[[int(i==j) for j in range(3)] for i in range(3)]
        X=[M[i][:]+I[i][:] for i in range(3)]
        for j in range(3):
            piv=next(i for i in range(j,3) if X[i][j])
            X[j],X[piv]=X[piv],X[j]
            a=F.inv(X[j][j]);X[j]=[F.mul(a,t) for t in X[j]]
            for i in range(3):
                if i!=j:
                    a=X[i][j];X[i]=[F.sub(u,F.mul(a,v)) for u,v in zip(X[i],X[j])]
        return [x[3:] for x in X]
    def key(M):return tuple(t for row in M for t in row)
    distinct={key(D) for D in ds}
    assert len(distinct)==len(ds)
    normals=[[[0,0,0],[0,0,0],[0,0,0]], [[1,0,0],[0,0,0],[0,0,1]]]
    if q%2==0:normals.append([[1,0,0],[0,1,0],[0,0,0]])
    seen=set();sizes=[]
    for D in normals:
        orbital={key(product_matrices(product_matrices(S,D,F),inverse(S),F)) for S in aut}
        assert orbital <=distinct
        assert not orbital & seen
        seen|=orbital;sizes.append(len(orbital))
    assert seen==distinct,(len(seen),len(distinct))
    print('H_3(F_%d) automorphism-orbit sizes: %s'%(q,sizes))

if __name__=='__main__':
    for q in (2,3):orbit_test(q)
    print('ORBIT_OK')
