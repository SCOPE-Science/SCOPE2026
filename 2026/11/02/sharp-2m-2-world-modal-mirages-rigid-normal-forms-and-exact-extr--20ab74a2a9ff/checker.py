"""Finite checks for the modal separation-extremizer theorem.

Run with Python 3 standard library.  All relations are represented by outgoing
bitmask rows; enumeration is exact for the stated finite domains only.
"""
from itertools import permutations
from math import factorial
import random


def iteration(rows):
    """Truth masks of top, (box diamond)top, ... through stabilization."""
    n = len(rows)
    allbits = (1 << n) - 1
    out = [allbits]
    for _ in range(n + 2):
        old = out[-1]
        nxt = 0
        for x, rx in enumerate(rows):
            # box diamond old: every successor of x has a successor in old.
            if all(rows[y] & old for y in range(n) if (rx >> y) & 1):
                nxt |= 1 << x
        if nxt == old:
            return out
        assert (nxt | old) == old, (n, rows, out)
        out.append(nxt)
    raise AssertionError("No stabilization within n+2 steps")


def strata(rows, maxlevel):
    """Independent direct predecessor construction of N_i and P_i."""
    n = len(rows)
    N = [0]
    P = [sum(1 << x for x, row in enumerate(rows) if row == 0)]
    for _ in range(maxlevel):
        pre = sum(1 << x for x, row in enumerate(rows) if row & P[-1])
        N.append(pre)
        P.append(sum(1 << x for x, row in enumerate(rows) if not row & ~pre))
    return N, P


def labels_and_edges(m):
    """Canonical role labels N_1..N_(m+1), P_0..P_m."""
    n = 2*m + 2
    def N(i): return i - 1
    def P(j): return m + 1 + j
    rows = [0] * n
    opt = []
    for i in range(1, m+2):
        rows[N(i)] |= 1 << P(i-1)
        for l in range(1, m+2):
            opt.append((N(i), N(l)))
        for j in range(i, m+1):
            opt.append((N(i), P(j)))
    for j in range(1, m+1):
        rows[P(j)] |= 1 << N(j)
        for l in range(1, j):
            opt.append((P(j), N(l)))
    assert len(opt) == 2*m*m + 2*m + 1
    return rows, opt


def from_option_bits(base, opts, mask):
    rows = base.copy()
    for i, (u,v) in enumerate(opts):
        if (mask >> i) & 1:
            rows[u] |= 1 << v
    return rows


def test_canonical(m, mask):
    base, opts = labels_and_edges(m)
    rows = from_option_bits(base, opts, mask)
    N, P = strata(rows, m+1)
    for i in range(1, m+2):
        assert N[i] & ~N[i-1] == 1 << (i-1), (m, mask, 'N',i)
    for j in range(m+1):
        assert P[j] & ~(P[j-1] if j else 0) == 1 << (m+1+j), (m,mask,'P',j)
    out = iteration(rows)
    assert (out[m] >> m) & 1
    assert not ((out[m+1] >> m) & 1)
    assert out[m] & ~out[m+1] == 1 << m


def exhaustive_small():
    for n in range(1, 5):
        allbits = (1 << n) - 1
        diff_count = [0] * (n + 1)
        fixed_root_count = [0] * (n + 1)
        for bits in range(1 << (n*n)):
            rows = [(bits >> (n*i)) & allbits for i in range(n)]
            truths = iteration(rows)
            ns, ps = strata(rows, n+1)
            for i in range(len(truths)):
                assert allbits ^ truths[i] == ns[i], (n,rows,i)
            assert all(not (a & b) for a in ns for b in ps)
            for m in range(n):
                tm = truths[m] if m < len(truths) else truths[-1]
                tn = truths[m+1] if m+1 < len(truths) else truths[-1]
                if tm != tn:
                    diff_count[m] += 1
                    if (tm ^ tn) & 1: fixed_root_count[m] += 1
        print('EXHAUSTIVE', n, diff_count, fixed_root_count)
        for m in range(n):
            if n < 2*m+2:
                assert diff_count[m] == 0
            elif n == 2*m+2:
                expected = factorial(n)*(1 << (2*m*m+2*m+1))
                assert diff_count[m] == expected
                assert fixed_root_count[m] == expected//n

if __name__ == '__main__':
    exhaustive_small()
    for m in (0,1,2):
        base, opts = labels_and_edges(m)
        for mask in range(1 << len(opts)):
            test_canonical(m, mask)
        print('CANONICAL_ALL',m,1<<len(opts))
    # Distinct normal forms are nonisomorphic and have no automorphisms
    # in the fully enumerated four-world case.
    m=1
    b, opts=labels_and_edges(m)
    witnesses = [from_option_bits(b,opts,k) for k in range(1<<len(opts))]
    assert len({tuple(rows) for rows in witnesses}) == 32
    for rows in witnesses:
        for perm in permutations(range(4)):
            if perm == tuple(range(4)): continue
            if all(rows[perm[i]] == sum(1 << perm[j] for j in range(4) if rows[i]>>j&1) for i in range(4)):
                raise AssertionError('Unexpected automorphism')
    print('RIGIDITY_4_WORLD_CLASSES',len(witnesses))
    m=3
    _, opts=labels_and_edges(m)
    random.seed(54321)
    for mask in [0,(1<<len(opts))-1]+[random.getrandbits(len(opts)) for _ in range(2000)]:
        test_canonical(m,mask)
    print('CANONICAL_SAMPLED',m,2002)
    for m in range(0,13):
        n=2*m+2
        rows=[(1 << (j+1)) if j+1<n else 0 for j in range(n)]
        truth=iteration(rows)
        assert truth[m] & 1
        assert not truth[m+1] & 1
    print('PATH_WITNESSES',list(range(13)))
    print('ALL_CHECKS_OK')
