"""Standalone exact-rational checks for the two-dimensional sketch-risk phase diagram.

Run: python3 verify.py
This is a finite consistency check, not a substitute for the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import cos, sin, pi, fsum


def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def power(A, n):
    result = [[F(1), F(0)], [F(0), F(1)]]
    for _ in range(n):
        result = mul(result, A)
    return result


def apply(A, x):
    return [sum(A[i][j]*x[j] for j in range(2)) for i in range(2)]


def dot(x, y):
    return sum(x[i]*y[i] for i in range(2))


def direct_rademacher_risk(A, q):
    Ap = power(A, 2*q+1)
    A2 = mul(A, A)
    trace_a2 = sum(A2[i][i] for i in range(2))
    errors = []
    for signs in product((-1, 1), repeat=2):
        y = apply(Ap, signs)
        err = trace_a2 - dot(y, apply(A2, y))/dot(y, y)
        errors.append(err)
    return sum(errors)/4


def formula_risk(a, b, q, T):
    alpha, beta = a**(2*q+1), b**(2*q+1)
    S, D = alpha**2+beta**2, alpha**2-beta**2
    return b**2+(a**2-b**2)*beta**2*(S+D*T)/(S*S-D*D*T)


def gaussian_formula(a, b, q):
    alpha, beta = a**(2*q+1), b**(2*q+1)
    return b**2+(a**2-b**2)*F(beta, alpha+beta)


def matrix_for_rotation(a, b, c, s):
    return [[a*c*c+b*s*s, (a-b)*c*s],
            [(a-b)*c*s, a*s*s+b*c*c]]


checks=0
for a,b in [(F(3),F(1)), (F(5),F(2)), (F(7),F(3))]:
    for c,s in [(F(1),F(0)),(F(3,5),F(4,5)),
                (F(5,13),F(12,13)),(F(0),F(1))]:
        assert c*c+s*s==1
        T=4*c*c*s*s
        A=matrix_for_rotation(a,b,c,s)
        for q in range(5):
            assert direct_rademacher_risk(A,q)==formula_risk(a,b,q,T)
            checks+=1
    for q in range(5):
        A45=[[F(a+b,2),F(a-b,2)],[F(a-b,2),F(a+b,2)]]
        assert direct_rademacher_risk(A45,q)==F(a*a+b*b,2)
        assert formula_risk(a,b,q,F(1))==F(a*a+b*b,2)
        alpha,beta=a**(2*q+1), b**(2*q+1)
        threshold=F(alpha*alpha+beta*beta,(alpha+beta)**2)
        assert F(0)<threshold<F(1)
        assert formula_risk(a,b,q,threshold)==gaussian_formula(a,b,q)
        assert formula_risk(a,b,q,F(0))<gaussian_formula(a,b,q)
        assert formula_risk(a,b,q,F(1))>gaussian_formula(a,b,q)
        checks+=4

# Independent numerical angular integral for the isotropic-Gaussian risk.
for a,b,q in [(3.0,1.0,0),(5.0,2.0,1),(3.0,1.0,2)]:
    alpha,beta=a**(2*q+1),b**(2*q+1)
    N=50000
    angular=fsum((b*b+(a*a-b*b)*beta*beta*sin((j+.5)*2*pi/N)**2 /
          (alpha*alpha*cos((j+.5)*2*pi/N)**2 +
           beta*beta*sin((j+.5)*2*pi/N)**2)) for j in range(N))/N
    assert abs(angular-float(gaussian_formula(F(int(a)),F(int(b)),q)))<1e-9
    checks+=1

print('VERIFY_OK',checks)
