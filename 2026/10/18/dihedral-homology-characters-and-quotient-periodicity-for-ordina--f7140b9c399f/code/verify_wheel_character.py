"""Exact finite check of wheel matching-complex dihedral characters.

Python 3 standard library only. Comparisons are exhaustive over all matchings
and group elements in the specified finite range, not a proof of all n.
"""
from math import gcd


def path_eval(m):
    assert m >= 0
    return (1, 0, -1, -1, 0, 1)[m % 6]


def degree_rank(n):
    assert n >= 3
    if n % 3 == 0:
        return n // 3 - 1, 2
    if n % 3 == 1:
        return (n - 1) // 3, n - 1
    return (n - 2) // 3, n + 1


def character(n, a, reflected):
    h, b = degree_rank(n)
    if not reflected:
        if a % n == 0:
            return b
        d = gcd(n, a)
        neg_cycle_eval = (-2, -1, 1, 2, 1, -1)[d % 6]
        return (-1) ** h * neg_cycle_eval
    return 0 if n % 2 else (-1) ** h * path_eval(n // 2 - 2)


def graph_edges(n):
    return [tuple(sorted((j, (j + 1) % n))) for j in range(n)] + [(-1, j) for j in range(n)]


def enumerate_matchings(n):
    # Complete face list, including the empty matching.
    output = []
    for spoke in [-1] + list(range(n)):
        for mask in range(1 << n):
            if any((mask & (1 << i)) and (mask & (1 << ((i + 1) % n))) for i in range(n)):
                continue
            if spoke >= 0 and ((mask >> spoke) & 1 or (mask >> ((spoke - 1) % n)) & 1):
                continue
            output.append(mask | ((1 << (n + spoke)) if spoke >= 0 else 0))
    return output


def index_permutation(n, a, reflected):
    edges = graph_edges(n)
    index = {edge: i for i, edge in enumerate(edges)}

    def transform(v):
        if v == -1:
            return -1
        return (a - v if reflected else a + v) % n

    return [index[tuple(sorted((transform(u), transform(v))))] for u, v in edges]


def signed_trace(n, faces, permutation):
    # Exact augmented chain Lefschetz sum, independent of orbit reduction.
    value = 0
    for face in faces:
        if face == 0:
            value -= 1
            continue
        vertices = [i for i in range(2 * n) if face & (1 << i)]
        mapped = [permutation[i] for i in vertices]
        if set(mapped) != set(vertices):
            continue
        inversions = sum(mapped[i] > mapped[j] for i in range(len(mapped))
                         for j in range(i + 1, len(mapped)))
        value += (-1) ** (len(vertices) - 1 + inversions)
    return value


def check():
    comparisons = 0
    for n in range(3, 17):
        faces = enumerate_matchings(n)
        for reflected in (False, True):
            for a in range(n):
                direct = (-1) ** degree_rank(n)[0] * signed_trace(
                    n, faces, index_permutation(n, a, reflected))
                expected = character(n, a, reflected)
                assert direct == expected, (n, reflected, a, direct, expected)
                comparisons += 1
        print(f"PASS n={n} complete_faces={len(faces)} group_elements={2*n} "
              f"homology_degree={degree_rank(n)[0]} homology_rank={degree_rank(n)[1]}")

    for n in range(3, 241):
        rotations = sum(character(n, a, False) for a in range(n))
        reflections = sum(character(n, a, True) for a in range(n))
        assert rotations % n == 0
        assert (rotations + reflections) % (2 * n) == 0
        quotient_rank = (rotations + reflections) // (2 * n)
        predicted = int(n % 12 in (2, 5, 10, 11))
        assert quotient_rank == predicted, (n, quotient_rank, predicted)
    print(f"VERIFY_OK exact_signed_character_comparisons={comparisons} "
          "quotient_rank_checks=238")


if __name__ == '__main__':
    check()
