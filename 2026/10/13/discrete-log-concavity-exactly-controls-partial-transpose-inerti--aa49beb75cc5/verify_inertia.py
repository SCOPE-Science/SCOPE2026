#!/usr/bin/env python3
from fractions import Fraction
from math import comb

def idx(a,b,n): return a*n+b
def pt_matrix(n,p):
    M=[[Fraction(0) for _ in range(2*n)] for _ in range(2*n)]
    for k,pk in enumerate(p):
        u,v=idx(0,k+1,n),idx(1,k,n)
        M[u][u]+=pk/2; M[v][v]+=pk/2
        a,b=idx(1,k+1,n),idx(0,k,n)
        M[a][b]-=pk/2; M[b][a]-=pk/2
    return M

def check(n,p):
    M=pt_matrix(n,p); ext=[Fraction(0)]+list(p)+[Fraction(0)]
    assert M[idx(1,0,n)][idx(1,0,n)]==p[0]/2
    assert M[idx(0,n-1,n)][idx(0,n-1,n)]==p[-1]/2
    L=E=V=0
    for k in range(n-1):
        a,b=idx(0,k,n),idx(1,k+1,n)
        assert M[a][a]==ext[k]/2 and M[b][b]==ext[k+2]/2
        assert M[a][b]==M[b][a]==-p[k]/2
        q=p[k]*p[k]-ext[k]*ext[k+2]
        if q>0: L+=1
        elif q==0: E+=1
        else: V+=1
    inertia=(n+1+V,E,L)
    assert sum(inertia)==2*n
    return inertia

for n in range(2,13):
    N=n-2; den=2**N
    p=[Fraction(comb(N,k),den) for k in range(N+1)]
    assert sum(p)==1
    assert check(n,p)==(n+1,0,n-1)

for n in range(3,11):
    raw=[2**k for k in range(n-1)]; den=sum(raw)
    p=[Fraction(x,den) for x in raw]
    assert check(n,p)==(n+1,n-3,2)

p=[Fraction(8,18),Fraction(1,18),Fraction(1,18),Fraction(8,18)]
assert check(5,p)==(8,0,2)
print("VERIFY_OK")
