"""Independent numerical and algebraic checks for diametral sections of a two-ball product.

Requirements: Python 3 and NumPy. Execute: python CHECK.py
All tests are finite sanity checks; the universal proof is analytical.
"""
import math
import random
import numpy as np


def formula(h):
    assert h > 0.0
    return math.pi * h / (2.0 * (1.0 + h*h))


def oriented_plane_event(q, h):
    # q has four orthonormal-column rows and two columns.
    proj = q[:2, :].T @ q[:2, :]
    lam = np.linalg.eigvalsh(proj)
    c = 1.0 / (1.0 + h*h)
    return bool(lam[0] <= c <= lam[1])


def grassmann_and_hodge_agree():
    rng = np.random.default_rng(20261017)
    count = 0
    for h in (0.25, 0.5, 1.0, 2.0, 4.0):
        c = 1.0 / (1.0 + h*h)
        successes = 0
        for _ in range(12000):
            q, _ = np.linalg.qr(rng.normal(size=(4, 2)))
            w12 = float(np.linalg.det(q[:2, :]))
            w34 = float(np.linalg.det(q[2:, :]))
            a, b = w12 + w34, w12 - w34
            assert abs(a) <= 1.0 + 1.0e-12
            assert abs(b) <= 1.0 + 1.0e-12
            x, y = (a+b)/2.0, (a-b)/2.0
            ellipse = (x*x/c + y*y/(1.0-c) <= 1.0)
            event = oriented_plane_event(q, h)
            assert event == ellipse
            successes += int(event)
            count += 1
        # Binomial margin ~6 standard deviations, fixed seed reproducible.
        empirical = successes / 12000.0
        assert abs(empirical - formula(h)) < 0.024, (h, empirical, formula(h))
    return count


def diamond_uniform_check():
    rng = random.Random(11919)
    count = 0
    n = 90000
    for h in (0.25, 0.5, 1.0, 2.0, 4.0):
        c = 1.0 / (1.0 + h*h)
        hits = 0
        for _ in range(n):
            a = 2.0 * rng.random() - 1.0
            b = 2.0 * rng.random() - 1.0
            x, y = (a+b)/2.0, (a-b)/2.0
            hits += (x*x/c + y*y/(1.0-c) <= 1.0)
            count += 1
        assert abs(hits/n - formula(h)) < 0.009, (h, hits/n)
    return count


def higher_dimensional_witness_check():
    rng = random.Random(803)
    count = 0
    for h in (0.1, 1.0, 7.0):
        for _ in range(2500):
            normal = [rng.gauss(0,1) for i in range(4)]
            r1 = math.hypot(normal[0], normal[1])
            r2 = math.hypot(normal[2], normal[3])
            if min(r1,r2) == 0.0: continue
            w = [-normal[1]/r1, normal[0]/r1,
                 -h*normal[3]/r2, h*normal[2]/r2]
            assert abs(sum(x*y for x,y in zip(w,normal))) < 2e-13*(1+h)*max(r1,r2)
            assert abs(math.hypot(*w[:2])-1.0) < 1e-13
            assert abs(math.hypot(*w[2:])-h) < 1e-13*(1+h)
            count += 1
    return count


def exact_profiles():
    # Values of the exact one-parameter formula and its reciprocal symmetry.
    for h in (0.125, 0.5, 1, 2, 8):
        assert math.isclose(formula(h),formula(1.0/h),rel_tol=1e-14)
        assert formula(h) <= math.pi/4.0+1e-14
    assert math.isclose(formula(1),math.pi/4.0)


if __name__ == '__main__':
    exact_profiles()
    p=grassmann_and_hodge_agree()
    q=diamond_uniform_check()
    r=higher_dimensional_witness_check()
    print(f'VERIFY_OK random_planes={p} independent_diamond_draws={q} '
          f'hyperplane_witnesses={r} aspect_ratios=5')
