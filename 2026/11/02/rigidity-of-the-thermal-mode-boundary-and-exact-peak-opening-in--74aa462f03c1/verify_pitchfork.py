"""Numerical checks for a Gaussian-smoothed symmetric Beta law.

Run: python3 verify_pitchfork.py
No dependencies beyond the Python standard library.
The mathematical proof is analytic; this executable supplies finite corroboration.
"""
import math


def moments(b, z, n=8192):
    """Ratios of exponentially tilted Beta moments; midpoint change of variable."""
    a0 = a1 = a2 = 0.0
    for j in range(n):
        u = (j + 0.5) / n
        t = -math.expm1(math.log1p(-u * u) / b)
        w = u / math.sqrt(t) * math.exp(-z * t)
        a0 += w
        a1 += w * t
        a2 += w * t * t
    return a1 / a0, a2 / a0


def critical(b):
    def h(z):
        return 2.0 * z * moments(b, z)[0] - 1.0
    low, high = 0.1, 2.0
    while h(high) < 0:
        high *= 2
    for _ in range(48):
        mid = (low + high) / 2.0
        if h(mid) > 0:
            high = mid
        else:
            low = mid
    return 1 / (low + high)


def mode_integral(x, b, B, n=4096):
    out = 0.0
    for j in range(n):
        u = (j + 0.5) / n
        t = -math.expm1(math.log1p(-u * u) / b)
        yy = math.sqrt(t)
        w = u / yy
        out += w * ((yy - x) * math.exp(-((x - yy) ** 2) / (2 * B))
                    - (yy + x) * math.exp(-((x + yy) ** 2) / (2 * B)))
    return out


def mode(b, B):
    low, high = 0.005, 1.0
    assert mode_integral(low, b, B) > 0
    assert mode_integral(high, b, B) < 0
    for _ in range(32):
        mid = (low + high) / 2
        if mode_integral(mid, b, B) > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def run():
    checks = 0
    values = []
    for b in (0.15, 0.25, 0.5, 0.75, 0.85):
        B = critical(b)
        H, H2 = moments(b, 1/(2*B))
        assert abs(H-B) < 8e-8
        checks += 1
        assert abs(H2-(2*b+1)*B*B) < 1e-6
        checks += 1
        values.append((b,B))
        assert 0<B<1
        checks += 1
        for eps in (.03, .01, .003):
            if eps >= B: continue
            m = mode(b,B-eps)
            ratio=m/math.sqrt(3*eps)
            assert .93<ratio<1.04, (b,B,eps,ratio)
            checks += 1
        print('b=%.2f  B*=%.12f'% (b,B))
    assert all(values[i][1] > values[i+1][1] for i in range(len(values)-1))
    checks += 1
    for b,B in values:
        for delta in (-.01, .01):
            z=1/(2*(B+delta))
            H,_=moments(b,z)
            q=H/(B+delta)-1
            assert (q>0)==(delta<0)
            checks += 1
    print('PASS: %d finite numerical checks'%checks)

if __name__=='__main__':
    run()
