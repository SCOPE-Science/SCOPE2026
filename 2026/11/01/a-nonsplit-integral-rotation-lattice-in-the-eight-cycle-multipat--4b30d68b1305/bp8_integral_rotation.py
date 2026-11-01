"""Exact finite verification for the bidirected eight-cycle multipath complex.

Python 3, standard library only. Enumerate every simplex, construct cochain
coboundaries over F_2, and compute the action of rotation on H^3(F_2).
"""

N = 8
ARCS = [(i, (i + 1) % N) for i in range(N)] + [((i + 1) % N, i) for i in range(N)]
FWD = (1 << N) - 1


def add_basis(basis, vec, label=0):
    """Insert an F_2 vector, retaining the expression in quotient generators."""
    while vec:
        pivot = vec.bit_length() - 1
        if pivot in basis:
            old, old_label = basis[pivot]
            vec ^= old
            label ^= old_label
        else:
            basis[pivot] = (vec, label)
            return True
    assert label == 0, "Unexpected relation among quotient generators"
    return False


def simplex_faces():
    faces = [[] for _ in range(N)]
    for mask in range(1, 1 << (2 * N)):
        # All-forward or all-backward arrows create a directed full cycle.
        if (mask & FWD) == FWD or (mask >> N) == FWD:
            continue
        if any((mask >> i) & 1 and (mask >> (i + N)) & 1 for i in range(N)):
            continue  # Directed two-cycle.
        indeg, outdeg = [0] * N, [0] * N
        for i, (src, dst) in enumerate(ARCS):
            if (mask >> i) & 1:
                outdeg[src] += 1
                indeg[dst] += 1
        if max(indeg) > 1 or max(outdeg) > 1:
            continue
        faces[mask.bit_count() - 1].append(mask)
    return faces


def main():
    faces = simplex_faces()
    indices = [{s: j for j, s in enumerate(level)} for level in faces]
    assert [len(level) for level in faces] == [16, 96, 272, 384, 272, 96, 16, 0]

    def coboundary(k):
        """Columns of C^k -> C^(k+1), using exact unsigned F_2 incidences."""
        cols = []
        for sigma in faces[k]:
            col = 0
            for vertex in range(2 * N):
                if not (sigma >> vertex) & 1:
                    tau = sigma | (1 << vertex)
                    if tau in indices[k + 1]:
                        col |= 1 << indices[k + 1][tau]
            cols.append(col)
        return cols

    def rank(columns):
        pivots = {}
        for v in columns:
            add_basis(pivots, v)
        return len(pivots)

    d2, d3 = coboundary(2), coboundary(3)
    assert rank(d2) == 191
    assert rank(d3) == 190
    assert 384 - 190 - 191 == 3

    # Gaussian elimination on the rows of the degree-three coboundary.
    rows = []
    for row in range(len(faces[4])):
        rows.append(sum(1 << col for col, v in enumerate(d3) if (v >> row) & 1))
    equations = {}
    for v in rows:
        add_basis(equations, v)
    assert len(equations) == 190

    # Nullspace basis, with one free coordinate per vector.
    free = [i for i in range(len(faces[3])) if i not in equations]
    nullspace = []
    for free_idx in free:
        cocycle = 1 << free_idx
        for p in sorted(equations):
            if (equations[p][0] & cocycle).bit_count() & 1:
                cocycle ^= 1 << p
        nullspace.append(cocycle)
    assert len(nullspace) == 194

    # Build a quotient basis in ker(delta^3)/im(delta^2), recording
    # coordinates of all stored elimination vectors in H^3(F_2).
    labeled_basis = {}
    for v in d2:
        add_basis(labeled_basis, v)
    classes = []
    for v in nullspace:
        probe = v
        while probe:
            p = probe.bit_length() - 1
            if p in labeled_basis:
                probe ^= labeled_basis[p][0]
            else:
                break
        if probe:
            add_basis(labeled_basis, v, 1 << len(classes))
            classes.append(v)
    assert len(classes) == 3

    def cohomology_coordinates(vec):
        coeff = 0
        while vec:
            p = vec.bit_length() - 1
            assert p in labeled_basis, "Rotated cocycle left the cohomology span"
            old, old_label = labeled_basis[p]
            vec ^= old
            coeff ^= old_label
        return coeff

    columns = []
    for cocycle in classes:
        rotated = 0
        for j, simplex in enumerate(faces[3]):
            if (cocycle >> j) & 1:
                image = 0
                for arc in range(2 * N):
                    if (simplex >> arc) & 1:
                        mapped_arc = (arc // N) * N + (arc % N + 1) % N
                        image |= 1 << mapped_arc
                rotated ^= 1 << indices[3][image]
        columns.append(cohomology_coordinates(rotated))

    assert columns == [7, 4, 1], columns
    a_minus_i = [columns[i] ^ (1 << i) for i in range(3)]
    assert rank(a_minus_i) == 2

    def multiply(x):
        y = 0
        for i, col in enumerate(columns):
            if (x >> i) & 1:
                y ^= col
        return y

    assert all(multiply(multiply(multiply(multiply(x)))) == x for x in range(8))
    assert sum((-1) ** k * len(f) for k, f in enumerate(faces)) - 1 == -1
    print("FACES 16 96 272 384 272 96 16")
    print("COBOUNDARY_RANKS degree2=191 degree3=190")
    print("H3_F2_DIMENSION 3")
    print("ROTATION_COLUMNS_BINARY 7 4 1")
    print("RANK_ROTATION_MINUS_IDENTITY 2")
    print("FIXED_DIMENSION 1")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
