"""Numerical diagnostics for the exact enclosing ellipsoid of a ball plus a point.

Run: python3 verify_cap.py
All mathematical proofs and quantifiers are in RESULT.md; finite testing is diagnostic.
"""
import math
import random


def params(d, H):
    assert d >= 2 and H > 1
    r = 2.0 / ((d - 1) * H + math.hypot((d - 1) * H, 2 * math.sqrt(d)))
    a = d * (H + r) / (d + 1)
    c = (H - d * r) / (d + 1)
    b2 = d * d * (1 - r * r) / (d * d - 1)
    return r, a, math.sqrt(b2), c


def verify():
    rng = random.Random(389716)
    count = 0
    for d in (2, 3, 4, 7, 20, 100):
        for H in (1.0001, 1.01, 1.5, 2.0, 5.0, 40.0):
            r, a, b, c = params(d, H)
            assert 0 < r < 1 / d and a > b > 1 and 0 < c < a
            assert abs(d * r*r + (d-1)*H*r-1) < 4e-12
            assert abs((H-c)/a - 1) < 4e-12
            assert abs((-r-c)/a + 1/d) < 4e-12
            assert abs((1-r*r)/(b*b) - (1-1/(d*d))) < 4e-12
            assert abs(b*b - d*a*r) < 4e-12
            w_apex = 1/(d+1)
            w_ring = d/(d+1)
            assert abs(w_apex-w_ring/d) < 1e-15
            assert abs(w_apex+w_ring/(d*d)-1/d) < 1e-15
            assert abs(w_ring*(1-1/(d*d))/(d-1)-1/d) < 1e-15
            count += 9
            k = 1/(b*b)-1/(a*a)
            assert k > 0
            for i in range(250):
                z = 2*rng.random()-1
                q = ((z-c)/a)**2 + (1-z*z)/(b*b)
                assert q <= 1+4e-12
                assert abs(1-q-k*(z+r)**2) < 4e-12
                count += 2
            # The following affine test uses a diagonal ellipsoid and an arbitrary exterior point.
            axes = [rng.uniform(0.4, 3.5) for _ in range(d)]
            u = [rng.gauss(0, 1) for _ in range(d)]
            norm = math.sqrt(sum(t*t for t in u))
            u = [t/norm for t in u]
            for _ in range(10):
                z = [rng.gauss(0, 1) for _ in range(d)]
                norm = math.sqrt(sum(t*t for t in z))
                z = [t/norm for t in z]
                x = [axes[j]*z[j] for j in range(d)]
                m = sum((x[j]/axes[j]-c*u[j])*u[j] for j in range(d))
                perp2 = sum((x[j]/axes[j]-c*u[j])**2 for j in range(d))-m*m
                assert m*m/(a*a)+perp2/(b*b) <= 1+4e-12
                count += 1
    for d in (100, 250, 600, 1200):
        for H in (1.2, 2, 7):
            r, a, b, c = params(d,H)
            volume_ratio = a * math.exp((d-1)*math.log(b))
            approx = H - (H-1/H)/(2*d)
            assert abs(volume_ratio-approx) < 4/(d*d)*H
            count += 1
    for d in (2,3,10,50):
        target = d/(d+1)*(d/math.sqrt(d*d-1))**(d-1)
        r,a,b,c = params(d,1e7)
        assert abs(a*b**(d-1)/1e7-target)<2e-7
        count += 1
    print('PASS',count,'deterministic numerical diagnostics')


if __name__ == '__main__':
    verify()
