#!/usr/bin/env python3
"""Standalone numerical consistency checks for finite-horizon two-state discharge.

The universal conclusions are proved analytically in RESULT.md; this bounded
program checks formulas, numerical optimizers, and parameter boundaries.
Requires Python 3.10+ standard library only.
"""
import math


def occupation_eq(beta, energy):
    return 1.0 / (1.0 + math.exp(beta * energy))


def voltage(beta, energy, occupation):
    return energy + math.log(occupation / (1 - occupation)) / beta


def stationary_loaded(beta, energy, load):
    x = beta * (energy - load)
    return 1.0 / (1.0 + math.exp(x))


def relaxation(beta, energy, scale, load):
    return 2.0 * scale * math.cosh(0.5 * beta * (energy - load))


def relaxation_prime(beta, energy, scale, load):
    return -beta * scale * math.sinh(0.5 * beta * (energy - load))


def truncated_mean(lam, time):
    u = lam * time
    if u > 700.0:
        return 1.0 / lam
    return 1.0 / lam - time / math.expm1(u)


def truncated_variance(lam, time):
    u = lam * time
    if u > 700.0:
        return 1.0 / (lam * lam)
    em = math.expm1(u)
    return 1.0 / (lam * lam) - time * time * (em + 1.0) / (em * em)


def work(beta, energy, scale, occupation, load, time):
    lam = relaxation(beta, energy, scale, load)
    q = stationary_loaded(beta, energy, load)
    return load * (occupation - q) * (-math.expm1(-lam * time))


def gradient(beta, energy, scale, occupation, load, time):
    phi = voltage(beta, energy, occupation)
    x = 0.5 * beta * (phi - load)
    c = 0.5 * beta
    lam = relaxation(beta, energy, scale, load)
    return 1.0 / load - c / math.tanh(x) - relaxation_prime(beta, energy, scale, load) * truncated_mean(lam, time)


def optimum(beta, energy, scale, occupation, time):
    phi = voltage(beta, energy, occupation)
    lo, hi = 0.0, phi
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        if gradient(beta, energy, scale, occupation, mid, time) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def test():
    checks = 0
    cases = 0
    for beta in (0.4, 1.0, 2.0):
        for energy in (0.3, 1.0, 3.0):
            p_eq = occupation_eq(beta, energy)
            for scale in (0.2, 1.0, 5.0):
                for frac in (0.2, 0.5, 0.8, 0.95):
                    p = p_eq + frac * (1 - p_eq)
                    phi = voltage(beta, energy, p)
                    pc = 0.5 + beta * energy / 4.0
                    loads = []
                    for T in (0.01, 0.05, 0.2, 1, 4, 20):
                        w = optimum(beta, energy, scale, p, T)
                        loads.append(w)
                        assert 0 < w < phi
                        checks += 1
                        assert (w - energy) * (p - pc) >= -1e-9
                        checks += 1
                        assert abs(gradient(beta, energy, scale, p, w, T)) < 1e-8
                        checks += 1
                        # CTMC solution and direct integrated-current calculation.
                        lam = relaxation(beta, energy, scale, w)
                        q = stationary_loaded(beta, energy, w)
                        pend = q + (p - q) * math.exp(-lam * T)
                        expected = w * (p - pend)
                        assert abs(expected - work(beta, energy, scale, p, w, T)) < 2e-13
                        checks += 1
                        # The stationary point is strictly better than natural trial loads.
                        peak = work(beta, energy, scale, p, w, T)
                        for a in (0.02, 0.25, 0.50, 0.75, 0.98):
                            assert peak + 1e-12 >= work(beta, energy, scale, p, a * phi, T)
                            checks += 1
                        if 0.1 * phi < w < 0.9 * phi:
                            h = 1e-5 * phi
                            dnum = (math.log(work(beta, energy, scale, p, w + h, T)) -
                                    math.log(work(beta, energy, scale, p, w - h, T))) / (2 * h)
                            assert abs(dnum) < 1e-7
                            checks += 1
                    if p < pc - 1e-12:
                        assert all(a < b + 1e-9 for a, b in zip(loads, loads[1:]))
                    elif p > pc + 1e-12:
                        assert all(a > b - 1e-9 for a, b in zip(loads, loads[1:]))
                    else:
                        assert max(abs(x-energy) for x in loads) < 1e-7
                    checks += 1
                    cases += 1
    # Numerical check of the exact truncated-exponential variance inequality,
    # including nearly-uniform and nearly-untruncated regimes.
    for lam in (0.1, 0.5, 2.0, 10.0):
        for u in (0.1, 0.2, 0.5, 1, 3, 10, 30, 80):
            T = u / lam
            mu = truncated_mean(lam, T)
            var = truncated_variance(lam, T)
            assert mu > 0 and var > 0 and var <= mu / lam + 1e-12
            if u < 40:
                assert var < mu / lam
            checks += 1
    # Exact critical occupation: the intrinsic gap is optimal at every horizon.
    for beta, E in ((1.0, 1.0), (0.5, 1.0), (1.0, 1.6)):
        pc = 0.5 + beta * E / 4
        for T in (0.001, 0.2, 1.0, 10.0):
            w = optimum(beta, E, 2.0, pc, T)
            assert abs(w - E) < 2e-10
            checks += 1
    # Finite charging and finite retention thresholds are genuine crossings.
    beta, E = 1.0, 1.0
    pe = occupation_eq(beta, E)
    pc = 0.5 + beta * E / 4
    pa = stationary_loaded(beta, E, 3.0)
    rate_c = relaxation(beta, E, 2.0, 3.0)
    tc = math.log((pa - pe) / (pa - pc)) / rate_c
    def charged(t):
        return pe + (pa - pe) * (-math.expm1(-rate_c*t))
    assert charged(0.9 * tc) < pc < charged(1.1 * tc)
    checks += 1
    assert abs(charged(tc) - pc) < 1e-13
    checks += 1
    p0 = charged(2 * tc)
    rate_hold = 0.3
    hc = math.log((p0-pe)/(pc-pe))/rate_hold
    def held(h):
        return pe + (p0-pe)*math.exp(-rate_hold*h)
    assert held(0.8*hc) > pc > held(1.2*hc)
    checks += 1
    assert abs(held(hc)-pc) < 1e-13
    checks += 1
    print(f'PASS: {checks} bounded checks across {cases} discharge parameter families')
    print('Examples beta=E=scale=1')
    for p in (0.65, 0.75, 0.9):
        print('p=',p,'load at T=0.01, 1, 20:',
              *(f'{optimum(1,1,1,p,T):.10f}' for T in (.01,1.,20.)))

if __name__ == '__main__':
    test()
