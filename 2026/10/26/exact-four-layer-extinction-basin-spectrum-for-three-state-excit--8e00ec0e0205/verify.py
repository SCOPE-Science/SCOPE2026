"""Standalone exhaustive checks for complete-tripartite three-state excitation.

Standard-library only; tests all part-size triples 1 <= a <= b <= c <= 4
with a+b+c <= 10. Uses the actual vertex update rather than a
color-support quotient. This is finite testing, not the all-size proof.
"""
from itertools import product


def predicted_depths(a, b, c):
    n = a + b + c
    sizes = (a, b, c)
    q = sum(3**k - 2 ** (k + 1) + 1 for k in sizes)
    s = sum(2**k for k in sizes)
    return (1, 2**n - 1, 2**n - 1 + q,
            2**n + 4 - s + q, s - 6 + q)


def visit(a, b, c):
    part = (0,) * a + (1,) * b + (2,) * c
    n = len(part)
    neighbors = [tuple(j for j in range(n) if part[i] != part[j])
                 for i in range(n)]
    depths = [0] * 5
    orbits = 0
    for start in product(range(3), repeat=n):
        current = start
        for t in range(5):
            if not any(current):
                depths[t] += 1
                break
            current = tuple((x + 1) % 3 if x else
                            (1 if any(current[j] == 1 for j in neighbors[i])
                             else 0)
                            for i, x in enumerate(current))
        else:
            # Once past four updates, no extinction can occur in this tested range.
            # Check a nonzero genuine 3-cycle at the image of step four.
            def step(s):
                return tuple((x + 1) % 3 if x else
                             (1 if any(s[j] == 1 for j in neighbors[i]) else 0)
                             for i, x in enumerate(s))
            assert step(step(step(current))) == current
            assert any(current)
            orbits += 1
    expected = predicted_depths(a, b, c)
    assert tuple(depths) == expected, (a, b, c, depths, expected)
    assert orbits == 3**n - sum(depths)
    if n == 3:
        assert max(t for t, val in enumerate(depths) if val) == 3
    else:
        assert depths[4] > 0
    return n, sum(depths), depths, orbits


def main():
    tested = 0
    states = 0
    for a in range(1, 5):
        for b in range(a, 5):
            for c in range(b, 5):
                if a + b + c > 10:
                    continue
                n, basin, depth, periodic = visit(a, b, c)
                states += 3**n
                tested += 1
                print(f"{a},{b},{c}: basin={basin}; depths={depth}; persistent={periodic}")
    print(f"VERIFY_OK triples={tested} total_initial_states={states}")


if __name__ == '__main__':
    main()
