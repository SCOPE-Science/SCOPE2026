"""Independent exact-arithmetic checks for the signed six-neighbor mean-field cusp."""
from fractions import Fraction as Q
from math import comb, sqrt

CHECKS = 0

def check(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(f'{CHECKS}: {msg}')


def A(b, z):
    return 6*b-1+5*b*b*(4*b-3)*z+3*b**4*(2*b-5)*z*z-b**6*z**3


def dA(b, z):
    return 5*b*b*(4*b-3)+6*b**4*(2*b-5)*z-3*b**6*z*z


def force_direct(b, p, m):
    c=(1+m)/2
    z=(1+b*m)/2
    return 2*((1-p)*((1-c)*z**6-c*(1-z)**6)+p*(Q(1,2)-c))


def force_factored(b, p, m):
    return m*((1-p)*A(b,m*m)-32*p)/32

# This compares a source-definition calculation against the independent
# factored polynomial for rational parameter choices.
for b in [Q(-1),Q(-3,4),Q(0),Q(1,6),Q(1,2),Q(3,4),Q(7,8),Q(1)]:
    check(A(b,Q(1))==-(1-b)**6,'inward physical boundary identity')
    for p in [Q(1,100),Q(7,71),Q(1,2),Q(99,100)]:
        for m in [Q(-1),Q(-2,3),Q(-1,5),Q(0),Q(1,7),Q(3,5),Q(1)]:
            check(force_direct(b,p,m)==force_factored(b,p,m),'exact drift factorization')
            check(force_factored(b,p,-m)==-force_factored(b,p,m),'odd symmetry')
            if m==1:
                check(force_factored(b,p,m)<0,'physical boundary strict inward')
            if m==-1:
                check(force_factored(b,p,m)>0,'physical boundary strict inward')

# Prove the derivative at z=1 is negative by an exact positive decomposition.
for b in [Q(3,4),Q(4,5),Q(7,8),Q(9,10),Q(1)]:
    check(dA(b,Q(1))==-b*b*(3*(b-1)**4+4*(3*b*b-2*b+3)),'negative endpoint derivative identity')
    check(dA(b,Q(1))<0,'negative endpoint derivative')

# Check the exact tricritical equation, a fifth-order stabilizing zero.
b=Q(3,4); pc=Q(7,71)
check(force_factored(b,pc,Q(0))==0,'center equilibrium')
for m in [Q(-1),Q(-1,2),Q(-1,100),Q(1,100),Q(1,2),Q(1)]:
    check(force_factored(b,pc,m)==-Q(243,145408)*m**5*(3*m*m+56),'critical exact drift')
    check(force_factored(b,pc,m)*m<0,'critical drift toward zero')
check(Q(243*56,145408)==Q(1701,18176),'fifth-power relaxation coefficient')

# Cusp leading coefficients, obtained from derivatives at b=3/4.
delta=Q(1,100000)
b=Q(3,4)+2*delta
coefficient_linear=5*b*b*(4*b-3)
coefficient_quadratic=3*b**4*(2*b-5)
check(coefficient_linear>0 and coefficient_quadratic<0,'cusp signs')
check(Q(5)*Q(3,4)**2*8==Q(45,2),'linear coefficient of A_prime(0)')
check(3*Q(3,4)**4*(2*Q(3,4)-5)==-Q(1701,512),'quadratic coefficient at tricritical point')
check(-Q(45,2)/(2*(-Q(1701,512)))==Q(640,189),'spinodal-squared-magnetization constant')
check(-Q(45,2)**2/(4*(-Q(1701,512)))==Q(800,21),'A height coefficient')
check(Q(800,21)*Q(128,5041)==Q(102400,105861),'width coefficient')

# Physical spinodal and exact sign pattern at independent rational parameters.
for r in [Q(0),Q(1,64),Q(1,16),Q(1,10),Q(3,25)]:
    b=1-2*r
    z_s=(float(2*b-5)+sqrt(float((2*b-5)**2+Q(5,3)*(4*b-3))))/float(b*b)
    check(0<z_s<1,'spinodal inside physical interval')
    for dz in [1e-5,1e-4]:
        check(float(dA(b,Q(str(z_s-dz))))>0,'derivative positive left')
        check(float(dA(b,Q(str(z_s+dz))))<0,'derivative negative right')
    p0=float((6*b-1)/(6*b+31))
    ps=float(A(b,Q(str(z_s)))/(A(b,Q(str(z_s)))+32))
    check(0<p0<ps<1,'nonzero hysteresis window')

# Closed-form zero-antagonism benchmark: p_s=(74-24sqrt(6))/101.
b=Q(1)
z_s=-3+4*sqrt(6)/3
ps=float(A(b,Q(str(z_s)))/(A(b,Q(str(z_s)))+32))
check(abs(ps-(74-24*sqrt(6))/101)<1e-13,'benchmark upper spinodal')
check(abs(float(Q(5,37)) - (6*float(b)-1)/(6*float(b)+31))<1e-14,'benchmark lower spinodal')

print('VERIFIED',CHECKS,'assertions')
