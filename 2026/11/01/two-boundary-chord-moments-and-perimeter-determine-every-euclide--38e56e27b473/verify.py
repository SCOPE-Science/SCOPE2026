"""Exact checks for the perimeter-chord two-moment triangle reconstruction theorem.
Run: python verify.py  (requires SymPy).  All algebraic identities are symbolic.
"""
import sympy as sp

a,b,c = sp.symbols('a b c', positive=True)
t,u = sp.symbols('t u', real=True)
p = a+b+c
q = a*b+b*c+c*a
r = a*b*c
G = sp.Matrix([[c*c,(b*b+c*c-a*a)/2],[(b*b+c*c-a*a)/2,b*b]])
# The vertices have Gram coordinates A=(0,0), B=(1,0), C=(0,1).
# Thus the Gram bilinear form accounts for the prescribed side lengths.
edges = [(c,sp.Matrix([t,0])),(b,sp.Matrix([0,t])),(a,sp.Matrix([1-t,t]))]
def pair_integral(n):
    total=0
    for Li,xi in edges:
        for Lj,xj in edges:
            z=xi-xj.subs(t,u)
            squared=sp.expand((z.T*G*z)[0])
            integral=sp.integrate(sp.integrate(squared**n,(t,0,1)),(u,0,1))
            total += Li*Lj*integral
    return sp.cancel(total/p**2)

m2=pair_integral(1)
m4=pair_integral(2)
assert sp.simplify(m2 - (p**3/sp.Integer(6)-p*q/2+r)/p)==0
assert sp.simplify(m4 - (p**5/sp.Integer(15)-5*p**3*q/18+p*p*r/2+p*q*q/9-2*q*r/9)/p)==0
area2=sp.factor((2*a*a*b*b+2*b*b*c*c+2*c*c*a*a-a**4-b**4-c**4)/16)
assert sp.simplify(area2 - (-p**4+4*p*p*q-8*p*r)/16)==0
assert sp.simplify(m2-(p*p/24-2*area2/p**2))==0
assert sp.simplify(m4-(p*p*m2/2-p**4/60+4*area2*q/(9*p*p)))==0
# All quantities are rational functions; following is an identity on every
# nondegenerate triangle, not a finite-case extrapolation.
q_from_moments= 9*p*p*(m4 -p*p*m2/2+p**4/60)/(4*area2)
r_from_moments=p*(m2-p*p/6+q_from_moments/2)
assert sp.simplify(sp.factor(q_from_moments-q))==0
assert sp.simplify(sp.factor(r_from_moments-r))==0
# Two equal-perimeter equal-area but noncongruent triangles: a 3-4-5 triangle
# and a triangle with three distinct algebraic sides.
A=sp.Rational(9,2); B=(15-sp.sqrt(17))/4; C=(15+sp.sqrt(17))/4
subs1={a:3,b:4,c:5}; subs2={a:A,b:B,c:C}
assert sp.simplify(p.subs(subs1)-p.subs(subs2))==0
assert sp.simplify(area2.subs(subs1)-area2.subs(subs2))==0
assert sp.simplify(m2.subs(subs1)-m2.subs(subs2))==0
assert sp.simplify(m4.subs(subs1)-sp.Rational(2503,45))==0
assert sp.simplify(m4.subs(subs2)-sp.Rational(10007,180))==0
assert sp.simplify(m4.subs(subs1)-m4.subs(subs2)-sp.Rational(1,36))==0
# The discriminating coefficient is 4 A^2/(9 P^4)>0 for A>0;
# at A=0 all normalized collapsed segment laws are identical.
print('VERIFY_OK symbolic_2nd_and_4th_moments, Heron, inversion, exact_equal_area_example')
