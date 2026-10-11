#!/usr/bin/env python3
from itertools import permutations, combinations


def tonnetz_facets(k: int):
    """Facets of Tonn^{k+1,k}(1,...,1,2), directly from Definition 1.3."""
    n = k + 1
    lengths = (2,) + (1,) * (k - 1)
    increment_orders = sorted(set(permutations(lengths)))
    facets = set()
    for x in range(n):
        for order in increment_orders:
            s = x
            face = [x]
            for a in order[:-1]:
                s = (s + a) % n
                face.append(s)
            assert len(set(face)) == k
            facets.add(tuple(sorted(face)))
    return facets


def boundary_facets(k: int):
    verts = set(range(k + 1))
    return {tuple(sorted(verts - {missing})) for missing in verts}


def face_vector_from_facets(facets):
    faces = set()
    for facet in facets:
        for r in range(1, len(facet) + 1):
            faces.update(combinations(facet, r))
    maxdim = max(len(f) for f in faces) - 1
    return tuple(sum(1 for f in faces if len(f) == d + 1) for d in range(maxdim + 1))


def expected_face_vector(k: int):
    # Boundary of a k-simplex: all nonempty proper subsets of k+1 vertices.
    import math
    return tuple(math.comb(k + 1, r) for r in range(1, k + 1))


def symbolic_position_check(k: int):
    """Check the proof's prefix-sum description for every position of the 2."""
    n = k + 1
    for x in range(n):
        for pos in range(k):
            order = [1] * k
            order[pos] = 2
            # Remove one 1 so there are k entries total: one 2 and k-1 ones.
            del order[-1 if pos != k - 1 else 0]
            # Rebuild more transparently to avoid depending on deletion indexing.
            order = [1] * (k - 1)
            order.insert(pos, 2)
            s = x
            face = [x]
            for a in order[:-1]:
                s = (s + a) % n
                face.append(s)
            assert len(set(face)) == k
            missing = set(range(n)) - set(face)
            assert len(missing) == 1


def main():
    rows = []
    for k in range(4, 11):
        actual = tonnetz_facets(k)
        expected = boundary_facets(k)
        assert actual == expected
        fv = face_vector_from_facets(actual)
        assert fv == expected_face_vector(k)
        symbolic_position_check(k)
        rows.append((k, len(actual), fv))
    # The direct symbolic coverage step used in the proof: placing the 2 last
    # gives the facet {x,x+1,...,x+k-1}, which misses x-1 mod k+1.
    for k in range(4, 65):
        n = k + 1
        seen_missing = set()
        for x in range(n):
            face = {(x + j) % n for j in range(k)}
            missing = set(range(n)) - face
            assert missing == {(x - 1) % n}
            seen_missing |= missing
        assert seen_missing == set(range(n))
    print("definition_vs_boundary_checked_k=4..10")
    for k, nf, fv in rows:
        print(f"k={k} facets={nf} f_vector={fv}")
    print("coverage_identity_checked_k=4..64")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
