"""Exact finite checks for labelled unary maps of forward height <=2."""
import itertools
from math import comb, factorial, log, exp

def counts_formula(n):
    ans={}
    for r in range(1,n+1):
        for s in range(n-r+1):
            t=n-r-s
            if s==0 and t>0: continue
            z=factorial(n)//(factorial(r)*factorial(s)*factorial(t))
            z *= r**s * (s**t if s else 1)
            ans[(r,s,t)]=z
    return ans

def counts_bruteforce(n):
    out={}
    for f in itertools.product(range(n), repeat=n):
        if any(f[f[f[i]]] != f[f[i]] for i in range(n)):
            continue
        r=sum(f[i]==i for i in range(n))
        s=sum(f[i]!=i and f[f[i]]==f[i] for i in range(n))
        t=n-r-s
        out[(r,s,t)]=out.get((r,s,t),0)+1
    return out

for n in range(1,7):
    left=counts_formula(n); right=counts_bruteforce(n)
    assert left==right,(n,left,right)
    print(f'n={n}; structures={sum(left.values())}; strata={len(left)}')
