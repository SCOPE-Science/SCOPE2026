"""Independently verify the exact 48-row maximizing census and symmetry orbit."""
from itertools import product, permutations
from math import gcd
from pathlib import Path
import sys


def determinant(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def coordinates(index):
    assert 0 <= index < 125
    return (index // 25 - 2, (index // 5) % 5 - 2, index % 5 - 2)


def main(filename):
    lines = Path(filename).read_text(encoding="utf-8").splitlines()
    assert lines[0] == "a\tb\tc\td\tn_a\tn_b\tn_c\tn_d"
    assert len(lines) == 49
    census = set()
    for line in lines[1:]:
        fields = [int(t) for t in line.split("\t")]
        assert len(fields) == 8
        idx, counts = fields[:4], fields[4:]
        assert idx == sorted(set(idx))
        vertices = tuple(coordinates(j) for j in idx)
        cofactors = [((-1) ** j) * determinant(*[vertices[k] for k in range(4) if k != j]) for j in range(4)]
        assert all(cofactors) and (all(c > 0 for c in cofactors) or all(c < 0 for c in cofactors))
        primitive = [abs(c) // gcd(*cofactors) for c in cofactors]
        assert primitive == counts
        assert sorted(counts) == [15, 18, 20, 26]
        assert sum(counts) == 79
        assert all(sum(c * v[d] for c, v in zip(counts, vertices)) == 0 for d in range(3))
        canonical = frozenset(zip(vertices, counts))
        assert len(canonical) == 4
        census.add(canonical)
    assert len(census) == 48
    representative = frozenset({
        ((-2, -2, -2), 15), ((-2, 1, 2), 20),
        ((1, 2, -2), 18), ((2, -1, 1), 26)
    })
    assert representative in census
    orbit = set()
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            orbit.add(frozenset((tuple(signs[d] * v[perm[d]] for d in range(3)), n)
                                for v, n in representative))
    assert len(orbit) == 48 and orbit == census
    print("ORBIT_OK maxima=48 symmetry_group=48 orbit_size=48 unique_orbits=1")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "extremizers.tsv")
