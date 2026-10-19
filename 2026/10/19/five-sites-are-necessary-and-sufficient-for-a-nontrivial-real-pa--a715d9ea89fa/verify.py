"""Standalone algebraic and bounded combinatorial consistency checks for finite real Pauli pairs.
Usage: python verify.py
The analytic arbitrary-support proof, not this finite test, gives universality.
"""
from itertools import combinations, product
from collections import defaultdict
from fractions import Fraction

def auto(sites,weights):
    out=defaultdict(int)
    for i in range(len(sites)):
        for j in range(i+1,len(sites)):
            out[sites[j]-sites[i]] += weights[i]*weights[j]
    return dict(out)

def trivial(sites,a,b):
    if a==b or all(x == -y for x,y in zip(a,b)):
        return True
    # Reflection with translation mapping support onto itself.
    if all(sites[i]+sites[-i-1] == sites[0]+sites[-1] for i in range(len(sites))):
        if all(b[i]==a[-i-1] for i in range(len(sites))) or all(b[i]==-a[-i-1] for i in range(len(sites))):
            return True
    return False

# Validate exceptional 5-term products, with exact integer coefficients.
for u,t in product((-5,-4,-3,-2,2,3,4,5), (-4,-3,-2,-1,1,2,3,4)):
    f=[1,t,u-1,u*t,-u]
    g=[-1,t,1-u,u*t,u]
    assert all(abs(a)==abs(b) for a,b in zip(f,g))
    assert auto(range(5),f)==auto(range(5),g)
    assert not trivial(list(range(5)),f,g)

# Exhaustive test finite coefficients on arbitrary 1--4 point supports in [0,9].
checks=0
for k in range(1,5):
    for sites in combinations(range(10),k):
        for aa in product((-2,-1,1,2),repeat=k):
            original=auto(sites,aa)
            for signs in product((-1,1),repeat=k-1):
                bb=(aa[0],)+tuple(aa[j+1]*signs[j] for j in range(k-1))
                if auto(sites,bb)==original:
                    assert trivial(sites,aa,bb), (sites,aa,bb)
                checks+=1
print(f'VERIFY_OK {checks} four-site and smaller exact tests; 64 explicit five-site parametric examples')
