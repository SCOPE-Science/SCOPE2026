"""Finite exact verification of first-branch leaf-count identities.

Run: python3 verification.py
Requires only the Python standard library. Computations are finite
spot checks; the theorem for all sizes is established analytically.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial

checks = 0

def eq(a, b):
    global checks
    checks += 1
    assert a == b, (a, b)

def eulerian(m):
    assert m >= 1
    row = [1]
    for t in range(2, m + 1):
        row = [(k + 1) * (row[k] if k < len(row) else 0)
               + (t-k) * (row[k-1] if k else 0)
               for k in range(t)]
    return row

def leaf_law(t):
    if t == 1:
        return {1: Fraction(1)}
    return {k + 1: Fraction(a, factorial(t-1))
            for k, a in enumerate(eulerian(t-1))}

def convolve(a, b):
    z = Counter()
    for x, px in a.items():
        for y, py in b.items():
            z[x + y] += px * py
    return dict(z)

def conditional_law(n, s):
    x = convolve(leaf_law(s), leaf_law(n-s))
    if n-s == 1:
        return {k-1: p for k, p in x.items()}
    return x

def moments(law, order):
    return [Fraction(1)] + [sum(p * k**r for k,p in law.items())
                            for r in range(1, order+1)]

def cumulants(law, order):
    raw = moments(law,order)
    kappa=[Fraction(0)]*(order+1)
    for r in range(1,order+1):
        kappa[r] = raw[r] - sum(Fraction(comb(r-1,j-1))*kappa[j]*raw[r-j]
                                 for j in range(1,r))
    return kappa

def bernoulli(r):
    vals = [Fraction(1)]
    for n in range(1,r+1):
        vals.append(-sum(Fraction(comb(n+1,k))*vals[k]
                         for k in range(n))/Fraction(n+1))
    return vals[r]

def enumerate_trees(n):
    counts = Counter()
    for parents in product(*(range(1,t) for t in range(2,n+1))):
        children = [[] for _ in range(n+1)]
        for t,p in enumerate(parents, start=2):
            children[p].append(t)
        leaves = sum(not children[v] for v in range(1,n+1))
        stack = [2]
        size = 0
        while stack:
            v=stack.pop()
            size+=1
            stack.extend(children[v])
        counts[(size,leaves)] += 1
    return counts

# Independently enumerate every recursive tree for small orders.
for n in range(2,10):
    obs = enumerate_trees(n)
    eq(sum(obs.values()), factorial(n-1))
    marg=Counter()
    for (s,l),c in obs.items():
        marg[s]+=c
    for s in range(1,n):
        eq(Fraction(marg[s], factorial(n-1)), Fraction(1,n-1))
        law=conditional_law(n,s)
        for l in range(1,n+1):
            eq(Fraction(obs[(s,l)],marg[s]), law.get(l,Fraction(0)))
    for l in range(1,n+1):
        eq(Fraction(sum(c for (s,k),c in obs.items() if k==l),factorial(n-1)),
           leaf_law(n).get(l,Fraction(0)))

# Independent finite cumulant and sharp-boundary checks via Eulerian numbers.
for n in range(2,34):
    ll = leaf_law(n)
    order = min(n-1,10)
    k_all = cumulants(ll,order)
    for r in range(1,order+1):
        target = Fraction(n,2) if r==1 else Fraction(n,r)*bernoulli(r)
        eq(k_all[r], target)
    for s in range(1,n):
        cc=conditional_law(n,s)
        eq(sum(cc.values()), 1)
        rs = min(min(s,n-s)-1,order)
        if rs>0:
            k_cond=cumulants(cc,rs)
            for r in range(1,rs+1):
                eq(k_cond[r], k_all[r])
                eq(moments(cc,r)[r], moments(ll,r)[r])
        if 2<=s<=n-2:
            eq(moments(cc,1)[1],Fraction(n,2))

for r in (2,4,6,8):
    n=2*r+3
    eq(cumulants(conditional_law(n,r),r)[r]-cumulants(leaf_law(n),r)[r],
       -bernoulli(r))
    eq(cumulants(conditional_law(n,r+1),r)[r],cumulants(leaf_law(n),r)[r])

for n in range(2,34):
    # E[L | B=s] and B-uniform yield the stated unconditional covariance.
    EBL=sum(Fraction(s,n-1)*moments(conditional_law(n,s),1)[1]
            for s in range(1,n))
    eq(EBL-Fraction(n,2)*Fraction(n,2),-Fraction(n-2,2*(n-1)))

print('PASS', checks, 'exact rational assertions; exhaustive trees through n=9')
