"""Exact arithmetic checks for the stated SEITFR endemic-caseload result.

Python 3 standard library only. Finite checks support, but do not replace, the
parameter-uniform differentiation and sign arguments supplied in RESULT.md.
"""
from fractions import Fraction as Q
from math import isqrt


def clean(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    return clean([Q(a[i] if i < len(a) else 0) + Q(b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))])


def neg(a):
    return tuple(-x for x in a)


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += Q(x)*Q(y)
    return clean(c)


def deriv(a):
    return clean([Q(i)*a[i] for i in range(1, len(a))] or [Q(0)])


def scale(a, q):
    return clean([Q(q)*x for x in a])


k5 = (Q(5), Q(1))
t10k21 = (Q(21), Q(10))
R_num = scale(k5, Q(42))
R_den = scale(t10k21, Q(5))
# R' numerator over R_den**2 is -6090, equivalent to -1218/[5(10k+21)^2].
assert add(mul(deriv(R_num), R_den), neg(mul(R_num, deriv(R_den)))) == (Q(-6090),)

B_num = mul((Q(105), Q(-8)), (Q(31), Q(60)))
AB = mul(k5, t10k21)
# The exact quotient-rule numerator before the factor 462.
qpoly = (Q(-80871), Q(33180), Q(18920))
assert add(mul(deriv(B_num), AB), neg(mul(B_num, deriv(AB)))) == scale(qpoly, Q(-5))
assert qpoly[0] < 0 and sum(qpoly) < 0 and qpoly[0] + 2*qpoly[1] + 4*qpoly[2] > 0
assert qpoly[1] > 0 and qpoly[2] > 0  # exactly one positive root

Pi=Q(1, 10); mu=Q(1, 10); beta=Q(231, 50); eps=Q(1, 10)
Phi=Q(1); a1=Q(2); a2=Q(1, 10); a3=Q(1, 10)
psi=Q(3, 10); delta=Q(0)
a=a1+mu; b=a2+psi+mu; c=a3+mu; C=beta*Phi/(Phi+mu)
u0=a/Phi+1; u1=1/Phi+1/b+psi/(b*c)
v0=a1/(mu+delta); v1=(a2/b+a3*psi/(b*c))/(mu+delta)
assert (u0,u1,v0,v1) == (Q(31, 10),Q(6),Q(20),Q(5))
assert C == Q(21, 5) and b > eps*a and C/a == 2

def eq(k):
    k=Q(k)
    R0=C*(b+eps*k)/(b*(a+k))
    U=u0+u1*k; V=v0+v1*k
    N=Pi/mu
    I=N*(1-1/R0)/(U+V)
    E=(a+k)/Phi*I
    T=k/b*I
    F=psi*k/(b*c)*I
    R=V*I
    S=N/R0
    lam=beta*(I+eps*T)/(S+E+I+T+F+R)
    residuals=(Pi-(lam+mu)*S+delta*R,lam*S-(Phi+mu)*E,
        Phi*E-(a+k)*I,k*I-b*T,psi*T-c*F,
        a1*I+a2*T+a3*F-(mu+delta)*R)
    assert all(z==0 for z in residuals)
    assert S+E+I+T+F+R == N
    if 0 < k < Q(105,8):
        assert all(z>0 for z in (S,E,I,T,F,R))
    B=(E+I+T+F)/N
    assert R0 == Q(42)*(k+5)/(Q(5)*(10*k+21))
    assert B == (105-8*k)*(60*k+31)/(Q(462)*(k+5)*(10*k+21))
    return R0,B

for k in (Q(1,10),Q(1,2),Q(1),Q(3,2),Q(2)):
    eq(k)
r1,z1=eq(Q(1,10));r2,z2=eq(Q(1))
assert (r1,z1) == (Q(1071,550),Q(19277,259182))
assert (r2,z2) == (Q(252,155),Q(1261,12276))
assert r2 < r1 and z2 > z1
# Exact first-order criterion: log derivative of B at k=0 is positive.
L=(u1*v0-u0*v1)/(u0*(u0+v0))
RHS=(b-eps*a)/(a*b*(C/a-1))
assert L > RHS
assert L-RHS == Q(0)+L-RHS and L-RHS > 0
print('VERIFY_OK')
