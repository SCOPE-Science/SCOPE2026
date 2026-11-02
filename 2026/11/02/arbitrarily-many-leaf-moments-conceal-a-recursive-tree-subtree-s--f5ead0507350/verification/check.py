"""Finite independent exact checks for the conditional leaf laws of recursive trees.
Run: python3 verification/check.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial

checks = 0

def test(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def leaf_dist(m):
    # Independent recursion by leaf count, not using the splitting formula.
    d = {1: Fraction(1)}
    for size in range(1, m):
        nd = {}
        for k, weight in d.items():
            nd[k] = nd.get(k, 0) + weight * Fraction(k, size)
            nd[k+1] = nd.get(k+1, 0) + weight * Fraction(size-k, size)
        d = {k:v for k,v in nd.items() if v}
    return d

def convolve(a, b, shift=0):
    d = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = ka + kb - shift
            d[key] = d.get(key, 0) + va*vb
    return {k:v for k,v in d.items() if v}

def moment(d, r):
    return sum((Fraction(k)**r)*p for k,p in d.items())

for n in range(3, 10):
    counts = {s:Counter() for s in range(1, n)}
    for parents in product(*(range(j-1) for j in range(2, n+1))):
        children=[0]*n
        for parent in parents:
            children[parent] += 1
        leaves=sum(v == 0 for v in children)
        subtree={1}
        for v in range(2, n):
            if parents[v-1] in subtree:
                subtree.add(v)
        s=len(subtree)
        counts[s][leaves] += 1
    test(sum(sum(z.values()) for z in counts.values()) == factorial(n-1), f'enumeration n={n}')
    marginal=leaf_dist(n)
    empirical=Counter()
    for s in range(1,n):
        test(sum(counts[s].values())==factorial(n-2),f'uniform sizes n={n},s={s}')
        conditional={k:Fraction(v,factorial(n-2)) for k,v in counts[s].items()}
        predicted=convolve(leaf_dist(s),leaf_dist(n-s),int(n-s==1))
        test(conditional==predicted, f'conditional law n={n},s={s}')
        for k,v in counts[s].items():
            empirical[k]+=v
        if s>=2 and n-s>=2:
            for r in range(min(s,n-s)):
                test(moment(conditional,r)==moment(marginal,r), f'cumulant disguise n={n},s={s},r={r}')
            test(conditional.get(1,0)==0 and marginal.get(1,0)>0, f'distinct n={n},s={s}')
        test(sum(conditional.values())==1, f'normalized n={n},s={s}')
    marginal_emp={k:Fraction(v,factorial(n-1)) for k,v in empirical.items()}
    test(marginal_emp==marginal, f'unconditional law n={n}')
    mean_s=sum(Fraction(s,n-1) for s in range(1,n))
    mean_l=sum(moment({k:Fraction(v,factorial(n-2)) for k,v in counts[s].items()},1)/ (n-1) for s in range(1,n))
    cov=sum(Fraction(s,n-1)*moment({k:Fraction(v,factorial(n-2)) for k,v in counts[s].items()},1) for s in range(1,n))-mean_s*mean_l
    test(cov == Fraction(-(n-2),2*(n-1)), f'covariance n={n}')
print(f'PASS: {checks} exact-rational assertions; exhaustive recursive trees n=3..9 ({sum(factorial(n-1) for n in range(3,10))} trees).')
