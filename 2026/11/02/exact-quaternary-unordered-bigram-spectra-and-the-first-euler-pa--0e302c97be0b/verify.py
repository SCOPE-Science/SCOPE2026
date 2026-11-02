"""Independent integer-profile and literal-word checks for four-letter unordered bigrams.

Run: python3 verify.py. No third-party packages required.
Finite checks support, but do not replace, the all-length graph-theoretic proof.
"""
from itertools import product, combinations_with_replacement
from math import comb

ALPHABET = range(4)
EDGE_TYPES = tuple((i, j) for i in ALPHABET for j in range(i, 4))
EDGE_INDEX = {e: k for k, e in enumerate(EDGE_TYPES)}


def word_profile(w):
    a = [0] * len(EDGE_TYPES)
    for i, j in zip(w, w[1:]):
        a[EDGE_INDEX[min(i, j), max(i, j)]] += 1
    return tuple(a)


def graph_feasible(profile):
    active = set()
    odd = [0] * 4
    adjacency = [set() for _ in ALPHABET]
    for multiplicity, (i, j) in zip(profile, EDGE_TYPES):
        if not multiplicity:
            continue
        active.add(i)
        active.add(j)
        if i != j:
            adjacency[i].add(j)
            adjacency[j].add(i)
            odd[i] ^= multiplicity & 1
            odd[j] ^= multiplicity & 1
    if not active:
        return False
    if sum(odd) not in (0, 2):
        return False
    # Loops never connect different vertices.
    root = min(active)
    reached = {root}
    todo = [root]
    while todo:
        u = todo.pop()
        for v in adjacency[u] - reached:
            reached.add(v)
            todo.append(v)
    return reached == active


def composition_vector(multiplicities):
    a = [0] * 10
    for edge in multiplicities:
        a[edge] += 1
    return tuple(a)


def poly_mul(a, b, n):
    r = [0] * (n + 1)
    for i, u in enumerate(a[:n + 1]):
        if u:
            for j, v in enumerate(b[:n + 1 - i]):
                r[i + j] += u * v
    return r


def gf_coefficients(max_m):
    # Reduced rational function N(z)/((1-z)^10(1+z)^4).
    numerator = [0, 10, -26, 22, 85, -120, -23, 178,
                 -126, -70, 128, -30, -30, 20, -4]
    p = [comb(t + 9, 9) for t in range(max_m + 1)]
    h = [(-1)**t * comb(t + 3, 3) for t in range(max_m + 1)]
    d = poly_mul(p, h, max_m)
    return poly_mul(numerator, d, max_m)


def check():
    predicted = gf_coefficients(13)
    literal_count = 0
    for m in range(1, 9):
        observed = set()
        for w in product(ALPHABET, repeat=m + 1):
            observed.add(word_profile(w))
            literal_count += 1
        assert len(observed) == predicted[m], (m, len(observed), predicted[m])
        assert all(graph_feasible(p) for p in observed)

    # This profile enumeration is independent of the word enumeration.
    profile_count = 0
    for m in range(1, 13):
        feasible = 0
        for multi in combinations_with_replacement(range(10), m):
            if graph_feasible(composition_vector(multi)):
                feasible += 1
            profile_count += 1
        assert feasible == predicted[m], (m, feasible, predicted[m])
    assert predicted[1:13] == [10,34,116,367,1060,2782,6704,14963,31276,61738,116020,208848]
    print('VERIFY_OK', 'literal_lengths=2..9',
          f'literal_words={literal_count}', 'graph_profiles_m=1..12',
          f'profile_vectors_tested={profile_count}',
          'rational_coefficients_m=1..12', 'exact_match=True')

if __name__ == '__main__':
    check()
