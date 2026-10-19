"""Independent finite checks for commuting cliques of matrix units.

Run `python3 verify.py` with only the Python standard library.
Checks literal matrix-unit products and enumerates actual cliques and automorphism fixed facets.
Finite checks corroborate, but cannot prove, all-size formulas.
"""
from collections import Counter
from itertools import permutations, product
from math import comb, factorial


def multiply(a, b):
    i, j = a
    k, l = b
    return (i, l) if j == k else None


def graph(n):
    vertices = list(product(range(n), repeat=2))
    adjacent = [set() for _ in vertices]
    for a, p in enumerate(vertices):
        for b, q in enumerate(vertices):
            if a != b and multiply(p, q) == multiply(q, p):
                adjacent[a].add(b)
    return vertices, adjacent


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def ppow(a, k):
    v = [1]
    for _ in range(k):
        v = pmul(v, a)
    return v


def clique_coefficients_formula(n):
    total = ppow([1, 1], n)
    for s in range(1, n):
        for t in range(1, n-s+1):
            f = [0] * (s*t + 1)
            for a in range(s+1):
                for b in range(t+1):
                    w = (-1)**(s-a+t-b)*comb(s, a)*comb(t, b)
                    x = ppow([1, 1], a*b)
                    for j, coeff in enumerate(x):
                        f[j] += w*coeff
            term = pmul(f, ppow([1, 1], n-s-t))
            factor = factorial(n) // (factorial(s)*factorial(t)*factorial(n-s-t))
            total += [0] * max(0, len(term) - len(total))
            for j, coeff in enumerate(term):
                total[j] += factor*coeff
    while total[-1] == 0:
        total.pop()
    return total


def all_cliques(adj):
    frequencies = Counter({0: 1})
    def rec(candidates, k):
        for ix, u in enumerate(candidates):
            frequencies[k+1] += 1
            rec([v for v in candidates[ix+1:] if v in adj[u]], k+1)
    rec(list(range(len(adj))), 0)
    return [frequencies[i] for i in range(max(frequencies)+1)]


def maximal_cliques(adj):
    result = []
    def rec(R, P, X):
        if not P and not X:
            result.append(frozenset(R))
            return
        pivot = max(P | X, key=lambda v:len(P & adj[v]), default=None)
        for u in list(P - (adj[pivot] if pivot is not None else set())):
            rec(R|{u}, P & adj[u], X & adj[u])
            P.remove(u)
            X.add(u)
    rec(set(), set(range(len(adj))), set())
    return result


def expected_maximal(n):
    answer = Counter({n:1})
    for s in range(1, n):
        for t in range(1, n-s+1):
            answer[s*t+n-s-t] += factorial(n)//(factorial(s)*factorial(t)*factorial(n-s-t))
    return answer


def expected_fixed(n, permutation, swapped):
    seen = set()
    c = 0
    even = 0
    for i in range(n):
        if i in seen: continue
        v = i
        m = 0
        while v not in seen:
            seen.add(v)
            m += 1
            v = permutation[v]
        c += 1
        even += (m % 2 == 0)
    return 3**even if swapped else 3**c - 2**(c+1) + 2


def main():
    for n in range(2, 7):
        vertices, adj = graph(n)
        maxima = maximal_cliques(adj)
        assert Counter(map(len, maxima)) == expected_maximal(n)
        assert len(maxima) == 3**n-2**(n+1)+2
        for clique in maxima:
            chosen = {vertices[j] for j in clique}
            offdiag = {(a,b) for a,b in chosen if a != b}
            if not offdiag:
                assert chosen == {(i,i) for i in range(n)}
            else:
                S = {a for a,b in offdiag}
                T = {b for a,b in offdiag}
                assert not S & T
                assert chosen == {(a,b) for a in S for b in T} | {(v,v) for v in range(n) if v not in S|T}
        if n <= 5:
            actual = all_cliques(adj)
            predicted = clique_coefficients_formula(n)
            assert actual == predicted, ('clique polynomial', n, actual, predicted)
            assert sum((-1)**k*v for k,v in enumerate(actual)) == (-1)**(n+1)*(2**n-2)
        index = {u:k for k,u in enumerate(vertices)}
        for permutation in permutations(range(n)):
            for swapped in (False, True):
                fixed = 0
                for clique in maxima:
                    transformed = frozenset(index[(permutation[b], permutation[a]) if swapped else (permutation[a],permutation[b])] for i in clique for a,b in [vertices[i]])
                    fixed += (transformed == clique)
                assert fixed == expected_fixed(n, permutation, swapped), ('character',n,permutation,swapped,fixed)
        print('n', n, 'maximal', len(maxima), 'fixed-permutation action', 'PASS', 'all-cliques' if n <= 5 else 'all-cliques skipped')
    print('VERIFY_OK_BRANDT_CLIQUES_CHARACTER')

if __name__ == '__main__':
    main()
