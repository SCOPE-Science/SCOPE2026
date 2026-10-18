"""Exact finite checks for graph-variation lattice norms.

Run with Python 3. Uses rational arithmetic only. This verifies finite
orientation inequalities and explicit moment witnesses; the accompanying
proof handles unbounded graph orders and all real conjugate exponents.
"""
from fractions import Fraction
from itertools import product
from collections import Counter


def divergences(n, edges):
    for signs in product((-1, 1), repeat=len(edges)):
        b = [0] * n
        for (u, v), s in zip(edges, signs):
            b[u] += s
            b[v] -= s
        yield tuple(b)


def cycle(n):
    return [(i, (i + 1) % n) for i in range(n)]


def complete(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def friendship(r):
    edges = []
    for h in range(r):
        a, b = 2*h + 1, 2*h + 2
        edges += [(0, a), (0, b), (a, b)]
    return edges


count = Counter()
for n in range(2, 7):
    c = [n + 1 - 2*i for i in range(1, n + 1)]
    prefix = [sum(c[:k]) for k in range(1, n)]
    max_q = {q: sum(abs(x)**q for x in c) for q in range(1, 6)}
    for b in divergences(n, complete(n)):
        s = sorted(b, reverse=True)
        for k in range(1, n):
            assert sum(s[:k]) <= prefix[k-1]
            count['complete_majorization'] += 1
        for q in range(1, 6):
            assert sum(abs(x)**q for x in b) <= max_q[q]
            count['complete_power_bounds'] += 1

for n in range(3, 12):
    top = 2 * (n // 2)
    attained = False
    for b in divergences(n, cycle(n)):
        assert all(x in (-2, 0, 2) for x in b)
        support = sum(x != 0 for x in b)
        assert support <= top
        if support == top:
            attained = True
        count['cycle_support_bounds'] += 1
    assert attained

for r in range(1, 5):
    ed = friendship(r)
    for b in divergences(2*r + 1, ed):
        k = 0
        for h in range(r):
            a, v = b[2*h + 1], b[2*h + 2]
            # Since the triangle's total divergence is zero,
            # its central contribution is minus the two leaf divergences.
            local_c = -(a + v)
            assert local_c in (-2, 0, 2)
            k += bool(local_c)
        assert abs(b[0]) <= 2*k
        for q in range(1, 6):
            assert abs(b[0])**q <= (2*r)**q * Fraction(k, r)
            assert sum(abs(x)**q for x in b[1:]) <= 2**q*(2*r-k)
            count['friendship_pointwise'] += 1
    # Exact two-design moment certificate; extreme weights 2/3, middle 1/3.
    extreme = []
    for leaf_signs in product((-1, 1), repeat=r):
        div = [0]*(2*r+1)
        for h, z in enumerate(leaf_signs):
            a, v = 2*h+1, 2*h+2
            div[0] += 2
            div[a] += -1+z
            div[v] += -1-z
        extreme.append(tuple(div))
    middle = [0]*(2*r+1)
    for h in range(r):
        a, v = 2*h+1, 2*h+2
        middle[a], middle[v] = -2, 2
    assert tuple(middle) in set(divergences(2*r+1, ed))
    for b in extreme:
        assert b in set(divergences(2*r+1, ed))
    for q in range(1, 6):
        moments = [Fraction(1, 3)*abs(middle[i])**q +
                   Fraction(2, 3*len(extreme))*sum(abs(b[i])**q for b in extreme)
                   for i in range(2*r+1)]
        assert moments[0] == Fraction(2, 3)*(2*r)**q
        assert all(v == Fraction(2, 3)*2**q for v in moments[1:])
        count['friendship_moment_witness'] += 1

print('PASS: exact orientation inequalities and explicit norming moments')
print(dict(count))
