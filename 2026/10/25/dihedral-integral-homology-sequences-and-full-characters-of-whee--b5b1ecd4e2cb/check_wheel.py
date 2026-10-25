"""Exact finite checks for dihedral characters of wheel matching complexes.

Scientific computation only: finite enumerations are not proofs for all n.
Run: python3 check_wheel.py
"""
from math import gcd


def path_eval(j):
    if j == -1:
        return 1
    if j == 0:
        return 1
    a, b = 1, 0
    for _ in range(2, j + 1):
        a, b = b, b - a
    return b


def cycle_eval(d):
    return (2, 1, -1, -2, -1, 1)[d % 6]


def cycle_degree(n):
    return (n // 3) if n % 3 == 2 else (n // 3 - 1)


def wheel_degree(n):
    return (n - 1) // 3 if n % 3 else n // 3 - 1


def cycle_char(n, kind, a):
    if kind == 'rotation':
        L = -cycle_eval(gcd(n, a))
    elif n & 1:
        q = n // 2
        L = -path_eval(q - 1) + path_eval(q - 2)
    elif (a - 1) % 2 == 0:
        L = -path_eval(n // 2 + 1)
    else:
        L = -path_eval(n // 2 - 2)
    return (-1) ** cycle_degree(n) * L


def spoke_stabilizer_sign(k):
    return (-1) ** (k * (k - 1) // 2)


def predicted_character(n, kind, a):
    c = cycle_char(n, kind, a)
    fixed = (n if a == 0 else 0) if kind == 'rotation' else sum(1 for j in range(n) if (a - j) % n == j)
    if n % 3 == 0:
        return c
    if n % 3 == 1:
        return c * (fixed - 1)
    if kind == 'rotation':
        return c + (n if a == 0 else 0)
    return c + fixed * spoke_stabilizer_sign(n // 3)


def independent_rim_masks(n):
    for mask in range(1 << n):
        if mask & (mask << 1):
            continue
        if mask & 1 and mask & (1 << (n - 1)):
            continue
        yield mask


def wheel_faces(n):
    for rim in independent_rim_masks(n):
        yield rim
        for j in range(n):
            if rim & (1 << j) or rim & (1 << ((j - 1) % n)):
                continue
            yield rim | (1 << (n + j))


def vertex_action(n, kind, a, wheel):
    rim = [(j + a) % n if kind == 'rotation' else (a - j - 1) % n for j in range(n)]
    if not wheel:
        return rim
    return rim + [n + ((j + a) % n if kind == 'rotation' else (a - j) % n) for j in range(n)]


def direct_character(faces, perm, degree):
    reduced_lefschetz = -1  # empty simplex in augmented chains
    for face in faces:
        if face == 0:
            continue
        idx = [j for j in range(len(perm)) if face >> j & 1]
        mapped = [perm[j] for j in idx]
        if set(mapped) != set(idx):
            continue
        inversions = sum(mapped[i] > mapped[j] for i in range(len(idx)) for j in range(i + 1, len(idx)))
        reduced_lefschetz += (-1) ** (len(idx) - 1 + inversions)
    return (-1) ** degree * reduced_lefschetz


def gf2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            p = col.bit_length() - 1
            if p in pivots:
                col ^= pivots[p]
            else:
                pivots[p] = col
                break
    return len(pivots)


def mod2_betti(n):
    by_degree = {}
    for face in wheel_faces(n):
        if face:
            by_degree.setdefault(face.bit_count() - 1, []).append(face)
    dims = sorted(by_degree)
    ranks = {}
    for d in dims[1:]:
        prev = {f: i for i, f in enumerate(by_degree[d - 1])}
        columns = []
        for face in by_degree[d]:
            bitset = 0
            s = face
            while s:
                bit = s & -s
                s -= bit
                bitset ^= 1 << prev[face ^ bit]
            columns.append(bitset)
        ranks[d] = gf2_rank(columns)
    return {d: len(by_degree[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0) - (1 if d == 0 else 0)
            for d in dims}


def main():
    character_checks = 0
    for n in range(3, 19):
        faces = tuple(wheel_faces(n))
        rim = tuple(independent_rim_masks(n))
        for kind in ('rotation', 'reflection'):
            for a in range(n):
                wheel_perm = vertex_action(n, kind, a, True)
                cycle_perm = vertex_action(n, kind, a, False)
                observed = direct_character(faces, wheel_perm, wheel_degree(n))
                expected = predicted_character(n, kind, a)
                assert observed == expected, (n, kind, a, observed, expected)
                cycle_observed = direct_character(rim, cycle_perm, cycle_degree(n))
                assert cycle_observed == cycle_char(n, kind, a), ('cycle', n, kind, a)
                character_checks += 2
    print('PASS: signed wheel and rim character equalities:', character_checks)
    for n in range(3, 11):
        betti = mod2_betti(n)
        expect = n - 1 if n % 3 == 1 else n + 1 if n % 3 == 2 else 2
        assert betti.get(wheel_degree(n)) == expect, (n, betti, expect)
        assert not {d: v for d, v in betti.items() if d != wheel_degree(n) and v}, (n, betti)
    print('PASS: independent mod-two boundary-matrix homology:', 8, 'wheel sizes')
    print('FINITE CHECKS ONLY; all-parameter proof is the equivariant cone-attachment sequence.')


if __name__ == '__main__':
    main()
