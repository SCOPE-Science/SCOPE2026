"""Reproducibility checks for the explicit John ellipsoid of an asymmetric suspension.

The finite checks support, but do not replace, the analytic proof in RESULT.md.
Requires Python 3 standard library only.
"""
from math import hypot, sqrt, isclose


def parameters(a, b, d):
    assert a > 0 and b > 0 and isinstance(d, int) and d >= 2
    T = a*a + b*b
    q = (T + sqrt(T*T + 4*(d*d-1)*a*a*b*b))/(2*(d*d-1))
    t = sqrt(q)
    X, Y = hypot(a, t), hypot(b, t)
    u = (a+b)/(X+Y)
    v = t*u
    c = u*X-a
    return u, v, c, t


def objective(a, b, d):
    u, v, _, _ = parameters(a, b, d)
    return u**(d-1)*v


checks = 0
for d in range(2, 16):
    for ia in range(1, 22):
        a = ia / 13
        for ib in range(1, 17):
            b = ib / 11
            u, v, c, t = parameters(a, b, d)
            assert isclose(hypot(a*u, v), a+c, rel_tol=2e-12, abs_tol=2e-12)
            assert isclose(hypot(b*u, v), b-c, rel_tol=2e-12, abs_tol=2e-12)
            assert isclose(hypot(a, t)*hypot(b, t), d*t*t,
                           rel_tol=2e-12, abs_tol=2e-12)
            assert -a < c < b
            assert c * (b-a) >= -1e-12
            # Exact stationary point has strictly larger objective than scaled competitors.
            for m in (.5, .8, .97, 1.03, 1.3, 2):
                z = t*m
                ratio = z/(hypot(a,z)+hypot(b,z))**d
                optimum_ratio = t/(hypot(a,t)+hypot(b,t))**d
                assert ratio < optimum_ratio*(1+5e-12)
            checks += 1
    H = 3.
    last = -1.
    # More imbalanced configurations strictly lose optimal ellipsoid volume.
    for i in range(100, -1, -1):
        a = H*(1+i/100)/2
        b = H-a
        # Endpoint with b=0 has no actual positive-base double pyramid;
        # use the exact continuous limiting formula there.
        if b == 0:
            u = sqrt((d-1)/(d+1)); v = H/(d+1)
            value = u**(d-1)*v
        else:
            value = objective(a,b,d)
        assert value > last*(1-3e-12)
        last = value
        checks += 1
    symmetric = ((d-1)/d)**((d-1)/2)*H/(2*sqrt(d))
    cone_limit = ((d-1)/(d+1))**((d-1)/2)*H/(d+1)
    ratio = (d+1)/(2*sqrt(d))*((d+1)/d)**((d-1)/2)
    assert isclose(symmetric/cone_limit, ratio, rel_tol=1e-12)
    checks += 1

print(f"PASS: {checks} analytic-identity, uniqueness, and imbalance-profile checks")
