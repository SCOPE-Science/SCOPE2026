"""Reproducible finite checks for the discrete Huygens ring's alternating two-cycle.

The universal statements follow from the accompanying analytic proof, not from
these numerical samples. Requires only Python 3's standard library.
"""
from math import pi, sin, cos, sqrt, isclose


def bisect_monotone(f, left, right, target=0.0):
    for _ in range(90):
        mid = (left + right) / 2
        if f(mid) < target:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def h_of_a(a):
    return a / (2 * sin(a))


def t_of_a(a):
    return a * cos(a) / (2 * sin(a))


def phase_update(phase, h):
    n = len(phase)
    return [phase[j] + h * (sin(phase[j] - phase[(j-1) % n]) + sin(phase[j] - phase[(j+1) % n])) for j in range(n)]


def phase_distance(x, y):
    return abs((x - y + pi) % (2*pi) - pi)


def cycle_eigenvalues(n):
    return [2 - 2 * cos(2*pi*j/n) for j in range(1, n)]


def spectral_radius(n, a):
    t = t_of_a(a)
    return max((1 - t*l)**2 for l in cycle_eigenvalues(n))


for n in (4, 6, 8, 12, 20):
    for h in (0.51, 0.60, 0.73, pi/4 - 0.001):
        a = bisect_monotone(h_of_a, 1e-9, pi/2, h)
        theta = [0.0 if j % 2 == 0 else pi+a for j in range(n)]
        halfway = phase_update(theta, h)
        back = phase_update(halfway, h)
        first_error = max(phase_distance(halfway[j], a if j % 2 == 0 else pi) for j in range(n))
        second_error = max(phase_distance(theta[j], back[j]) for j in range(n))
        assert first_error < 4e-12 and second_error < 4e-12, (n, h, first_error, second_error)
        rho = spectral_radius(n, a)
        assert 0 <= rho < 1, (n, h, rho)
    s2 = sin(pi/n)**2
    t_star = 1 / (2 * (1+s2))
    a_star = bisect_monotone(lambda x: -t_of_a(x), 1e-9, pi/2, -t_star)
    h_star = h_of_a(a_star)
    rho_star = spectral_radius(n, a_star)
    rho_closed = ((1-s2)/(1+s2))**2
    assert abs(rho_star-rho_closed) < 2e-12
    for nearby in (a_star * .75, (a_star+pi/2)/2):
        assert spectral_radius(n, nearby) > rho_star + 1e-10
    print(f'PASS n={n:2d} h_opt={h_star:.12f} a_opt={a_star:.12f} min_rho2={rho_star:.12f}')
print('PASS 20 exact-identity phase-return and transverse-stability samples')
print('PASS five spectral minimax and unique-optimum samples')
print('NOT_PROOF finite checks do not establish local two-cycle uniqueness or all-n claims')
