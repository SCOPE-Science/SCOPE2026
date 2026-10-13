from fractions import Fraction
from itertools import combinations, product


def face_minimizer(a, support):
    z = sum(Fraction(1, a[i]) for i in support)
    return [Fraction(1, a[i]) / z if i in support else Fraction(0) for i in range(len(a))]


def objective(a, x):
    return sum(Fraction(a[i]) * x[i] * x[i] for i in range(len(a))) / 2


def gradient(a, x):
    return [Fraction(a[i]) * x[i] for i in range(len(a))]


def exact_vertex_fw_step(a, x, j):
    g = gradient(a, x)
    d = [Fraction(int(i == j)) - x[i] for i in range(len(a))]
    numerator = -sum(g[i] * d[i] for i in range(len(a)))
    denominator = sum(Fraction(a[i]) * d[i] * d[i] for i in range(len(a)))
    gamma = numerator / denominator
    assert 0 < gamma <= 1
    y = [(1 - gamma) * x[i] + gamma * Fraction(int(i == j)) for i in range(len(a))]
    return y, gamma


# Exact illustrative chain for a=(1,2,3,6).
a = [1, 2, 3, 6]
x = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
expected = [
    ([Fraction(2,3), Fraction(1,3), 0, 0], Fraction(1,3)),
    ([Fraction(6,11), Fraction(3,11), Fraction(2,11), 0], Fraction(2,11)),
    ([Fraction(1,2), Fraction(1,4), Fraction(1,6), Fraction(1,12)], Fraction(1,12)),
]
for j, (target, gamma_target) in zip([1,2,3], expected):
    x, gamma = exact_vertex_fw_step(a, x, j)
    assert x == [Fraction(v) for v in target]
    assert gamma == gamma_target
assert objective(a, x) == Fraction(1,4)

# Deterministic exact stress test of the one-step identity for all nonempty proper
# supports, dimensions 2..5, and integer diagonal entries 1..4.
for n in range(2, 6):
    for a_tuple in product(range(1, 5), repeat=n):
        a = list(a_tuple)
        for r in range(1, n):
            for support_tuple in combinations(range(n), r):
                support = set(support_tuple)
                x = face_minimizer(a, support)
                z = sum(Fraction(1, a[i]) for i in support)
                g = gradient(a, x)
                assert all(g[i] == Fraction(1,1) / z for i in support)
                assert all(g[i] == 0 for i in range(n) if i not in support)
                # Every standard vertex LMO choice is an unseen coordinate.
                for j in range(n):
                    if j in support:
                        continue
                    y, gamma = exact_vertex_fw_step(a, x, j)
                    target = face_minimizer(a, support | {j})
                    gamma_formula = Fraction(1, a[j]) / (z + Fraction(1, a[j]))
                    assert gamma == gamma_formula
                    assert y == target
                    assert objective(a, x) == Fraction(1,1) / (2*z)
                    # The FW gap at an incomplete face minimizer is 1/z.
                    gap = sum(x[i] * g[i] for i in range(n)) - g[j]
                    assert gap == Fraction(1,1) / z

print("VERIFY_OK")
