#!/usr/bin/env python3
"""Exact checks for the one-step image language of the binary majority sliding-block map.

Uses only the Python standard library. Finite checks support, but do not replace,
the automaton induction proving the all-length statements.
"""
from itertools import product
from fractions import Fraction
import math

PAIRS = ((0, 0), (0, 1), (1, 0), (1, 1))
SINK = 0
START = 15
EXPECTED = {
    0: (0, 0), 1: (3, 0), 2: (4, 8), 3: (7, 8),
    4: (1, 2), 5: (3, 2), 7: (7, 10), 8: (0, 12),
    10: (4, 12), 12: (1, 14), 14: (5, 14), 15: (7, 14),
}
FORBIDDEN = ('01001', '01101', '10010', '10110', '0100010', '1011101')

def trans(q, output):
    a = set()
    for i, (u, v) in enumerate(PAIRS):
        if q & (1 << i):
            for w in (0, 1):
                if (u + v + w >= 2) == bool(output):
                    a.add((v, w))
    return sum(1 << PAIRS.index(z) for z in a)

def read(q, word):
    for a in word:
        q = trans(q, int(a))
    return q

def matrix_product(A, vec):
    return [sum(A[i][j] * vec[j] for j in range(len(vec))) for i in range(len(vec))]

def brute_language(n):
    found = set()
    for x in product((0, 1), repeat=n + 2):
        found.add(''.join(str(int(sum(x[i:i + 3]) >= 2)) for i in range(n)))
    return found

def main():
    assert {q: (trans(q, 0), trans(q, 1)) for q in EXPECTED} == EXPECTED
    reached = {START}
    frontier = [START]
    while frontier:
        q = frontier.pop()
        for nxt in EXPECTED[q]:
            if nxt not in reached:
                reached.add(nxt)
                frontier.append(nxt)
    assert reached == set(EXPECTED) and len(reached) == 12
    Q = tuple(sorted(reached - {0}))
    # Pairs whose two nonempty resulting states remain different under one output word.
    P = {(q, r) for q in Q for r in Q if q != r}
    counts = [len(P)]
    for _ in range(6):
        P = {(EXPECTED[q][b], EXPECTED[r][b]) for q, r in P for b in (0, 1)
             if EXPECTED[q][b] and EXPECTED[r][b]
             and EXPECTED[q][b] != EXPECTED[r][b]}
        counts.append(len(P))
    assert counts == [110, 40, 24, 12, 8, 4, 0], counts
    # All allowed 6-letter suffixes act as unambiguous state resets.
    for bits in product('01', repeat=6):
        w = ''.join(bits)
        destinations = {read(q, w) for q in Q} - {0}
        assert len(destinations) <= 1
    # Exact minimal forbidden words through length seven.
    language = {''}
    minimal = []
    all_counts = [1]
    for n in range(1, 14):
        words = {w + a for w in language for a in '01'}
        bad = sorted(w for w in words if read(START, w) == 0
                     and read(START, w[1:]) != 0)
        if n <= 7:
            minimal.extend(bad)
        language = {w for w in words if read(START, w) != 0}
        all_counts.append(len(language))
        if n <= 12:
            assert language == brute_language(n)
        assert language == {w for w in map(''.join, product('01', repeat=n))
                            if not any(f in w for f in FORBIDDEN)}
    assert tuple(sorted(minimal)) == tuple(sorted(FORBIDDEN)), minimal
    assert all_counts == [1, 2, 4, 8, 16, 28, 50, 88, 156, 278,
                          496, 886, 1582, 2824], all_counts
    # Matrix certificate for the unrestricted linear recurrence.
    M = [[0] * len(Q) for _ in Q]
    for i, q in enumerate(Q):
        for nxt in EXPECTED[q]:
            if nxt:
                M[i][Q.index(nxt)] += 1
    v = [1] * len(Q)
    vs = [v]
    for _ in range(5):
        vs.append(matrix_product(M, vs[-1]))
    identity = [vs[5][i] - 2 * vs[4][i] + vs[2][i] - vs[0][i]
                for i in range(len(Q))]
    assert identity == [-int(q == START) for q in Q]
    assert all(START not in EXPECTED[q] for q in Q)
    # Independent integer characteristic-polynomial certificate (Faddeev--LeVerrier).
    nstates = len(Q)
    B = [[int(i == j) for j in range(nstates)] for i in range(nstates)]
    char = [1]
    for k in range(1, nstates + 1):
        AB = [[sum(M[i][t] * B[t][j] for t in range(nstates))
               for j in range(nstates)] for i in range(nstates)]
        trace = sum(AB[i][i] for i in range(nstates))
        assert trace % k == 0
        ck = -trace // k
        char.append(ck)
        B = [[AB[i][j] + (ck if i == j else 0) for j in range(nstates)]
             for i in range(nstates)]
    def mul(a, b):
        z = [0] * (len(a) + len(b) - 1)
        for i, p in enumerate(a):
            for j, q in enumerate(b): z[i+j] += p*q
        return z
    assert char == mul(mul([1,0,0,1,0,-1], [1,-2,0,1,0,-1]), [1,0])
    # Hence a[n+5]-2a[n+4]+a[n+2]-a[n]=0 for n>=1.
    for n in range(1, 9):
        assert all_counts[n+5] - 2*all_counts[n+4] + all_counts[n+2] - all_counts[n] == 0
    # For A(z)=sum a[n] z^n, D(z)A(z)=N(z).
    D = (1, -2, 0, 1, 0, -1)
    N = (1, 0, 0, 1, 2, -1)
    for n in range(6):
        assert sum(D[j]*all_counts[n-j] for j in range(n+1)) == N[n]
    assert sum(D[j]*all_counts[6-j] for j in range(6)) == 0
    # Unique real root >1 of lambda^5 - 2lambda^4 + lambda^2 -1.
    def poly(x): return x**5 - 2*x**4 + x*x - 1
    lo, hi = 1.78, 1.79
    assert poly(lo) < 0 < poly(hi)
    for _ in range(85):
        mid = (lo+hi)/2
        if poly(mid) > 0: hi = mid
        else: lo = mid
    root = (lo+hi)/2
    h = math.log(root)
    assert abs(root-1.78459893336865) < 3e-14
    assert abs(h-0.579193702797223) < 3e-14
    print(f'VERIFY_OK: 12 deterministic states; reset ambiguity {counts}; six minimal words; '
          f'{len(all_counts)} exact block counts; exact matrix identity; '
          f'lambda={root:.14f}; h={h:.14f}')

if __name__ == '__main__':
    main()
