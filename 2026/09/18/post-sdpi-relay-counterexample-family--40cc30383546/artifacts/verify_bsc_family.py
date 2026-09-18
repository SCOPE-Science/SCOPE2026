import math


def h2(x):
    if x == 0.0 or x == 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def capacity(delta):
    return 1.0 - h2(delta)


def eta(delta):
    return (1.0 - 2.0 * delta) ** 2


def bounds(delta1, delta2):
    c1 = capacity(delta1)
    c2 = capacity(delta2)
    exact = 1.0 + min(c1, c2)
    proposed_upper = 1.0 + eta(delta1) * c2
    return c1, c2, exact, proposed_upper, exact - proposed_upper


cases = [(0.25, 0.25), (0.125, 0.125), (0.10, 0.20), (0.20, 0.30)]
for d1, d2 in cases:
    c1, c2, exact, upper, gap = bounds(d1, d2)
    print(
        f"delta1={d1:.6f} delta2={d2:.6f} "
        f"C1={c1:.12f} C2={c2:.12f} "
        f"capacity={exact:.12f} proposed_upper={upper:.12f} gap={gap:.12f}"
    )

for i in range(1, 50):
    d1 = i / 100.0
    for j in range(i, 50):
        d2 = j / 100.0
        _, c2, exact, upper, gap = bounds(d1, d2)
        expected = 4.0 * d1 * (1.0 - d1) * c2
        assert gap > 0.0
        assert abs(gap - expected) < 1e-12
        assert exact > upper

print("wedge_grid_check=PASS")
print("verification=PASS")
