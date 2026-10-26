"""Independent finite verification of ternary Hamming majority-colouring claims.

Run: python3 checker.py
No third-party modules required. Finite computations complement, but do not
replace, the all-dimensions mathematical proof in RESULT.md.
"""
from itertools import combinations, product

ALPHABET = range(3)


def color3(a, b, c):
    if c == 2:
        return "A"
    if b < 2:
        return "B" if c == 0 else "C"
    return "D"


def hamming_adjacent(x, y):
    return sum(a != b for a, b in zip(x, y)) == 1


def colors(d):
    assert d >= 3 and d % 2 == 1
    for v in product(ALPHABET, repeat=d):
        yield v, (color3(*v[:3]),) + v[3::2]


def check_dimension(d):
    assignments = dict(colors(d))
    assert len(assignments) == 3 ** d
    assert len(set(assignments.values())) == 4 * 3 ** ((d - 3) // 2)
    minimum_internal_degree = 2 * d
    for vertex, col in assignments.items():
        internal = 0
        for coord in range(d):
            for new_value in ALPHABET:
                if new_value == vertex[coord]:
                    continue
                neighbor = vertex[:coord] + (new_value,) + vertex[coord + 1 :]
                internal += assignments[neighbor] == col
        assert internal >= d, (vertex, d, col, internal)
        minimum_internal_degree = min(minimum_internal_degree, internal)
    return minimum_internal_degree


def check_small_classes():
    vertices = list(product(ALPHABET, repeat=3))
    adj = [sum(1 << j for j, w in enumerate(vertices) if hamming_adjacent(v, w))
           for v in vertices]
    totals = {}
    for size in range(1, 6):
        tested = 0
        for members in combinations(range(27), size):
            tested += 1
            mask = sum(1 << i for i in members)
            degrees = [(adj[i] & mask).bit_count() for i in members]
            assert min(degrees) < 3, (size, members)
        totals[size] = tested
    assert totals == {1:27, 2:351, 3:2925, 4:17550, 5:80730}, totals
    return totals


def check_four_classes():
    classes = {}
    for v, col in colors(3):
        classes.setdefault(col[0], []).append(v)
    assert {k: len(vs) for k, vs in classes.items()} == {
        "A":9, "B":6, "C":6, "D":6
    }
    degrees = {}
    for k, vs in classes.items():
        degrees[k] = min(sum(hamming_adjacent(u, w) for w in vs) for u in vs)
    assert degrees == {"A":4, "B":3, "C":3, "D":3}, degrees
    return degrees


if __name__ == "__main__":
    tested = check_small_classes()
    degree = check_four_classes()
    high = {dimension: check_dimension(dimension) for dimension in (3, 5, 7, 9)}
    print("VERIFY_OK", "small_subsets", tested,
          "base_internal_degrees", degree, "odd_dimensions", high)
