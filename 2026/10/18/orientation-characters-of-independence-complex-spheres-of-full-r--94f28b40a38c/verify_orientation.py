"""Exact generator-by-generator orientation checks for full rooted trees.

Only Python's standard library is required. The proof in RESULT.md covers
all heights; this finite computation verifies the recurrences independently.
"""

def pair(b, height):
    a, c = 1, -1
    for _ in range(height):
        a, c = (a + c) ** b, -a ** b
    return a, c


def quotient_at_depth(b, height, depth):
    """Independence evaluation at -1 of a sibling-swap quotient tree."""
    remain = height - depth
    a, c = pair(b, remain - 1)
    aa, cc = (a + c) ** (b - 1), -a ** (b - 1)
    for k in range(remain + 1, height + 1):
        a, c = pair(b, k - 1)
        aa, cc = (a + c) ** (b - 1) * (aa + cc), -a ** (b - 1) * aa
    return aa + cc


def expected_sign(b, height, depth):
    orbit_blocks = sum(b ** (level - depth - 1)
                       for level in range(height - 1, depth, -3))
    return -1 if orbit_blocks % 2 else 1


def verify():
    count = 0
    for b in range(2, 11):
        for h in range(0, 31):
            a, c = pair(b, h)
            z = a + c
            assert (z == 0) == (h % 3 == 0), (b, h, z)
            assert z in (-1, 0, 1)
            if z:
                for j in range(h):
                    q = quotient_at_depth(b, h, j)
                    assert q == z * expected_sign(b, h, j), (b, h, j, z, q)
                    count += 1
    print('analytic recurrence and orbit-quotient generator tests:', count, 'passed')


if __name__ == '__main__':
    verify()
