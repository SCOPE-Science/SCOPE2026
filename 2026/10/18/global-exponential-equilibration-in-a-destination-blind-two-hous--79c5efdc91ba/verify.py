"""Exact and numerical checks for the two-house destination-blind relocation theorem.
Runs on Python >=3.10, using only the standard library.
The proof of infinite-time convergence is mathematical, not a computational claim.
"""
from fractions import Fraction as F
from itertools import product
from math import log

ST=((0,0),(1,0),(0,1),(2,0),(0,2),(1,1))
IDX={s:i for i,s in enumerate(ST)}

def events(beta,lam):
    """Directed ordered pair relocations (source,target,after_source,after_target,rate)."""
    ev=[]
    for s,(b,r) in enumerate(ST):
      for t,(B,R) in enumerate(ST):
        vacant=2-B-R
        if not vacant: continue
        if b:
          ev.append((s,t,IDX[(b-1,r)],IDX[(B+1,R)],F(b,2)*(beta+lam*r)*vacant))
        if r:
          ev.append((s,t,IDX[(b,r-1)],IDX[(B,R+1)],F(r,2)*(beta+lam*b)*vacant))
    return ev

def equilibrium(z,w,beta,lam):
    a=beta/(beta+lam)
    weights=[F(1),2*z,2*w,z*z,w*w,2*a*z*w]
    Z=sum(weights)
    return [x/Z for x in weights]

def derivative(p,beta,lam):
    out=[F(0) for _ in ST]
    for i,j,k,l,rate in events(beta,lam):
        flow=rate*p[i]*p[j]
        out[i]-=flow;out[j]-=flow;out[k]+=flow;out[l]+=flow
    return out

count=0
for beta,lam,z,w in product((F(1),F(3,2),F(7,3)),(F(0),F(1,2),F(5)),(F(1,3),F(2),F(5,4)),(F(1,4),F(3,4),F(7,3))):
    p=equilibrium(z,w,beta,lam)
    assert sum(p)==1 and min(p)>0
    assert derivative(p,beta,lam)==[F(0)]*6
    indexed=events(beta,lam)
    for i,j,k,l,r in indexed:
        reverses=[rv for x,y,u,v,rv in indexed if x==l and y==k and u==j and v==i]
        assert reverses, (i,j,k,l)
        assert r*p[i]*p[j]==sum(reverses)*p[l]*p[k], (i,j,k,l)
    rb=(p[1]+2*p[3]+p[5])/2
    rr=(p[2]+2*p[4]+p[5])/2
    if lam>0: assert p[5]<2*rb*rr
    else: assert p[5]==2*rb*rr
    count+=1

# Exactly conservation-preserving interior perturbation; entropy production <0.
p=equilibrium(F(2,3),F(3,4),F(3,2),F(5))
p[0]-=F(1,100); p[1]+=F(2,100); p[3]-=F(1,100)
q=equilibrium(F(2,3),F(3,4),F(3,2),F(5))
assert min(p)>0
assert sum(p)==1
assert sum(ST[i][0]*p[i] for i in range(6))==sum(ST[i][0]*q[i] for i in range(6))
assert sum(ST[i][1]*p[i] for i in range(6))==sum(ST[i][1]*q[i] for i in range(6))
D=sum(float(derivative(p,F(3,2),F(5))[i])*log(float(p[i]/q[i])) for i in range(6))
assert D<0
print(f"PASS: {count} exact parameter grids; {count*len(events(F(1),F(1)))} oriented flux comparisons; exact ODE residuals, invariant masses, strict anti-mixing and entropy dissipation.")
