"""Reproducibility checks for a two-particle run-and-tumble first-contact theorem.

Run: python verification.py
Requires sympy and mpmath for the symbolic/high-precision checks.
"""
import math
import random
import sympy as sp
import mpmath as mp


def transform(s, alpha, half_circumference, speed, gap):
    """Laplace transform of the first contact time, initially closing."""
    if s == 0:
        return 1.0
    k = math.sqrt(s * (s + 4 * alpha)) / (2 * speed)
    delta = math.sqrt(s * (s + 4 * alpha)) / (s + 2 * alpha)
    return (math.cosh(k * (half_circumference - gap))
            + delta * math.sinh(k * (half_circumference - gap))) / (
            math.cosh(k * half_circumference)
            + delta * math.sinh(k * half_circumference))


def exact_mean(alpha, half_circumference, speed, gap):
    return gap / speed + alpha * gap * (2 * half_circumference - gap) / (2 * speed ** 2)


def sample_first_contact(alpha, half_circumference, speed, gap, rng):
    """Independent event-driven simulation of the three-state relative process."""
    state = 0  # 0 closing, 1 opening, 2 stalled
    t = 0.0
    x = gap
    for _ in range(1000000):
        jump_time = rng.expovariate(2 * alpha)
        if state == 0:
            time_to_contact = x / (2 * speed)
            if time_to_contact <= jump_time:
                return t + time_to_contact
            t += jump_time
            x -= 2 * speed * jump_time
            state = 2
        elif state == 1:
            time_to_far_end = (half_circumference - x) / (2 * speed)
            if time_to_far_end <= jump_time:
                t += time_to_far_end
                x = half_circumference
                state = 0  # torus folding, without a physical bounce
            else:
                t += jump_time
                x += 2 * speed * jump_time
                state = 2
        else:
            t += jump_time
            state = rng.randrange(2)
    raise AssertionError('unbounded trajectory')


def verify():
    checks = 0
    s, a, x, h, v = sp.symbols('s a x h v', positive=True)
    k2 = s * (s + 4 * a) / (4 * v ** 2)
    dk = s * (s + 4 * a) / (2 * v * (s + 2 * a))

    # Independent formal Taylor expansion of the backward-equation solution.
    def cos_part(y):
        return 1 + k2 * y ** 2 / 2 + k2 ** 2 * y ** 4 / 24

    def sin_part(y):
        return dk * y * (1 + k2 * y ** 2 / 6)

    numer = sp.series(cos_part(h - x) + sin_part(h - x), s, 0, 2).removeO()
    denom = sp.series(cos_part(h) + sin_part(h), s, 0, 2).removeO()
    first = sp.series(numer / denom, s, 0, 2).removeO()
    predicted_mean = x / v + a * x * (2 * h - x) / (2 * v ** 2)
    assert sp.simplify(-sp.diff(first, s).subs(s, 0) - predicted_mean) == 0
    checks += 1

    # Symmetric/antisymmetric ODE and endpoint data.
    k = sp.sqrt(s * (s + 4 * a)) / (2 * v)
    d = 2 * v * k / (s + 2 * a)
    norm = sp.cosh(k * h) + d * sp.sinh(k * h)
    fc = (sp.cosh(k * (h - x)) + d * sp.sinh(k * (h - x))) / norm
    fo = (sp.cosh(k * (h - x)) - d * sp.sinh(k * (h - x))) / norm
    fs = a * (fc + fo) / (s + 2 * a)
    assert sp.simplify(fc.subs(x, 0) - 1) == 0
    assert sp.simplify((fo - fc).subs(x, h)) == 0
    assert sp.simplify(-2 * v * sp.diff(fc, x) - (s + 2 * a) * fc + 2 * a * fs) == 0
    assert sp.simplify(2 * v * sp.diff(fo, x) - (s + 2 * a) * fo + 2 * a * fs) == 0
    assert sp.simplify((s + 2 * a) * fs - a * (fc + fo)) == 0
    checks += 5

    # Formal rare-tumble moment coefficients, verifying orders 2 to 10.
    z, order = sp.symbols('z order')
    first_alpha = -x / (2 * v) * z * (z + 4) / (z + 2)
    for m in range(2, 11):
        coefficient = sp.expand(sp.series(first_alpha, z, 0, m + 1).removeO()).coeff(z, m)
        assert sp.simplify((-1) ** m * sp.factorial(m) * coefficient -
                           sp.factorial(m) * x / (2 ** m * v)) == 0
        checks += 1

    # Independent numerical evaluation of exact first-contact trajectories.
    rng = random.Random(4052026)
    for alpha, half, speed, gap in [
        (1., 1., 1., .6), (.17, 1., 1., .6), (.5, 2., 1.5, 1.1),
    ]:
        count = 38000
        times = [sample_first_contact(alpha, half, speed, gap, rng)
                 for _ in range(count)]
        avg = sum(times) / count
        var = sum((t - avg) ** 2 for t in times) / (count - 1)
        standard_error = math.sqrt(var / count)
        assert abs(avg - exact_mean(alpha, half, speed, gap)) < 7 * standard_error + .001
        checks += 1
        for ss in (.25, .8):
            values = [math.exp(-ss * t) for t in times]
            avg_lap = sum(values) / count
            var_lap = sum((y - avg_lap) ** 2 for y in values) / (count - 1)
            se_lap = math.sqrt(var_lap / count)
            assert abs(avg_lap - transform(ss, alpha, half, speed, gap)) < 7 * se_lap + .001
            checks += 1

    # Uniform-in-small-alpha expansion at the natural Laplace scale.
    mp.mp.dps = 50
    for aa in (mp.mpf('0.01'), mp.mpf('0.003'), mp.mpf('0.001')):
        for zz in (mp.mpf('.2'), mp.mpf('1.3')):
            xx, hh, vv = mp.mpf('.6'), mp.mpf('1'), mp.mpf('1')
            ss = aa * zz
            kk = mp.sqrt(ss * (ss + 4 * aa)) / (2 * vv)
            dd = mp.sqrt(ss * (ss + 4 * aa)) / (ss + 2 * aa)
            exact = ((mp.cosh(kk * (hh - xx)) + dd * mp.sinh(kk * (hh - xx))) /
                     (mp.cosh(kk * hh) + dd * mp.sinh(kk * hh)))
            approximation = 1 - aa * xx * zz * (zz + 4) / (2 * vv * (zz + 2))
            assert abs(exact - approximation) < aa ** 2
            checks += 1

    print(f'PASS: {checks} symbolic, simulation and asymptotic checks')
    print('Note: finite simulations are diagnostics, not the proof of the analytic theorem.')


if __name__ == '__main__':
    verify()
