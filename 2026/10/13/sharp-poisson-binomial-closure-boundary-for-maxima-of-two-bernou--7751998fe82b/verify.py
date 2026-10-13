#!/usr/bin/env python3
"""Exact-rational finite checks for the PGFs of two-sample binomial maxima.

Scientific limits: finite evaluations are not proofs of parameter-uniform identities.
Use only Python's standard library.
"""
from fractions import Fraction as Q
from math import comb


def original_binomial(m, p):
    return [Q(comb(m, k))*p**k*(1-p)**(m-k) for k in range(m+1)]


def maximum_pmf(pmf):
    cdf = Q(0)
    answer = []
    for pk in pmf:
        previous = cdf
        cdf += pk
        answer.append(cdf*cdf - previous*previous)
    assert sum(answer) == 1
    return answer


def discriminant_cubic(b):
    d, c, t, a = b  # increasing powers; polynomial a*z^3+t*z^2+c*z+d
    return t*t*c*c - 4*a*c**3 - 4*t**3*d - 27*a*a*d*d + 18*a*t*c*d


def R(p):
    return 4*p**6+8*p**3+3*p*p+6*p-1


def verify():
    cases_two = 0
    for i in range(12):
        for j in range(12):
            p, r = Q(i, 11), Q(j, 11)
            pmf = [(1-p)*(1-r),p*(1-r)+r*(1-p),p*r]
            b0,b1,b2 = maximum_pmf(pmf)
            A = (p-r)**2+2*p*r*(1-p)*(1-r)
            assert b1*b1-4*b0*b2 == A*(A+4*(1-p)*(1-r))
            assert b1*b1-4*b0*b2 >= 0
            cases_two += 1
    cases_three = 0
    for j in range(1,46):
        p=Q(j,47)
        b=maximum_pmf(original_binomial(3,p))
        formula=[(1-p)**6,3*p*(1-p)**4*(p+2),3*p*p*(1-p)**2*(2+2*p-p*p),p**3*(2-p**3)]
        assert b==formula
        assert discriminant_cubic(b)==108*p**6*(1-p)**12*R(p)
        cases_three+=1
    low,high=Q(150732,1000000),Q(150733,1000000)
    assert R(low)<0<R(high)
    a,b=low,high
    for _ in range(64):
        mid=(a+b)/2
        if R(mid)<0: a=mid
        else: b=mid
    assert 0<b-a<Q(1,10**20)
    cases_scaled=0
    p=Q(1,100000)
    for m in range(3,8):
        bb=maximum_pmf(original_binomial(m,p))
        assert abs(bb[0]-1)<Q(1,1000)
        for k in range(1,m+1):
            assert abs(bb[k]/p**k - 2*comb(m,k))<Q(1,20)
            cases_scaled+=1
    print('VERIFY_OK two_trial_cases=%d cubic_cases=%d scaled_coefficients=%d phase_interval=(%.12f,%.12f)' % (cases_two,cases_three,cases_scaled,float(a),float(b)))


if __name__=='__main__':
    verify()
