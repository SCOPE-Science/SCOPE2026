"""Standalone finite checks for reversal-fixed bidirected-path multipath complexes.
Run: python verify.py
Uses only the Python standard library.
"""
from itertools import combinations


def arcs(n):
    return [(i, i + 1) for i in range(n)] + [(i + 1, i) for i in range(n)]


def is_multipath(edge_list):
    ind = {}
    outd = {}
    for u, v in edge_list:
        outd[u] = outd.get(u, 0) + 1
        ind[v] = ind.get(v, 0) + 1
        if outd[u] > 1 or ind[v] > 1:
            return False
    # On an underlying path, a directed cycle is necessarily a two-cycle.
    return all((v, u) not in edge_list for u, v in edge_list)


def reversal(n, arc):
    return (n - arc[0], n - arc[1])


def orbit_pairs(n):
    all_arcs = set(arcs(n))
    seen = set()
    output = []
    for a in sorted(all_arcs):
        if a in seen:
            continue
        b = reversal(n, a)
        assert b in all_arcs and b != a
        seen.update((a, b))
        output.append((a, b))
    assert len(seen) == 2 * n
    return output


def fixed_face(n, chosen_orbits):
    chosen = [arc for o in chosen_orbits for arc in o]
    return is_multipath(chosen)


def band(n):
    t = (n - 1) // 2
    low = list(range(t))
    high = list(range(n - t, n))
    return t, low, high


def check_all_faces(n):
    os = orbit_pairs(n)
    # label orbit by its forward arc's index
    orbit_at = {next(u for u, v in o if v == u + 1): o for o in os}
    t, low, high = band(n)
    admissible = low + high
    for i in range(n):
        assert fixed_face(n, [orbit_at[i]]) == (i in admissible)
    for i, j in combinations(admissible, 2):
        predicted = not ((i in low and j in high or i in high and j in low)
                         and abs(i + j - (n - 1)) <= 1)
        assert fixed_face(n, [orbit_at[i], orbit_at[j]]) == predicted
    # Complete face check, independent from the pair test.
    counts = [0] * (len(admissible) + 1)
    for mask in range(1 << len(admissible)):
        I = [admissible[j] for j in range(len(admissible)) if mask >> j & 1]
        actual = fixed_face(n, [orbit_at[i] for i in I])
        predicted = all(abs(i + j - (n - 1)) > 1
                        for i, j in combinations(I, 2)
                        if ((i in low and j in high) or (j in low and i in high)))
        assert actual == predicted, (n, mask)
        if actual:
            counts[len(I)] += 1
    euler = sum((-1) ** (k - 1) * counts[k] for k in range(1, len(counts)))
    sphere_dimension = (t + 1) // 2 - 1
    assert euler == 1 + (-1) ** sphere_dimension, (n, euler, sphere_dimension)
    return len(admissible), sum(counts), sphere_dimension


def neighborhood_graph(t):
    N = {('L', i): set() for i in range(t)}
    N.update({('H', i): set() for i in range(t)})
    for i in range(t):
        for j in range(t):
            if abs(i - j) <= 1:
                u, v = ('L', i), ('H', j)
                N[u].add(v)
                N[v].add(u)
    return N


def delete_by_fold(N, dominated, dominator):
    assert dominated != dominator and dominated in N and dominator in N
    assert dominator not in N[dominated]
    assert N[dominator] <= N[dominated], (dominated, dominator)
    for neighbor in N[dominated]:
        N[neighbor].remove(dominated)
    del N[dominated]


def check_fold(t):
    N = neighborhood_graph(t)
    a = 0
    while a + 1 < t:
        delete_by_fold(N, ('L', a + 1), ('L', a))
        delete_by_fold(N, ('H', a + 1), ('H', a))
        a += 2
    survivors = list(N)
    assert len(survivors) == 2 * ((t + 1) // 2)
    assert all(len(v) == 1 for v in N.values())
    assert all(next(iter(N[v])) != v for v in N)
    return t - ((t + 1) // 2)


def check_sign(n):
    a = (n - 1) // 2
    b = ((n - 1) // 2 + 1) // 2 - 1
    predicted = -1 if n % 8 in (1, 2, 3, 4) else 1
    assert (-1) ** (a + b) == predicted


def main():
    for n in range(3, 14):
        v, faces, b = check_all_faces(n)
        check_sign(n)
        print(f'n={n}: {v} admissible orbit vertices, {faces} faces including empty, fixed S^{b}')
    total = 0
    for t in range(1, 121):
        total += check_fold(t)
    for n in (1, 2):
        assert not any(fixed_face(n, [o]) for o in orbit_pairs(n))
    print(f'PASS: full fixed-face enumeration n=3..13; 120 folding certificates; n=1,2 empty; sign periodicity.')
    print(f'Fold vertex-pair removals checked: {total}.')

if __name__ == '__main__':
    main()
