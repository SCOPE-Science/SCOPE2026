from itertools import combinations, product


def rref_subspaces(n, q):
    out = []
    for k in range(n + 1):
        for pivots in combinations(range(n), k):
            free = [(i, j) for i, p in enumerate(pivots)
                    for j in range(p + 1, n) if j not in pivots]
            for vals in product(range(q), repeat=len(free)):
                rows = [[0] * n for _ in range(k)]
                for i, p in enumerate(pivots):
                    rows[i][p] = 1
                for (i, j), a in zip(free, vals):
                    rows[i][j] = a
                out.append((tuple(tuple(r) for r in rows), pivots))
    return out


def in_span(v, basis, pivots, q):
    v = list(v)
    for row, p in zip(basis, pivots):
        a = v[p] % q
        if a:
            v = [(x - a * y) % q for x, y in zip(v, row)]
    return all(x % q == 0 for x in v)


def span_rref(rows, q):
    rows = [list(r) for r in rows if any(x % q for x in r)]
    if not rows:
        return tuple(), tuple()
    n = len(rows[0])
    r = 0
    pivots = []
    for c in range(n):
        pivot = next((i for i in range(r, len(rows)) if rows[i][c] % q), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = pow(rows[r][c] % q, -1, q)
        rows[r] = [(inv * x) % q for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % q:
                a = rows[i][c] % q
                rows[i] = [(x - a * y) % q for x, y in zip(rows[i], rows[r])]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    rows = rows[:r]
    return tuple(tuple(x % q for x in row) for row in rows), tuple(pivots)


def bracket(a, b, q):
    z = (a[0] * b[1] - a[1] * b[0] + a[2] * b[3] - a[3] * b[2]) % q
    return (0, 0, 0, 0, z)


def is_subalgebra(basis, pivots, q):
    for i in range(len(basis)):
        for j in range(i + 1, len(basis)):
            if not in_span(bracket(basis[i], basis[j], q), basis, pivots, q):
                return False
    return True


def permutable(A, B, q):
    abasis, _ = A
    bbasis, _ = B
    s_basis, s_pivots = span_rref(abasis + bbasis, q)
    for a in abasis:
        for b in bbasis:
            if not in_span(bracket(a, b, q), s_basis, s_pivots, q):
                return False
    return True


def formula(q):
    N = q**5 + 3*q**4 + 5*q**3 + 6*q**2 + 4*q + 6
    P = (3*q**9 + 12*q**8 + 34*q**7 + 62*q**6 + 91*q**5
         + 111*q**4 + 108*q**3 + 88*q**2 + 48*q + 36)
    return N, P


def check(q):
    subs = [s for s in rref_subspaces(5, q) if is_subalgebra(*s, q)]
    perm = sum(permutable(A, B, q) for A in subs for B in subs)
    expected_n, expected_perm = formula(q)
    assert len(subs) == expected_n
    assert perm == expected_perm
    print(f"q={q}: subalgebras={len(subs)}, permutable_ordered_pairs={perm}")


if __name__ == "__main__":
    check(2)
    check(3)
