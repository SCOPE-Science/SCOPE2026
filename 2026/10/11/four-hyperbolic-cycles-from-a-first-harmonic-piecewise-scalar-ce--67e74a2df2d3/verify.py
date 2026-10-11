"""Numerical consistency checks for a periodic piecewise scalar equation.

Analytical proofs are in RESULT.md; quadrature/integration here do not certify
any interval for all parameters or prove global root counts.
"""
import math

PI = math.pi


def profile(s, n=32768):
    """Composite midpoint quadrature for the nonsmooth but continuous kernel."""
    h = 2 * PI / n
    return h * sum(math.exp(-abs(s - 2 * math.cos((k + 0.5) * h))) for k in range(n))


def derivative_profile(s, n=32768):
    h = 2 * PI / n
    return h * sum(
        -math.copysign(1.0, s - 2 * math.cos((k + 0.5) * h))
        * math.exp(-abs(s - 2 * math.cos((k + 0.5) * h)))
        for k in range(n)
    )


def z_return_displacement(s, eps, p=7.0, r=20.0, n=8192):
    """RK4 flow of z'=2 sin(t)+eps*(p-r*exp(-abs(z)))."""
    dt = 2 * PI / n
    z = s - 2.0
    def f(t, y):
        return 2 * math.sin(t) + eps * (p - r * math.exp(-abs(y)))
    for k in range(n):
        t = k * dt
        k1 = f(t, z)
        k2 = f(t + dt / 2, z + dt * k1 / 2)
        k3 = f(t + dt / 2, z + dt * k2 / 2)
        k4 = f(t + dt, z + dt * k3)
        z += dt * (k1 + 2*k2 + 2*k3 + k4) / 6
    return z - (s - 2.0)


def bisect(f, a, b, rounds=34):
    fa = f(a)
    fb = f(b)
    assert fa * fb < 0
    for _ in range(rounds):
        mid = (a + b) / 2
        fm = f(mid)
        if fa * fm <= 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm
    return (a + b) / 2


def main():
    lam = 7 * PI / 10
    i0, imid, i2 = profile(0), profile(1.3), profile(2)
    assert 2.1 < i0 < lam < imid < 2.3
    assert i2 < 2 < i0
    assert derivative_profile(0.5) > 0 and derivative_profile(1.8) < 0
    crossings = []
    for a, b in [(-1.9,-1.35),(-1.1,-0.5),(0.5,1.1),(1.35,1.9)]:
        crossings.append(bisect(lambda s:profile(s, n=2048)-lam,a,b))
    assert len(crossings) == 4 and crossings == sorted(crossings)
    eps = 0.001
    displacements = [z_return_displacement(s,eps) for s in [-1.9,-1.35,-1.1,-0.5,0.5,1.1,1.35,1.9]]
    for i in [0,2,4,6]:
        assert displacements[i] * displacements[i+1] < 0
    print("CHECK_OK")
    print("I(0)=%.10f, I(1.3)=%.10f, I(2)=%.10f, sample level=%.10f" % (i0, imid, i2, lam))
    print("four limiting roots", ", ".join("%.8f" % s for s in crossings))
    print("four return-displacement brackets at eps=0.001 verified")

if __name__ == "__main__":
    main()
