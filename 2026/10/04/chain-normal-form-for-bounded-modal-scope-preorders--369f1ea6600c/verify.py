#!/usr/bin/env python3
from itertools import product

def chain_relation(n):
    return {(i, j) for i in range(n) for j in range(n) if i <= j}

def is_transitive(R):
    for a, b in R:
        for bb, c in R:
            if b == bb and (a, c) not in R:
                return False
    return True

def classes(n, R):
    unseen = set(range(n))
    out = []
    while unseen:
        x = min(unseen)
        C = {y for y in range(n) if (x, y) in R and (y, x) in R}
        out.append(tuple(sorted(C)))
        unseen -= C
    return out

def from_blocks(blocks):
    R = set()
    for i, A in enumerate(blocks):
        for j, B in enumerate(blocks):
            if i <= j:
                for a in A:
                    for b in B:
                        R.add((a, b))
    return R

def generated_from_bits(n, bits):
    blocks = []
    start = 0
    for i, cut in enumerate(bits):
        if cut:
            blocks.append(tuple(range(start, i + 1)))
            start = i + 1
    blocks.append(tuple(range(start, n)))
    return frozenset(from_blocks(blocks))

for n in range(1, 7):
    base = chain_relation(n)
    reverse_candidates = [(j, i) for i in range(n) for j in range(i + 1, n)]

    valid = set()
    for mask in range(1 << len(reverse_candidates)):
        R = set(base)
        for k, edge in enumerate(reverse_candidates):
            if (mask >> k) & 1:
                R.add(edge)
        if not is_transitive(R):
            continue

        Cs = classes(n, R)

        # Classes are intervals.
        for C in Cs:
            assert C == tuple(range(min(C), max(C) + 1))

        # They occur left to right and reconstruct the relation exactly.
        Cs = sorted(Cs, key=lambda C: C[0])
        assert from_blocks(Cs) == R

        ell = {}
        for C in Cs:
            for x in C:
                ell[x] = C[0]

        assert ell[0] == 0
        for i in range(n - 1):
            assert ell[i + 1] in (ell[i], i + 1)

        for d in range(n):
            for e in range(n):
                assert (((d, e) in R) == (ell[d] <= e))

        for d in range(n):
            for b in range(n):
                direct = {e for e in range(n) if (d, e) in R and b <= e}
                suffix = {e for e in range(n) if e >= max(ell[d], b)}
                assert direct == suffix

        valid.add(frozenset(R))

    assert len(valid) == 2 ** (n - 1), (n, len(valid))

    generated = {
        generated_from_bits(n, bits)
        for bits in product([0, 1], repeat=max(0, n - 1))
    }
    assert generated == valid

print("VERIFY_OK")
