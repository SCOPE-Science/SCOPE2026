#!/usr/bin/env python3
"""Supplementary deterministic checks for five symmetric tones under a Gaussian STFT."""
import cmath
import math
from fractions import Fraction

pi = math.pi
s_b = (math.sqrt(5) - 1) / 4
D_a = math.sqrt(math.log(2) / (2*pi))
D_b = math.sqrt(math.log(1 + math.sqrt(5)) / (2*pi))
assert 0 < D_a < D_b

# Exact polynomial identity, not a floating-point factorization.
a = [Fraction(-1),Fraction(2)]
b = [Fraction(-1),Fraction(2),Fraction(4)]
prod = [Fraction(0) for _ in range(4)]
for i, x in enumerate(a):
    for j, y in enumerate(b):
        prod[i+j] += x*y
assert prod == [Fraction(1),Fraction(-4),Fraction(0),Fraction(8)]

# The window and signal convention is V_g f(x,xi) =
# integral f(t) exp(-pi(t-x)^2) exp(-2pi*i*xi*t) dt.
def direct_five_mode_formula(D,x,xi):
    return sum(cmath.exp(-pi*(xi-k*D)**2+2j*pi*(k*D-xi)*x)
               for k in (-2,-1,0,1,2))

def factored(D,x,xi):
    q = math.exp(-pi*D*D)
    z = 2*pi*D*(xi+1j*x)
    return cmath.exp(-pi*xi**2-2j*pi*xi*x) * (1+2*q*cmath.cosh(z)+2*q**4*cmath.cosh(2*z))

def zero_coordinates(D):
    q=math.exp(-pi*D*D);s=q*q
    h=1-4*s+8*s*s*s
    y_plus=(-1+cmath.sqrt(h))/(4*q**3)
    y_minus=(-1-cmath.sqrt(h))/(4*q**3)
    coords=[]
    for y in (y_plus,y_minus):
        v=cmath.acosh(y)
        for w in (v,-v):
            coords.append(((w.imag/(2*pi*D))%(1/D),w.real/(2*pi*D)))
    return coords

comparisons=0
for D in (0.07,0.18,0.29,0.345,0.37,0.40,0.42,0.45,0.52,0.72,1.05):
    T=1/D
    for j in range(11):
        for k in range(17):
            x=T*(j+0.31)/12
            xi=D*(k-7.63)/3
            lhs=direct_five_mode_formula(D,x,xi)
            rhs=factored(D,x,xi)
            assert abs(lhs-rhs) <= 3e-11 * max(1,abs(lhs),abs(rhs))
            comparisons += 1
    zeros=zero_coordinates(D)
    assert len(zeros)==4
    for x,xi in zeros:
        assert abs(direct_five_mode_formula(D,x,xi)) < 2e-10
        comparisons += 1
    if D<D_a:
        assert all(abs(xi)<1e-8 for _,xi in zeros)
    elif D>D_b:
        assert all(abs(x-T/2)<1e-8 for x,_ in zeros)
        assert len({round(abs(xi),7) for _,xi in zeros})==2
    else:
        assert all(abs(xi)>0.01 for _,xi in zeros)
        assert len({round(x,7) for x,_ in zeros})==2
        assert len({round(xi,7) for _,xi in zeros})==2

# Values at discriminant collisions, evaluated independently from the quadratic roots.
q_a=math.exp(-pi*D_a*D_a)
assert abs(q_a*q_a-0.5)<1e-14
for fraction in (3/8,5/8):
    x=fraction/D_a
    assert abs(direct_five_mode_formula(D_a,x,0))<2e-13
    comparisons+=1
q_b=math.exp(-pi*D_b*D_b)
assert abs(q_b*q_b-s_b)<1e-14
u=math.acosh(1/(4*q_b**3))/(2*pi*D_b)
for xi in (-u,u):
    assert abs(direct_five_mode_formula(D_b,0.5/D_b,xi))<2e-13
    comparisons+=1

# At critical scales d/dz H vanishes, while d^2/dz^2 H does not.
def H_derivatives(D,z):
    q=math.exp(-pi*D*D);r=2*pi*D
    return (2*q*r*cmath.sinh(r*z)+4*q**4*r*cmath.sinh(2*r*z),
            2*q*r*r*cmath.cosh(r*z)+8*q**4*r*r*cmath.cosh(2*r*z))
for D,locations in ((D_a,[1j*3/(8*D_a),1j*5/(8*D_a)]),
                    (D_b,[u+0.5j/D_b,-u+0.5j/D_b])):
    for z in locations:
        first,second=H_derivatives(D,z)
        assert abs(first)<1e-11
        assert abs(second)>0.1
        comparisons += 1

print('VERIFY_OK exact discriminant factorization and',comparisons,
      'independent formula/zero/critical-derivative comparisons;',
      'thresholds',format(D_a,'.14f'),format(D_b,'.14f'))
