"""Standalone verification of cyclic-rotation DFA state counts."""
from collections import defaultdict


def check(a, b):
    s = '0' * a + '1' * b
    n = a + b
    rotations = {s[j:] + s[:j] for j in range(n)}
    assert len(rotations) == n
    total = 1  # dead state
    for d in range(n + 1):
        residuals = defaultdict(set)
        for w in rotations:
            residuals[w[:d]].add(w[d:])
        count = len({frozenset(x) for x in residuals.values()})
        expected = 1 if d in (0, n) else 2 * min(a, b, d, n - d)
        assert count == expected, (a, b, d, count, expected)
        total += count
    assert total == 2 * a * b + 3, (a, b, total)


def run():
    cases = 0
    for a in range(1, 25):
        for b in range(1, 25):
            check(a, b)
            cases += 1
    print(f'VERIFY_OK pairs={cases} lengths=2..48 all_depth_residuals=checked')


if __name__ == '__main__':
    run()
