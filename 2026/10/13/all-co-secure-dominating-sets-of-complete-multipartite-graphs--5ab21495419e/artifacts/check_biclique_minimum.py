"""Check the biclique minimum by direct enumeration from the swap definition."""
from itertools import combinations


def minimum(a, b):
    n = a + b
    full = (1 << n) - 1
    left = (1 << a) - 1
    adj = [full ^ left] * a + [left] * b

    def dominates(s):
        seen = s
        m = s
        while m:
            bit = m & -m
            m ^= bit
            seen |= adj[bit.bit_length() - 1]
        return seen == full

    for size in range(1, n + 1):
        for vertices in combinations(range(n), size):
            s = sum(1 << v for v in vertices)
            if dominates(s) and all(
                any(adj[v] & (1 << u) and dominates((s ^ (1 << v)) | (1 << u))
                    for u in range(n) if not s & (1 << u))
                for v in vertices
            ):
                return size, vertices
    raise AssertionError((a, b))


def main():
    for a in range(1, 8):
        for b in range(a, 8):
            size, witness = minimum(a, b)
            expected = b if a == 1 else min(a, b, 4)
            assert size == expected, (a, b, size, expected)
            if (a, b) == (5, 5):
                print(f'K_{{5,5}}: minimum={size}, witness={witness}')
    print('Verified scalar minimum on 28 biclique profiles with 1 <= a <= b <= 7.')


if __name__ == '__main__':
    main()
