from __future__ import annotations


def predicted(r: int, a: int, b: int, terminal: bool) -> bool:
    assert r >= 2 and 1 <= a <= b
    d = b - a
    if terminal:
        return d < r and a < r + d
    return d <= r and a <= r + d


def quotient_ok(r: int, m: int, c: int, terminal: bool) -> bool:
    if m == 1:
        return True
    for k in range(1, m):
        numerator = r * k + (k * c) % m
        if terminal:
            if numerator <= m:
                return False
        else:
            if numerator < m:
                return False
    return True


def local_reid_tai(r: int, a: int, b: int, terminal: bool) -> bool:
    return quotient_ok(r, a, b, terminal) and quotient_ok(r, b, a, terminal)


def global_fractional_part_test(r: int, a: int, b: int, terminal: bool) -> bool:
    weights = [1] * r + [a, b]
    n = len(weights) - 1
    h = sum(weights)
    for k in range(2, h - 1):
        residue_sum = sum((k * w) % h for w in weights)
        assert residue_sum % h == 0
        height = residue_sum // h
        if terminal:
            if not (2 <= height <= n - 1):
                return False
        else:
            if not (1 <= height <= n - 1):
                return False
    return True


def count_formula(r: int, terminal: bool) -> int:
    if terminal:
        return 3 * r * (r - 1) // 2
    return 3 * r * (r + 1) // 2


def main() -> None:
    checked = 0
    for terminal in (False, True):
        for r in range(2, 13):
            # The search box extends well beyond the claimed feasible triangle.
            for a in range(1, 3 * r + 7):
                for b in range(a, a + 3 * r + 7):
                    p = predicted(r, a, b, terminal)
                    q = local_reid_tai(r, a, b, terminal)
                    g = global_fractional_part_test(r, a, b, terminal)
                    assert p == q == g, (r, a, b, terminal, p, q, g)
                    checked += 1

        # Count all predicted pairs in a box known to contain the feasible region.
        for r in range(2, 31):
            total = 0
            for a in range(1, 2 * r + 2):
                for b in range(a, a + r + 2):
                    total += int(predicted(r, a, b, terminal))
            assert total == count_formula(r, terminal), (r, terminal, total)

    print(f"VERIFY_OK cases={checked} r=2..12; pair-count formulas checked through r=30")


if __name__ == "__main__":
    main()
