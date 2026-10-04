import itertools
import sympy as sp
from math import comb
p, d, u, h = sp.symbols("p d u h", real=True)
q = p + d
def pmf(x): return [(1-x)**2, 2*x*(1-x), x**2]
def tie_success_probability(scores):
    cutoff = sorted(scores, reverse=True)[1]
    above = [i for i,s in enumerate(scores) if s > cutoff]
    tied = [i for i,s in enumerate(scores) if s == cutoff]
    need = 2-len(above); den = comb(len(tied), need); out=sp.Rational(0)
    for choose in itertools.combinations(tied, need):
        if set(above).union(choose).isdisjoint({0,1}): out += sp.Rational(1,den)
    return out
ap, aq = pmf(p), pmf(q)
P_enum=0
for scores in itertools.product(range(3), repeat=4):
    P_enum += ap[scores[0]]*ap[scores[1]]*aq[scores[2]]*aq[scores[3]]*tie_success_probability(scores)
P_enum=sp.expand(P_enum)
A_p=[0,ap[0],ap[0]+ap[1]]; A_q=[0,aq[0],aq[0]+aq[1]]
P_int=0
for r in range(3):
    P_int += 2*aq[r]*sp.integrate((A_p[r]+ap[r]*u)**2*(1-A_q[r]-aq[r]*u),(u,0,1))
assert sp.simplify(P_enum-sp.expand(P_int))==0
pc=(1-d)/2; P_h=sp.expand(P_enum.subs(p,pc+h)); P_c=sp.expand(P_enum.subs(p,pc))
G=29+64*d+38*d**2-3*d**4-(84-12*d**2)*h**2-16*h**4
assert sp.simplify(P_h-P_c-d*h**2*G/24)==0
z=sp.symbols('z'); Gu=29+64*d+38*d**2-3*d**4-(84-12*d**2)*z-16*z**2
assert sp.simplify(Gu.subs(z,(1-d)**2/4)-(7+110*d+14*d**2-2*d**3-d**4))==0
for dv,pv in [(sp.Rational(1,5),sp.Rational(1,10)),(sp.Rational(1,2),sp.Rational(1,4)),(sp.Rational(3,4),sp.Rational(1,8))]:
    hv=pv-(1-dv)/2
    lhs=sp.simplify(P_enum.subs({d:dv,p:pv})-P_enum.subs({d:dv,p:(1-dv)/2}))
    rhs=sp.simplify(dv*hv**2*(29+64*dv+38*dv**2-3*dv**4-(84-12*dv**2)*hv**2-16*hv**4)/24)
    assert sp.simplify(lhs-rhs)==0 and rhs>=0
print("VERIFY_OK")
