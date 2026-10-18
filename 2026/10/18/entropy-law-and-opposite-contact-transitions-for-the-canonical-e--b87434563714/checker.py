"""Independent scalar consistency checks for the ellipsoid direct-sum identities.

Run with Python 3; no external modules required. Numerical samples do not prove
continuous assertions, which are established analytically in RESULT.md.
"""
from math import isclose, exp, log, sqrt, inf
from random import Random

rng = Random(271828)
trials = 0
for dimensions in ((1, 2), (2, 1, 3), (4, 2, 1, 5)):
    n = sum(dimensions)
    weights = [d / n for d in dimensions]
    entropy = -sum(w * log(w) for w in weights)
    for p in (1, 1.3, 1.5, 2, 3, 4, 8, inf):
        inverse_p = 0.0 if p == inf else 1 / p
        q_inner = 2 * p / (2 - p) if p < 2 else None
        q_outer = 2 * p / (p - 2) if 2 < p < inf else 2.0 if p == inf else None
        a = [w ** (1 / q_inner) for w in weights] if p < 2 else [1.] * len(weights)
        c = [w ** (1 / q_outer) for w in weights] if p > 2 else [1.] * len(weights)
        if p < 2:
            assert isclose(sum(t ** q_inner for t in a), 1., rel_tol=1e-12)
            inner_r = [sqrt(w) for w in weights]
            attained = sum((a[i] * inner_r[i]) ** p for i in range(len(weights)))
            assert isclose(attained, 1., rel_tol=1e-12)
        elif p > 2:
            outer_s = [w ** inverse_p if p < inf else 1. for w in weights]
            attained = sum((c[i] * outer_s[i]) ** 2 for i in range(len(weights)))
            assert isclose(attained, 1., rel_tol=1e-12)
            assert isclose(sum(t ** q_outer for t in c), 1., rel_tol=1e-12)
        log_ratio = -sum(dimensions[i] * log(a[i] * c[i]) for i in range(len(weights)))
        assert isclose(log_ratio, n * entropy * abs(inverse_p - .5), abs_tol=1e-12)
        for j in range(1500):
            components = [abs(rng.gauss(0, 1)) + 1e-9 for _ in weights]
            norm2 = sqrt(sum(t*t for t in components))
            r = [t / norm2 for t in components]
            if p < 2:
                power = sum((a[i] * r[i]) ** p for i in range(len(weights)))
                assert power <= 1.00000000001
            else:
                power = max(a[i] * r[i] for i in range(len(weights))) if p == inf else sum((a[i] * r[i]) ** p for i in range(len(weights)))
                assert power <= 1.00000000001
            if p < inf:
                normp = sum(t ** p for t in components) ** (1 / p)
                s = [t / normp for t in components]
            else:
                mx = max(components)
                s = [t / mx for t in components]
            outer_power = sum((c[i] * s[i]) ** 2 for i in range(len(weights)))
            assert outer_power <= 1.00000000001
            trials += 1
print('PASS: dimension-weighted analytic identities and', trials, 'sampled scalar norm constraints')
