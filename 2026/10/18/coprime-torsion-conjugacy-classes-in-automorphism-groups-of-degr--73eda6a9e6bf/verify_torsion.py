"""Independent checks for the prime-to-characteristic torsion counts of
Aut(F_q<variables> / (variables)^3). Requires Python 3, no dependencies.
"""
from itertools import product
from math import prod


def modinv(a,p):return pow(a,-1,p)

def mm(A,B,p):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%p for j in range(len(B[0]))]for i in range(len(A))]

def eye(n):return [[int(i==j) for j in range(n)]for i in range(n)]

def rank(A,p):
    a=[r[:]for r in A]
    n=len(a); m=len(a[0]); k=0
    for j in range(m):
        i=next((i for i in range(k,n) if a[i][j]%p),None)
        if i is None:continue
        a[k],a[i]=a[i],a[k]
        fac=modinv(a[k][j]%p,p)
        a[k]=[x*fac%p for x in a[k]]
        for i in range(n):
            if i==k:continue
            f=a[i][j]
            a[i]=[(x-f*y)%p for x,y in zip(a[i],a[k])]
        k+=1
        if k==n:break
    return k

def gl_order(n,p):
    return prod(p**n-p**j for j in range(n))

def theory(d,p,L):
    roots=[a for a in range(1,p) if pow(a,L,p)==1]
    assert len(roots)==L
    ans=0
    def comps(n,k):
        if k==1:yield (n,);return
        for t in range(n+1):
            for z in comps(n-t,k-1):yield(t,)+z
    for r in comps(d,L):
        invariant=sum(r[i]*r[j]*r[roots.index(roots[i]*roots[j]%p)]
                      for i in range(L) for j in range(L))
        cnt=gl_order(d,p)//prod(gl_order(t,p) for t in r)
        ans+=cnt*p**(d**3-invariant)
    return ans

def kronecker(A,B,p):
    n=len(A);m=len(B)
    return [[A[i][j]*B[a][b]%p for j in range(n) for b in range(m)]
            for i in range(n) for a in range(m)]

def inv2(g,p):
    a,b=g[0];c,d=g[1]; delta=(a*d-b*c)%p
    if delta==0:return None
    v=modinv(delta,p)
    return [[d*v%p,-b*v%p],[-c*v%p,a*v%p]]

def direct_2(p,L):
    ret=0
    tested=0
    for a,b,c,d in product(range(p),repeat=4):
        g=[[a,b],[c,d]]
        gi=inv2(g,p)
        if gi is None:continue
        gp=eye(2)
        for _ in range(L):gp=mm(gp,g,p)
        if gp!=eye(2):continue
        T=kronecker(kronecker(g,g,p),list(map(list,zip(*gi))),p)
        # Kronecker order on vectorized 4x2 map is (g tensor g) kron ((g^-1)^transpose)
        N=[[0]*8 for _ in range(8)]
        Tk=eye(8)
        for _ in range(L):
            N=[[(N[i][j]+Tk[i][j])%p for j in range(8)]for i in range(8)]
            Tk=mm(Tk,T,p)
        assert Tk==eye(8)
        ret+=p**(8-rank(N,p));tested+=1
    return ret,tested

if __name__=='__main__':
    cases=[(3,2),(5,2),(5,4),(7,2),(7,3),(7,6)]
    for p,L in cases:
        theoretical=theory(2,p,L)
        observed,linear_count=direct_2(p,L)
        assert observed==theoretical,(p,L,observed,theoretical)
        print('PASSED',p,L,'linear parts',linear_count,'torsion automorphisms',observed)
    assert theory(2,3,2)==7534
    assert theory(2,5,2)==409376
    print('ALL_TORSION_ENUMERATIONS_PASSED',len(cases))
