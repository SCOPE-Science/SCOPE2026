#!/usr/bin/env python3
"""Standalone exact checks for the succession disturbance-diversity theorem.
Only Python standard library is required. The analytic arguments are in RESULT.md.
"""
from fractions import Fraction
from math import comb, log


def stages(rates, disturbance):
    """Laplace-transform/renewal representation of stationary stage masses."""
    d = Fraction(disturbance)
    survive = Fraction(1)
    result = []
    for rate in rates:
        rate = Fraction(rate)
        next_survive = survive * rate / (rate + d)
        result.append(survive - next_survive)
        survive = next_survive
    result.append(survive)
    assert sum(result) == 1 and all(x > 0 for x in result)
    return result


def linear_solve(A, b):
    n = len(b)
    aug = [[Fraction(A[i][j]) for j in range(n)] + [Fraction(b[i])] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        z = aug[k][k]
        aug[k] = [v / z for v in aug[k]]
        for i in range(n):
            if i == k:
                continue
            z = aug[i][k]
            aug[i] = [u - z * v for u, v in zip(aug[i], aug[k])]
    return [row[-1] for row in aug]


def stationary_by_balance(rates, d):
    """Independent balance-equation computation without stage-product formula."""
    n = len(rates) + 1
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    d = Fraction(d)
    for source in range(n):
        if source < n - 1:
            forward = Fraction(rates[source])
            A[source][source] -= forward
            A[source + 1][source] += forward
        if source > 0:
            A[source][source] -= d
            A[0][source] += d
    A[-1] = [Fraction(1) for _ in range(n)]
    b = [Fraction(0) for _ in range(n)]
    b[-1] = Fraction(1)
    return linear_solve(A, b)


def simpson(p):
    return 1 - sum(x*x for x in p)


def shannon(p):
    return -sum(float(x)*log(float(x)) for x in p if x)


def mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def power(a, n):
    v = [1]
    for _ in range(n):
        v = mul(v, a)
    return v


def polyeval(p, x):
    return sum(c * x**j for j, c in enumerate(p))


def mobius_coeff(p, left, right):
    """Coefficients of (1+t)^d p((left+right*t)/(1+t)), ascending."""
    d = len(p)-1
    z = [0]*(d+1)
    for i, c in enumerate(p):
        tmp = mul(power([left, right], i), power([1, 1], d-i))
        for j, val in enumerate(tmp):
            z[j] += c*val
    return z


def det_fraction(a):
    n = len(a)
    A = [[Fraction(v) for v in row] for row in a]
    sign = 1
    determinant = Fraction(1)
    for k in range(n):
        piv = next((i for i in range(k,n) if A[i][k]), None)
        if piv is None:
            return Fraction(0)
        if piv != k:
            A[k], A[piv] = A[piv], A[k]
            sign = -sign
        pivot = A[k][k]
        determinant *= pivot
        for i in range(k+1,n):
            fac = A[i][k] / pivot
            if not fac: continue
            for j in range(k+1,n):
                A[i][j] -= fac * A[k][j]
            A[i][k] = 0
    return sign*determinant


def resultant(f, g):
    """Sylvester determinant for descending polynomial coefficients."""
    m, n = len(f)-1, len(g)-1
    out = []
    for i in range(n):
        out.append([0]*i + f + [0]*(n-1-i))
    for i in range(m):
        out.append([0]*i + g + [0]*(m-1-i))
    return det_fraction(out)


def discriminant_at_ratio(r):
    # P=x^4+(3-r)x^3+3x^2+(r-1)^2 x-r(r+1)
    p = [1, 3-r, 3, (r-1)**2, -r*(r+1)]
    der = [4, 3*(3-r), 6, (r-1)**2]
    return resultant(p, der)


def F(r):
    return r**7-27*r**6+252*r**5-918*r**4+594*r**3-540*r**2-135*r-27


def main():
    total_balances = 0
    total_sign_checks = 0
    for n in range(2, 9):
        R = 10_000 * n**4
        rates = [R**(n-2-j) for j in range(n-1)]
        high = []
        low = []
        for i in range(n-1):
            d = rates[i]
            p = stages(rates, d)
            assert p == stationary_by_balance(rates, d)
            total_balances += 1
            assert p[i] > Fraction(49,100) and p[i+1] > Fraction(49,100)
            assert simpson(p) > Fraction(48,100)
            high.append((d, simpson(p), shannon(p)))
            total_sign_checks += 3
        for i in range(n-2):
            d = rates[i+1] * (100*n*n)  # exact geometric mean
            assert d*d == rates[i]*rates[i+1]
            p = stages(rates, d)
            assert p == stationary_by_balance(rates, d)
            total_balances += 1
            assert p[i+1] >= 1 - Fraction(1,100*n)
            assert simpson(p) <= Fraction(1,50*n)
            low.append((d, simpson(p), shannon(p)))
            total_sign_checks += 3
        assert all(h[2] > .48 for h in high)
        assert all(l[2] < .105 for l in low)
        total_sign_checks += 2*(len(high)+len(low))
    # Certify polynomial sign and derivative-discriminant algebra exactly.
    f = [-27,-135,-540,594,-918,252,-27,1]
    c1 = mobius_coeff(f,0,4)
    c2 = mobius_coeff(f,4,12)
    assert c1[::-1] == [-42359,-194085,-313947,-181089,-14229,-12447,-729,-27]
    assert c2[::-1] == [-172719,-6143121,-7014411,-6340005,-5014413,-2274579,-501369,-42359]
    assert all(z < 0 for z in c1+c2)
    # Shift t -> 12+t: exactly one coefficient sign change, hence one positive root.
    shift = [sum(f[k]*comb(k,j)*12**(k-j) for k in range(j,8)) for j in range(8)]
    assert shift[::-1] == [1,57,1332,16362,112050,409644,616761,-172719]
    assert shift[0]<0 and all(y>0 for y in shift[1:])
    assert F(12)<0 and F(13)>0
    # Since resultant as polynomial in r has degree <= 14 (7x7 determinant,
    # each entry of degree <=2), 15 exact values prove its polynomial identity.
    for r in range(1,16):
        assert discriminant_at_ratio(r) == 4*r*r*F(r)
    # At r=20, P signs yield three positive roots; at other positive r the
    # only possible collision is at the sole positive discriminant root.
    def P(x, r):
        return x**4+(3-r)*x**3+3*x*x+(r-1)**2*x-r*(r+1)
    assert P(1,20)<0<P(2,20) and P(4,20)>0>P(5,20) and P(10,20)<0<P(16,20)
    assert P(0,20)<0 and P(-100,20)>0
    # Small illustrative three-stage rational witness for both indices.
    values = [stages([100,1], d) for d in (1,10,100)]
    assert values == [[Fraction(1,101),Fraction(50,101),Fraction(50,101)],
                      [Fraction(11,121),Fraction(100,121),Fraction(10,121)],
                      [Fraction(101,202),Fraction(100,202),Fraction(1,202)]]
    assert simpson(values[0])>simpson(values[1])<simpson(values[2])
    assert shannon(values[0])>shannon(values[1])<shannon(values[2])
    print('PASS: 2--8 stage exact occupation/balance checks:',total_balances)
    print('PASS: strict-separation witness checks:',total_sign_checks)
    print('PASS: Möbius sign certificates and 15 exact resultant identities')
    print('PASS: three-stage witness p and Simpson fractions; illustrative Shannon values:')
    for d,p in zip((1,10,100),values):
        print('    c=',d,'Simpson=',simpson(p),'Shannon=',round(shannon(p),9))


if __name__ == '__main__':
    main()
