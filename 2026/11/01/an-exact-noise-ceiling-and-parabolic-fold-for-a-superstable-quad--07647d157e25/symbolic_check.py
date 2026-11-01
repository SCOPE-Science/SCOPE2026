"""Exact symbolic checks of the polynomial elimination and fold factorization.

Requires SymPy. The analytic justification and sign ranges are in RESULT.md.
"""
import sympy as s

u,e=s.symbols('u e')
p=3*e-e**2+2*(1-e)*u**2-u**4-u
q=s.diff(p,u)
r=s.resultant(p,q,u)
assert s.factor(r)==-256*e**4+2336*e**2-5
crit=s.sqrt(73-22*s.sqrt(11))/4
uc=(51+64*crit**3-16*crit**2-556*crit)/88
assert s.simplify(p.subs({u:uc,e:crit}))==0
assert s.simplify(q.subs({u:uc,e:crit}))==0
H=2*(1-crit)-3*uc**2-2*uc*u-u**2
assert s.simplify(p.subs(e,crit)-(u-uc)**2*H)==0
print('PASS 4 exact polynomial certificates')
