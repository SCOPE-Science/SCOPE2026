from itertools import combinations, product


def rank(rows, n):
    rows = list(rows)
    r = 0
    for col in range(n):
        p = next((i for i in range(r, len(rows)) if (rows[i] >> col) & 1), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> col) & 1):
                rows[i] ^= rows[r]
        r += 1
    return r


def rref_subspaces(n, k):
    for pivots in combinations(range(n), k):
        free_slots = []
        for i, p in enumerate(pivots):
            for c in range(p + 1, n):
                if c not in pivots:
                    free_slots.append((i, c))
        for bits in product((0, 1), repeat=len(free_slots)):
            rows = [1 << p for p in pivots]
            for bit, (i, c) in zip(bits, free_slots):
                if bit:
                    rows[i] |= 1 << c
            yield tuple(rows)


def check_doubling(m):
    # H = low m coordinates; W = high m coordinates.
    H = set(range(1 << m))
    z = 1 << m
    A = H | {z}
    sums = {a ^ b for a in A for b in A}
    assert len(A) == (1 << m) + 1
    assert len(sums) == (1 << (m + 1))
    return len(sums), len(A)


def check_structural(m):
    n = 2 * m
    H_basis = tuple(1 << i for i in range(m))
    checked = 0
    for d in range(m + 1):
        for V in rref_subspaces(n, d):
            h = m + d - rank(H_basis + V, n)
            proj_rows = tuple(v >> m for v in V)
            proj_dim = rank(proj_rows, m)
            assert proj_dim == d - h
            min_cover = 1 << (m - h)
            # Any L-coset cover of H requires L >= min_cover.
            # For every such L, the projected union has at most
            # L * 2^proj_dim <= L^2 quotient classes.
            assert (1 << proj_dim) <= min_cover
            for L in (min_cover, min_cover + 1, 2 * min_cover):
                assert L * (1 << proj_dim) <= L * L
            checked += 1
    return checked


def main():
    for m in range(1, 9):
        s, a = check_doubling(m)
        assert s / a < 2

    total = 0
    for m in range(1, 4):
        total += check_structural(m)

    print("doubling identities checked for m=1..8")
    print(f"subspaces checked for m=1..3: {total}")
    print("PASS")


if __name__ == "__main__":
    main()
