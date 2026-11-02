"""Reproducible finite checks of the analytic period-two construction.

This script uses only the Python standard library. Its floating-point tests are
illustrations; the infinite existence and uniqueness claims use the proof.
"""
import math


def correction(z):
    a = (1.0 - z + z*z/2.0) / (1.0 - z + z*z)
    r = 1.0 / (math.hypot(1.0, z) + z) if z >= 0.0 else math.hypot(1.0, z) - z
    return 2.0 / (1.0 + a*r)


def eval_q(x, delta):
    f = x + delta*math.sin(x)
    df = 1.0 + delta*math.cos(x)
    ddf = -delta*math.sin(x)
    ell = f*ddf/(df*df)
    return correction(ell)*f/(x*df)


def step(x, delta):
    if x == 0.0:
        return 0.0
    return x*(1.0 - eval_q(x, delta))


def newton(x, delta):
    return x - (x + delta*math.sin(x))/(1.0 + delta*math.cos(x))


def root_in_interval(delta, n):
    lo = 2.0*math.pi*n + 5.0*math.pi/4.0
    hi = 2.0*math.pi*n + 3.0*math.pi/2.0
    if not (eval_q(lo, delta) > 2.0 > eval_q(hi, delta)):
        return None
    for _ in range(75):
        mid = (lo+hi)/2.0
        if eval_q(mid, delta) > 2.0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0


def main():
    checks = 0
    # The first several windows may lack a cycle, as allowed by the theorem.
    for delta in (0.025, 0.05, 0.1, 0.2, 0.3):
        roots = []
        for n in (100, 300, 1000, 3000, 10000):
            r = root_in_interval(delta, n)
            if r is None:
                continue
            roots.append(r)
            assert abs(step(r, delta)+r) < 4e-6
            checks += 1
            assert abs(step(-r, delta)-r) < 4e-6
            checks += 1
            assert 0 < (1.0-delta) <= 1.0+delta*math.cos(r) <= 1.0+delta
            checks += 1
        assert len(roots) >= 2, (delta, roots)
        checks += 1

        # Newton's contraction estimate holds for every real initial value.
        rho = 2.0*delta/(1.0-delta)
        for x in (-10000.0, -100.0, -10.0, -1.0, -0.01,
                  0.01, 1.0, 10.0, 100.0, 10000.0):
            y = newton(x, delta)
            assert abs(y) <= rho*abs(x) + 1e-11
            checks += 1
        for n in (1000, 3000, 10000):
            r = root_in_interval(delta, n)
            if r is None:
                continue
            B = 2.0*math.pi*n + 3.0*math.pi/2.0
            limit = 1.0 + 1.0/(4.0*delta*delta)
            scaled = B*(B-r)
            assert abs(scaled/limit-1.0) < 0.12, (delta, n, scaled, limit)
            checks += 1
    print(f"PASS {checks} finite tests; analytic asymptotics proved separately")


if __name__ == "__main__":
    main()
