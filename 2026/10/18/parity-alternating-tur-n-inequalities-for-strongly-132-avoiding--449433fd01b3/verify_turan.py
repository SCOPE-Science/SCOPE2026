"""Exact coefficient and independent small-order verification of a Catalan-composition enumeration.

Run with Python 3.10+ (standard library only). No external data files are needed.
"""
from itertools import permutations
from math import comb, pi, sqrt

DEGREE = 240


def multiplication(a, b):
    result = [0] * (DEGREE + 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j in range(min(len(b), DEGREE + 1 - i)):
            if b[j]:
                result[i + j] += ai * b[j]
    return result


def reciprocal(a):
    assert a[0] == 1
    result = [0] * (DEGREE + 1)
    result[0] = 1
    for n in range(1, DEGREE + 1):
        result[n] = -sum(a[j] * result[n-j] for j in range(1, min(n+1, len(a))))
    return result


def quotient(a, b):
    return multiplication(a, reciprocal(b))


def generating_coefficients():
    catalan = [comb(2*n, n)//(n+1) for n in range(DEGREE + 1)]
    c2 = [catalan[n//2] if n % 2 == 0 else 0 for n in range(DEGREE+1)]
    c3 = [catalan[n//3] if n % 3 == 0 else 0 for n in range(DEGREE+1)]
    z = [0, 0, 0] + c3[:-3]  # x^3 C(x^3)
    composition = [0]*(DEGREE+1)
    composition[0] = 1
    z_power = [1] + [0]*DEGREE
    for k in range(1, DEGREE//3+1):
        z_power = multiplication(z_power, z)
        for n in range(3*k, DEGREE+1):
            composition[n] += catalan[k]*z_power[n]
    c_p = multiplication([1,1], composition)
    den_p = [2 - c_p[0]] + [-x for x in c_p[1:]]
    p = quotient(composition, den_p)
    den_f = [1,-1] + [-c2[n-2] for n in range(2, DEGREE+1)]
    f = quotient([1,-1], den_f)
    c3_minus_1 = c3[:]
    c3_minus_1[0] -= 1
    g = quotient(multiplication([0,2,4], c3_minus_1), [1,0,-1])
    return multiplication(p, [f[n]+g[n] for n in range(DEGREE+1)])


def avoids_132(p):
    n = len(p)
    for j in range(1,n-1):
        for i in range(j):
            if p[i] < p[j]:
                for k in range(j+1,n):
                    if p[i] < p[k] < p[j]:
                        return False
    return True


def independent_count(n):
    count=0
    for perm in permutations(range(1,n+1)):
        if not avoids_132(perm):
            continue
        square = tuple(perm[perm[i]-1] for i in range(n))
        count += avoids_132(square)
    return count


def c_value(x):
    return (1 - sqrt(1 - 4*x))/(2*x) if x != 0 else 1


def p_value(x):
    y=x**3*c_value(x**3)
    return c_value(y)/(2-(1+x)*c_value(y))


def verify():
    a=generating_coefficients()
    expected=[1,1,2,5,12,24,50,101,202,398,806,1568,3148,6198,12306,24223]
    assert a[:len(expected)] == expected, (a[:len(expected)], expected)
    brute=[independent_count(n) for n in range(1,9)]
    assert brute==a[1:9], (brute,a[1:9])
    turan=[a[n]**2-a[n-1]*a[n+1] for n in range(1,DEGREE)]
    assert all((-1)**n*turan[n-1] > 0 for n in range(8, DEGREE)), 'finite range parity check'
    pp=p_value(0.5); pm=p_value(-0.5)
    constant=3*pp*pm/(2*pi)
    for n in (100,180,230):
        ratio = ((-1)**n*turan[n-1])*(n*n)/(4**n)/constant
        assert abs(ratio-1)<0.12, (n,ratio)
    print('Exact generating-function coefficients matched the published first sixteen terms.')
    print('Independent permutation enumeration matched for sizes 1 through 8:',brute)
    print('Turan parity verified for finite indices 8 through',DEGREE-1,'(not an infinite proof).')
    print('Analytic constant:',repr(constant),'P(+1/2)=',repr(pp),'P(-1/2)=',repr(pm))
    print('CHECKS PASSED')


if __name__ == '__main__':
    verify()
