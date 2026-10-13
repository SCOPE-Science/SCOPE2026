"""Exact checks of graph subsets against a labelled star-component recurrence."""
from functools import lru_cache
from math import comb

def add(A,B,coeff=1,shift=0):
    a=list(A)
    if len(a)<len(B)+shift:a += [0]*(len(B)+shift-len(a))
    for k,b in enumerate(B):a[k+shift]+=coeff*b
    return tuple(a)

@lru_cache(None)
def poly(m,n):
    if m == 0 or n == 0:return (1,)
    a=poly(m-1,n) # first left vertex is isolated
    for d in range(1,n+1):
        a=add(a,poly(m-1,n-d),comb(n,d),d) # first left vertex is star center
    for q in range(1,m):
        a=add(a,poly(m-1-q,n-1),n*comb(m-1,q),q+1) # right-centered star
    return a

def brute(m,n):
    N=m*n
    out=[0]*(N+1)
    # Distances in rook graph: one when same row or column, else two.
    # For every selected triple, no one on geodesic between two others.
    # Check direct triple by (row,col) metric.
    def dist(i,j):
        a,b=divmod(i,n);c,d=divmod(j,n)
        return (a!=c)+(b!=d)
    ds=[[dist(i,j) for j in range(N)] for i in range(N)]
    for mask in range(1<<N):
        vs=[i for i in range(N) if (mask>>i)&1]
        good=True
        for a in range(len(vs)):
            if not good:break
            for b in range(a+1,len(vs)):
                if not good:break
                for c in range(b+1,len(vs)):
                    i,j,k=vs[a],vs[b],vs[c]
                    if (ds[i][j]+ds[j][k]==ds[i][k] or
                        ds[i][k]+ds[k][j]==ds[i][j] or
                        ds[j][i]+ds[i][k]==ds[j][k]):
                        good=False;break
        if good:out[len(vs)]+=1
    while out and not out[-1]:out.pop()
    return tuple(out)

def max_count(m,n):
    if m==n==2:return 6
    if m==2:return 2**n
    if n==2:return 2**m
    return m*n

def run():
    cases=0; subsets=0; coeffs=0
    for m in range(1,6):
        for n in range(1,7):
            if m*n>16:continue
            p=poly(m,n);b=brute(m,n)
            assert p==b,(m,n,p,b)
            cases+=1;subsets+=2**(m*n);coeffs+=len(p)
            if m>=2 and n>=2:
                assert len(p)-1==m+n-2,(m,n,p)
                assert p[-1]==max_count(m,n),(m,n,p[-1],max_count(m,n))
    # Fixed small output examples
    print('VERIFY_OK cases=%d subset_checks=%d coefficient_checks=%d P_2_3=%s P_3_3=%s P_4_4_leading=%d'%(cases,subsets,coeffs,poly(2,3),poly(3,3),poly(4,4)[-1]))
if __name__=='__main__':run()
