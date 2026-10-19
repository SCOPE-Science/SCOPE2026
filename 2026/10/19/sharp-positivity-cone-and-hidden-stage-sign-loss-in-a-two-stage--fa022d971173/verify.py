#!/usr/bin/env python3
"""Self-contained calculations for a two-stage Chebyshev two-step method.

Uses only Python's standard library; finite checks complement the analytic proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def coeff_q(z):
    t = 1 - 2*z + z*z/Fraction(2)
    return t, Fraction(3,5)*(1+t), -t/Fraction(5)


def stage_update(yold, y, z):
    # f(y)=-lambda*y and z=h*lambda.
    v0 = (3*y-yold)/2
    v1 = (1-z/2)*v0
    v2 = 2*v1-v0-z*v1
    return Fraction(3,5)*y+Fraction(2,5)*v2


def coefficient_checks():
    alpha, r, beta = Fraction(3,5), Fraction(1,5), Fraction(2)
    assert 2*alpha-r==1
    assert 2*alpha+(alpha-r)*beta==2
    assert alpha+alpha*beta+(alpha-r)*beta**2/8==2
    # At zero, roots of the recurrence are 1 and r, giving zero stability.
    assert (Fraction(3,5)*(2)) - r == 1
    count=0
    for k in range(1,64):
        z=Fraction(k,16)
        t,a,b=coeff_q(z)
        assert Fraction(-1)<=t<Fraction(1)
        assert abs(b)<1 and 1-a-b>0 and 1+a-b>0
        for i in range(1,7):
            for j in range(1,7):
                yold,y=Fraction(i,7),Fraction(j,11)
                expected=a*y+b*yold
                assert stage_update(yold,y,z)==expected
                count+=1
    return count


def dcoeff(z):
    one=Decimal(1)
    t=one-2*z+z*z/2
    a=Decimal(3)/5*(one+t)
    b=-t/5
    D=a*a+4*b
    if t>=0:
        lo=(a-D.sqrt())/2
        hi=(a+D.sqrt())/2
    else:
        lo=hi=None
    return t,a,b,lo,hi


def root_equation(z):
    t,a,b,lo,hi=dcoeff(z)
    return (-z).exp()-lo


def bisection_root():
    with localcontext() as c:
        c.prec=75
        low=Decimal("3.415")
        high=Decimal(4)
        assert root_equation(low)>0 and root_equation(high)<0
        for _ in range(260):
            m=(low+high)/2
            if root_equation(m)>0: low=m
            else: high=m
        return +(low+high)/2


def sequence_sign(z, nmax):
    t,a,b,lo,hi=dcoeff(z)
    y0=Decimal(1)
    y1=(-z).exp()
    out=[y0,y1]
    for k in range(2,nmax+1):
        out.append(a*out[-1]+b*out[-2])
    return out


def first_negative_formula(z):
    t,a,b,lo,hi=dcoeff(z)
    q=(-z).exp()
    assert t>0 and q<lo
    R=(lo-q)/(hi-q)
    ratio=lo/hi
    # Strict negativity: first integer strictly larger than logarithmic quotient.
    return int((R.ln()/ratio.ln()).to_integral_value(rounding='ROUND_FLOOR'))+1


def numerical_checks(root):
    with localcontext() as c:
        c.prec=75
        cases=['0.125','0.5','0.8','1.05','2','3','3.4','3.46','3.48','3.480888475','3.49','3.6','3.8','3.95']
        count=0
        for zstr in cases:
            z=Decimal(zstr)
            s=sequence_sign(z,100)
            expect_positive=z<=root
            if expect_positive:
                assert all(v>0 for v in s)
            else:
                N=first_negative_formula(z)
                assert all(v>0 for v in s[:N]), (z,N)
                assert s[N]<0, (z,N,s[N])
            count+=len(s)
        for e in (4,8,12,16,24,32):
            z=root+Decimal(10)**(-e)
            N=first_negative_formula(z)
            vals=sequence_sign(z,N)
            assert all(v>0 for v in vals[:N]) and vals[N]<0
            count+=len(vals)
        # Even when the exact-start endpoints stay positive, first stage is negative.
        z=Decimal(2)
        q=(-z).exp()
        assert q>0 and (3*q-1)/2<0
        assert all(v>0 for v in sequence_sign(z,100))
        count+=101
        return count


def main():
    n=coefficient_checks()
    with localcontext() as c:
        c.prec=75
        zstar=bisection_root()
        assert Decimal('3.48088')<zstar<Decimal('3.48090')
        _,_,_,lo,hi=dcoeff(zstar)
        assert abs(root_equation(zstar))<Decimal(10)**(-65)
        assert lo>0 and hi>lo
        count=numerical_checks(zstar)
        slope=Decimal(1)/(hi/lo).ln()
        print('fractional_stage_and_schur_tests:',n)
        print('finite_sequence_checks:',count)
        print('unique_threshold:',zstar)
        print('boundary_roots:',lo,hi)
        print('logarithmic_first_negative_coefficient:',slope)
        print('all_checks_passed')


if __name__=='__main__':
    main()
