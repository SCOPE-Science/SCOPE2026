"""Independent line-local count using orthogonal complements and parity.

Run: python verify_lines.py
Counts pairs by their common line; does not enumerate code pairs.
"""

def dot(a, b):
    return (a & b).bit_count() % 2


def predicted(n):
    h = 2 ** (n - 2)
    if n % 2:
        return (2 ** (n - 1) - 1) * h * (h - 2) // 4
    return 2 ** (n - 1) * h * (h - 1) // 4


def via_lines(n):
    edges = 0
    active_lines = 0
    for u in range(1, 2 ** n):
        if dot(u, u) == 0:
            continue
        # A binary LCD 2-plane with its distinguished odd line <u>
        # corresponds to one odd vector in u-perp.
        choices = [v for v in range(1, 2 ** n)
                   if dot(u, v) == 0 and dot(v, v) == 1]
        if choices:
            active_lines += 1
        for i, v in enumerate(choices):
            for w in choices[i + 1:]:
                if dot(v, w) == 1:
                    edges += 1
    return active_lines, edges

if __name__ == '__main__':
    for n in range(2, 10):
        lines, got = via_lines(n)
        expected_lines = 2 ** (n - 1) - (n % 2)
        want = predicted(n)
        assert lines == expected_lines and got == want
        print(f"n={n} active_odd_lines={lines} associated_edges={got} formula={want} OK")
    print("LINE_ENUMERATION_OK")
