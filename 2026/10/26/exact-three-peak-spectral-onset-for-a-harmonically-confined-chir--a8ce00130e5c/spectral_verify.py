"""Reproducible symbolic checks of a chiral Brownian swimmer's stationary power-spectrum phase change.
Run: python spectral_verify.py  (requires sympy; numpy optional and not used).
"""
import sympy as sp
z,h,t=sp.symbols('z h t', real=True)
Q=(h+z)*(z*z+2*(1-t)*z+(1+t)**2)
P=sp.expand(Q-(1+t+z)*sp.diff(Q,z))
claimed=-2*z**3-(5+h+t)*z**2+2*(1+t)*(2*t-2-h)*z-(1+t)*((1+t)**2+h*(1-3*t))
checks=0
def check(label,a,b):
 global checks
 assert sp.simplify(a-b)==0, (label,sp.factor(a-b))
 checks+=1
check('spectral numerator',P,claimed)
p=sp.factor(P.subs(h,1))
check('cubic discriminant',sp.discriminant(p,z),16*t**4*(1+t)*(17*t-108))
tc=sp.Rational(108,17);zc=sp.Rational(55,17)
check('double-root factorization',p.subs(t,tc),-sp.Rational(2,4913)*(17*z-55)**2*(17*z+215))
check('critical value',p.subs({z:zc,t:tc}),0)
check('critical spatial derivative',sp.diff(p,z).subs({z:zc,t:tc}),0)
check('parameter slope',sp.diff(p,t).subs({z:zc,t:tc}),sp.Rational(432,17))
check('local concavity',sp.diff(p,z,2).subs({z:zc,t:tc}),-sp.Rational(1080,17))
check('fold coefficient',-2*sp.diff(p,t).subs({z:zc,t:tc})/sp.diff(p,z,2).subs({z:zc,t:tc}),sp.Rational(4,5))
check('matched zero numerator',p.subs(z,0),-(1+t)*(t*t-t+2))
check('achiral derivative',p.subs(t,0),-2*(z+1)**3)
check('central-curvature polynomial',P.subs(z,0),-(1+t)*((1+t)**2+h*(1-3*t)))
for hh,tt,expect_positive in [(1,0,0),(1,6,0),(1,7,2),(1,10,2),(1,100,2),(2,1,0),(2,2,1),(2,3,1),(2,4,2),(9,4,1)]:
 roots=sp.polys.polytools.intervals(sp.Poly(P.subs({h:hh,t:tt}),z),eps=sp.Rational(1,10000))
 strictly_positive=0
 for (a,b),mult in roots:
  if a>0: strictly_positive+=mult
 # boundary P(0)=0 causes a degenerate zero which is not counted.
 assert strictly_positive==expect_positive,(hh,tt,strictly_positive,expect_positive,roots)
 checks+=1
print('PASS:',checks,'independent symbolic and root-isolation assertions')
