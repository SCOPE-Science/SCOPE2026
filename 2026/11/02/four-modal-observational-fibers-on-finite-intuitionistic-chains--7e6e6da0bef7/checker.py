"""Exhaustive finite tests for observational fibers of the four intuitionistic modal operations."""
from collections import Counter, defaultdict
from itertools import product


def extrema(row, n):
    members = [j for j in range(n) if (row >> j) & 1]
    return (min(members), max(members)) if members else (n, -1)


def signature(rows, n):
    m, M = zip(*(extrema(row, n) for row in rows))
    P, H = [], []
    p, h = -1, -1
    for j in range(n):
        p = max(p, M[j]); h = max(h, m[j]); P.append(p); H.append(h)
    Q, K = [0] * n, [0] * n
    q, k = n, n
    for j in range(n - 1, -1, -1):
        q = min(q, M[j]); k = min(k, m[j]); Q[j] = q; K[j] = k
    return tuple(map(tuple, (P, Q, H, K)))


def direct_profile(rows, n):
    """Interpret four connectives literally on every persistent one-atom valuation."""
    out = []
    for j in range(n + 1):
        U = sum(1 << k for k in range(j, n))
        for s in range(n):
            hit = lambda t: bool(rows[t] & U)
            contained = lambda t: (rows[t] & ~U) == 0
            out.extend((
                any(hit(t) for t in range(s + 1)),
                all(hit(t) for t in range(s, n)),
                any(contained(t) for t in range(s + 1)),
                all(contained(t) for t in range(s, n)),
            ))
    return tuple(out)


def predicted_fiber(sig, n):
    P, Q, H, K = sig
    prod = 1
    for i in range(n):
        pprev = -1 if i == 0 else P[i - 1]
        hprev = -1 if i == 0 else H[i - 1]
        qnext = n if i == n - 1 else Q[i + 1]
        knext = n if i == n - 1 else K[i + 1]
        row_total = 0
        for row in range(1 << n):
            m, M = extrema(row, n)
            if (max(pprev, M) == P[i] and min(M, qnext) == Q[i]
                and max(hprev, m) == H[i] and min(m, knext) == K[i]):
                row_total += 1
        prod *= row_total
    return prod


def verify(n):
    profiles = defaultdict(set)
    counts = Counter()
    sig2direct = {}
    direct2sig = {}
    for rows in product(range(1 << n), repeat=n):
        sig = signature(rows, n)
        prof = direct_profile(rows, n)
        if sig in sig2direct:
            assert sig2direct[sig] == prof
        else:
            sig2direct[sig] = prof
        if prof in direct2sig:
            assert direct2sig[prof] == sig
        else:
            direct2sig[prof] = sig
        counts[sig] += 1
    assert len(sig2direct) == len(direct2sig)
    assert sum(counts.values()) == 2 ** (n * n)
    for sig, actual in counts.items():
        assert predicted_fiber(sig, n) == actual, (n, sig, actual)
    expected_classes = {1: 2, 2: 16, 3: 279, 4: 7171}
    expected_max = {1: 1, 2: 1, 3: 8, 4: 324}
    assert len(counts) == expected_classes[n]
    assert max(counts.values()) == expected_max[n]
    print(f'n={n}; relations={2**(n*n)}; signatures={len(counts)}; largest_fiber={max(counts.values())}')


def bound_example(n):
    """All rows contain both endpoints; interiors vary without changing the operators."""
    base = (1 << 0) | (1 << (n - 1))
    sig = None
    for interiors in product(range(1 << (n-2)), repeat=n):
        rows = tuple(base | (v << 1) for v in interiors)
        if sig is None: sig = signature(rows, n)
        else: assert signature(rows, n) == sig
    assert predicted_fiber(sig, n) >= 2 ** (n * (n - 2))
    print(f'n={n}; guaranteed_indistinguishable_relations={2**(n*(n-2))}')

if __name__ == '__main__':
    for n in range(1, 5):
        verify(n)
    for n in (3, 4):
        bound_example(n)
    print('ALL_CHECKS_OK')
