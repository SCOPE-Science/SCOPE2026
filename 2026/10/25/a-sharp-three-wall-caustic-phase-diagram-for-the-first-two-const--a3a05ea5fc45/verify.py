"""Reproduce the exact algebra and representative root counts for the two-harmonic caustic theorem.

Requires Python 3 and SymPy. The continuous parameter classification is established in the accompanying proof.
"""
from fractions import Fraction
import sympy as S

u, a, b, y, t = S.symbols('u a b y t', real=True)
p = a*S.cos(3*u) + b*S.cos(5*u)
D = p + S.diff(p,u,2)
normal = S.Matrix([S.cos(u),S.sin(u)])
tangent = S.Matrix([-S.sin(u),S.cos(u)])
W = p*normal + S.diff(p,u)*tangent
C = W - D*normal
assert all(S.trigsimp(z)==0 for z in S.diff(W,u)-D*tangent)
assert all(S.trigsimp(z)==0 for z in S.diff(C,u)+S.diff(D,u)*normal)
qw = 4*y-3 + 3*t*(16*y*y-20*y+5)
qc = 4*y-1 + 5*t*(16*y*y-12*y+1)
assert S.simplify(S.discriminant(qw,y)-16*(45*t*t+6*t+1))==0
assert S.simplify(S.discriminant(qc,y)-16*(125*t*t-10*t+1))==0
assert qw.subs(y,0)==15*t-3 and qw.subs(y,1)==3*t+1
assert qc.subs(y,0)==5*t-1 and qc.subs(y,1)==25*t+3
# Signed areas of periodic parametrizations, counted once over u in [0,pi].
def area(Z):
    return S.simplify(S.integrate(S.expand_trig((Z[0]*S.diff(Z[1],u)-Z[1]*S.diff(Z[0],u))/2),(u,0,S.pi)))
for aa,bb,aw,ac in [(1,0,-2*S.pi,-18*S.pi),(0,1,-6*S.pi,-150*S.pi)]:
    assert S.simplify(area(W.subs({a:aa,b:bb}))-aw)==0
    assert S.simplify(area(C.subs({a:aa,b:bb}))-ac)==0
# Cross terms vanish by Fourier orthogonality; verify directly.
assert S.simplify(area(W.subs({a:1,b:1}))-(-8*S.pi))==0
assert S.simplify(area(C.subs({a:1,b:1}))-(-168*S.pi))==0

def interior_root_count(q, ratio):
    if ratio==0: return 1
    z=S.Poly(q.subs(t,S.Rational(ratio.numerator,ratio.denominator)), y)
    roots=S.nroots(z, maxsteps=100)
    return sum(abs(float(S.im(r)))<1e-12 and 0<float(S.re(r))<1 for r in roots)
for ratio,wc,cc in [(Fraction(-1,1),5,5),(Fraction(-1,4),3,5),
                    (Fraction(0,1),3,3),(Fraction(1,10),3,3),
                    (Fraction(1,4),5,5),(Fraction(1,1),5,5)]:
    assert 1+2*interior_root_count(qw,ratio)==wc
    assert 1+2*interior_root_count(qc,ratio)==cc
# At exceptional coefficient values, these are the exact vanishing orders.
f = S.cos(3*u)+3*t*S.cos(5*u)
g = S.sin(3*u)+5*t*S.sin(5*u)
for fun,ratio,u0,k in [(f,S.Rational(-1,3),0,2),(g,S.Rational(-3,25),0,3),
                        (f,S.Rational(1,5),S.pi/2,3),(g,S.Rational(1,5),S.pi/2,2)]:
    x=fun.subs(t,ratio)
    assert all(S.simplify(S.diff(x,u,i).subs(u,u0))==0 for i in range(k))
    assert S.simplify(S.diff(x,u,k).subs(u,u0))!=0
print('PASS: exact caustic derivatives, discriminants, signed areas, sample cusp counts and wall orders')
