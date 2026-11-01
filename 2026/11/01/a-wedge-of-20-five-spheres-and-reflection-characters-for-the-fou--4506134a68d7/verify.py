"""Exact finite certificate for the four-robust clique complex of P3 x P4.

Uses only Python's standard library. All simplices and codimension-one
relations are constructed directly from the stated graph and definitions.
"""

from collections import Counter, deque
from itertools import combinations, product
from hashlib import sha256
import json

ROWS, COLS = 3, 4
VERTICES = tuple(product(range(ROWS), range(COLS)))
N = len(VERTICES)
ORDER = (1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6)
EXPECTED_CRITICAL = (2, 221, 252, 629, 753, 1241, 1272, 1621, 1649,
                     1652, 1740, 2205, 2236, 2261, 2292, 2737, 3276,
                     3281, 3312, 3724, 3780)
EXPECTED_FACES = (12, 66, 220, 434, 466, 217)
EXPECTED_CHARACTER = {(0, 0): 20, (0, 1): -4,
                      (1, 0): 0, (1, 1): 0}


def bits(mask):
    return tuple(i for i in range(N) if mask & (1 << i))


def graph_edges():
    return frozenset((i, j) for i, j in combinations(range(N), 2)
                     if sum(abs(a - b) for a, b in
                            zip(VERTICES[i], VERTICES[j])) == 1)


def build_complex():
    edges = graph_edges()
    forbidden = tuple(sum(1 << i for i in c)
                      for c in combinations(range(N), 4)
                      if all((i, j) not in edges for i, j in combinations(c, 2)))
    faces = frozenset(mask for mask in range(1, 1 << N)
                      if all((mask & bad) != bad for bad in forbidden))
    # Independent definition check: for every face and nonface, enumerate
    # all its own four-subsets, without using the precomputed masks.
    for mask in range(1, 1 << N):
        subset = bits(mask)
        has_independent_four = any(
            all((i, j) not in edges for i, j in combinations(q, 2))
            for q in combinations(subset, 4))
        assert (mask in faces) == (not has_independent_four)
    assert len(forbidden) == 61
    assert sum(1 for f in forbidden if all((i // COLS + i % COLS) % 2 == 0
                                           for i in bits(f))) == 15
    assert sum(1 for f in forbidden if all((i // COLS + i % COLS) % 2 == 1
                                           for i in bits(f))) == 15
    assert len(faces) == 1415
    fvec = tuple(sum(mask.bit_count() == d + 1 for mask in faces)
                 for d in range(6))
    assert fvec == EXPECTED_FACES
    assert all(mask.bit_count() <= 6 for mask in faces)
    return faces, forbidden, fvec


def construct_matching(faces):
    remaining = set(faces)
    pairs = []
    for v in ORDER:
        one = 1 << v
        for lower in sorted(remaining):
            higher = lower | one
            if (lower & one) == 0 and higher in remaining:
                assert lower in remaining
                assert higher in faces
                assert higher.bit_count() == lower.bit_count() + 1
                pairs.append((lower, higher))
                remaining.remove(lower)
                remaining.remove(higher)
    assert len(pairs) == 697
    assert len(set(pairs)) == len(pairs)
    assert len(remaining) == 21
    assert tuple(sorted(remaining)) == EXPECTED_CRITICAL
    assert Counter(mask.bit_count() - 1 for mask in remaining) == {0: 1, 5: 20}
    assert 2 * len(pairs) + len(remaining) == len(faces)
    return frozenset(pairs), frozenset(remaining)


def verify_gradient_acyclicity(faces, pairs):
    # Face poset cover relations: high -> low, except matched edges reversed.
    indegree = {mask: 0 for mask in faces}
    adjacency = {mask: [] for mask in faces}
    num_incidence = 0
    for higher in faces:
        for i in bits(higher):
            lower = higher ^ (1 << i)
            if lower == 0:
                continue
            assert lower in faces
            num_incidence += 1
            start, end = ((lower, higher) if (lower, higher) in pairs
                          else (higher, lower))
            adjacency[start].append(end)
            indegree[end] += 1
    q = deque(node for node in faces if indegree[node] == 0)
    removed = 0
    while q:
        node = q.popleft()
        removed += 1
        for following in adjacency[node]:
            indegree[following] -= 1
            if indegree[following] == 0:
                q.append(following)
    assert removed == len(faces), "A directed gradient cycle was detected"
    assert num_incidence > 0
    return num_incidence


def permutation_character(faces, flip_rows, flip_columns):
    action = tuple(VERTICES.index((ROWS - 1 - r if flip_rows else r,
                                    COLS - 1 - c if flip_columns else c))
                   for r, c in VERTICES)
    assert sorted(action) == list(range(N))
    chain_trace = Counter()
    for face in faces:
        original = bits(face)
        images = tuple(action[i] for i in original)
        if frozenset(images) != frozenset(original):
            continue
        inversions = sum(images[i] > images[j]
                         for i in range(len(images))
                         for j in range(i + 1, len(images)))
        chain_trace[len(original) - 1] += (-1) ** inversions
    lefschetz = sum((-1) ** d * trace for d, trace in chain_trace.items())
    # There is one trivial H_0 and only H_5 in positive degrees.
    return 1 - lefschetz


def run():
    faces, forbidden, fvec = build_complex()
    pairs, remaining = construct_matching(faces)
    incidences = verify_gradient_acyclicity(faces, pairs)
    character = {(r, c): permutation_character(faces, r, c)
                 for r, c in product(range(2), repeat=2)}
    assert character == EXPECTED_CHARACTER
    # Orthogonality of the four one-dimensional characters of C2 x C2.
    multiplicities = {(r_sign, c_sign):
                      sum(character[(r, c)] * r_sign ** r * c_sign ** c
                          for r, c in product(range(2), repeat=2)) // 4
                      for r_sign, c_sign in product((-1, 1), repeat=2)}
    assert multiplicities == {(1, 1): 4, (-1, 1): 4,
                              (1, -1): 6, (-1, -1): 6}
    assert sum(multiplicities.values()) == 20
    assert sum((-1) ** d * count for d, count in enumerate(fvec)) == -19
    print('VERIFY_OK')
    print('vertices=12 forbidden_independent_4=61 mixed_independent_4=31')
    print('faces=1415 f_vector=' + str(fvec))
    print('matched_pairs=697 critical_cells=(one_0,twenty_5)')
    print('hasse_incidences=' + str(incidences) + ' gradient_DAG=1415')
    print('reflections_H5_character=' + str(character))
    print('rational_irrep_multiplicities=' + str(multiplicities))
    digest = sha256(json.dumps(sorted(pairs), separators=(',', ':')).encode()).hexdigest()
    print('matching_sha256=' + digest)
    return digest


if __name__ == '__main__':
    run()
