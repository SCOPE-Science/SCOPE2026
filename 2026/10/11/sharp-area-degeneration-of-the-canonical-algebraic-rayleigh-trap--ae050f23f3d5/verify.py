"""Finite quadrature checks for the published Rayleigh algebraic ovals.
The accompanying proof, not these numerical tests, establishes the limits.
Run: python3 verify.py
"""
import math

C = 8.0 / 3.0
R = math.sqrt(C)


def simpson(fun, a, b, n=12000):
    assert n % 2 == 0
    step = (b - a) / n
    total = fun(a) + fun(b)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * fun(a + step * j)
    return total * step / 3.0


def inner_endpoint(lam):
    if lam == 0.0:
        return R
    left, right = R, math.sqrt(3.0)
    for _ in range(100):
        mid = 0.5 * (left + right)
        h = mid * (1.0 - mid*mid/3.0)
        discr = lam*lam*h*h+4.0*(C-mid*mid)
        if discr > 0:
            left = mid
        else:
            right = mid
    return 0.5*(left+right)


def inside(lam):
    Y = inner_endpoint(lam)
    def integrand(theta):
        y = Y * math.sin(theta)
        h = y * (1.0 - y*y/3.0)
        discr = lam*lam*h*h+4.0*(C-y*y)
        return Y*math.cos(theta)*math.sqrt(max(0.0, discr))
    return 2.0 * simpson(integrand, 0.0, math.pi/2.0)


def disc_poly(z, lam):
    return lam*lam*(648.0 + 9.0*z*z - z*z*z) + 108.0*lam + 288.0 - 36.0*z


def outer_endpoint(lam):
    left, right = 8.0, 20.0
    while disc_poly(right, lam) > 0:
        right *= 2.0
    for _ in range(100):
        mid = (left + right) / 2.0
        if disc_poly(mid, lam) > 0:
            left = mid
        else:
            right = mid
    return math.sqrt((left + right) / 2.0)


def outside(lam):
    U = outer_endpoint(lam)
    def integrand(theta):
        v = U * math.sin(theta)
        z = v*v
        return U * math.cos(theta) * math.sqrt(max(0.0, disc_poly(z, lam) / 9.0))
    return 2.0 * simpson(integrand, 0.0, math.pi / 2.0)


def outer_leading():
    a, b = 8.0, 20.0
    for _ in range(100):
        m = (a+b) / 2.0
        if 648.0 + 9.0*m*m - m*m*m > 0:
            a=m
        else:
            b=m
    U = math.sqrt((a+b)/2.0)
    def integrand(theta):
        u = U * math.sin(theta)
        z = u*u
        return U * math.cos(theta)*math.sqrt(max(0.0, 648 + 9*z*z - z*z*z))
    return (2.0/3.0) * simpson(integrand, 0.0, math.pi/2.0)


def main():
    assert abs(inside(0)-8*math.pi/3)<1e-9
    assert abs(outside(0)-8*math.pi)<1e-6
    low=0.03
    coeff=(inside(low)-8*math.pi/3)/low**2
    assert abs(coeff-13*math.pi/243)<0.005, coeff
    high=300.0
    ai=inside(high)
    ao=outside(high)
    log_constant=high*(ai-1.5*high)-10.0*math.log(high)
    expected=5.0+2.0*math.log(243.0/256.0)
    assert abs(log_constant-expected)<0.02,(log_constant,expected)
    Couter=outer_leading()
    assert abs(Couter-60.00037902855482)<2e-6, Couter
    assert abs(ao/high-Couter)<0.03
    ratio=1.5/Couter
    assert abs(ai/ao-ratio)<0.0001,(ai/ao,ratio)
    print('CHECK_OK')
    print('small-L quadratic coefficient',coeff)
    print('large-L renormalized inner constant',log_constant,'target',expected)
    print('large-L outer area coefficient',ao/high,'target',Couter)
    print('large-L area ratio',ai/ao,'limit',ratio)


if __name__ == '__main__':
    main()
