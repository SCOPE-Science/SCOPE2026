#!/usr/bin/env python3
"""Exact finite tests for a dihedral character formula for wheel discrete-Morse complexes.

No optional packages. This checks finite cases, not the infinite proof.
"""
from itertools import product


def wheel(k):
    assert k >= 3
    a = {0: tuple(range(1, k + 1))}
    for i in range(k):
        a[i + 1] = tuple(sorted({0, 1 + ((i - 1) % k), 1 + ((i + 1) % k)}))
    return a


def sym(k, reflection, shift):
    return tuple([0] + [1 + ((shift - i if reflection else shift + i) % k)
                         for i in range(k)])


def permutation_orbits(g):
    seen = set()
    answer = []
    for v in range(len(g)):
        if v not in seen:
            orbit = []
            u = v
            while u not in seen:
                orbit.append(u)
                seen.add(u)
                u = g[u]
            assert u == v
            answer.append(tuple(orbit))
    return answer


def determinant_integer(M):
    """Fraction-free Bareiss elimination with row pivoting."""
    A = [list(row) for row in M]
    n = len(A)
    if n == 0:
        return 1
    sign, previous = 1, 1
    for p in range(n - 1):
        if A[p][p] == 0:
            swap = next((q for q in range(p + 1, n) if A[q][p]), None)
            if swap is None:
                return 0
            A[p], A[swap] = A[swap], A[p]
            sign = -sign
        pivot = A[p][p]
        for i in range(p + 1, n):
            for j in range(p + 1, n):
                numerator = A[i][j] * pivot - A[i][p] * A[p][j]
                assert numerator % previous == 0
                A[i][j] = numerator // previous
        for i in range(p + 1, n):
            A[i][p] = 0
        previous = pivot
    return sign * A[-1][-1]


def quotient_determinant(k, g):
    """Det(I-L) for the orbit multigraph of admissible directed arcs."""
    adj = wheel(k)
    orbits = permutation_orbits(g)
    where = {v: j for j, orbit in enumerate(orbits) for v in orbit}
    n = len(orbits)
    I_minus_L = [[int(i == j) for j in range(n)] for i in range(n)]
    for i, orbit in enumerate(orbits):
        rep = orbit[0]
        for target in adj[rep]:
            t = target
            for _ in orbit:
                t = g[t]
            if t != target or where[target] == i:
                continue
            j = where[target]
            I_minus_L[i][i] -= 1
            I_minus_L[i][j] += 1
    return determinant_integer(I_minus_L)


def is_directed_forest(next_vertex):
    n = len(next_vertex)
    for initial in range(n):
        visited = set()
        v = initial
        while v is not None and v not in visited:
            visited.add(v)
            v = next_vertex[v]
        if v is not None:
            return False
    return True


def orbit_forest_sum(k, g):
    """Directly enumerate equivariant choices, without determinant calculation."""
    adj = wheel(k)
    orbit_choices = []
    for orbit in permutation_orbits(g):
        rep = orbit[0]
        possibilities = []
        for target in (None,) + adj[rep]:
            now = target
            choices = {}
            for v in orbit:
                choices[v] = now
                now = None if now is None else g[now]
            if now == target:
                possibilities.append(choices)
        orbit_choices.append(possibilities)
    result = 0
    for opts in product(*orbit_choices):
        parent = [None] * (k + 1)
        orbit_arcs = 0
        for d in opts:
            for v, p in d.items():
                parent[v] = p
            orbit_arcs += any(p is not None for p in d.values())
        if is_directed_forest(parent):
            result += (-1) ** orbit_arcs
    return result


def top_character(k, reflection, shift):
    if not reflection:
        return k ** 3 if shift % k == 0 else 0
    return 0 if k % 2 == 0 else (-1) ** ((k - 1) // 2)


def sign_of_reordering(sequence):
    inversions = sum(sequence[i] > sequence[j] for i in range(len(sequence))
                     for j in range(i + 1, len(sequence)))
    return (-1) ** inversions


def exhaustive_augmented_chain_trace(k):
    """A separate chain-level enumeration of ALL simplices for small wheels."""
    adj = wheel(k)
    options = [(None,) + adj[v] for v in range(k + 1)]
    faces = []
    for choices in product(*options):
        if is_directed_forest(choices):
            faces.append(tuple(sorted((v, p) for v, p in enumerate(choices) if p is not None)))
    assert () in faces
    expected_count = len(faces)
    for reflection in (False, True):
        for shift in range(k):
            g = sym(k, reflection, shift)
            trace = 0
            for face in faces:
                if not face:
                    trace -= 1
                    continue
                permuted = tuple((g[a], g[b]) for a, b in face)
                if set(permuted) == set(face):
                    trace += (-1) ** (len(face) - 1) * sign_of_reordering(permuted)
            predicted_trace = (-1) ** (k - 1) * top_character(k, reflection, shift)
            assert trace == predicted_trace, (k, reflection, shift, trace, predicted_trace)
    return expected_count


def main():
    cases = 0
    for k in range(5, 13):
        for reflection in (False, True):
            for shift in range(k):
                g = sym(k, reflection, shift)
                predicted = top_character(k, reflection, shift)
                qdet = quotient_determinant(k, g)
                direct = orbit_forest_sum(k, g) if (reflection or shift != 0 or k <= 6) else qdet
                assert qdet == direct == ((-1) ** k) * predicted, (k, reflection, shift, qdet, direct, predicted)
                cases += 1
        if k % 2 == 0:
            assert (k * k) // 2 * (2 * k) == k ** 3
        else:
            assert (k * k - 1) // 2 * (2 * k) + k == k ** 3
    chain_counts = {k: exhaustive_augmented_chain_trace(k) for k in (5, 6, 7)}
    print('QUOTIENT_ORBIT_CASES', cases)
    print('ALL_FACE_CHECKS', chain_counts)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
