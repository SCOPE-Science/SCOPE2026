"""Finite exact tests for missing monochromatic cycles in random edge colorings.

The universal negative-association and asymptotic assertions are proved
analytically; this checker tests small graphs and moment-generating inequalities.
"""
from itertools import product
from fractions import Fraction
from collections import Counter
from math import exp


def has_directed_cycle(s, edges):
    adj = [[] for _ in range(s)]
    for u, v in edges:
        adj[u].append(v)
    state = [0] * s
    def dfs(u):
        state[u] = 1
        for v in adj[u]:
            if state[v] == 1 or (state[v] == 0 and dfs(v)):
                return True
        state[u] = 2
        return False
    return any(state[u] == 0 and dfs(u) for u in range(s))


def census(s):
    edges = tuple(product(range(s), repeat=2))
    totals = Counter()
    single = [0] * s
    joint = [[0] * s for _ in range(s)]
    count = 0
    for labelling in product(range(s), repeat=s*s):
        absent = []
        for color in range(s):
            subgraph = [edges[i] for i, col in enumerate(labelling) if col == color]
            absent.append(int(not has_directed_cycle(s, subgraph)))
        m = sum(absent)
        totals[m] += 1
        count += 1
        for i in range(s):
            single[i] += absent[i]
            for j in range(s):
                joint[i][j] += absent[i] * absent[j]
    assert count == s ** (s*s)
    q = Fraction(single[0], count)
    assert all(Fraction(x, count) == q for x in single)
    for i in range(s):
        for j in range(i+1,s):
            assert Fraction(joint[i][j],count) <= q*q
    mean = s*q
    variance = sum((Fraction(m)*Fraction(m)*Fraction(cnt,count) for m,cnt in totals.items()),Fraction(0)) - mean*mean
    assert variance <= mean*(1-q)
    a = (1-Fraction(1,s))**s
    a2 = (1-Fraction(2,s))**s
    var_empty_loops = s*a + s*(s-1)*a2 - s*s*a*a
    lower = (q/a)**2 * var_empty_loops
    assert lower <= variance, (s,lower,variance)
    assert lower > 0
    for t in (-2.0,-0.5,0.5,1.0,2.0):
        left = sum(cnt*exp(t*m)/count for m,cnt in totals.items())
        right = (1-float(q)+float(q)*exp(t))**s
        assert left <= right + 1e-12, (s,t,left,right)
    return {'s':s,'count':count,'distribution':dict(sorted(totals.items())),
            'q':str(q),'mean':str(mean),'variance':str(variance),
            'binomial_variance':str(mean*(1-q)), 'loop_occupancy_lower':str(lower)}


def main():
    for s in (2,3):
        print(census(s))
    print('VERIFICATION_OK: exact distribution/covariance/variance and mgf checks')

if __name__ == '__main__':
    main()
