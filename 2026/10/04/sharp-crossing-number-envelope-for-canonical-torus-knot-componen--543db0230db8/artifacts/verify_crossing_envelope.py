from math import gcd


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def depth_pairs(u):
    pairs = {(1, 1)}
    for _ in range(u):
        nxt = set()
        for a, b in pairs:
            nxt.add((a + b, b))
            nxt.add((a, a + b))
        pairs = nxt
    assert len(pairs) == 2 ** u
    return pairs


def crossing(P, Q):
    assert 2 <= P < Q and gcd(P, Q) == 1
    return P * (Q - 1)


def canonical_split(P, Q):
    p = pow(Q, -1, P)
    r = (p * Q - 1) // P
    q, s = P - p, Q - r
    assert min(p, q, r, s) > 0
    assert p * s - q * r == 1
    return p, q, r, s


def sub_length(a, b):
    a, b = sorted((a, b))
    count = 0
    while (a, b) != (1, 1):
        b -= a
        a, b = sorted((a, b))
        count += 1
    return count


def knots_for_uv(u, v):
    d = v - u
    rows = []
    for a, b in depth_pairs(u):
        P = a + b
        Q = d * P + b
        rows.append((P, Q, crossing(P, Q), a, b))
        p, q, r, s = canonical_split(P, Q)
        lengths = sorted((sub_length(p, q), sub_length(r, s)))
        assert lengths == [u, v], ((u, v), (P, Q), (p, q, r, s), lengths)
    assert len({(P, Q) for P, Q, *_ in rows}) == 2 ** u
    return rows


def check_pairwise():
    for u in range(0, 13):
        for v in range(u + 1, 15):
            d = v - u
            rows = knots_for_uv(u, v)
            min_formula = d * (u + 2) ** 2
            max_formula = fib(u + 3) * (d * fib(u + 3) + fib(u + 2) - 1)
            min_knot = (u + 2, d * (u + 2) + 1)
            max_knot = (fib(u + 3), d * fib(u + 3) + fib(u + 2))
            cvals = [r[2] for r in rows]
            assert min(cvals) == min_formula
            assert max(cvals) == max_formula
            mins = [(P, Q) for P, Q, c, *_ in rows if c == min_formula]
            maxs = [(P, Q) for P, Q, c, *_ in rows if c == max_formula]
            assert mins == [min_knot], ((u, v), mins, min_knot)
            assert maxs == [max_knot], ((u, v), maxs, max_knot)


def check_global():
    for n in range(1, 25):
        all_rows = []
        for u in range((n - 1) // 2 + 1):
            v = n - u
            all_rows.extend(knots_for_uv(u, v))
        best = max(c for _, _, c, *_ in all_rows)
        best_knots = sorted((P, Q) for P, Q, c, *_ in all_rows if c == best)
        if n == 1:
            expected = 4
            expected_knots = [(2, 3)]
        elif n == 2:
            expected = 8
            expected_knots = [(2, 5)]
        elif n == 3:
            expected = 12
            expected_knots = [(2, 7), (3, 5)]
        else:
            u = (n - 1) // 2
            d = n - 2 * u
            P = fib(u + 3)
            Q = d * P + fib(u + 2)
            expected = P * (Q - 1)
            expected_knots = [(P, Q)]
        assert best == expected, (n, best, expected)
        assert best_knots == expected_knots, (n, best_knots, expected_knots)


if __name__ == "__main__":
    check_pairwise()
    check_global()
    print("VERIFY_OK pairwise u<=12,v<=14 and global n<=24")
