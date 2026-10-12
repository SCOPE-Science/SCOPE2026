import itertools
import math


def gl_order(d, q):
    if d == 0:
        return 1
    ans = 1
    for i in range(d):
        ans *= q ** d - q ** i
    return ans


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for first in range(n + 1):
        for rest in compositions(n - first, k - 1):
            yield (first,) + rest


def formula_tuple_count(n, m, q):
    g = gl_order(n, q)
    return sum(
        g // math.prod(gl_order(d, q) for d in profile)
        for profile in compositions(n, 2 ** m)
    )


def formula_idempotent_count(n, q):
    g = gl_order(n, q)
    return sum(
        g // (gl_order(r, q) * gl_order(n - r, q))
        for r in range(n + 1)
    )


def matmul(a, b, n, q):
    return tuple(
        sum(a[i * n + k] * b[k * n + j] for k in range(n)) % q
        for i in range(n)
        for j in range(n)
    )


def matrices(n, q):
    return itertools.product(range(q), repeat=n * n)


def idempotents(n, q):
    out = []
    for raw in matrices(n, q):
        a = tuple(raw)
        if matmul(a, a, n, q) == a:
            out.append(a)
    return out


def commute(a, b, n, q):
    return matmul(a, b, n, q) == matmul(b, a, n, q)


def check_pairs(n, q, expected):
    idem = idempotents(n, q)
    assert len(idem) == formula_idempotent_count(n, q)
    direct = sum(1 for a in idem for b in idem if commute(a, b, n, q))
    closed = formula_tuple_count(n, 2, q)
    assert direct == closed == expected, (n, q, direct, closed, expected)
    print("PAIR", n, q, direct)


def check_triples(n, q, expected):
    idem = idempotents(n, q)
    direct = 0
    for a in idem:
        for b in idem:
            if not commute(a, b, n, q):
                continue
            for c in idem:
                if commute(a, c, n, q) and commute(b, c, n, q):
                    direct += 1
    closed = formula_tuple_count(n, 3, q)
    assert direct == closed == expected, (n, q, direct, closed, expected)
    print("TRIPLE", n, q, direct)


if __name__ == "__main__":
    for case in [(1, 2, 4), (2, 2, 40), (2, 3, 76), (2, 5, 184), (3, 2, 1012)]:
        check_pairs(*case)
    for case in [(2, 2, 176), (2, 3, 344)]:
        check_triples(*case)
    print("VERIFY_OK")
