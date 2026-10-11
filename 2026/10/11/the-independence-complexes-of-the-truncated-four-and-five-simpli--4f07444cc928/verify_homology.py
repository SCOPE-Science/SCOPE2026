"""Independent field-chain verification for low-dimensional truncated simplices.

Run: python verify_homology.py
Uses a partial-function enumeration, not the graph-independent-set enumerator.
"""
from collections import defaultdict
from itertools import product


def enumerate_faces(n):
    arcs = [(a, b) for a in range(n) for b in range(n) if a != b]
    labels = {arc: index for index, arc in enumerate(arcs)}
    by_dimension = defaultdict(list)
    for choices in product(range(-1, n), repeat=n):
        if any(choices[a] == a for a in range(n)):
            continue
        if any(choices[a] >= 0 and choices[choices[a]] == a
               for a in range(n) if choices[a] >= 0):
            continue
        mask = 0
        for a, b in enumerate(choices):
            if b >= 0:
                mask |= 1 << labels[a, b]
        if mask:
            by_dimension[mask.bit_count() - 1].append(mask)
    for d in by_dimension:
        by_dimension[d].sort()
    return by_dimension


def boundary_rank_mod_p(lower, upper, p):
    rows = {x: j for j, x in enumerate(lower)}
    basis = {}
    for s in upper:
        entries = {}
        bitset = s
        pos = 0
        while bitset:
            bit = bitset & -bitset
            bitset -= bit
            row = rows[s ^ bit]
            entries[row] = (1 if pos % 2 == 0 else p - 1)
            pos += 1
        while entries:
            pivot = max(entries)
            value = entries[pivot]
            if pivot not in basis:
                inv = pow(value, -1, p)
                basis[pivot] = {k: v * inv % p for k, v in entries.items()}
                break
            elimination = basis[pivot]
            for k, v in elimination.items():
                new = (entries.get(k, 0) - value * v) % p
                if new:
                    entries[k] = new
                elif k in entries:
                    del entries[k]
    return len(basis)


def analyze(n, p):
    by_dimension = enumerate_faces(n)
    dimensions = sorted(by_dimension)
    f = [len(by_dimension[d]) for d in dimensions]
    ranks = [0] + [boundary_rank_mod_p(by_dimension[d - 1], by_dimension[d], p)
                   for d in dimensions[1:]]
    betti = [f[d] - ranks[d] - (ranks[d + 1] if d + 1 < len(ranks) else 0)
             for d in dimensions]
    betti[0] -= 1
    target = {5: [0, 0, 0, 5, 23], 6: [0, 0, 0, 0, 6, 967]}[n]
    assert betti == target, (n, p, betti)
    print('n=%d field=F_%d f=%s ranks=%s reduced_Betti=%s' % (n, p, f, ranks, betti))


if __name__ == '__main__':
    for n in (5, 6):
        for p in (2, 3, 5):
            analyze(n, p)
    print('INDEPENDENT FIELD VERIFICATION PASSED')
