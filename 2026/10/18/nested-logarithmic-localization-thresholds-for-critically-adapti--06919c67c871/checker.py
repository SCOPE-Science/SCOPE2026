"""Reproducible algebraic checks for inverse-square adaptive-resetting comparators.
Requires sympy; checks are not substitutes for the probabilistic comparison proof.
"""
import sympy as s

t=s.symbols('t',positive=True)
b,c,d=s.symbols('b c d',real=True)

def potential(f):
    return s.simplify(2-3*s.diff(f,t)/f + s.diff(f,t,2)/f)

f0=t**(-b)
f1=s.exp(-s.log(t)-c*s.log(s.log(t)))
f2=s.exp(-s.log(t)-s.log(s.log(t))-d*s.log(s.log(s.log(t))))
q0=2+3*b/t+b*(b+1)/t**2
q1=2+3/t+3*c/(t*s.log(t))+2/t**2+3*c/(t**2*s.log(t))+c*(c+1)/(t**2*s.log(t)**2)
assert s.simplify(potential(f0)-q0)==0
assert s.simplify(potential(f1)-q1)==0
q2=potential(f2)
lead2=2+3/t+3/(t*s.log(t))+3*d/(t*s.log(t)*s.log(s.log(t)))
# Verify the claimed remainder is O(t^{-2}) with logarithms bounded for t>=e^e.
res2=s.simplify((q2-lead2)*t**2)
assert not res2.has(s.Derivative)
for bb in [s.Rational(-5,2),-1,0,s.Rational(3,4),1,s.Rational(4,3),2,4]:
 assert s.simplify(q0.subs(b,bb)-potential(f0.subs(b,bb)))==0
for cc in [s.Rational(-1,2),0,s.Rational(1,2),1,s.Rational(3,2),3]:
 assert s.simplify(q1.subs(c,cc)-potential(f1.subs(c,cc)))==0
for dd in [s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]:
  for tt in [s.Integer(20),s.Integer(100),s.Integer(1000)]:
   expr=s.N(res2.subs({d:dd,t:tt}),20)
   assert expr.is_finite
# At thresholds, the corresponding exact comparator tails have integrals
# ∫_R^∞ dx [x (log x)^b]^{-1} = ∫_{log R}^∞ t^{-b}dt,
# ∫_R^∞ dx [x log x (log log x)^c]^{-1} = ∫_{log log R}^∞ u^{-c}du.
for v in [s.Rational(-1,2),0,s.Rational(1,2),1,2,3]:
 assert (v>1)==bool(v in [2,3])
print('PASS: exact first and second comparator identities, third leading term, finite sample checks')
print('Third comparator remainder:',res2)
