"""Independent finite-field checks for tame substitution invariants.
Run: python3 checker.py. Pure Python, no dependencies.
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,p,e=1):
        self.p,self.e,self.q=p,e,p**e
        self.mod={1:None,(2,2):(1,1,1),(3,2):(1,0,1)}[1 if e==1 else (p,e)]
        self.addtab=[[self.op(a,b,False) for b in range(self.q)] for a in range(self.q)]
        self.multab=[[self.op(a,b,True) for b in range(self.q)] for a in range(self.q)]
        self.inv=[None]+[next(j for j in range(1,self.q) if self.multab[i][j]==1) for i in range(1,self.q)]
    def coeff(self,x):
        return [(x//self.p**i)%self.p for i in range(self.e)]
    def enc(self,a):return sum(v*self.p**i for i,v in enumerate(a))
    def op(self,a,b,mul):
        p,e=self.p,self.e
        A,B=self.coeff(a),self.coeff(b)
        if not mul:return self.enc([(x+y)%p for x,y in zip(A,B)])
        C=[0]*(2*e-1)
        for i,x in enumerate(A):
            for j,y in enumerate(B):C[i+j]=(C[i+j]+x*y)%p
        if e>1:
            for k in range(2*e-2,e-1,-1):
                v=C[k]
                for j in range(e):C[k-e+j]=(C[k-e+j]-v*self.mod[j])%p
        return self.enc(C[:e])
    def add(self,a,b):return self.addtab[a][b]
    def mul(self,a,b):return self.multab[a][b]
    def sub(self,a,b):return self.add(a,self.neg(b))
    def neg(self,a):return self.enc([(-z)%self.p for z in self.coeff(a)])
    def power(self,a,n):
        b=1
        for _ in range(n):b=self.mul(b,a)
        return b

def poly_mul(a,b,F,n):
    c=[0]*n
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:n-i]):
                if y:c[i+j]=F.add(c[i+j],F.mul(x,y))
    return c

def echelon_rank(mat,F):
    a=[row[:] for row in mat]
    if not a:return 0
    r=0
    for col in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][col]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        inv=F.inv[a[r][col]]
        a[r]=[F.mul(inv,v) for v in a[r]]
        for i in range(r+1,len(a)):
            w=a[i][col]
            if w:a[i]=[F.sub(u,F.mul(w,v)) for u,v in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r

def fixed_dim(phi,F):
    n=len(phi);columns=[];cur=[1]+[0]*(n-1)
    for j in range(n):
        col=cur[:];col[j]=F.sub(col[j],1);columns.append(col)
        cur=poly_mul(cur,phi,F,n)
    return n-echelon_rank([list(row) for row in zip(*columns)],F)

def check(p,e,d,m,a):
    F=Field(p,e)
    assert F.power(a,d)==1 and all(F.power(a,j)!=1 for j in range(1,d))
    assert m<=p
    n=m*d+1
    counts=Counter()
    for tail in product(range(F.q),repeat=n-2):
        phi=[0,a,*tail]
        counts[fixed_dim(phi,F)]+=1
    # Directly check that canonical resonance representatives fix precisely the
    # predicted monomial tail subalgebras.
    for r in range(1,m+1):
        phi=[0,a]+[0]*(n-2)
        if r<m:phi[r*d+1]=1
        assert fixed_dim(phi,F)==r+1
        h=m-r+1
        cur=[1]+[0]*(n-1)
        for j in range(1,n):
            cur=poly_mul(cur,phi,F,n)
            if j%d==0 and j//d>=h:
                want=[0]*n;want[j]=1
                assert cur==want,(p,e,d,m,r,j)
    total=F.q**(n-2)
    expect={r+1:total*(F.q-1)//(F.q**r) for r in range(1,m)}
    expect[m+1]=total//(F.q**(m-1))
    assert counts==expect,(p,e,d,m,counts,expect)
    return total,dict(sorted(counts.items()))

if __name__=='__main__':
    cases=[(2,1,1,2,1),(3,1,1,2,1),(3,1,2,2,2),(5,1,1,3,1),(5,1,2,2,4),(5,1,2,3,4),(7,1,3,2,2),(7,1,2,3,6),(2,2,3,2,2),(3,2,2,2,2)]
    aggregate=0
    for cs in cases:
        total,counts=check(*cs);aggregate+=total
        print('OK p,e,d,m,a=',cs,'automorphisms=',total,'fixed_dimensions=',counts)
    F=Field(2)
    outside=Counter(fixed_dim([0,1,u,v],F) for u,v in product(range(2),repeat=2))
    assert outside=={3:3,4:1},outside
    print('EXPECTED_BOUNDARY_FAILURE p=2,m=3:',dict(outside))
    print('ALL_TAME_FIXED_ALGEBRA_TESTS_PASSED',len(cases),aggregate)
