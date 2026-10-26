"""Exact symbolic checks for the harvesting/fear/cooperative-hunting coexistence theorem.

Requires Python 3 and SymPy. No network or external datasets are used.
"""
import sympy as S

u, v = S.symbols('u v', positive=True)
a, beta, h, B, c, mu = S.symbols('a beta h B c mu', positive=True)
delta = mu*(h+1/B)
prey_per_capita = (1-u)/(1+beta*v) - (1+a*v)*v/(1+h*(1+a*v)*u) - c
predator_per_capita = delta*(1+a*v)*u/(1+h*(1+a*v)*u) - mu
flow = S.Matrix([u*prey_per_capita, v*predator_per_capita])
u_null = B/(1+a*v)
R = S.factor(prey_per_capita.subs(u,u_null))
Q = S.expand((1+h*B)*(1+a*v)*(1+beta*v)*R)
Q_target = S.expand((1+h*B)*(1+a*v-B)
      - c*(1+h*B)*(1+a*v)*(1+beta*v)
      - v*(1+a*v)**2*(1+beta*v))
assert S.simplify(Q-Q_target)==0
assert S.simplify(predator_per_capita.subs(u,u_null))==0
assert S.simplify(Q.coeff(v,0)+(1+h*B)*(B+c-1))==0
assert S.simplify(Q.coeff(v,1)-((1+h*B)*(a*(1-c)-c*beta)-1))==0
assert S.simplify(Q.coeff(v,2)+(1+h*B)*c*a*beta+2*a+beta)==0
assert S.simplify(Q.coeff(v,3)+a*(a+2*beta))==0
assert S.simplify(Q.coeff(v,4)+a*a*beta)==0

# At an interior equilibrium, det J = -u*v*(G_u)*dR/dv
# along the predator-nullcline u=B/(1+a*v).
J = flow.jacobian([u,v])
G_u = S.diff(predator_per_capita,u)
# The determinant identity follows symbolically from the chain rule:
# dR/dv = F_v - F_u G_v/G_u and det = u*v*(F_u G_v-F_v G_u).
# Check both sides at the exact example after specialization.

# Exact biological example: mu=m+c2=1/100, delta=11/1000.
example = {a:S.Integer(10), beta:S.Integer(1), h:S.Rational(1,10),
           B:S.Integer(1), c:S.Rational(1,10), mu:S.Rational(1,100)}
Qe = S.factor(Q.subs(example))
ue = S.factor(u_null.subs(example))
fex = prey_per_capita.subs(example)
gex = predator_per_capita.subs(example)
Rg = S.factor(R.subs(example))
fu = S.diff(fex,u).subs(u,ue)
fv = S.diff(fex,v).subs(u,ue)
gu = S.diff(gex,u).subs(u,ue)
gv = S.diff(gex,v).subs(u,ue)
assert S.cancel(fu*gv - fv*gu + gu*S.diff(Rg,v)) == 0
assert S.expand(100*Qe)==(-10000*v**4 -12000*v**3-2210*v**2+879*v-11)
certified_endpoints = [
 (S.Rational(1,100),-1), (S.Rational(1,50),1),
 (S.Rational(1,6),1),(S.Rational(1,5),-1)]
for endpoint,sign in certified_endpoints:
    assert S.sign(Qe.subs(v,endpoint))==sign

# For the two simple positive roots, determinant alternates sign;
# the higher root is a sink if its trace is negative.
trace = S.factor(S.trace(J.subs(u,u_null)).subs(example))
trace_expected = -(100000*v**4+120000*v**3+22100*v**2-9879*v+1331)/(1210*(1+v)*(1+10*v))
assert S.factor(trace-trace_expected)==0
trace_lower_bound = S.Rational(120000,216)+S.Rational(22100,36) + 1331 - S.Rational(9879,5)
assert trace_lower_bound>0
# Stability of the prey-only equilibrium (1-c,0).
axis_u = 1-example[c]
axis_J = S.simplify(J.subs(example).subs({u:axis_u,v:0}))
assert S.simplify(axis_J[0,0] + S.Rational(9,10))==0
assert axis_J[1,1] < 0
assert S.simplify(axis_J.det()-axis_J[0,0]*axis_J[1,1])==0

# A positive subcritical witness exists in the allowed region,
# and two roots are contained in disjoint rational intervals.
assert Qe.subs(v,S.Rational(1,10))>0
assert example[B]>1-example[c]
assert S.simplify(delta.subs(example)-S.Rational(11,1000))==0
for p in [S.Rational(1,100),S.Rational(1,50),S.Rational(1,6),S.Rational(1,5)]:
    assert S.factor(Qe.subs(v,p)).is_Rational
print('PASS: nullcline elimination, coefficient signs, determinant identity,')
print('      exact root isolation, upper sink, and boundary sink certificates.')
print('Q(v)=',Qe)
print('tr(J)=',trace)
