"""Finite reproducibility diagnostics for monomial Bergman composition spectra.

Only finite numerical checks; the infinite-dimensional arguments are analytic.
Run: python3 CHECK.py
"""
import math


def mm(a, b):
    return (
        (a[0][0]*b[0][0]+a[0][1]*b[1][0],
         a[0][0]*b[0][1]+a[0][1]*b[1][1]),
        (a[1][0]*b[0][0]+a[1][1]*b[1][0],
         a[1][0]*b[0][1]+a[1][1]*b[1][1]),
    )


def mpow(a, n):
    result = ((1, 0), (0, 1))
    while n:
        if n & 1:
            result = mm(result, a)
        a = mm(a, a)
        n //= 2
    return result


def moment(k, beta):
    if beta == -1:
        return 1.0
    return math.exp(math.lgamma(beta+2)+math.lgamma(k+1)-math.lgamma(k+beta+2))


def monomial_weight(a, nu, beta):
    mn = (a[0][0]*nu[0]+a[0][1]*nu[1],
          a[1][0]*nu[0]+a[1][1]*nu[1])
    return math.sqrt(moment(mn[0], beta)*moment(mn[1], beta)
                     /(moment(nu[0], beta)*moment(nu[1], beta)))


def exact_essential(a, beta):
    x, y = a[0]
    z, w = a[1]
    return (math.sqrt(x*w)+math.sqrt(y*z))**(-(beta+1))


def pfroot(a):
    x,y = a[0]
    z,w = a[1]
    return (x+w+math.sqrt((x-w)**2+4*y*z))/2


def check():
    cases = [((1, 1), (1, 2)), ((2, 1), (1, 1)),
             ((1, 2), (2, 1)), ((1, 3), (1, 2))]
    betas = [-1, -0.5, 0, 0.75, 2]
    tested = 0
    for a in cases:
        assert a[0][0]*a[1][1] != a[0][1]*a[1][0]
        rho = pfroot(a)
        assert rho > 1
        for beta in betas:
            for m in range(12):
                for k in range(12):
                    w = monomial_weight(a, (m,k), beta)
                    assert -1.e-9 <= w <= 1+1.e-9
                    if beta == -1:
                        assert abs(w-1) < 1.e-12
                    tested += 1
            for n in range(1,7):
                b = mpow(a,n)
                r = math.sqrt(b[0][1]*b[1][1]/(b[0][0]*b[1][0]))
                homogeneous = math.sqrt(r/((b[0][0]*r+b[0][1])
                                             *(b[1][0]*r+b[1][1])))
                assert math.isclose(homogeneous, exact_essential(b,0),
                                    rel_tol=2.e-12)
                if beta == -1:
                    assert exact_essential(b,beta) == 1
                else:
                    for scale in (1000, 10000):
                        approximate = monomial_weight(b,(round(scale*r),scale),beta)
                        target = exact_essential(b,beta)
                        assert abs(approximate-target)/target < 0.045
                        tested += 1
                tested += 1
    a = ((1,1),(1,2))
    for n in range(1,12):
        b = mpow(a,n)
        fib = [0,1]
        for _ in range(2,2*n+2):
            fib.append(fib[-1]+fib[-2])
        assert b == ((fib[2*n-1],fib[2*n]),(fib[2*n],fib[2*n+1]))
        f = fib[2*n]
        q = exact_essential(b,0)
        assert math.isclose(q, math.sqrt(f*f+1)-f, rel_tol=1e-8)
        tested += 1
    print('PASS: %d finite diagnostic checks; no infinite-proof certification.' % tested)


if __name__ == '__main__':
    check()
