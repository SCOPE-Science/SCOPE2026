"""Independent, exact finite-case checks for bidirected cycle percolation."""
from fractions import Fraction
from math import comb, exp

checks = 0


def assert_eq(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1


def sizes_from_reachability(n, cw, ccw):
    reach = [[i == j for j in range(n)] for i in range(n)]
    for i in range(n):
        if cw[i]:
            reach[i][(i + 1) % n] = True
        if ccw[i]:
            reach[(i + 1) % n][i] = True
    for pivot in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] |= reach[i][pivot] and reach[pivot][j]
    remaining = set(range(n))
    components = []
    while remaining:
        i = min(remaining)
        group = {j for j in remaining if reach[i][j] and reach[j][i]}
        components.append(len(group))
        remaining -= group
    return sorted(components, reverse=True), reach


def sizes_from_reduction(n, cw, ccw):
    if all(cw) or all(ccw):
        return [n]
    reach = [[i == j for j in range(n)] for i in range(n)]
    for i in range(n):
        if cw[i] and ccw[i]:
            reach[i][(i + 1) % n] = reach[(i + 1) % n][i] = True
    for pivot in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] |= reach[i][pivot] and reach[pivot][j]
    remaining = set(range(n))
    components = []
    while remaining:
        i = min(remaining)
        group = {j for j in remaining if reach[i][j]}
        components.append(len(group))
        remaining -= group
    return sorted(components, reverse=True)


for n in range(3, 7):
    for mask in range(1 << (2 * n)):
        cw = [bool(mask & (1 << i)) for i in range(n)]
        ccw = [bool(mask & (1 << (n + i))) for i in range(n)]
        components, reach = sizes_from_reachability(n, cw, ccw)
        assert_eq(components, sizes_from_reduction(n, cw, ccw))
    print(f"all {1 << (2 * n)} directed-arc configurations checked for cycle size n={n}")

for n in range(3, 6):
    for p in (Fraction(1, 3), Fraction(3, 5)):
        full_mass = Fraction(0)
        mean_size = Fraction(0)
        pairwise = [Fraction(0) for _ in range(n)]
        total_mass = Fraction(0)
        for mask in range(1 << (2 * n)):
            arcs = mask.bit_count()
            mass = p ** arcs * (1 - p) ** (2 * n - arcs)
            cw = [bool(mask & (1 << i)) for i in range(n)]
            ccw = [bool(mask & (1 << (n + i))) for i in range(n)]
            components, reach = sizes_from_reachability(n, cw, ccw)
            full_mass += mass * (components == [n])
            mean_size += mass * sum(reach[0][j] and reach[j][0] for j in range(n))
            for j in range(n):
                pairwise[j] += mass * (reach[0][j] and reach[j][0])
            total_mass += mass
        assert_eq(total_mass, 1)
        predicted_full = 2*p**n - p**(2*n) + n*(1-p)**2*p**(2*n-2)
        assert_eq(full_mass, predicted_full)
        for j in range(n):
            predicted_pair = (p**j + p**(n-j) - p**n)**2
            assert_eq(pairwise[j], predicted_pair)
        assert_eq(mean_size, sum(pairwise))
        print(f"exact rational event probabilities: n={n}, p={p}, full={full_mass}")

for lam in (0.2, 0.5, 1, 2):
    e = exp(-lam)
    full = 2*e - e*e
    assert 0 < full < 1
    mean = 2*e + e*e + (1-4*e+3*e*e)/lam
    assert full < mean < 1
    print(f"critical-window lambda={lam}: P(full)={full:.12f}, E[component fraction]={mean:.12f}")

print(f"PASS: {checks} exact assertions; limiting formulas checked for normalization bounds")
