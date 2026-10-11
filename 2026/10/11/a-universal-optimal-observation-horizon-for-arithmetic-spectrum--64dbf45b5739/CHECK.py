#!/usr/bin/env python3
"""Self-contained arithmetic checks for an exponential-spectrum two-channel sampling theorem."""
from fractions import Fraction
from math import exp, log


def rational_det(M):
    A = [list(map(Fraction, row)) for row in M]
    n = len(A)
    sign = 1
    answer = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j,n) if A[i][j]),None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            A[pivot], A[j] = A[j], A[pivot]
            sign = -sign
        p = A[j][j]
        answer *= p
        for i in range(j+1,n):
            ratio = A[i][j] / p
            for h in range(j+1,n):
                A[i][h] -= ratio * A[j][h]
            A[i][j] = Fraction(0)
    return sign*answer


def sampled_matrix(k, q, alpha, d):
    # alpha=a/d is an integer in exact tests, lambda_j=d*(alpha+j).
    return [
        [(d*(alpha+j) if channel else 1) * q**(ell*(alpha+j))
         for j in range(2*k)]
        for ell in range(k) for channel in (0,1)
    ]


def product_formula(k, q, alpha, d):
    # Exponent beta is integral in these tests.
    beta = k*(k-1)*(Fraction(alpha,1)+Fraction(4*k-5,6))
    assert beta.denominator == 1
    result = Fraction(d**k)*q**int(beta)
    for h in range(1,k):
        result *= (1-q**h)**(4*(k-h))
    return result


def equation_in_c(k, alpha, c):
    beta=k*(k-1)*(alpha+(4*k-5)/6)
    return 4*sum(h*(k-h)/__import__('math').expm1(c*h/k) for h in range(1,k))-beta


def root_c(k,alpha):
    low=1e-6
    high=30.0
    assert equation_in_c(k,alpha,low)>0
    assert equation_in_c(k,alpha,high)<0
    for _ in range(90):
        mid=(low+high)/2
        if equation_in_c(k,alpha,mid)>0:
            low=mid
        else:
            high=mid
    return (low+high)/2


def integral(c,steps=20000):
    from math import expm1
    # Simpson with removable endpoint at zero.
    def v(x):
        return 1/c if x==0 else x*(1-x)/expm1(c*x)
    h=1/steps
    total=v(0)+v(1)
    for j in range(1,steps):
        total+=(4 if j%2 else 2)*v(h*j)
    return total*h/3


def run():
    tests=0
    for k in (2,3,4,5):
        for q in (Fraction(1,2),Fraction(2,3)):
            for alpha,d in ((1,1),(2,3)):
                det=abs(rational_det(sampled_matrix(k,q,alpha,d)))
                expected=product_formula(k,q,alpha,d)
                assert det==expected,(k,q,alpha,d,det,expected)
                tests+=1
    # Closed form of the two-time optimum.
    for alpha in (0.5,1,2,3):
        beta=2*alpha+1
        qstar=beta/(beta+4)
        c=-2*log(qstar)
        assert abs(equation_in_c(2,alpha,c))<1e-11
        assert abs(root_c(2,alpha)-c)<1e-11
        tests+=2
    # Asymptotic optimizer and limiting integral, checked numerically only.
    lo,hi=.1,20.
    for _ in range(70):
        mid=(lo+hi)/2
        if 4*integral(mid)>2/3:
            lo=mid
        else:
            hi=mid
    cstar=(lo+hi)/2
    assert 2.12146<cstar<2.12148
    for k in (10,20,40,80,160):
        c=root_c(k,1.0)
        assert 1<c<cstar
        tests+=1
    assert abs(root_c(160,1.0)-cstar)<.007
    tests+=2
    print('VERIFY_OK',tests,'exact_or_numeric_tests','cstar=%.12f'%cstar)

if __name__=='__main__':
    run()
