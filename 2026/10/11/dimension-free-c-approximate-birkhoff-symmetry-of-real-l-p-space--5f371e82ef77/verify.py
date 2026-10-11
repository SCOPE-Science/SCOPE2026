"""Supplementary exact and sampled verification of the Lp two-atom symmetry theorem."""
from fractions import Fraction as Q
from itertools import product
import math
import random
import sympy as s

z=s.symbols('z',real=True)
t=s.symbols('t',positive=True)
f=z**3*(1-z**2)/(1+z**2)**2
assert s.simplify(s.diff(f,z)-z**2*(3-6*z*z-z**4)/(1+z*z)**3)==0
w=2*s.sqrt(3)-3
assert s.simplify(f.subs(z,s.sqrt(w))**2-(78*s.sqrt(3)-135)/16)==0
assert 0<float(w)<1
phi3cub=t*(t-1)**3/((1+t)*(1+t*t)**2)
sub=((t-1)/(t+1))**3*(1-((t-1)/(t+1))**2)/(1+((t-1)/(t+1))**2)**2
assert s.factor(phi3cub-sub)==0

def phi(p,t):
    return (t**(1/p)*abs(t**(p-2)-1)/
            ((1+t)**(1/p)*(1+t**(p-1))**((p-1)/p)))

def num_mean_abs(p,vals,weights):
    A=sum(w*(abs(v)**(p-1))*(1 if v>0 else -1 if v<0 else 0)
          for v,w in zip(vals,weights))
    M=sum(w*(abs(v)**p) for v,w in zip(vals,weights))
    return abs(A)/M**((p-1)/p) if M else 0.

for p in (1.25,1.5,1.75,2.2,3,4,6,9):
    q=p/(p-1)
    for t0 in (0.05,0.2,0.75,2,5,20):
        assert abs(phi(p,t0)-phi(q,t0**(p-1)))<3e-12

# Construct many EXACT rational finite laws satisfying E[T]=0, and verify
# p=3 compression using exact Fraction arithmetic, not floating point.
exact_checks=0
for v in product((-3,-2,-1,0,1,2,3),repeat=3):
    if max(v)<=0 or min(v)>=0:
        continue
    for w1,w2 in product(range(1,5),repeat=2):
        # Solve w1*v1+w2*v2+w3*v3=0 for positive w3 when possible.
        if v[2]==0:
            continue
        w3=Q(-w1*v[0]-w2*v[1],v[2])
        if w3<=0 or w3>5:
            continue
        raw=[Q(w1),Q(w2),w3]
        den=sum(raw)
        weights=[u/den for u in raw]
        m=sum(w*max(u,0) for w,u in zip(weights,v))
        if m<=0:
            continue
        A=sum(w*max(u,0)**2 for w,u in zip(weights,v))
        B=sum(w*max(-u,0)**2 for w,u in zip(weights,v))
        aa=A/m;bb=B/m
        S=m/aa+m/bb
        moment=sum(w*abs(u)**3 for w,u in zip(weights,v))
        assert S<=1
        assert moment>=m*(aa*aa+bb*bb)
        # exact sixth-power comparison removes any fractional exponents
        # from the p=3 quotient.
        left=abs(A-B)**3/moment**2
        va=(aa*bb/(aa+bb))*(aa-bb)
        pm=aa*bb*(aa*aa+bb*bb)/(aa+bb)
        right=abs(va)**3/pm**2
        assert left<=right
        exact_checks+=1
assert exact_checks>20

# Sample an arbitrary vector y orthogonal to a normalized x by subtracting
# its Jp(x) projection in a finite real ell_p space.
random.seed(20261008)
numchecks=0
for p in (1.4,1.5,2.,2.4,3.,4.,6.):
    q=p/(p-1)
    env=max(phi(p,math.exp((i-400)/35)) for i in range(801))
    # A fine scalar numerical grid is not a certificate of global optimality;
    # check against a conservative positive margin only.
    for n in (2,3,5,10,16):
        for _ in range(200):
            x=[random.uniform(-2,2) for _ in range(n)]
            xn=sum(abs(a)**p for a in x)**(1/p)
            x=[a/xn for a in x]
            yy=[random.uniform(-2,2) for _ in range(n)]
            j=[math.copysign(abs(a)**(p-1),a) for a in x]
            c=sum(a*b for a,b in zip(j,yy))
            y=[b-c*a for a,b in zip(x,yy)]
            yn=sum(abs(a)**p for a in y)**(1/p)
            if yn<1e-12:continue
            y=[a/yn for a in y]
            assert abs(sum(a*b for a,b in zip(j,y)))<1e-9
            defect=abs(sum(math.copysign(abs(b)**(p-1),b)*a for a,b in zip(x,y)))
            assert defect<=env+1.4e-3,(p,n,defect,env)
            numchecks+=1

for p in (1.4,1.5,2.4,3.,4.,6.):
    tbest=max((phi(p,math.exp((i-400)/50)),math.exp((i-400)/50)) for i in range(801))[1]
    a,b=tbest,1.
    ww=b/(a+b)
    x=[ww**(1/p),(1-ww)**(1/p)]
    v=[a*x[0],-b*x[1]]
    vn=sum(abs(c)**p for c in v)**(1/p)
    y=[c/vn for c in v]
    assert abs(sum(math.copysign(abs(c)**(p-1),c)*d for c,d in zip(x,y)))<1e-10
    got=abs(sum(math.copysign(abs(c)**(p-1),c)*d for c,d in zip(y,x)))
    assert abs(got-phi(p,tbest))<2e-10

print(f'VERIFY_OK cubic_symbolic=4 exact_weighted_laws={exact_checks} '
      f'sampled_pairs={numchecks} conjugate_pairs=48 two_atom_witnesses=6')
