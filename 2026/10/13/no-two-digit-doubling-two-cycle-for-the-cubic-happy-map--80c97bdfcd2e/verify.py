#!/usr/bin/env python3

def s3(n, b):
    total = 0
    while n:
        n, d = divmod(n, b)
        total += d**3
    return total

rows = []
total_admissible = 0
first_equation = []
two_cycle_hits = []

for b in range(2, 9):
    admissible = 0
    first = []
    for a in range(1, b):
        for c in range(b):
            X = a*b + c
            if not (b <= X and b <= 2*X < b*b):
                continue
            admissible += 1
            assert X == a*b + c
            assert s3(X, b) == a**3 + c**3
            if s3(X, b) == 2*X:
                first.append((a, c, X))
                first_equation.append((b, a, c, X))
                if s3(2*X, b) == X:
                    two_cycle_hits.append((b, X))
    rows.append((b, admissible, first))
    total_admissible += admissible

expected = [
    (2, 0, []),
    (3, 2, []),
    (4, 4, []),
    (5, 8, []),
    (6, 12, []),
    (7, 18, []),
    (8, 24, [(3, 3, 27)]),
]
assert rows == expected, (rows, expected)
assert total_admissible == 68
assert first_equation == [(8, 3, 3, 27)]
assert two_cycle_hits == []
assert s3(54, 8) == 432

# Corroborate the analytic cutoff inequality on a large integer range.
for b in range(9, 100000):
    assert b**3 > 8*(b*b + b - 2)

print(
    "VERIFY_OK",
    f"admissible={total_admissible}",
    f"first_equation={first_equation}",
    f"two_cycle_hits={two_cycle_hits}",
    f"cutoff_checked=9..99999",
)
