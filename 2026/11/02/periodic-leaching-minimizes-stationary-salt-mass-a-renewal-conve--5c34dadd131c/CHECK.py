from fractions import Fraction as F
from sympy import symbols, simplify, exp, log, sqrt, factor, diff
import random, math

# Independent regenerative-reward calculation for b=0; exact rational moments.
for r in [F(1,4), F(1,2), F(3,4)]:
  for a in [F(1),F(3,2)]:
    for z in [F(1,2),F(3,4),F(1),F(3,2)]:
      # Any two-point law with equal weights and mean one.
      L1,L2=z,2-z
      mu=(L1+L2)/2
      m2=(L1**2+L2**2)/2
      m3=(L1**3+L2**3)/2
      ex=r*a*mu/(1-r)
      ex2=r*r*(2*a*mu*ex + a*a*m2)/(1-r*r)
      time_mean=ex+a*m2/(2*mu)
      time_m2=ex2+a*ex*m2/mu+a*a*m3/(3*mu)
      var_reward=time_m2-time_mean**2
      var_rep=a*a*(m3/(3*mu) - (m2/(2*mu))**2 + r*r*(m2-mu**2)/(1-r*r))
      assert var_reward==var_rep,(r,a,z,var_reward,var_rep)
      assert time_mean-a*(r*mu/(1-r)+mu/2)==a*(m2-mu*mu)/(2*mu)
      assert var_reward>=a*a*mu*mu/12
print('Exact b=0 regenerative moments and universal variance comparisons checked:',3*2*4)

# b>0: direct renewal-cycle reward expression vs transformed stationary formula.
a,b,r,mu,q=symbols('a b r mu q', positive=True)
post=(r*a/b)*(1-q)/(1-r*q)
via_reward=(a*mu/b + (post-a/b)*(1-q)/b)/mu
via_formula=a/b*(1-(1-r)*(1-q)/(b*mu*(1-r*q)))
assert simplify(via_reward-via_formula)==0
q0=symbols('q0', positive=True)
gap=simplify(via_formula-via_formula.subs(q,q0))
expected=a*(1-r)**2*(q-q0)/(b*b*mu*(1-r*q0)*(1-r*q))
assert simplify(gap-expected)==0
assert simplify(diff(via_formula,q)-a*(1-r)**2/(b*b*mu*(1-r*q)**2))==0
print('Exact symbolic b>0 regenerative formula, sharp gap, monotonic derivative checked: 3')

# Exact calculation for L=1/2 or 3/2 equally likely, r=1/2 and b=ln 2,
# where q=(2^-1/2+2^-3/2)/2=3/(4sqrt2)>1/2.
from sympy import Rational as Q
qp=3/(4*sqrt(2)); qp0=Q(1,2); rr=Q(1,2)
assert simplify(qp-qp0).is_positive
finite_gap = expected.subs({a:1, b:log(2),mu:1,r:rr,q:qp,q0:qp0})
assert finite_gap.evalf(40)>0
print('Exact two-point b>0 strict mean difference numerically:',finite_gap.evalf(17))

# Independent numerical integral of time sampled mass using a regenerative event-stationary trajectory.
# Deterministic PRNG to make checks reproducible.
def sample_time_average(B,N,values,probs,aa=1.,rr=.5):
    rng=random.Random(8710097+int(B*100))
    x=0.; total_time=0.; total_area=0.
    for j in range(N):
       t=rng.choices(values,probs)[0]
       if B:
           e=math.exp(-B*t)
           area=aa*t/B+(x-aa/B)*(1-e)/B
           x=rr*(aa/B+(x-aa/B)*e)
       else:
           area=x*t+aa*t*t/2
           x=rr*(x+aa*t)
       if j>200:
           total_time+=t; total_area+=area
    return total_area/total_time
for B in [0.,0.25,1.,2.]:
    vals=[.5,1.5]; prob=[.5,.5]
    qv=(math.exp(-B*.5)+math.exp(-B*1.5))/2 if B else None
    theo=(1/B)*(1-(1-.5)*(1-qv)/(B*(1-.5*qv))) if B else 1+.625
    sim=sample_time_average(B,300000,vals,prob)
    assert abs(sim-theo)<.007,(B,theo,sim)
    print('regenerative simulation',B,'predicted',round(theo,7),'sample',round(sim,7))
