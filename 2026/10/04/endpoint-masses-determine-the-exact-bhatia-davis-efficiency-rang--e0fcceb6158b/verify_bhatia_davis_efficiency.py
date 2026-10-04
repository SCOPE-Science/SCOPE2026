#!/usr/bin/env python3
from fractions import Fraction
import random

def normalize(raw):
    s = sum(raw)
    return [Fraction(x, s) for x in raw]

def moments(ps, xs):
    mu = sum(p*x for p, x in zip(ps, xs))
    ex2 = sum(p*x*x for p, x in zip(ps, xs))
    var = ex2 - mu*mu
    return mu, var

def efficiency(ps, xs):
    mu, var = moments(ps, xs)
    return var / (mu*(1-mu))

def lower_square_gap(eta, a, c):
    return eta*eta*(1-a)*(1-c) - (2-eta)*(2-eta)*a*c

def run():
    rng = random.Random(20261002)
    upper_checks = 0
    lower_checks = 0
    strict_lower_checks = 0
    conditional_checks = 0
    binary_checks = 0
    equality_checks = 0
    lower_approach_checks = 0
    upper_approach_checks = 0
    equal_mass_checks = 0

    for _ in range(16000):
        m = rng.randrange(2, 9)
        ps = normalize([rng.randrange(1, 35) for __ in range(m)])
        if m == 2:
            xs = [Fraction(0), Fraction(1)]
        else:
            picks = sorted(rng.sample(range(1, 100), m-2))
            xs = [Fraction(0)] + [Fraction(k, 100) for k in picks] + [Fraction(1)]

        eta = efficiency(ps, xs)
        a, c = ps[0], ps[-1]
        assert eta <= 1
        upper_checks += 1

        if m == 2:
            assert eta == 1
            binary_checks += 1
            continue

        assert eta < 1
        gap = lower_square_gap(eta, a, c)
        assert gap >= 0
        lower_checks += 1
        if m >= 4:
            assert gap > 0
            strict_lower_checks += 1

        b = 1-a-c
        t = sum(p*x for p, x in zip(ps[1:-1], xs[1:-1])) / b
        vint = sum((p/b)*(x-t)*(x-t) for p, x in zip(ps[1:-1], xs[1:-1]))
        mu, var = moments(ps, xs)
        var0 = c + b*t*t - (c+b*t)*(c+b*t)
        assert var == var0 + b*vint
        eta0 = var0 / (mu*(1-mu))
        assert eta >= eta0
        assert lower_square_gap(eta0, a, c) >= 0
        conditional_checks += 3

    # Exact rational equality family. Let endpoint odds be u^2 and v^2.
    for _ in range(4000):
        u = Fraction(rng.randrange(1, 8), rng.randrange(9, 18))
        v = Fraction(rng.randrange(1, 8), rng.randrange(9, 18))
        if u*v >= 1:
            continue
        a = u*u/(1+u*u)
        c = v*v/(1+v*v)
        b = 1-a-c
        assert b > 0
        z = (v/u)*(1+u*u)/(1+v*v)
        t = z/(1+z)
        ps = [a, b, c]
        xs = [Fraction(0), t, Fraction(1)]
        eta = efficiency(ps, xs)
        L = 2*u*v/(1+u*v)
        assert eta == L
        assert lower_square_gap(eta, a, c) == 0
        equality_checks += 2

    # Exact equal-mass simplification and boundary approaches.
    for m in range(3, 51):
        ps = [Fraction(1, m)]*m
        a = c = Fraction(1, m)
        L = Fraction(2, m)

        eps = Fraction(1, 10**7)
        center = Fraction(m-1, 2)
        interior = [Fraction(1,2) + eps*(Fraction(i)-center) for i in range(1, m-1)]
        xs_low = [Fraction(0)] + interior + [Fraction(1)]
        assert all(xs_low[i] < xs_low[i+1] for i in range(m-1))
        eta_low = efficiency(ps, xs_low)
        assert eta_low > L if m >= 4 else eta_low == L
        assert eta_low - L < Fraction(1, 100000)
        lower_approach_checks += 1

        eps2 = Fraction(1, 10**9)
        xs_up = [Fraction(0)] + [eps2*i for i in range(1, m-1)] + [Fraction(1)]
        eta_up = efficiency(ps, xs_up)
        assert eta_up < 1
        assert 1-eta_up < Fraction(1, 100000)
        upper_approach_checks += 1

        # Radical-free formula for equal endpoint masses gives L = 2/m.
        assert lower_square_gap(L, a, c) == 0
        equal_mass_checks += 1

    print(
        "VERIFY_OK "
        f"upper_checks={upper_checks} "
        f"lower_checks={lower_checks} "
        f"strict_lower_checks={strict_lower_checks} "
        f"conditional_checks={conditional_checks} "
        f"binary_checks={binary_checks} "
        f"equality_checks={equality_checks} "
        f"lower_approach_checks={lower_approach_checks} "
        f"upper_approach_checks={upper_approach_checks} "
        f"equal_mass_checks={equal_mass_checks}"
    )

if __name__ == "__main__":
    run()
