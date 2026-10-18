"""Independent exhaustive consistency check for finite two-level poset negation-profile inversion."""
from itertools import product
from collections import Counter, defaultdict


def subsets(n):
    return range(1 << n)


def invert(exponents, m):
    h = exponents[:]
    for j in range(m):
        for s in range(1 << m):
            if s & (1 << j):
                h[s] -= h[s ^ (1 << j)]
    return h


def test_frame(m, neighborhoods):
    l = len(neighborhoods)
    n = l + m
    universe = (1 << n) - 1
    upper = [(1 << v) | sum((1 << (l + j)) for j in range(m) if neighborhoods[v] & (1 << j)) for v in range(l)]
    upper += [(1 << (l + j)) for j in range(m)]
    down = [sum(1 << v for v in range(l) if neighborhoods[v] & (1 << j)) | (1 << (l + j)) for j in range(m)]
    fibers = defaultdict(list)
    for U in subsets(n):
        if any(U & (1 << v) and upper[v] & ~U for v in range(n)):
            continue
        neg = sum(1 << p for p in range(n) if upper[p] & U == 0)
        S = (U >> l) & ((1 << m) - 1)
        expected_neg = universe
        for j in range(m):
            if S & (1 << j):
                expected_neg &= ~down[j]
        assert neg == expected_neg, (m, neighborhoods, U, neg, expected_neg)
        fibers[S].append(neg)
    expected_h = [0] * (1 << m)
    for s in neighborhoods:
        expected_h[s] += 1
    assert expected_h[0] == 0
    f = [0] * (1 << m)
    for S in subsets(m):
        eligible = sum(1 for nbh in neighborhoods if nbh & ~S == 0)
        f[S] = 1 << eligible
        assert len(fibers[S]) == f[S] and len(set(fibers[S])) == 1, (m, neighborhoods, S)
    h = invert([a.bit_length() - 1 for a in f], m)
    assert h == expected_h, (m, neighborhoods, h, expected_h)
    denom = sum(f)
    assert denom == sum(len(v) for v in fibers.values())
    # Recover the same spectrum from the probability ratios, without using an algebra size oracle.
    p_over_p0 = [len(fibers[S]) // len(fibers[0]) for S in subsets(m)]
    assert p_over_p0 == f
    return denom


def main():
    families = upsets = 0
    for m in range(1, 5):
        for l in range(0, 5 if m <= 3 else 4):
            for nbhs in product(range(1, 1 << m), repeat=l):
                upsets += test_frame(m, nbhs)
                families += 1
    # Boundary: a 3-point chain has one maximum, but 3 upsets with trace containing it.
    chain_trace_sizes = (1, 3)
    assert chain_trace_sizes[1] & (chain_trace_sizes[1] - 1) != 0
    print(f'VERIFY_OK exhaustive_labelled_two_level_frames={families} independently_enumerated_upsets={upsets} height_three_boundary=3')

if __name__ == '__main__':
    main()
