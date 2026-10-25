"""Reproducible finite checks for circular-ladder primitive screw fixed loci.

The proof for all widths is combinatorial and does not depend on these tests.
Run: python VERIFY.py
"""
from itertools import combinations
from math import gcd


def data(n):
    edges = sorted(set(
        [tuple(sorted((n * a + i, n * a + (i + 1) % n)))
         for a in (0, 1) for i in range(n)]
        + [(i, n + i) for i in range(n)]))
    lookup = {edge: j for j, edge in enumerate(edges)}
    adjacent = [[] for _ in range(2 * n)]
    for j, (a, b) in enumerate(edges):
        adjacent[a].append((b, j))
        adjacent[b].append((a, j))
    perfect = []

    def rec(remaining, selected):
        if not remaining:
            perfect.append(tuple(selected))
            return
        a = min(remaining)
        for b, j in adjacent[a]:
            if b in remaining:
                rec(remaining - {a, b}, selected + [j])

    rec(set(range(2 * n)), [])
    faces = {0}
    for matching in perfect:
        for choice in range(1 << n):
            mask = 0
            for i, j in enumerate(matching):
                if choice >> i & 1:
                    mask |= 1 << j
            faces.add(mask)
    return edges, lookup, faces, len(perfect)


def fixed_faces_and_lefschetz(n, edges, lookup, faces, shift, swap):
    def move(v):
        return n * ((v // n) ^ swap) + ((v % n + shift) % n)

    induced = [lookup[tuple(sorted((move(a), move(b))))]
               for a, b in edges]
    invariant = []
    augmented_signed_sum = 0
    for face in faces:
        old = [i for i in range(len(edges)) if face >> i & 1]
        transformed = [induced[i] for i in old]
        if set(transformed) != set(old):
            continue
        invariant.append(face)
        inversions = sum(transformed[i] > transformed[j]
                         for i in range(len(transformed))
                         for j in range(i + 1, len(transformed)))
        augmented_signed_sum += (-1) ** (len(old) + inversions)
    return set(invariant), -augmented_signed_sum


def expected_support(n, edges, lookup, k, swap):
    rung = frozenset(lookup[(i, n + i)] for i in range(n))
    if not swap or n % 2:
        return {0, sum(1 << j for j in rung)}
    groups = []
    for parity in (0, 1):
        group = []
        for i in range(n):
            a = parity if i % 2 == 0 else 1 - parity
            u = n * a + i
            v = n * a + (i + 1) % n
            group.append(lookup[tuple(sorted((u, v)))])
        groups.append(sum(1 << j for j in group))
    return {0, sum(1 << j for j in rung), *groups}


def main():
    actions = 0
    face_tests = 0
    for n in range(3, 11):
        edges, lookup, faces, n_perfect = data(n)
        for k in range(1, n):
            if gcd(n, k) != 1:
                continue
            for swap in (0, 1):
                fixed, lefschetz = fixed_faces_and_lefschetz(
                    n, edges, lookup, faces, k, swap)
                predicted_faces = expected_support(n, edges, lookup, k, swap)
                predicted_lefschetz = 2 if (swap and n % 2 == 0) else 0
                assert fixed == predicted_faces, (n, k, swap, fixed, predicted_faces)
                assert lefschetz == predicted_lefschetz, (n, k, swap, lefschetz)
                assert len(fixed) == 1 + (3 if swap and n % 2 == 0 else 1)
                actions += 1
                face_tests += len(faces)
        print(f'n={n}: {n_perfect} perfect matchings; '
              f'{len(faces)} faces; all primitive actions PASS')
    print(f'PASS: {actions} primitive symmetry actions, '
          f'{face_tests} face-action membership checks.')


if __name__ == '__main__':
    main()
