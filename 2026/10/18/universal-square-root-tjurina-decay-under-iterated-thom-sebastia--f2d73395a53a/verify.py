"""Exact checks for higher separated sums of square-zero Milnor multiplication.
This self-contained finite verifier does not replace the general proof.
"""
from math import comb, sqrt, pi

def closed(mu, tau, r):
    c=mu-tau; s=2*tau-mu
    assert c>=0 and s>=0 and r>=1
    return sum(comb(r,k)*comb(k,k//2)*(c**k)*(s**(r-k)) for k in range(r+1))

def modular_rank(A, p=101):
    m=len(A); n=len(A[0]) if m else 0; rank=0
    for j in range(n):
        pivot=next((i for i in range(rank,m) if A[i][j]%p),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank]
        inv=pow(A[rank][j]%p,-1,p)
        A[rank][j:]=[(x*inv)%p for x in A[rank][j:]]
        for i in range(rank+1,m):
            v=A[i][j]%p
            if v:
                A[i][j:]=[(a-v*b)%p for a,b in zip(A[i][j:],A[rank][j:])]
        rank+=1
        if rank==m:break
    return rank

def kronecker_sum(mu, c, r):
    from itertools import product
    basis=list(product(range(mu),repeat=r)); idx={t:i for i,t in enumerate(basis)}
    d=len(basis); M=[[0]*d for _ in range(d)]
    for col,t in enumerate(basis):
        for h,v in enumerate(t):
            if v<2*c and v%2==0: # J2 maps even index to odd index
                u=list(t);u[h]+=1; M[idx[tuple(u)]][col]+=1
    return M

for c,s,r in [(1,0,5),(1,1,4),(2,0,3),(2,1,3),(0,3,4)]:
    mu=2*c+s;tau=mu-c
    M=kronecker_sum(mu,c,r)
    measured=mu**r-modular_rank(M)
    expected=closed(mu,tau,r)
    assert measured==expected,(c,s,r,measured,expected)
    print('matrix',mu,tau,r,measured,'OK')

mu,tau=16,15
for r in range(1,7):
    print('example',r,closed(mu,tau,r))
assert [closed(mu,tau,r) for r in range(1,5)] == [15,226,3419,51918]
for mu,tau in [(16,15),(12,11),(3,2)]:
    c=mu-tau
    for r in [100,300,1000]:
        ratio=closed(mu,tau,r)/(mu**r)
        approx=sqrt(mu/(pi*c*r))
        print('asymptotic',mu,tau,r,round(ratio/approx,6))
print('VERIFY_OK')
