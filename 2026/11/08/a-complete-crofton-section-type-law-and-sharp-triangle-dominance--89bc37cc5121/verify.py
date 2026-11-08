"""Reproducibility checks for Crofton-plane sections of right rectangular pyramids.

Requires only Python 3 standard library. Numerical integration and Monte Carlo
corroborate, but do not prove, the analytic statement.
"""
import math
import random


def integrate_simpson(f, lo, hi, panels=4000):
    assert panels % 2 == 0
    step = (hi - lo) / panels
    val = f(lo) + f(hi)
    for i in range(1, panels):
        val += (4 if i % 2 else 2) * f(lo + i * step)
    return val * step / 3


def formulas(a, b, h):
    assert min(a, b, h) > 0
    ell = math.sqrt(a * a + b * b + h * h)
    angle = math.atan(h * ell / (a * b))
    denominator = (a + b) * math.pi - a * math.atan(h / b) - b * math.atan(h / a) + ell * angle

    def term(c):
        return c * math.atan(h / c) if c > 1e-14 else 0.

    def integrand(t):
        cp = a * math.cos(t) + b * math.sin(t)
        cm = abs(a * math.cos(t) - b * math.sin(t))
        return term(cp) - term(cm)

    kink = math.atan2(a, b)
    J = integrate_simpson(integrand, 0, kink) + integrate_simpson(integrand, kink, math.pi / 2)
    expected = 2 * math.pi * (a + b + ell) / denominator
    p5 = J / denominator
    p3 = 4 - expected + p5
    p4 = expected - 3 - 2 * p5
    return (p3, p4, p5, expected, denominator)


def sample_intersection(a, b, h, proposals, seed):
    rng = random.Random(seed)
    vertices = [(a, b, 0), (-a, b, 0), (-a, -b, 0), (a, -b, 0), (0, 0, h)]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)] + [(k, 4) for k in range(4)]
    normbound = math.sqrt(a*a+b*b+h*h)
    counts = [0] * 6
    for _ in range(proposals):
        z = rng.uniform(-1, 1)
        az = rng.uniform(0, 2*math.pi)
        r = math.sqrt(1-z*z)
        u = (r*math.cos(az), r*math.sin(az), z)
        heights = [sum(ui*vi for ui,vi in zip(u,v)) for v in vertices]
        s = rng.uniform(-normbound, normbound)
        if not min(heights) < s < max(heights):
            continue
        side = [t > s for t in heights]
        n = sum(side[i] != side[j] for i, j in edges)
        assert n in (3, 4, 5)
        counts[n] += 1
    total = sum(counts)
    assert total > 1000
    return [counts[k]/total for k in (3, 4, 5)], sum(k*counts[k] for k in (3, 4, 5))/total, total


def main():
    samples = [(1,1,.25), (1,1,math.sqrt(2)), (1,1,3), (2,1,1), (3,.5,5)]
    accepted = 0
    for i, (a,b,h) in enumerate(samples):
        p3,p4,p5,e,D = formulas(a,b,h)
        assert 0 < p5 < p3 < 1
        assert 0 < p4 < 1
        assert abs(p3+p4+p5 - 1) < 1e-12
        assert 2+math.sqrt(2) < e < 4
        eps = 1e-5*h
        Ddiff = (formulas(a,b,h+eps)[4]-formulas(a,b,h-eps)[4])/(2*eps)
        rhs = h/math.sqrt(a*a+b*b+h*h)*math.atan(h*math.sqrt(a*a+b*b+h*h)/(a*b))
        assert abs(Ddiff-rhs) < 3e-8*max(1,rhs)
        weights, emc, n = sample_intersection(a,b,h,90000,4810+i)
        accepted += n
        assert max(abs(q-v) for q,v in zip(weights,(p3,p4,p5))) < .015
        assert abs(emc - e) < .025
        print(f"{a:g},{b:g},{h:.6g}: P3={p3:.8f} P4={p4:.8f} P5={p5:.8f} mean={e:.8f} accepted={n}")
    e_low = formulas(1,1,1e-5)[3]
    e_high = formulas(1,1,1e5)[3]
    assert 0 < e_low - (2+math.sqrt(2)) < 1e-4
    assert 0 < 4 - e_high < 1e-4
    print(f"RECTANGULAR_PYRAMID_CROFTON_LAW_OK accepted={accepted}")

if __name__=='__main__':
    main()
