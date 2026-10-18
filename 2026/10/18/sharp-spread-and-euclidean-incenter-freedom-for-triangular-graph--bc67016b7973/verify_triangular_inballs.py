"""Independent finite exact checks of a Johnson-graph transport inball theorem.
Run with Python 3 (standard library only); no external files or libraries.
"""
from itertools import combinations
from math import comb


def rank_fraction(rows):
    from fractions import Fraction
    a = [[Fraction(v) for v in row] for row in rows]
    if not a:
        return 0
    pivots = 0
    for col in range(len(a[0])):
        found = next((j for j in range(pivots, len(a)) if a[j][col]), None)
        if found is None:
            continue
        a[pivots], a[found] = a[found], a[pivots]
        d = a[pivots][col]
        for k in range(col, len(a[0])):
            a[pivots][k] /= d
        for j in range(pivots + 1, len(a)):
            d = a[j][col]
            if d:
                for k in range(col, len(a[0])):
                    a[j][k] -= d * a[pivots][k]
        pivots += 1
        if pivots == len(a):
            return pivots
    return pivots


def exhaustive(n):
    edges = list(combinations(range(n), 2))
    N = len(edges)
    adj_prior = [tuple(j for j in range(i) if len(set(edges[i]) & set(edges[j])) == 1)
                 for i in range(N)]
    x = [0] * N
    top = -1
    winners = set()
    count = 0

    def rec(i, minimum, total, squares):
        nonlocal top, winners, count
        if i == N:
            if minimum:
                return
            count += 1
            score = N * squares - total * total
            if score > top:
                top = score
                winners = {tuple(x)}
            elif score == top:
                winners.add(tuple(x))
            return
        for val in (0, 1, 2):
            if any(abs(val-x[j]) > 1 for j in adj_prior[i]):
                continue
            x[i] = val
            rec(i+1, min(minimum, val), total + val, squares+val*val)

    rec(0, 3, 0, 0)
    expected_score = N*(n-2)*((n*n)//4)//n
    assert top == expected_score, (n, top, expected_score)
    balanced = set()
    for k in (n//2, (n+1)//2):
        for upper in combinations(range(n), k):
            up = set(upper)
            vals = [int(a in up) + int(b in up) for a,b in edges]
            vmin = min(vals)
            balanced.add(tuple(z-vmin for z in vals))
    assert winners == balanced, (n, len(winners), len(balanced))
    print('n=%d N=%d tested %d normalized integer potentials; max(N*norm2)=%d; contact facets=%d'
          % (n, N, count, top, len(winners)))


def check_contacts(n):
    E = list(combinations(range(n), 2))
    N = len(E)
    norm = (n-2)*((n*n)//4)  # M*n
    assert norm > 0
    vectors = set()
    for k in (n//2, (n+1)//2):
        for ss in combinations(range(n), k):
            S = set(ss)
            values = [int(a in S) + int(b in S) for a,b in E]
            tot = sum(values)
            centered = tuple(N*v-tot for v in values)
            assert sum(centered) == 0
            assert sum(q*q for q in centered) * n == norm * N*N
            vectors.add(centered)
    target = (comb(n, n//2) if n % 2 == 0 else 2*comb(n, n//2))
    assert len(vectors) == target
    r = rank_fraction(list(vectors))
    assert r == n-1, (n,r)
    print('n=%d: %d contacting normals, span rank %d, predicted center dimension %d'
          % (n, len(vectors), r, N-n))

if __name__ == '__main__':
    for n in range(4, 7):
        exhaustive(n)
    for n in range(4, 9):
        check_contacts(n)
    print('ALL EXACT TRIANGULAR-GRAPH TESTS PASSED')
