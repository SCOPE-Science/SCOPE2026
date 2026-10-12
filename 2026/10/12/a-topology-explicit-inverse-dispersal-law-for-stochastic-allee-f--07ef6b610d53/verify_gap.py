"""Exact finite sanity checks for an Allee threshold fast-mixing estimate.

The global probability inequality is proved in RESULT.md; these checks verify
its local algebra, the two-site sharpness construction, and some spectral forms.
Only the Python standard library is used.
"""
from fractions import Fraction as Q
from itertools import product, combinations


def energy(x):
    n = len(x)
    mean = sum(x, Q(0)) / n
    return sum(((z - mean) ** 2 for z in x), Q(0))


def mix(x, u, v, mu):
    y = list(x)
    y[u] = (1 - mu) * x[u] + mu * x[v]
    y[v] = (1 - mu) * x[v] + mu * x[u]
    return tuple(y)


def check_edge_contraction():
    checks = 0
    grid = [Q(0), Q(1, 3), Q(2, 3), Q(1)]
    for n in range(2, 6):
        for x in product(grid, repeat=n):
            for u, v in combinations(range(n), 2):
                for mu in (Q(1, 7), Q(1, 5), Q(1, 2)):
                    y = mix(x, u, v, mu)
                    assert sum(y, Q(0)) == sum(x, Q(0))
                    delta = energy(x) - energy(y)
                    assert delta == 2 * mu * (1 - mu) * (x[u] - x[v]) ** 2
                    checks += 1
    return checks


def check_complete_graph_gap():
    checks = 0
    grid = [Q(0), Q(1, 3), Q(1)]
    for n in range(2, 7):
        for x in product(grid, repeat=n):
            lap = sum(((x[u] - x[v]) ** 2
                       for u, v in combinations(range(n), 2)), Q(0))
            assert lap == n * energy(x)
            checks += 1
    return checks


def check_lower_event():
    mu = Q(1, 5)
    theta = Q(9, 20)
    x = (Q(1), Q(0))
    assert sum(x) / 2 > theta
    y = mix(x, 0, 1, mu)
    assert y == (Q(4, 5), Q(1, 5)) and y[1] < theta
    z = (y[0], Q(0))
    assert sum(z) / 2 == Q(2, 5) < theta
    assert energy(z) == Q(8, 25)
    lam2 = Q(2)
    c = 2 * mu * (1 - mu) * lam2
    assert c == Q(16, 25)
    delta = theta - sum(z) / 2
    assert delta == Q(1, 20)
    for alpha in (1000, 10000, 100000):
        upper_next = 2 * energy(z) / (delta ** 2 * (2 + c * alpha))
        lower_original_error = (Q(alpha) / (alpha + 2) ** 2) * (1 - upper_next)
        assert 0 < lower_original_error < 1
        assert lower_original_error <= Q(alpha) / (alpha + 2) ** 2
    return True

if __name__ == '__main__':
    a = check_edge_contraction()
    b = check_complete_graph_gap()
    assert check_lower_event()
    print(f'VERIFY_OK edge_energy_identities={a} complete_graph_gap_identities={b} two_patch_lower_event=1')
