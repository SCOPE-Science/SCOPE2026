"""Standalone exact and numerical checks for the two-particle nearest-neighbour symmetric exclusion bracket theorem.
No external files required; scipy is optional only for the limiting-mean numerical probe.
"""
from fractions import Fraction as Q
from math import comb, exp, sqrt, pi, erf, erfc

checks = 0

def check(cond, label):
    global checks
    if not cond: raise AssertionError(label)
    checks += 1


def states(x,y):
    """Local generator, two particles (x<y), each allowable move at rate 1/2."""
    assert x<y
    out=[]
    for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if nx<ny: out.append((nx,ny,Q(1,2)))
    return out

def C(s): return Q(s[0]+s[1],2)
def R(s): return s[1]-s[0]
def LG(s,f): return sum((rate*(f((u,v))-f(s)) for u,v,rate in states(*s)),Q(0))
def Gam(s,f,g): return sum((rate*(f((u,v))-f(s))*(g((u,v))-g(s)) for u,v,rate in states(*s)),Q(0))
for x in range(-19,20):
 for gap in range(1,22):
    s=(x,x+gap); adj=int(gap==1)
    check(LG(s,C)==0,(s,'L C'))
    check(LG(s,R)==adj,(s,'L R'))
    check(Gam(s,C,C)==Q(1,2)-Q(adj,4),(s,'Gamma CC'))
    check(Gam(s,R,R)==2-adj,(s,'Gamma RR'))
    check(Gam(s,C,R)==0,(s,'Gamma CR'))
    check(LG(s,lambda p:C(p)**2)-2*C(s)*LG(s,C)==Q(1,2)-Q(adj,4),(s,'L C2'))
    check(LG(s,lambda p:Q(R(p)**2))-2*R(s)*LG(s,R)==2-adj,(s,'L R2'))

# Independent uniformization at intensity 2 of the gap process on the positive integers.
# At gap 1, attempted downward steps are self-loops. Verify reflected image formula
# against unconstrained symmetric random walk for exact rational probabilities.
def lattice_walk_prob(k,d):
 return Q(comb(k,(k+d)//2),2**k) if abs(d)<=k and (k+d)%2==0 else Q(0)

def gap_transition(k,start):
 p={start:Q(1)}
 for _ in range(k):
    q={}
    for r,v in p.items():
        for dest in (r+1,max(r-1,1)):
            q[dest]=q.get(dest,Q(0))+v/2
    p=q
 return p
for start in range(1,15):
 for k in range(0,21):
    p=gap_transition(k,start)
    check(sum(p.values())==1,('stochastic',start,k))
    for target in range(1,start+k+2):
       image=lattice_walk_prob(k,target-start)+lattice_walk_prob(k,target+start-1)
       check(p.get(target,Q(0))==image,('Neumann images',start,k,target))

# Independently verify the exact Brownian-regulator formulas by elementary Gaussian integrals.
def phi(z): return exp(-z*z/2)/sqrt(2*pi)
def Phi(z): return (1+erf(z/sqrt(2)))/2
def K_mean(delta,t):
 z=delta/sqrt(2*t)
 return 2*(sqrt(2*t)*phi(z)-delta*(1-Phi(z)))
for delta,t in ((0,1),(0.25,0.8),(0.6,2.1),(1,1),(2,3)):
 z=delta/sqrt(2*t)
 check(abs(K_mean(delta,t)-(2*sqrt(t/pi)*exp(-delta*delta/(4*t))-2*delta*(1-Phi(z))))<1e-12,('mean formula',delta,t))
 check(abs((2*Phi(z)-1)+2*(1-Phi(z))-1)<1e-12,('atom+tail',delta,t))

try:
 from scipy.integrate import quad
 from scipy.special import ive
 for delta in (0.0,0.6,1.4):
  for n in (40,80):
   start=max(1, round(n*delta))
   # Bessel Neumann heat kernel for the microscopic gap process
   # P(R_u=1)=exp(-2u)(I_{start-1}(2u)+I_start(2u)).
   finite,_=quad(lambda s: n*(ive(start-1,2*n*n*s)+ive(start,2*n*n*s)),0,1,epsabs=1e-7,limit=250)
   limiting=K_mean(delta,1.0)
   check(abs(finite-limiting)<0.09,('local-time expectation',delta,n,finite,limiting))
except ImportError:
 print('scipy unavailable, skipped optional quadrature probes')
print('PASS',checks,'assertions')
