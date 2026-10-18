#!/usr/bin/env python3
"""Independent exact checks for fan-graph Lipschitz-dual ball volumes."""
from fractions import Fraction
from math import comb, factorial, atan, pi


def poly_transfer(coeff):
    # On [0,1], a reflection-even function becomes T f(x)
    # = integral_0^1 f(y)dy + integral_0^(1-x)f(y)dy.
    result = [Fraction(0)] * (len(coeff) + 1)
    result[0] = sum((a / (j+1) for j, a in enumerate(coeff)), Fraction(0))
    for j, a in enumerate(coeff):
        for k in range(j+2):
            result[k] += a * Fraction(comb(j+1, k) * ((-1)**k), j+1)
    return result


def volume_by_integration(n):
    f = [Fraction(1)]
    for _ in range(n-1):
        f = poly_transfer(f)
    return 2*sum((a/Fraction(j+1) for j,a in enumerate(f)), Fraction(0))


def integer_points(n, dilation):
    vals = list(range(-dilation, dilation+1))
    dp = {i:1 for i in vals}
    for _ in range(1,n):
        dp = {j:sum(dp[i] for i in vals if abs(j-i)<=dilation) for j in vals}
    return sum(dp.values())


def volume_by_ehrhart(n):
    # Constraint coefficient matrix is a graph incidence matrix and hence
    # totally unimodular; Q_n has integral vertices. Ehrhart leading term.
    count = [integer_points(n,m) for m in range(n+1)]
    return Fraction(sum((-1)**(n-m)*comb(n,m)*count[m] for m in range(n+1)), factorial(n))


def check():
    vals = [volume_by_integration(n) for n in range(1,17)]
    for n in range(1,13):
        assert vals[n-1] == volume_by_ehrhart(n), (n, vals[n-1], volume_by_ehrhart(n))
    expected = {1:Fraction(2), 2:Fraction(3), 3:Fraction(14,3), 4:Fraction(29,4), 5:Fraction(169,15)}
    for n,v in expected.items(): assert vals[n-1] == v
    alpha = 2*atan(Fraction(1,3))
    for n in range(1,15):
        actual = float(vals[n]/vals[n-1])
        assert ((-1)**n)*(actual-1/alpha)>0, (n, actual,1/alpha)
    for n in range(3,13):
        spectral = 0.8*sum((alpha+2*pi*j)**(-(n+1)) for j in range(-300,301))
        rel=abs(spectral/float(vals[n-1])-1)
        assert rel<1e-9, (n,rel)
    print('PASS: 12 independent Ehrhart-leading-coefficient exact volume matches; 16 polynomial-integral volumes; 14 alternating-ratio checks; 10 spectral sums.')
    print('V1..V12=', ', '.join(str(v) for v in vals[:12]))
    print('alpha=',alpha,'growth=',1/alpha)

if __name__=='__main__':check()
