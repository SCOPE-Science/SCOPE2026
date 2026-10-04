from functools import lru_cache

ALL = ("all_rank_zero",)


def blue_type(q, n):
    if q == 0:
        return ALL
    threshold = (1 << q) - 1
    return ("blue", q, min(n, threshold))


@lru_cache(None)
def red_type(q, a, b):
    if q == 0:
        return ALL
    p = q - 1
    chars = {("R", blue_type(p, a), blue_type(p, b))}
    for i in range(a):
        chars.add(("B", blue_type(p, i), red_type(p, a - 1 - i, b)))
    for j in range(b):
        chars.add(("B", red_type(p, a, j), blue_type(p, b - 1 - j)))
    return ("red", q, frozenset(chars))


def canonical(q, a, b):
    if q == 0:
        return ("all",)
    if q == 1:
        return ("only_red",) if a + b == 0 else ("red_and_blue",)
    threshold = (1 << q) - 1
    if a == 0:
        return ("red_first", min(b, threshold))
    if b == 0:
        return ("red_last", min(a, threshold))
    interior = threshold - 1
    return ("red_interior", min(a, interior), min(b, interior))


def check(q, bound):
    by_canonical = {}
    by_type = {}
    for a in range(bound + 1):
        for b in range(bound + 1):
            c = canonical(q, a, b)
            t = red_type(q, a, b)
            old = by_canonical.setdefault(c, t)
            if old != t:
                raise AssertionError(("same canonical, different type", q, a, b, c))
            old_c = by_type.setdefault(t, c)
            if old_c != c:
                raise AssertionError(("same type, different canonical", q, a, b, c, old_c))
    print("VERIFY", q, True, "canons", len(by_canonical))


if __name__ == "__main__":
    for q, bound in [(1, 10), (2, 12), (3, 18), (4, 22)]:
        check(q, bound)
    print("VERIFY_OK")
