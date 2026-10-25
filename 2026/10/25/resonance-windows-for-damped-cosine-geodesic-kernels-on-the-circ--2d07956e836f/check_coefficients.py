"""Optional numerical diagnostics for a circle damped-cosine kernel theorem.

Python 3 standard library only. This is finite evidence, not an infinite proof.
"""
import math
import random


def conditions(a, w):
    q = math.exp(-math.pi*a)
    c, s = math.cos(math.pi*w), math.sin(math.pi*w)
    y = q*w*s
    even = a*(1-q*c)
    odd = a*(1+q*c)
    r = a*a+w*w
    return even-y, even+y, odd+y, (1+r)*odd+(1-r)*y


def coefficient(a, w, n):
    q = math.exp(-math.pi*a)
    sig = 1 if n % 2 == 0 else -1
    x = a*(1-sig*q*math.cos(math.pi*w))
    y = sig*q*w*math.sin(math.pi*w)
    r = a*a+w*w
    denom = (a*a+(w+n)**2)*(a*a+(w-n)**2)
    return (x*(r+n*n)+y*(r-n*n))/denom


def simpson_integral(a, w, n, steps=8192):
    h = math.pi/steps
    acc = 0.0
    for j in range(steps+1):
        t = j*h
        v = math.exp(-a*t)*math.cos(w*t)*math.cos(n*t)
        acc += (1 if j == 0 or j == steps else 4 if j%2 else 2)*v
    return acc*h/3


def main():
    rng = random.Random(20261022)
    maximal_error = 0.0
    for _ in range(180):
        a = math.exp(rng.uniform(math.log(0.07), math.log(3.0)))
        w = rng.uniform(0.02, 35)
        possible = all(x >= -1e-10 for x in conditions(a, w))
        numerically_nonnegative = all(coefficient(a, w, n) >= -1e-10 for n in range(300))
        assert possible == numerically_nonnegative, (a, w)
        n = rng.randint(0, 55)
        err = abs(coefficient(a, w, n)-simpson_integral(a, w, n))
        maximal_error = max(maximal_error, err)
        assert err < 3e-8, (a, w, n, err)
    print('Parameter samples with matching first 300 Fourier signs: 180')
    print('Maximal direct quadrature discrepancy:', '%.3g'%maximal_error)
    a = 0.7
    gamma = a*(math.exp(math.pi*a)-1)/math.pi
    print('Asymptotic scaled half-width:', '%.12f'%gamma)
    for k in (25, 75, 200, 500):
        offsets = []
        for sign in (-1, 1):
            lower, upper = 0.0, min(.25, 2.0*gamma/k)
            for _ in range(60):
                mid = .5*(lower+upper)
                if min(conditions(a, k+sign*mid)) >= 0:
                    lower = mid
                else:
                    upper = mid
            offsets.append(sign*k*lower)
        print('integer frequency',k,'left/right scaled endpoints:',*[round(z,9) for z in offsets])
    print('All finite diagnostics passed; the written analytic proof handles infinitely many modes.')

if __name__ == '__main__':
    main()
