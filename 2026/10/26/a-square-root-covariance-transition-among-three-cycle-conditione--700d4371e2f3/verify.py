"""Exact and asymptotic checks for three-cycle-conditioned permutation covariance.
Run: python verify.py (stdlib only).
"""
from fractions import Fraction
from itertools import permutations
from collections import Counter
from math import factorial, floor, log, sqrt

NMAX=90
s=[[0]*(NMAX+1) for _ in range(NMAX+1)]
s[0][0]=1
for n in range(1,NMAX+1):
    for k in range(1,n+1):
        s[n][k]=s[n-1][k-1]+(n-1)*s[n-1][k]

def z(n,k):
    return Fraction(s[n][k],factorial(n)) if 0<=k<=n else Fraction(0)

def cov_formula(n,j,k):
    assert j != k and 1 <= j < n and 1 <= k < n
    return (z(n,3)*z(n-j-k,1)-z(n-j,2)*z(n-k,2))/(j*k*z(n,3)**2)

def profile(perm):
    n=len(perm);vis=[False]*n;cy=[]
    for i in range(n):
        if not vis[i]:
            t=i;count=0
            while not vis[t]:
                vis[t]=True;count+=1;t=perm[t]
            cy.append(count)
    return cy

brute=0
for n in range(4,9):
    bags=[]
    for p in permutations(range(n)):
        cy=profile(p)
        if len(cy)==3:
            bags.append(Counter(cy))
    for j in range(1,n):
        for k in range(j+1,n):
            avg=lambda f:Fraction(sum(f(b) for b in bags),len(bags))
            c=avg(lambda a:a[j]*a[k])-avg(lambda a:a[j])*avg(lambda a:a[k])
            assert c==cov_formula(n,j,k),(n,j,k,c,cov_formula(n,j,k))
            brute+=1
print('exhaustive conditional covariance comparisons',brute)

# Numerically independent harmonic-number formula checked against exact Stirling moments.
H=[Fraction(0)]*(NMAX+1)
H2=[Fraction(0)]*(NMAX+1)
for n in range(1,NMAX+1):
    H[n]=H[n-1]+Fraction(1,n)
    H2[n]=H2[n-1]+Fraction(1,n*n)
exact=0
for n in range(5,NMAX+1):
    for j in range(1,min(8,n-2)):
        for r in range(1,n-j-1):
            k=n-j-r
            if j==k:continue
            delta=(H[n-1]*H[n-1]-H2[n-1])/2-Fraction(n*r,(n-j)*(j+r))*H[n-j-1]*H[j+r-1]
            cov=cov_formula(n,j,k)
            assert (cov>0)-(cov<0)==(delta>0)-(delta<0)
            exact+=1
print('exact harmonic-Stirling sign comparisons',exact)

# The asymptotic claims are proved analytically. These diagnostics only check scale/sign.
gamma=0.5772156649015328606
critical=__import__('math').exp(-gamma/2)
for n in (100_000,1_000_000):
    j=2
    # float harmonic sums via digamma asymptotic with rigor not inferred from these floats
    def harm(m):
        return log(m)+gamma+1/(2*m)-1/(12*m*m)+1/(120*m**4)
    for c in (0.58,0.95):
        r=floor(c*sqrt(n));h=harm(n-1)
        delta=(h*h-(__import__('math').pi**2/6-1/(n-1)))/2-(n*r)/((n-j)*(j+r))*harm(n-j-1)*harm(j+r-1)
        assert delta*(critical-c)>0,(n,c,delta)
print('asymptotic scale sanity checks 4; critical constant',critical)
