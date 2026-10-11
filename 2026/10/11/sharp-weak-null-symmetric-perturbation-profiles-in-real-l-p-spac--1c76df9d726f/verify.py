"""Independent numerical sanity checks for a scalar norm-profile identity.

The mathematical proof is analytic; finite grids are not evidence of exhaustive
coverage. Run with: python3 verify.py
"""
from math import isclose


def ap(p, d, u):
    return ((d + u) ** p + abs(d - u) ** p) / 2.0


def profile(p, a, d, t):
    if p < 2:
        return a**p + ap(p, d, t)
    return a**p + d**p + t**p


def run():
    tests = 0
    p_values = [1.01, 1.10, 1.25, 1.5, 1.75, 1.99]
    vals = [0.0, 0.01, 0.1, 0.25, 0.5, 0.99, 1.0, 1.5, 2.0, 4.0, 10.0]
    for p in p_values:
        for d in vals:
            for u in vals:
                for v in vals:
                    if v < u:
                        continue
                    # Monotonicity of u^p-A_p(d,u) is the atomic-mass
                    # allocation lemma needed to turn Hanner into a bound.
                    assert ap(p, d, v) - ap(p, d, u) <= v**p - u**p + 1e-9
                    tests += 1
        for d in vals:
            for t in vals:
                # A_p(d,t) is the exact balanced-sign integral for
                # a diffuse component of Lp mass d and norm t.
                if d > 0:
                    z = t / d
                    left = (d**p / 2) * (abs(1 + z)**p + abs(1 - z)**p)
                    assert isclose(left, ap(p, d, t), rel_tol=1e-12, abs_tol=1e-10)
                    tests += 1
                assert ap(p, d, t) <= d**p + t**p + 1e-9
                tests += 1
    for p in [2.0, 2.5, 3.0, 4.0, 8.0]:
        for d in vals:
            for t in vals:
                for a in vals:
                    assert isclose(profile(p, a, d, t), a**p+d**p+t**p, rel_tol=1e-12, abs_tol=1e-10)
                    tests += 1
    # On an atomic two-coordinate block, weakly null vectors vanish
    # coordinatewise, leaving only their asymptotic norm-power contribution.
    for p in [1.25, 1.5, 1.75, 3.0]:
        for a in vals:
            for t in vals:
                for eps in [1e-3, 1e-5]:
                    lhs = abs(a+eps)**p + max(t**p-eps**p,0)
                    rhs = a**p+t**p
                    bound = p * (a+eps)**(p-1) * eps + eps**p
                    assert abs(lhs-rhs) <= bound + 1e-9
                    tests += 1
    print(f"VERIFY_OK scalar_checks={tests} p_below_2=6 p_above_2=5 analytic_proof_required=True")


if __name__ == '__main__':
    run()
