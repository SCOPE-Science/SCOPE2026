"""Reproduce exact positive-weight identities for the real four-ball.

Run: python verify.py
This finite checker corroborates, but does not replace, the proof for all degrees.
"""
from fractions import Fraction
from math import factorial
import mpmath as mp
import sympy as sp

m,s=sp.symbols('m s')
poly=sp.expand(2*(m+s+4)*(s+3)+m*(s+4)*(s+1))
assert sp.expand(poly-m*(s+2)*(s+5)-2*(s+3)*(s+4))==0

# Independent exact integration by three beta moments at nonnegative integer s.
def beta_int(a,b):
    return Fraction(factorial(a-1)*factorial(b-1),factorial(a+b-1))

def from_beta(mm,ss):
    coeffs=[(mm+2)**2,-2*mm*(mm+2),mm**2]
    return Fraction((ss+1)*(ss+2),4)*sum((Fraction(coeffs[j])*beta_int(mm+2+j,ss+1) for j in range(3)),Fraction())

def closed_rational(mm,ss):
    return Fraction(factorial(mm+2)*factorial(ss+2),4*factorial(mm+ss+4))*(mm*(ss+2)*(ss+5)+2*(ss+3)*(ss+4))
for mm in range(1,17):
    for ss in range(9):
        assert from_beta(mm,ss)==closed_rational(mm,ss), (mm,ss)

mp.mp.dps=55
def cont(mm,ss):
    return mp.gamma(mm+3)*mp.gamma(ss+3)*(mm*(ss+2)*(ss+5)+2*(ss+3)*(ss+4))/(4*mp.gamma(mm+ss+5))
def terminating_formula(mm,ss):
    return mp.rf(3,mm)/mp.rf(ss+4,mm)*(1+mm*(ss+4)*(ss+1)/(2*(mm+ss+4)*(ss+3)))
checks=0
for st in ['-7.5','-6.5','-5.5','-4.5','-3.5','-2.5','-1.5','0.5','2.5']:
    ss=mp.mpf(st)
    for mm in range(1,17):
        x,y=cont(mm,ss),terminating_formula(mm,ss)
        assert mp.almosteq(x,y,rel_eps=mp.mpf('1e-44')), (mm,st,x,y)
        checks+=1
positive=['-3.9','-3.5','-3.1','-2','-1.5','0','3']
for st in positive:
    ss=mp.mpf(st)
    assert all(cont(mm,ss)>0 for mm in range(1,101)),st
negative=['-2.7','-2.3','-4.9','-4.2','-5.1','-6.5','-9.5']
for st in negative:
    ss=mp.mpf(st)
    assert any(cont(mm,ss)<0 for mm in range(1,101)),st
# Exact s=-2 equality and the sign of I_1 for s<-5.
for mm in range(1,41):
    assert mp.almosteq(cont(mm,mp.mpf('-2')),mp.mpf(1))
for st in ['-5.1','-5.5','-7.5','-12.5']:
    assert cont(1,mp.mpf(st))<0
print(f'VERIFY_OK independent_exact_beta_cases={16*9} terminating_4F3_checks={checks} positive_parameter_samples={len(positive)} negative_parameter_samples={len(negative)} s_minus_two_cases=40')
