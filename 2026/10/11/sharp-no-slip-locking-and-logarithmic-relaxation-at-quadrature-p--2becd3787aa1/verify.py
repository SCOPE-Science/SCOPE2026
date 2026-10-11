"""Reproduce finite tests for the no-slip two-cluster map.

Universal statements are proved analytically in RESULT.md; these diagnostics
are not substitutes for the proof or checks of infinite orbits.
"""
import math

TWO_PI = 2 * math.pi

def root_t():
    lo, hi = math.pi / 2, math.pi - 1e-9
    for _ in range(100):
        mid = (lo + hi) / 2
        if math.tan(mid / 2) < mid:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def phi(x, b):
    return x + b * (1 - math.cos(x))

def iterate_x(x, b, n):
    for _ in range(n):
        x -= 2 * b * math.sin(x / 2) ** 2
        assert x > 0
    return x

def kuramoto_two_cluster_delta(p, q, u, v, k, beta=math.pi/2):
    angles = [u] * p + [v] * q
    upd = [angles[i] + k / (p + q) * sum(math.sin(w - angles[i] - beta)
                 for w in angles) for i in range(p + q)]
    return (upd[-1] - upd[0]) % TWO_PI

def main():
    assertions = 0
    t = root_t()
    bc = t / (1 - math.cos(t))
    assert abs(t - 2.3311223704144226) < 2e-13; assertions += 1
    assert abs(bc - 1.380050139689301) < 2e-13; assertions += 1
    xstar = TWO_PI - t
    assert abs(phi(xstar, bc) - TWO_PI) < 2e-14; assertions += 1
    for m in range(1, 2000):
        x = TWO_PI * m / 2000
        assert x < phi(x, bc) < TWO_PI + 4e-14; assertions += 1
        assert phi(x, 0.99 * bc) < TWO_PI; assertions += 1
    assert phi(xstar, 1.00001 * bc) > TWO_PI; assertions += 1
    for p, q in [(2, 1), (3, 1), (4, 2), (8, 3), (1, 3)]:
        for j in range(12):
            u = 0.27 * j - 1.1
            v = u + (j + 1) * 0.41
            k = 0.25 + 0.09 * j
            direct = kuramoto_two_cluster_delta(p,q,u,v,k)
            d = (v - u) % TWO_PI
            predicted = (d + k*(p-q)/(p+q)*(1-math.cos(d))) % TWO_PI
            assert abs(math.sin(direct - predicted)) < 2e-13
            assert math.cos(direct - predicted) > 0.999999999999
            assertions += 2
    for b in (0.2, 0.5, 1.0, 1.1):
        for x0 in (0.3, 0.6, 1.0, 2.0, 4.0, 5.5):
            x = iterate_x(x0, b, 400)
            assert 0 < x < x0
            assertions += 1
    for b in (0.5, 1.1):
        x0 = 1.0
        x1 = iterate_x(x0, b, 4000)
        x2 = iterate_x(x1, b, 12000)
        c1 = 1/x1 - b * 4000/2 - b * math.log(4000)/2
        c2 = 1/x2 - b * 16000/2 - b * math.log(16000)/2
        assert abs(c1 - c2) < 0.02
        assertions += 1
    print(f'PASS: {assertions} finite diagnostics; t={t:.15f}, Bc={bc:.15f}')

if __name__ == '__main__':
    main()
