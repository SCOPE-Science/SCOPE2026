"""Reproducibility diagnostics for a vanishing-perturbation periodic multiplier law.
This is a finite check, not a substitute for the analytic limit proof.
"""
import math


def periodic_point(b, n, eps, k):
    q = b**n - 1
    x = k / q
    for _ in range(12):
        y, dy = x, 1.0
        for _ in range(n):
            c = math.cos(2 * math.pi * y)
            dydx = b + eps * 2 * math.pi * c
            dy *= dydx
            y = b * y + eps * math.sin(2 * math.pi * y)
        delta = (y - x - k) / (dy - 1)
        x -= delta
        if abs(delta) < 1e-14:
            break
    return x % 1.0


def mean_log_multiplier(b, n, eps):
    q = b**n - 1
    total = 0.0
    for k in range(q):
        x = periodic_point(b, n, eps, k)
        y = x
        for _ in range(n):
            total += math.log(b + 2 * math.pi * eps * math.cos(2 * math.pi * y))
            y = b*y + eps*math.sin(2*math.pi*y)
    return total / q


def check_fourier(b, n):
    q = b**n-1
    freqs = [pow(b, j, q) for j in range(n)]
    assert q > 3
    # No first-order resonances in the uniform periodic grid.
    for f in freqs:
        assert f % q
        assert (2 * f) % q
    for i in range(n):
        for j in range(i):
            assert (freqs[i]-freqs[j]) % q
            assert (freqs[i]+freqs[j]) % q
    # Explicit Fourier computation of the periodic conjugacy coefficient.
    # u(x)=-(1/q)*sum_{j=0}^{n-1}b**(n-1-j)sin(2pi*b**j*x).
    # Only j=0 correlates with sin(2pi*x).
    u_sin_mean = -b**(n-1)/(2*q)
    h_mean = -4*math.pi**2/b * u_sin_mean - math.pi**2/b**2
    exact = math.pi**2/b**2 * (b**n+1)/q
    assert abs(h_mean-exact) < 1e-12 * max(1, exact)
    return q


def check_numerical_derivative(b,n):
    h=0.00012
    m0=mean_log_multiplier(b,n,0.0)
    mp=mean_log_multiplier(b,n,h)
    mm=mean_log_multiplier(b,n,-h)
    expected = n*math.pi**2/b**2*(b**n+1)/(b**n-1)
    approx=(mp+mm-2*m0)/(2*h*h)
    assert abs(approx-expected)/expected < 0.002, (b,n,expected,approx)
    linear=(mp-mm)/(2*h)
    assert abs(linear) < 1e-4, (b,n,linear)
    return expected, approx


def main():
    count=0
    for b in range(2,7):
        for n in range(3,10):
            check_fourier(b,n)
            count+=1
    pairs=[]
    for b,n in [(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,3),(4,4)]:
        pairs.append((b,n,*check_numerical_derivative(b,n)))
    print('PASS: %d exact finite Fourier nonresonance cases and %d moving-periodic-orbit curvature checks' % (count,len(pairs)))
    for b,n,expect,obs in pairs:
        print('%d %d predicted %.10g measured %.10g' % (b,n,expect,obs))

if __name__ == '__main__':
    main()
