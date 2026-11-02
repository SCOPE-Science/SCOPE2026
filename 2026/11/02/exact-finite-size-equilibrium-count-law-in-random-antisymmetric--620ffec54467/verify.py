"""Exact rational checks of finite antisymmetric random-game equilibrium law."""
from fractions import Fraction as Q
from math import factorial, comb
from itertools import product
from collections import Counter

def mul(a,b,cap):
    c=[Q(0)]*(cap+1)
    for i,x in enumerate(a):
        if not x: continue
        for j,y in enumerate(b[:cap+1-i]):
            if y:c[i+j]+=x*y
    return c

def distribution(n):
    # A_m(t) is coefficient of x^m in the logarithm of the labelled EGF.
    # t marks selected equilibrium events; the coefficient of t^k is E[binom(N,k)].
    A=[[Q(0)]*(n+1) for _ in range(n+1)]
    A[1][0]=Q(1)
    for m in range(2,n+1):
        A[m][m-1] += Q(1,n**(2*m-2)) * Q(n,n-1)**(m-2) # directed path of length m-1
    for m in range(3,n+1):
        A[m][m] += Q(1,m*n**(2*m)) * Q(n,n-1)**m # directed cycle length m
    F=[[Q(0)]*(n+1) for _ in range(n+1)]
    F[0][0]=Q(1)
    for s in range(1,n+1):
        for m in range(1,s+1):
            v=mul(A[m],F[s-m],n)
            for k,val in enumerate(v):F[s][k]+=Q(m,s)*val
    moments=[factorial(n)*v for v in F[n]]
    probs=[sum(((-1)**(k-j))*comb(k,j)*moments[k] for k in range(j,n+1)) for j in range(n+1)]
    assert sum(probs)==1 and all(p>=0 for p in probs)
    assert sum(j*p for j,p in enumerate(probs))==Q(n-1,n)
    assert sum((j-Q(n-1,n))**2*p for j,p in enumerate(probs))==Q(n**3-3*n**2+6*n-6,n**3)
    return probs

def enumerate_columns(n):
    # Every ordered (maximum,minimum) location in each column is equiprobable.
    pairs=[(h,l) for h in range(n) for l in range(n) if h!=l]
    counts=Counter()
    for choice in product(pairs, repeat=n):
        h=[a for a,b in choice];l=[b for a,b in choice]
        K=sum(h[j]==i and l[i]==j for i in range(n) for j in range(n) if i!=j)
        counts[K]+=1
    total=len(pairs)**n
    return [Q(counts[k],total) for k in range(n+1)]

if __name__=='__main__':
    for n in range(2,11):
        p=distribution(n)
        if n<=4:
            brute=enumerate_columns(n)
            assert p==brute,(n,p,brute)
        print('n=',n,'P(N=k)=',','.join(str(v) for v in p if v))
    print('PASS: EGF, exact moments, probability normalization, n=2..4 exhaustive column configurations')
