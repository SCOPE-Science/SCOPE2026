#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt
import random

def V(k):
    return Fraction(k*(k+1), 3)

def T(a, k):
    return Fraction(0) if k < a else Fraction(2*(k-a+1), 2*k+1)

def beta_floor(a):
    D = 36*a*a - 36*a + 25
    s = isqrt(D)
    b = (6*a - 11 + s) // 8
    def le_beta(x):
        y = 8*x - (6*a - 11)
        return y <= 0 or y*y <= D
    while le_beta(b+1):
        b += 1
    while not le_beta(b):
        b -= 1
    return b

def kappa(a):
    return beta_floor(a) + 1

def slope(a, k):
    return Fraction(3*(2*a-1), (k+1)*(2*k+1)*(2*k+3))

def interval_k(v, kap):
    lo = kap
    hi = max(kap+1, 2*kap+2)
    while V(hi) < v:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if V(mid) <= v:
            lo = mid
        else:
            hi = mid
    return lo

def envelope(a, v):
    kap = kappa(a)
    if v <= V(kap):
        return T(a,kap) * v / V(kap)
    k = interval_k(v, kap)
    return T(a,k) + slope(a,k) * (v - V(k))

def run():
    ratio_checks = slope_checks = point_checks = construction_checks = random_mixture_checks = 0

    for a in range(1, 101):
        kap = kappa(a)
        assert kap >= a
        rkap = T(a,kap) / V(kap)

        for k in range(a, 6*a + 121):
            assert T(a,k) / V(k) <= rkap
            ratio_checks += 1

        prev = None
        for k in range(kap, 6*a + 121):
            lhs = (T(a,k+1)-T(a,k)) / (V(k+1)-V(k))
            rhs = slope(a,k)
            assert lhs == rhs
            if prev is not None:
                assert rhs < prev
            prev = rhs
            slope_checks += 1

        for k in range(0, 6*a + 121):
            assert T(a,k) <= envelope(a, V(k))
            point_checks += 1

        for den in range(2, 11):
            for num in range(1, den):
                lam = Fraction(num, den)
                v = lam * V(kap)
                tail = lam * T(a,kap)
                assert tail == envelope(a,v)
                construction_checks += 1

        for k in range(kap, kap+15):
            for den in range(2, 6):
                for num in range(1, den):
                    lam = Fraction(num, den)
                    v = (1-lam)*V(k) + lam*V(k+1)
                    tail = (1-lam)*T(a,k) + lam*T(a,k+1)
                    assert tail == envelope(a,v)
                    construction_checks += 1

    rng = random.Random(20261001)
    for a in range(1, 41):
        for _ in range(80):
            K = rng.randint(a, 5*a + 30)
            raw = [rng.randint(0, 12) for _ in range(K+1)]
            if not sum(raw):
                raw[0] = 1
            total = sum(raw)
            v = sum(Fraction(raw[k],total)*V(k) for k in range(K+1) if raw[k])
            tail = sum(Fraction(raw[k],total)*T(a,k) for k in range(K+1) if raw[k])
            assert tail <= envelope(a,v)
            random_mixture_checks += 1

    print(
        "VERIFY_OK "
        f"ratio_checks={ratio_checks} "
        f"slope_checks={slope_checks} "
        f"point_checks={point_checks} "
        f"construction_checks={construction_checks} "
        f"random_mixture_checks={random_mixture_checks}"
    )

if __name__ == "__main__":
    run()
