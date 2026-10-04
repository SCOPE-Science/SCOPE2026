import math

def cancellation_budget(pair_weights):
    total = sum(x + y for x, y in pair_weights)
    assert abs(total - 1.0) < 1e-12
    a1 = sum(abs(x - y) for x, y in pair_weights)
    a2 = 1.0 - 2.0 * sum(min(x, y) for x, y in pair_weights)
    assert abs(a1 - a2) < 1e-12
    return a1

def cct_size_from_A(A, alpha):
    if A == 0.0:
        return 0.0
    threshold = 1.0 / math.tan(math.pi * alpha)
    return 0.5 - math.atan(threshold / A) / math.pi

# Exactness, partial cancellation, and total cancellation examples.
assert abs(cancellation_budget([(1.0, 0.0)]) - 1.0) < 1e-15
assert abs(cancellation_budget([(0.5, 0.5)]) - 0.0) < 1e-15
assert abs(cancellation_budget([(0.30, 0.10), (0.15, 0.05), (0.40, 0.0)]) - 0.7) < 1e-15
assert abs(cancellation_budget([(0.20, 0.20), (0.30, 0.30)]) - 0.0) < 1e-15

# One-pair consequences quoted in the result.
for w, target in {
    0.5: 0.0,
    0.75: 0.025155168137137418,
    0.9: 0.04011847996268625,
    1.0: 0.05,
}.items():
    A = abs(2.0 * w - 1.0)
    got = cct_size_from_A(A, 0.05)
    assert abs(got - target) < 2e-15, (w, got, target)

# Size is strictly increasing in A for alpha below one half.
for alpha in (0.001, 0.01, 0.05, 0.2, 0.49):
    vals = [cct_size_from_A(A, alpha) for A in (0.1, 0.2, 0.4, 0.6, 0.8, 1.0)]
    assert all(vals[i] < vals[i+1] for i in range(len(vals)-1))
    assert abs(vals[-1] - alpha) < 2e-15
    assert cct_size_from_A(0.0, alpha) == 0.0

# Tail-size ratio converges to A.
for A in (0.2, 0.5, 0.8):
    ratio = cct_size_from_A(A, 1e-6) / 1e-6
    assert abs(ratio - A) < 1e-9, (A, ratio)

print('VERIFY_OK')
