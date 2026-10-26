"""Exact calculations for finite-size covariance in Ford's alpha tree model.
Run with python verify.py (requires sympy)."""
import sympy as s
from collections import defaultdict
x,t=s.symbols('alpha t'); assertion_count=0

def check(statement):
 global assertion_count
 assert bool(statement)
 assertion_count+=1

# Transition weights independently from the four edge-event classes.
def next_pmf(pmf,n,alpha):
 out=defaultdict(lambda:s.S.Zero)
 for (A,C),prob in pmf.items():
  if prob==0: continue
  weights={ (A,C):2*A+alpha*(n-A-C-1),
            (A-1,C+1):(1-alpha)*A,
            (A+1,C):(2-alpha)*(C-A),
            (A,C+1):(1-alpha)*(n-A-2*C)}
  check(s.simplify(sum(weights.values())-(n-alpha))==0)
  for v,w in weights.items():
   check(s.simplify(w)>=0)
   if w!=0: out[v]+=prob*w/(n-alpha)
 return out

# Distinct recurrence derived from conditional transition increments.
def next_mom(v,n,alpha):
 C,A,C2,AC,A2=v; z=n-alpha
 return [(n-2+alpha)*C/z+n*(1-alpha)/z,
         ((n-3+alpha)*A+(2-alpha)*C)/z,
         ((n-4+3*alpha)*C2+2*(n-1)*(1-alpha)*C+n*(1-alpha))/z,
         ((n-5+3*alpha)*AC+(n-1)*(1-alpha)*A+(2-alpha)*C2)/z,
         ((n-6+3*alpha)*A2+2*(2-alpha)*AC+(2-alpha)*C-A)/z]

def pmf_mom(pmf):
 return [sum(p*z[i] for z,p in [( (C,A,C*C,A*C,A*A),v) for (A,C),v in pmf.items()]) for i in range(5)]

for alpha in map(s.Rational,['0','1/6','1/3','1/2','3/4','9/10','1']):
 pmf={(1,1):s.S.One};mom=[s.S.One]*5
 for n in range(3,14):
  pm=pmf_mom(pmf)
  for a,b in zip(pm,mom):check(s.cancel(a-b)==0)
  if n<13:
   pmf=next_pmf(pmf,n,alpha)
   mom=[s.cancel(z) for z in next_mom(mom,n,alpha)]
   check(s.cancel(sum(pmf.values())-1)==0)

v=[s.S.One]*5; cov={}
for n in range(3,9):
 C,A,C2,AC,A2=v
 cov[n]=s.factor(AC-A*C)
 if n<8:v=[s.factor(z) for z in next_mom(v,n,x)]
P6=11*x**4-88*x**3+391*x**2-458*x+240
P7=13*x**6-320*x**5+1409*x**4-1834*x**3-10164*x**2+20376*x-10080
check(cov[3]==0)
check(s.factor(cov[4]-2*(x-1)/(x-3)**2)==0)
check(s.factor(cov[5]-2*(x-1)*(x+2)**2/((x-4)**2*(x-3)**2))==0)
check(s.factor(cov[6]-2*(x-1)*P6/((x-5)**2*(x-4)**2*(x-3)**2))==0)
check(s.factor(cov[7]+2*(x-1)*P7/((x-6)**2*(x-5)**2*(x-4)**2*(x-3)**2))==0)
for poly,expected in [(P6,[240,502,457,280,96]),(-P7,[10080,40104,59484,40330,12517,2260,600])]:
 Q=s.Poly(s.cancel((1+t)**s.degree(poly,x)*poly.subs(x,t/(1+t))),t)
 check(list(reversed(Q.all_coeffs()))==expected)
 check(all(c>0 for c in Q.all_coeffs()))

# Linear-response coefficient at alpha=1, proved by differentiation of recurrences.
# This gives the same (n-3)/2-H_{n-3} for the covariance.
u=v=w=s.S.Zero
for n in range(3,150):
 r=s.simplify(w-u-v)
 expected=s.Rational(n-3,2)-s.harmonic(n-3)
 check(r==expected)
 check((r>0)==(n>=8) if n>=4 else r==0)
 un=u+s.Rational(n-2,n-1)
 vn=((n-2)*v+u-1)/(n-1)
 wn=((n-2)*w+(n-4)+3*u)/(n-1)
 u,v,w=un,s.cancel(vn),s.cancel(wn)

print('VERIFY_OK',assertion_count,'exact assertions; four-transition Markov law; finite certificates; harmonic response')
