import math


def threshold(A, B, beta):
    return A / (beta * (1.0 - beta)) + B / (1.0 - beta)


def beta_star(A, B):
    return math.sqrt(A) / (math.sqrt(A) + math.sqrt(A + B))


def optimum(A, B):
    return (math.sqrt(A) + math.sqrt(A + B)) ** 2


def check_close(x, y, tol=2e-10):
    scale = max(1.0, abs(x), abs(y))
    if abs(x - y) > tol * scale:
        raise AssertionError((x, y, abs(x-y)/scale))


for A in [0.03, 0.2, 1.0, 3.7, 12.0]:
    for B in [0.0, 0.05, 0.7, 4.0, 50.0, 5000.0]:
        bs = beta_star(A, B)
        assert 0.0 < bs < 1.0
        check_close(threshold(A, B, bs), optimum(A, B))
        default = threshold(A, B, 0.5)
        gap = (math.sqrt(A + B) - math.sqrt(A)) ** 2
        check_close(default - optimum(A, B), gap)
        # Dense-grid regression test: the analytic optimum must beat sampled competitors.
        best_grid = min(threshold(A, B, j / 10000.0) for j in range(1, 10000))
        if optimum(A, B) > best_grid + 1e-8 * max(1.0, best_grid):
            raise AssertionError((A, B, optimum(A, B), best_grid))

A = 1.0
ratios = []
for B in [1e2, 1e4, 1e6, 1e8]:
    ratios.append(optimum(A, B) / threshold(A, B, 0.5))
assert all(ratios[i+1] < ratios[i] for i in range(len(ratios)-1))
assert abs(ratios[-1] - 0.5) < 2e-4
print('VERIFY_OK')
