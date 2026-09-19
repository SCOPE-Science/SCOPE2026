import math


def h2(p):
    if p in (0.0, 1.0):
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def check_bsc(p, q):
    c1 = 1.0 - h2(p)
    c2 = 1.0 - h2(q)
    eta = (1.0 - 2.0 * p) ** 2
    capacity = 1.0 + min(c1, c2)
    proposed_upper = max(c1, 1.0 + eta * c2)
    return c1, c2, eta, capacity, proposed_upper

checks = 0
for i in range(1, 100):
    p = i / 200.0
    if p >= 0.5:
        break
    for j in range(i, 100):
        q = j / 200.0
        if q >= 0.5:
            break
        c1, c2, eta, capacity, upper = check_bsc(p, q)
        certified = 4.0 * p * (1.0 - p) * c2
        assert c1 >= c2 - 1e-14
        assert abs((capacity - upper) - certified) < 1e-12
        assert capacity > upper
        checks += 1

print(f"grid_checks={checks}")
for p in (1.0/8.0, 1.0/4.0):
    c1, c2, eta, capacity, upper = check_bsc(p, p)
    print(
        f"p=q={p:.6f} capacity={capacity:.12f} "
        f"proposed_upper={upper:.12f} certified_gap={capacity-upper:.12f}"
    )
print("PASS")
