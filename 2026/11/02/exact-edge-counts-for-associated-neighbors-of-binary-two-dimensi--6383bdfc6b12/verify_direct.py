"""Direct exhaustive count of associated pairs of binary LCD 2-planes.

Run: python verify_direct.py
All calculations use exact integer arithmetic.
"""
from itertools import combinations


def dot(a, b):
    return ((a & b).bit_count() & 1)


def plane(a, b):
    return frozenset((0, a, b, a ^ b))


def lcd2(p):
    a, b = sorted(p - {0})[:2]
    return ((dot(a, a) * dot(b, b)) ^ dot(a, b)) == 1


def all_lcd_planes(n):
    seen = {plane(a, b) for a in range(1, 1 << n)
            for b in range(a + 1, 1 << n)}
    return sorted((c for c in seen if lcd2(c)), key=lambda c: tuple(sorted(c)))


def associated_direct(c, d):
    intersection = c & d
    if len(intersection) != 2:
        return False
    # Literal definition: N(C,z) = span(C_0(z),z), with
    # z outside C union C^perp, and compare this plane with D.
    for z in d - intersection:
        c0 = frozenset(w for w in c if dot(w, z) == 0)
        if z not in c and len(c0) == 2 and frozenset(
            set(c0) | {z} | {z ^ next(iter(c0 - {0}))}
        ) == d:
            return True
    return False


def predicted(n):
    h = 1 << (n - 2)
    if n % 2 == 0:
        return (1 << (n - 1)) * h * (h - 1) // 4
    return ((1 << (n - 1)) - 1) * h * (h - 2) // 4


def run():
    for n in range(2, 8):
        codes = all_lcd_planes(n)
        count = sum(associated_direct(c, d) for c, d in combinations(codes, 2))
        want = predicted(n)
        assert count == want, (n, count, want)
        print(f"n={n} LCD_planes={len(codes)} associated_edges={count} formula={want} OK")
    print("DIRECT_ENUMERATION_OK")

if __name__ == '__main__':
    run()
