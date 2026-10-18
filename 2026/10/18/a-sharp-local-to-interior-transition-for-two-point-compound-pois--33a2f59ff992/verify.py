"""Reproducible exact coefficient and high-precision checks for two-point compound-Poisson jumps."""
from fractions import Fraction
from math import factorial
import sympy as s
import mpmath as mp

q = s.symbols('q')
def a_sym(n):
    return 2*(1+(5**(n+2)-1)*q)/(s.factorial(n+2)*(1+24*q))

def c_sym(n):
    return s.factor((1-n)*a_sym(n)+sum(a_sym(k)*a_sym(n-k) for k in range(1,n)))

assert s.factor(c_sym(2)-(16576*q*q-952*q+1)/(36*(1+24*q)**2))==0
assert s.factor(c_sym(3)-(80976*q*q-2852*q+1)/(45*(1+24*q)**2))==0
assert s.factor(c_sym(4)-(2796032*q*q-61664*q+7)/(720*(1+24*q)**2))==0
lo=(s.Integer(1927)+575*s.sqrt(11))/174752
hi=(s.Integer(713)+25*s.sqrt(781))/40488
critical=(s.Integer(17)/592)+(25*s.sqrt(21)/4144)
assert 0<s.Rational(1,50)<lo<s.Rational(1,40)<hi<s.Rational(1,25)<critical<1
for j in [2,3]:
    assert c_sym(j).subs(q,lo)<0
assert s.simplify(c_sym(3).subs(q,hi))==0
assert s.simplify(c_sym(4).subs(q,lo))==0
assert c_sym(4).subs(q,hi)>0
assert c_sym(2).subs(q,hi)<0
assert s.simplify(c_sym(2).subs(q,critical))==0
assert c_sym(3).subs(q,critical)>0
assert c_sym(4).subs(q,critical)>0

# For n>=5, positivity follows from a1,a2>=3/4 and exact ratio lower bounds.
assert s.factor(a_sym(1)-s.Rational(3,4)).subs(q,s.Rational(1,50))>0
assert s.factor(a_sym(2)-s.Rational(3,4)).subs(q,s.Rational(1,50))>0
n=s.symbols('n')
B=s.factor((1-n)+s.Rational(3,10)*(n+2)+s.Rational(3,50)*(n+2)*(n+1))
assert B.subs(n,5)>0 and s.diff(B,n).subs(n,5)>0 and s.diff(B,n,2)>0
for w in [lo,s.Rational(1,40),hi,critical,s.Rational(1,5),s.Integer(1)]:
    for j in range(5,25):
        assert c_sym(j).subs(q,w)>0

mp.mp.dps=75
w=mp.mpf(1)/40
def mm(t):
    if abs(t)<mp.mpf('1e-12'):
        return mp.nsum(lambda k: 2*(1+(mp.power(5,k+2)-1)*w)/(mp.factorial(k+2)*(1+24*w))*t**k, [0,20])
    return 2*((1-w)*mp.expm1(t)+w*mp.expm1(5*t)-(1+4*w)*t)/((1+24*w)*t*t)
def psi(t):return (1-1/mm(t))/t
def hh(t):return mm(t)*(mm(t)-1)-t*mp.diff(mm,t)
root=mp.findroot(hh,(mp.mpf('.45'),mp.mpf('.50')))
assert abs(root-mp.mpf('0.473723112'))<mp.mpf('0.00000001')
assert abs(psi(root)-mp.mpf('0.895416096'))<mp.mpf('0.00000001')
assert hh(root-mp.mpf('0.001'))<0<hh(root+mp.mpf('0.001'))
assert mp.diff(hh,root)>0
assert psi(root)>mp.mpf(41)/48
print('exact_coefficients_verified n2-4')
print('ordered_endpoints',s.N(lo,20),s.N(hi,20),s.N(critical,20))
d=s.diff(c_sym(2),q).subs(q,critical)
e=c_sym(3).subs(q,critical)
assert d>0 and e>0
print('onset_slopes',s.N(d/e,20),s.N(d*d/(2*e),20))
print('analytic_n_ge_5_inequality',B,'B5=',B.subs(n,5))
print('numerical_root',mp.nstr(root,35))
print('numerical_scale',mp.nstr(psi(root),35))
print('PASS')
