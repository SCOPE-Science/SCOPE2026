"""Symbolically derive the acyclic three-edge mapping table by inclusion-exclusion.
Optional: python derive_table.py (requires sympy). All identities hold as polynomials
in n and i; this is not a finite-size interpolation.
"""
from itertools import combinations, permutations
import sympy as sp

n, i = sp.symbols('n i', integer=True, positive=True)
sources = (i, i + 1, i + 2)
expected = {
    (1,2,3): 0, (1,3,2): -1, (2,1,3): -1,
    (2,3,1): 1, (3,1,2): 1, (3,2,1): 0,
}


def count_extensions(mapping, pattern):
    """Count injections with required rank order and the mapped edges forced."""
    if len(set(mapping.values())) != len(mapping):
        return sp.Integer(0)
    if not mapping:
        return sp.binomial(n, 3)
    if len(mapping) == 1:
        index, value = next(iter(mapping.items()))
        rank = pattern[index]
        return sp.binomial(value-1, rank-1)*sp.binomial(n-value,3-rank)
    if len(mapping) == 2:
        (j,y),(k,z) = list(mapping.items())
        sign = sp.expand(y-z)
        assert sign.is_positive or sign.is_negative
        if (sign.is_negative) != (pattern[j] < pattern[k]):
            return sp.Integer(0)
        free = next(iter({0,1,2}-set(mapping)))
        if pattern[free] < min(pattern[j],pattern[k]):
            return sp.Min(y,z)-1
        if pattern[free] > max(pattern[j],pattern[k]):
            return n-sp.Max(y,z)
        return abs(sign)-1
    v = [mapping[j] for j in range(3)]
    actual = tuple(1+sum(bool(sp.expand(z-y).is_negative) for z in v) for y in v)
    return sp.Integer(actual == pattern)


def derive(pattern):
    t = sp.binomial(n,3)
    for a in range(3):
        t -= count_extensions({a:sources[a]}, pattern)
    for a,b in combinations(range(3),2):
        t += count_extensions({a:sources[a],b:sources[b]}, pattern)
    t -= count_extensions({j:sources[j] for j in range(3)}, pattern)
    for a,b in combinations(range(3),2):
        edges = {a:sources[b],b:sources[a]}
        t -= count_extensions(edges,pattern)
        c = next(iter({0,1,2}-{a,b}))
        t += count_extensions(edges | {c:sources[c]},pattern)
    t -= count_extensions({0:sources[1],1:sources[2],2:sources[0]},pattern)
    t -= count_extensions({0:sources[2],1:sources[0],2:sources[1]},pattern)
    return sp.expand(sp.expand_func(t))


def main():
    for p in permutations((1,2,3)):
        q = derive(p)
        total = sp.factor(sp.summation(q,(i,1,n-2)))
        bias = sp.factor(2*(n-1)*(total/((n-1)*(n-2)*(n-3))-(n-2)/6))
        assert sp.simplify(bias-expected[p]) == 0, (p,bias)
        print(''.join(map(str,p)), ': 6Q =', sp.factor(6*q), '; exact bias =',bias)
    print('PASS: six formal polynomial identities for every integer n >= 4')

if __name__ == '__main__':
    main()
