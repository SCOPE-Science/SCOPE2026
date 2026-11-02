"""Reproducible numerical checks of exact regular-tetrahedron affine section laws.

Uses only the Python standard library. Monte Carlo checks supplement, not prove,
the analytic derivations in the accompanying report.
"""
import math
import random

V = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
PAFF = 2 * math.pi / math.acos(-1 / 3) - 3
PDIR = 12 / math.pi * (
    math.asinh(1 / math.sqrt(2)) - math.log(1 + math.sqrt(3)) / math.sqrt(3)
)

def survival(q):
    if not 0 <= q <= 1:
        raise ValueError('q must be in [0,1]')
    t = (1 - q) / (1 + q)
    return 12 / math.pi * (math.atan(math.sqrt(1 + 2 * t * t)) - math.pi / 4)

def simpson(f, n=16384):
    if n % 2:
        raise ValueError('n must be even')
    h = 1 / n
    return h / 3 * (f(0) + f(1) + 4 * sum(f(i * h) for i in range(1, n, 2))
                  + 2 * sum(f(i * h) for i in range(2, n, 2)))

def projection(u):
    return sorted(sum(x * y for x, y in zip(v, u)) for v in V)

def sample_unit(rng):
    z = 2 * rng.random() - 1
    theta = 2 * math.pi * rng.random()
    a = math.sqrt(1-z*z)
    return a*math.cos(theta), a*math.sin(theta), z

def run():
    assert abs(survival(0) - 1) < 1e-14
    assert abs(survival(1)) < 1e-14
    assert all(survival(i / 10) >= survival((i+1) / 10)
               for i in range(10))
    f = lambda t: 12 / math.pi * t / ((1+t*t)*math.sqrt(1+2*t*t))
    q = lambda t: (1-t)/(1+t)
    assert abs(simpson(f) - 1) < 1e-11
    assert abs(simpson(lambda t: f(t)*q(t)) - PDIR) < 2e-11
    for cutoff in (0.05, 0.2, 0.5, 0.8):
        t0 = (1-cutoff)/(1+cutoff)
        # Numerical integral over the complete unit interval (fixed scaling).
        val = t0 * simpson(lambda x: f(t0*x))
        assert abs(val - survival(cutoff)) < 2e-11
    rng = random.Random(20230427)
    size = 150000
    sum_w = sum_g = sum_q = 0.0
    high = 0
    count_direct = 0
    for i in range(size):
        u = sample_unit(rng)
        a, b, c, d = projection(u)
        width, gap = d-a, c-b
        ratio = gap/width
        co = sorted(abs(x) for x in u)
        expected = (co[2]-co[1])/(co[2]+co[1])
        assert abs(ratio-expected) < 2e-12
        sum_w += width
        sum_g += gap
        sum_q += ratio
        high += ratio > 0.5
        offset = a + width * rng.random()
        hits = sum((sum(x*y for x,y in zip(V[j],u)) - offset) *
                   (sum(x*y for x,y in zip(V[k],u)) - offset) < 0
                   for j in range(4) for k in range(j+1,4))
        count_direct += hits == 4
        assert hits in (3,4)
    mean_q = sum_q/size
    width_prob = sum_g/sum_w
    direct_prob = count_direct/size
    high_prob = high/size
    assert abs(mean_q - PDIR) < 0.006
    assert abs(direct_prob - PDIR) < 0.006
    assert abs(width_prob - PAFF) < 0.006
    assert abs(high_prob - survival(0.5)) < 0.006
    assert PAFF < PDIR
    print('EXACT', f'{PDIR:.15f}', f'{PAFF:.15f}', f'{survival(0.5):.15f}')
    print('SIMULATION', f'{mean_q:.6f}', f'{direct_prob:.6f}',
          f'{width_prob:.6f}', f'{high_prob:.6f}')
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    run()
