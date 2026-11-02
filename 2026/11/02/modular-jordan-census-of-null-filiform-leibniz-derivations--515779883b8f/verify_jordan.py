"""Independent finite-field matrix checks for the derivation Jordan census.
Run: python3 verify_jordan.py
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, q):
        self.q=q
        if q==4: self.p=2; self.ext=(1,1)
        elif q==9: self.p=3; self.ext=(2,0)
        else: self.p=q; self.ext=None
        self.inv={}
        for x in range(1,q):
            self.inv[x]=next(y for y in range(1,q) if self.mul(x,y)==1)
    def add(self,a,b):
        p=self.p
        return (a+b)%p if self.ext is None else (a%p+b%p)%p + p*((a//p+b//p)%p)
    def neg(self,a):
        p=self.p
        return (-a)%p if self.ext is None else (-a%p)+p*((-(a//p))%p)
    def mul(self,a,b):
        p=self.p
        if self.ext is None:return a*b%p
        a0,a1=a%p,a//p; b0,b1=b%p,b//p; c0,c1=self.ext
        return (a0*b0+c0*a1*b1)%p+p*((a0*b1+a1*b0+c1*a1*b1)%p)
    def smul(self,n,a):
        z=0
        for _ in range(n%self.p):z=self.add(z,a)
        return z

def rank(matrix,F):
    a=[row[:] for row in matrix]; nr=len(a); nc=len(a[0]) if nr else 0; r=0
    for col in range(nc):
        pivot=next((i for i in range(r,nr) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        s=F.inv[a[r][col]]
        a[r]=[F.mul(s,x) for x in a[r]]
        for i in range(r+1,nr):
            factor=a[i][col]
            if factor:
                a[i]=[F.add(x,F.neg(F.mul(factor,y))) for x,y in zip(a[i],a[r])]
        r+=1
        if r==nr: break
    return r

def matmul(a,b,F):
    n=len(a)
    return [[sumfield([F.mul(a[i][j],b[j][k]) for j in range(n)],F) for k in range(n)] for i in range(n)]

def sumfield(xs,F):
    s=0
    for x in xs:s=F.add(s,x)
    return s

def jordan_signature(M, eigenvalues,F):
    n=len(M); out=[]
    for eigen in sorted(set(eigenvalues)):
        B=[[F.add(M[i][j],F.neg(eigen)) if i==j else M[i][j] for j in range(n)] for i in range(n)]
        power=[[int(i==j) for j in range(n)] for i in range(n)]
        nul=[0]
        for t in range(n):
            power=matmul(power,B,F)
            nul.append(n-rank(power,F))
        sizes=[nul[t]-nul[t-1] for t in range(1,n+1)]
        blocks=[]
        for t in range(1,n+1):
            exact=sizes[t-1]-(sizes[t] if t<n else 0)
            blocks.extend([t]*exact)
        if blocks:out.append((eigen,tuple(sorted(blocks,reverse=True))))
    assert sum(sum(b) for _,b in out)==n,(M,out)
    return tuple(out)

def part(L,d):
    return tuple(sorted([(L-1-i)//d+1 for i in range(min(L,d))],reverse=True)) if L else ()

def predicted_signature(a1,n,p,r,F):
    if not a1:return ((0,part(n,r)),)
    out=[]
    for c in range(p):
        m=sum((j%p==c) for j in range(1,n+1))
        if m:out.append((F.smul(c,a1),part(m,r)))
    return tuple(sorted(out))

def predicted_nullity_counts(n,q,p):
    m=n//p; dist=Counter({n:1})
    for r in range(1,n):dist[r]+=(q-1)*q**(n-r-1)
    if m==0:dist[0]+=(q-1)*q**(n-1)
    else:
        for r in range(1,m):dist[r]+=(q-1)**2*q**(n-1-r)
        dist[m]+=(q-1)*q**(n-m)
    return {k:v for k,v in dist.items() if v}

def check(q,n):
    F=Field(q);p=F.p;k=(n-1)//p
    observed=Counter(); actual_nullities=Counter()
    for aa in product(range(q),repeat=n):
        M=[[0]*n for _ in range(n)]
        for j in range(n):
            for i in range(j,n):M[i][j]=F.smul(j+1,aa[0]) if i==j else aa[i-j]
        eig=[F.smul(j+1,aa[0]) for j in range(n)]
        sig=jordan_signature(M,eig,F)
        observed[(aa[0],sig)]+=1
        actual_nullities[n-rank(M,F)]+=1
    expected=Counter()
    for a1 in range(q):
        if a1==0:
            expected[(0,predicted_signature(0,n,p,n,F))]+=1
            for d in range(1,n):
                expected[(0,predicted_signature(0,n,p,d,F))]+=(q-1)*q**(n-d-1)
        else:
            for r in range(1,k+1):
                expected[(a1,predicted_signature(a1,n,p,r,F))]+=(q-1)*q**(n-r-1)
            expected[(a1,predicted_signature(a1,n,p,k+1,F))]+=q**(n-1-k)
    assert observed==expected,('jordan_failure',q,n,observed-expected,expected-observed)
    assert dict(actual_nullities)==predicted_nullity_counts(n,q,p),('rank_failure',q,n,actual_nullities,predicted_nullity_counts(n,q,p))
    assert sum(observed.values())==q**n
    print('ok',q,n,'derivations',q**n,'jordan_profiles',len(observed),'nullity_counts',dict(sorted(actual_nullities.items())))

if __name__=='__main__':
    cases=[(2,n) for n in range(2,8)]+[(3,n) for n in range(2,7)]+[(4,n) for n in range(2,6)]+[(5,n) for n in range(2,5)]+[(9,2),(9,3)]
    for q,n in cases:check(q,n)
    print('NULL_FILIFORM_MODULAR_JORDAN_CENSUS_OK',len(cases))
