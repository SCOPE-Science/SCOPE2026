#!/usr/bin/env python3
"""Finite numerical checks of a weak-harmonic-confinement entropy-flux theorem.

Only Python's standard library is needed. Finite checks illustrate, but cannot
replace, the analytic entropy-balance proof for the infinite limiting assertion.
"""
import math
import random


def model(mean, coeffs, diffusion):
    """coeffs contains (positive covariance spectral weight, relaxation rate)."""
    variance = sum(weight for weight, rate in coeffs)
    integrated_covariance = sum(weight / rate for weight, rate in coeffs)
    return mean, variance, integrated_covariance, coeffs, diffusion


def covariance_xv(kappa, t, coeffs):
    return sum(weight * (-math.expm1(-(kappa + rate) * t)) / (kappa + rate)
               for weight, rate in coeffs)


def centered_variance_x(kappa, t, coeffs, diffusion):
    # Solve the exactly closed equation Var'(X)=-2*kappa*Var(X)+2*Cov(V,X)+2D.
    e2 = math.exp(-2.0 * kappa * t)
    ans = diffusion * (-math.expm1(-2 * kappa * t)) / kappa
    for weight, rate in coeffs:
        term_a = -math.expm1(-2 * kappa * t) / (2 * kappa)
        if abs(kappa - rate) < 1e-9:
            term_b = t * e2
        else:
            term_b = (math.exp(-(kappa + rate) * t) - e2) / (kappa - rate)
        ans += 2 * weight / (kappa + rate) * (term_a - term_b)
    return ans


def flux(kappa, t, p):
    mean, velocity_var, _, coeffs, diffusion = p
    c = covariance_xv(kappa, t, coeffs)
    v = centered_variance_x(kappa, t, coeffs, diffusion)
    return (velocity_var + mean * mean * math.exp(-2*kappa*t)
            + kappa*kappa*v - 2*kappa*c - kappa*diffusion) / diffusion


def flux_limit(s, p):
    mean, velocity_var, _, _, diffusion = p
    return (velocity_var + mean*mean*math.exp(-2*s)) / diffusion


def area_limit(a, b, p):
    mean, velocity_var, _, _, diffusion = p
    return (velocity_var*(b-a) + (mean*mean/2)*(math.exp(-2*a)-math.exp(-2*b))) / diffusion


def simpson(f, a, b, n=1200):
    assert n % 2 == 0
    h = (b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+h*i) for i in range(1,n,2))
                +2*sum(f(a+h*i) for i in range(2,n,2)))


def exact_3state_correlation(t):
    # Symmetric reflecting 3-vertex chain with nearest-neighbour rate 1,
    # velocities (2,-1,0), stationary distribution (1/3,1/3,1/3).
    # Spectral rates 1 and 3, weights 2/3 and 8/9.
    return (2/3)*math.exp(-t) + (8/9)*math.exp(-3*t)


def monte_carlo_two_state(kappa, t, rate_plus=2., rate_minus=1., vplus=3., vminus=-1., diffusion=1., count=35000):
    rng = random.Random(410203)
    sumsq = 0.0
    for _ in range(count):
        state = +1 if rng.random() < rate_minus/(rate_plus+rate_minus) else -1
        elapsed = 0.0
        x = 0.0
        while elapsed < t:
            rate = rate_plus if state == +1 else rate_minus
            waiting = rng.expovariate(rate)
            delta = min(t-elapsed, waiting)
            ed = math.exp(-kappa*delta)
            f = -math.expm1(-kappa*delta)
            sd = math.sqrt(diffusion * (-math.expm1(-2*kappa*delta))/kappa)
            velocity = vplus if state == +1 else vminus
            x = ed*x + (velocity/kappa)*f + rng.gauss(0.0, sd)
            elapsed += delta
            if waiting <= delta + 1e-12 and elapsed < t:
                state *= -1
        vv = vplus if state == +1 else vminus
        sumsq += (vv-kappa*x)**2
    return sumsq/count/diffusion-kappa


def main():
    # First model is the asymmetric two-state persistent swimmer.
    cases = {
        "two-state": model(1/3, [(32/9, 3.)], 1.),
        "three-state path": model(1/3, [(2/3, 1.),(8/9, 3.)], 0.7),
        "constant velocity": model(1.7, [], 0.5),
        "zero drift": model(0., [(2/3, 1.),(8/9, 3.)], 1.2),
    }
    nchecked = 0
    for name, p in cases.items():
        mean, var_v, w, coeffs, d = p
        for k in [0.35, 0.07, 0.003]:
            for s in [0.1, 0.35, 1., 2.5]:
                t = s/k
                vp = centered_variance_x(k,t,coeffs,d)
                c = covariance_xv(k,t,coeffs)
                assert vp >= -1e-12
                assert -1e-12 <= c <= w+1e-12
                assert vp <= (d+w)/k +1e-8
                actual = flux(k,t,p)
                expected = flux_limit(s,p)
                assert abs(actual-expected) <= k*(2*w+d)/d+1e-10
                assert math.isfinite(actual)
                nchecked += 5
            for a,b in [(0.2, 1.),(1.,2.),(0.3,3.)]:
                integral = simpson(lambda s:flux(k,s/k,p),a,b)
                target = area_limit(a,b,p)
                bound = k*(b-a)*(2*w+d)/d
                assert abs(integral-target) <= bound+1e-8
                nchecked += 1
            # Large-time flux must reproduce the full stationary entropy production.
            large_t = max(100/k, 100)
            stationary = sum(weight*rate/(k+rate) for weight, rate in coeffs)/d
            assert abs(flux(k,large_t,p)-stationary) < 1e-9
            nchecked += 1
        print(name, "all finite deterministic checks passed")
    # A distinct pathwise simulator tests drift, switching and Brownian normalization.
    p=cases['two-state']
    k=0.06
    t=16.
    empirical=monte_carlo_two_state(k,t)
    predicted=flux(k,t,p)
    assert abs(empirical-predicted)<0.08, (empirical,predicted)
    nchecked += 1
    print("pathwise simulation", f"empirical={empirical:.6f}",f"moment prediction={predicted:.6f}")
    print("checked assertions:",nchecked)


if __name__ == '__main__':
    main()
