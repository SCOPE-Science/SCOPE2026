#!/usr/bin/env python3
"""Standalone finite checks for color-permutation Lefschetz traces.

Builds sigma-invariant independent faces as subsets of the original graph,
then evaluates the signed simplicial chain trace. No theorem-formula input
is used to enumerate these faces.
"""
from itertools import permutations
from collections import defaultdict


def cycle_orbits(perm):
    n = len(perm)
    unseen = set(range(n))
    orbits = []
    while unseen:
        x = min(unseen)
        orbit = []
        while x in unseen:
            unseen.remove(x)
            orbit.append(x)
            x = perm[x]
        orbits.append(tuple(orbit))
    return orbits


def invariant_row_masks(perm):
    n = len(perm)
    orbits = cycle_orbits(perm)
    opts = []
    for subset in range(1 << len(orbits)):
        mask = 0
        for j, orbit in enumerate(orbits):
            if (subset >> j) & 1:
                for x in orbit:
                    mask |= 1 << x
        opts.append((mask, -1 if subset.bit_count() % 2 else 1))
    return opts


def compatible(a, b):
    if not a or not b:
        return True
    return a == b and a.bit_count() == 1


def signed_invariant_face_sum(m, perm):
    # A matrix-free, cycle-closure dynamic program on ALL invariant row subsets.
    opts = invariant_row_masks(perm)
    result = 0
    for first, w0 in opts:
        state = {first: w0}
        for _ in range(1, m):
            next_state = defaultdict(int)
            for prev, count in state.items():
                for cur, weight in opts:
                    if compatible(prev, cur):
                        next_state[cur] += count * weight
            state = next_state
        result += sum(count for last, count in state.items()
                      if compatible(last, first))
    return result


def predicted_sum(m, fixed_colors):
    z = fixed_colors - 1
    return 3 * z ** (m // 3) + (-1) ** (m // 3) * z if m % 3 == 0 else (-1) ** m * z


def direct_small_betti(m, n):
    """Independent GF(2) simplicial boundary-rank check on small graphs."""
    verts = [(i, a) for i in range(m) for a in range(n)]
    adj = [0] * (m * n)
    for x, (i, a) in enumerate(verts):
        for y, (j, b) in enumerate(verts):
            if j in {(i - 1) % m, (i + 1) % m} and a != b:
                adj[x] |= 1 << y
    faces = defaultdict(list)
    def generate(pos, chosen, forbidden):
        faces[chosen.bit_count()].append(chosen)
        for x in range(pos, len(verts)):
            if not ((forbidden >> x) & 1):
                generate(x + 1, chosen | (1 << x), forbidden | adj[x] | (1 << x))
    generate(0, 0, 0)
    ranks = {}
    for cardinality in sorted(faces):
        if cardinality == 0:
            continue
        target = {face: i for i, face in enumerate(faces[cardinality - 1])}
        pivots = {}
        for face in faces[cardinality]:
            col = 0
            x = face
            while x:
                bit = x & -x
                x -= bit
                col ^= 1 << target[face - bit]
            while col:
                pivot = col.bit_length() - 1
                if pivot not in pivots:
                    pivots[pivot] = col
                    break
                col ^= pivots[pivot]
        ranks[cardinality] = len(pivots)
    ranks[0] = 0
    betti = {}
    for k, fs in faces.items():
        b = len(fs) - ranks.get(k, 0) - ranks.get(k + 1, 0)
        if b:
            betti[k - 1] = b
    return len(faces), sum(map(len, faces.values())), betti



def direct_original_simplex_lefschetz(m, perm):
    """Independently compute signed chain trace on ordered original vertices."""
    n = len(perm)
    adjacent = [0] * (m * n)
    for i in range(m):
        for a in range(n):
            x = i * n + a
            for j in ((i - 1) % m, (i + 1) % m):
                for b in range(n):
                    if a != b:
                        adjacent[x] |= 1 << (j * n + b)
    total = -1  # augmented empty face in dimension -1
    def visit(start, face, forbidden):
        nonlocal total
        if face:
            original = [k for k in range(m * n) if (face >> k) & 1]
            moved = [n * (x // n) + perm[x % n] for x in original]
            if sorted(moved) == original:
                inversions = sum(moved[i] > moved[j]
                                 for i in range(len(moved)) for j in range(i + 1, len(moved)))
                total += (-1) ** (len(original) - 1 + inversions)
        for x in range(start, m * n):
            if not ((forbidden >> x) & 1):
                visit(x + 1, face | (1 << x), forbidden | adjacent[x] | (1 << x))
    visit(0, 0, 0)
    return total


def main():
    tests = 0
    for n in (2, 3, 4):
        for perm in permutations(range(n)):
            fixed = sum(perm[i] == i for i in range(n))
            for m in range(3, 10):
                found = signed_invariant_face_sum(m, perm)
                expect = predicted_sum(m, fixed)
                if found != expect:
                    raise AssertionError((n, m, perm, found, expect))
                tests += 1
    print('All', tests, 'direct signed-face-trace comparisons passed.')
    original_checks = 0
    for m, n in ((3, 2), (3, 3), (6, 2), (6, 3)):
        for perm in permutations(range(n)):
            f = sum(perm[i] == i for i in range(n))
            direct = direct_original_simplex_lefschetz(m, perm)
            assert direct == -predicted_sum(m, f), (m, n, perm, direct)
            original_checks += 1
    print('All', original_checks, 'original-simplex oriented-chain checks passed.')
    for m, n in ((3, 2), (3, 3), (6, 2), (6, 3)):
        dims, nfaces, groups = direct_small_betti(m, n)
        d = 2 * (m // 3) - 1
        rank = predicted_sum(m, n)
        assert groups == {d: rank}, (m, n, groups, rank)
        print('mod-2 reduced homology:', (m, n),
              'total faces including empty:', nfaces,
              'Betti:', groups)
    print('Finite checks do not establish the infinite theorem or torsion-freeness.')


if __name__ == '__main__':
    main()
