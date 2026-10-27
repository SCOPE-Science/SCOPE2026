"""Exact symbolic checks for the two-loss NGN conditional-mean map.

Requires SymPy (see requirements.txt). All theorem-wide inequalities are
proved separately by elementary sign analysis; finite checks are illustrative.
"""
import sympy as sp

x, A, d, s = sp.symbols('x A d s', real=True)
h = lambda y: y * (y*y+d) / (A*y*y+d)
F = (h(x-1)+h(x+1))/2
B = (A+1)*d-2*A
C = d*d+(3-A)*d+A
D = (A*(x-1)**2+d)*(A*(x+1)**2+d)
P = A*x**4+B*x*x+C
assert sp.cancel(F-x*P/D) == 0
assert sp.simplify(sp.discriminant(A*s*s+B*s+C,s)-d*((A-1)**2*d-16*A)) == 0
assert sp.factor(C.subs(d,16*A/(A-1)**2)-B.subs(d,16*A/(A-1)**2)**2/(4*A)) == 0

Fw = sp.factor(F.subs({A:12,d:sp.Rational(8,5)}))
expected = x*(5*x*x-1)*(15*x*x-1)/(4*(15*x*x-30*x+17)*(15*x*x+30*x+17))
assert sp.cancel(Fw-expected) == 0
T_prime = sp.factor(sp.diff(x-11*Fw,x))
for xx, val in [(0,sp.Rational(1145,1156)),
                (1/sp.sqrt(15),sp.Rational(73,72)),
                (-1/sp.sqrt(15),sp.Rational(73,72)),
                (1/sp.sqrt(5),sp.Rational(19,20)),
                (-1/sp.sqrt(5),sp.Rational(19,20))]:
    assert sp.simplify(T_prime.subs(x,xx)-val) == 0
    assert sp.simplify(Fw.subs(x,xx)) == 0
assert sp.simplify((sp.Rational(1,2)*(x*x+1+sp.Rational(8,5))).subs(x,1/sp.sqrt(5))
                   -(sp.Rational(1,2)*(x*x+1+sp.Rational(8,5))).subs(x,0)) == sp.Rational(1,10)
# Exact comparison of the offset bounds, including the equality boundary.
a_critical = 5+4*sp.sqrt(2)
assert sp.simplify((a_critical-1)**2-8*(a_critical+1)) == 0
for aa in (sp.Rational(3),sp.Rational(10),sp.Rational(12),sp.Rational(50)):
    gap = sp.factor(2*aa/(aa+1)-16*aa/(aa-1)**2)
    assert (gap>0) == (aa>a_critical)
print('VERIFY_OK exact rational map, discriminant, threshold, and five multipliers')
