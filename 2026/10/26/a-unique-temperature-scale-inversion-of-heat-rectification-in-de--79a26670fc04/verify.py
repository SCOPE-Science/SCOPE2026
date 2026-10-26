#!/usr/bin/env python3
"""Independent stationary rate-generator checks for a two-qubit thermal diode.

Python standard library only; no package downloads or hidden inputs.
"""
import math
import random


def bose(w, T):
    return 1.0 / math.expm1(w / T)


def solve(A, b):
    m = len(b)
    aug = [list(A[i]) + [b[i]] for i in range(m)]
    for j in range(m):
        pivot = max(range(j, m), key=lambda z: abs(aug[z][j]))
        assert abs(aug[pivot][j]) > 1e-14
        aug[pivot], aug[j] = aug[j], aug[pivot]
        v = aug[j][j]
        aug[j] = [x / v for x in aug[j]]
        for i in range(m):
            if i != j:
                d = aug[i][j]
                aug[i] = [x - d * y for x, y in zip(aug[i], aug[j])]
    return [aug[i][-1] for i in range(m)]


def data(omega1, omega2, coupling):
    assert omega1 > omega2 > 0 and 0 < coupling < math.sqrt(omega1 * omega2)
    Om = math.hypot((omega1 - omega2) / 2, coupling)
    p = (1 + (omega1 - omega2) / (2 * Om)) / 2
    q = 1 - p
    w0 = (omega1 + omega2) / 2
    return p, q, w0 + Om, w0 - Om, w0, Om


def exact(omega1, omega2, coupling, rate, ratio, T, forward):
    p, q, wp, wm, _, _ = data(omega1, omega2, coupling)
    Th, Tc = ratio * T, T
    def channel(w, left, right):
        nh, nc = bose(w, Th), bose(w, Tc)
        Ch, Cc = 1 + 2 * nh, 1 + 2 * nc
        return rate * p * q * w * (nh - nc) / (left * Ch + right * Cc)
    if forward:
        return channel(wp, p, q) + channel(wm, q, p)
    return channel(wp, q, p) + channel(wm, p, q)


def markov_current(omega1, omega2, coupling, rate, ratio, T, forward):
    p, q, wp, wm, w0, Om = data(omega1, omega2, coupling)
    energies = [-w0, -Om, Om, w0]
    hot = 0 if forward else 1
    temps = [ratio * T, T] if forward else [T, ratio * T]
    L = [[0.0] * 4 for _ in range(4)]
    bath_edges = []
    # Edge entries contain (low index, high index, transition energy, local spin strengths).
    edges = [(0, 2, wp, (p, q)), (1, 3, wp, (p, q)),
             (0, 1, wm, (q, p)), (2, 3, wm, (q, p))]
    for lo, hi, w, coeffs in edges:
        assert abs(energies[hi] - energies[lo] - w) < 1e-10
        for bi, strength in enumerate(coeffs):
            nu = bose(w, temps[bi])
            up = rate * strength * nu
            down = rate * strength * (1 + nu)
            L[hi][lo] += up
            L[lo][lo] -= up
            L[lo][hi] += down
            L[hi][hi] -= down
            if bi == hot:
                bath_edges.append((lo, hi, w, up, down))
    A = [list(L[i]) for i in range(3)] + [[1., 1., 1., 1.]]
    state = solve(A, [0., 0., 0., 1.])
    assert abs(sum(state) - 1) < 2e-11
    assert min(state) > -1e-11
    return sum(w * (up * state[lo] - down * state[hi]) for lo, hi, w, up, down in bath_edges)


def U(x, ratio):
    a = 1.0 / ratio
    return 4 * math.sinh((1 - a) * x) ** 2 / (math.sinh(2 * a * x) * math.sinh(2 * x))


def diff_factor(omega1, omega2, coupling, rate, ratio, T):
    p, q, wp, wm, _, _ = data(omega1, omega2, coupling)
    def G(x):
        v = U(x, ratio)
        return v / (1 + p * q * v)
    return rate * p * q * (p - q) * (wm * G(wm / (2 * T)) - wp * G(wp / (2 * T))) / 2


def root(omega1, omega2, coupling, rate, ratio):
    low, high = .02, 15.
    assert diff_factor(omega1, omega2, coupling, rate, ratio, low) > 0
    assert diff_factor(omega1, omega2, coupling, rate, ratio, high) < 0
    for _ in range(85):
        mid = (low + high) / 2
        if diff_factor(omega1, omega2, coupling, rate, ratio, mid) > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def run():
    rng = random.Random(10441)
    total = 0
    for i in range(175):
        omega2 = rng.uniform(.75, 2.25)
        omega1 = omega2 + rng.uniform(.3, 1.5)
        coupling = math.sqrt(omega1 * omega2) * rng.uniform(.12, .48)
        rate = rng.uniform(.003, .03)
        ratio = rng.uniform(1.3, 3.2)
        T = rng.uniform(.35, 2.5)
        jf = exact(omega1, omega2, coupling, rate, ratio, T, True)
        jr = exact(omega1, omega2, coupling, rate, ratio, T, False)
        jf_ind = markov_current(omega1, omega2, coupling, rate, ratio, T, True)
        jr_ind = markov_current(omega1, omega2, coupling, rate, ratio, T, False)
        assert abs(jf_ind - jf) < 2e-11 * max(1.0, abs(jf))
        assert abs(jr_ind - jr) < 2e-11 * max(1.0, abs(jr))
        assert abs((jf - jr) - diff_factor(omega1, omega2, coupling, rate, ratio, T)) < 2e-12
        total += 1
    omega1, omega2, coupling, rate, ratio = 2., 1., .4, .01, 2.
    tstar = root(omega1, omega2, coupling, rate, ratio)
    assert abs(tstar - .7918074837116923) < 1e-10
    p, q, wp, wm, _, _ = data(omega1, omega2, coupling)
    def r(T):
        def g(w):
            v = U(w / (2 * T), ratio)
            return v / (1 + p * q * v)
        return wm * g(wm) / (wp * g(wp))
    temps = [.1 * 1.04 ** i for i in range(115)]
    rv = [r(v) for v in temps]
    assert all(rv[i] > rv[i+1] for i in range(len(rv) - 1))
    assert r(.2) > 1 and r(1.) < 1
    assert abs(exact(*[omega1, omega2, coupling, rate, ratio, tstar, True]) -
               exact(*[omega1, omega2, coupling, rate, ratio, tstar, False])) < 1e-13
    print('PASS: 175 independent 4-state generators, closed currents, factorization;')
    print('PASS: monotone sampled ratio, unique example root at %.15f' % tstar)

if __name__ == '__main__':
    run()
