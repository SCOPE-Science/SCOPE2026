"""Self-contained numerical and algebraic diagnostics for a lossy directed 4-cycle.
Run: python3 verify.py
"""
import math
import cmath

pi=math.pi
S=[[int((i-j)%4==1) for j in range(4)] for i in range(4)]
assert all(sum(r)==1 for r in S)
assert all(sum(S[i][j] for i in range(4))==1 for j in range(4))
assert [(sum(S[i][j]*[1,1,1,1][j] for j in range(4))) for i in range(4)]==[1]*4
v=[1,1j,-1,-1j]
# For this convention, the shift eigenvalue on v is -i.
assert all(abs(sum(S[i][j]*v[j] for j in range(4))+1j*v[i])<1e-14 for i in range(4))
assert all(abs(sum(S[i][j]*((-1)**j) for j in range(4))+(-1)**i)<1e-14 for i in range(4))


def ts(d): return pi/(2*(1-d))
def tc(d):
 p=1-d
 if d>=p:return math.inf
 return math.acos(-d/p)/(d+math.sqrt(p*p-d*d))

def h(t):return pi/2+t-(pi/2)*(math.sin(t)+math.cos(t))

lo,hi=0.6,0.7
# The positive crossing in t is obtained by a rigorously monotone convexity argument in RESULT.md.
assert h(lo)<0<h(hi)
for _ in range(90):
 mid=(lo+hi)/2
 if h(mid)<0:lo=mid
 else:hi=mid

t=(lo+hi)/2
q=math.sin(t)
dstar=q/(1+q)
assert abs(h(t))<1e-13
assert .3676<dstar<.3678
assert abs(ts(dstar)-tc(dstar))<1e-12
assert tc(.1)<ts(.1)
assert tc(.3)<ts(.3)
assert tc(.4)>ts(.4)

# Modal characteristic residuals at first crossing; no numerical time integration is used.
checks=0
for d in (.03,.1,.2,.3,dstar,.4,.45,.6,.8):
 p=1-d
 w=p
 tau=ts(d)
 z=1j*w
 assert abs(z+p*cmath.exp(-z*tau))<1e-12
 checks+=1
 if d<p:
  nu=math.sqrt(p*p-d*d)
  w=d+nu
  tau=tc(d)
  z=1j*w
  assert abs(z+d-1j*d+p*cmath.exp(-z*tau))<1e-12
  # Re of the exact implicit derivative, calculated independently.
  deriv=p*z*cmath.exp(-z*tau)/(1-p*tau*cmath.exp(-z*tau))
  direction=w*(w-d)/abs(1-p*tau*cmath.exp(-z*tau))**2
  assert abs(deriv.real-direction)<1e-12 and direction>0
  checks+=2

# Test the mode competition and minimality as d->0.
for d in (1e-5,1e-4,1e-3):
 p=1-d
 a3=1.5*d
 b3=math.sqrt(3)*d/2
 tau3=math.acos(-a3/p)/(b3+math.sqrt(p*p-a3*a3))
 assert tau3>ts(d)>tc(d)
 checks+=1

# The two distinct frequencies at the double crossing.
p=1-dstar
ws=p
wc=dstar+math.sqrt(p*p-dstar*dstar)
assert wc>ws>0
assert dstar < 1/(1+math.sqrt(2))
print('VERIFY_OK',checks,'mode tests; d_star=',format(dstar,'.16g'),'tau_star=',format(ts(dstar),'.16g'))
