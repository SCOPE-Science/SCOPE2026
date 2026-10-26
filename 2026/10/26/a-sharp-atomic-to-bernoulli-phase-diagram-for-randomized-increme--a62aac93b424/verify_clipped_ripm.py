"""Exact rational regression checks for clipped randomized incremental proximal dynamics.

The mathematical proof is independent of these finite tests.
Run: python verify_clipped_ripm.py
"""
from fractions import Fraction as F
from itertools import product
import random

checks = 0

def check(ok):
    global checks
    assert ok
    checks += 1

def prox_center(z, a, gamma):
    # Minimizes gamma*|v-a| + (v-z)**2/2 by direct subgradient cases.
    if z < a-gamma:
        return z+gamma
    if z > a+gamma:
        return z-gamma
    return a

def maps(x,r,c,a):
    return (min(a,r*x+c),max(-a,r*x-c))

# Derive the two clipped maps from the exact individual proximal definition,
# including all kink and boundary cases.
for rr in [F(i,12) for i in range(1,12)]:
    for cc in [F(j,5) for j in range(1,8)]:
        for aa in [F(k,6) for k in range(1,17)]:
            for x in [aa*F(t,7) for t in range(-7,8)]:
                z=rr*x
                expected=maps(x,rr,cc,aa)
                measured=(prox_center(z,aa,cc),prox_center(z,-aa,cc))
                check(expected==measured)
                check(-aa<=expected[0]<=aa and -aa<=expected[1]<=aa)
                # Lipschitz bound against left endpoint for both maps.
                y=-aa
                f_x=maps(x,rr,cc,aa)
                f_y=maps(y,rr,cc,aa)
                check(all(abs(f_x[j]-f_y[j])<=rr*abs(x-y) for j in range(2)))

# Exact sharp reset time, boundary collapse and infinite chain of atoms.
for rr in [F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(9,10)]:
    cc=F(1,2)
    bb=cc/(1-rr)
    ss=cc/(1+rr)
    cases=[ss/F(2),ss,(ss+bb)/2,(3*ss+bb)/4,(ss+3*bb)/4,bb,2*bb]
    for aa in cases:
        tp=lambda x:maps(x,rr,cc,aa)[0]
        tm=lambda x:maps(x,rr,cc,aa)[1]
        if aa<=ss:
            for x in [-aa,-aa/2,F(0),aa/2,aa]:
                check(tp(x)==aa and tm(x)==-aa)
        if aa<bb:
            q=F(1)
            N=0
            while q>(bb-aa)/(bb+aa):
                q*=rr
                N+=1
            check(N>=1)
            for x in [-aa,-aa/2,F(0),aa/2,aa]:
                y=x
                for _ in range(N):y=tp(y)
                check(y==aa)
                y=x
                for _ in range(N):y=tm(y)
                check(y==-aa)
            y=-aa
            for _ in range(N-1):y=tp(y)
            check(y<aa)
            if aa>ss:
                y=aa
                for n in range(1,21):
                    y=tp(tm(y))
                    check(y==ss+rr**(2*n)*(aa-ss))
                    check(ss<y<aa)
        else:
            for x in [-aa,-bb,F(0),bb,aa]:
                check(tp(x)==rr*x+cc and tm(x)==rr*x-cc)
            # Moments of the untruncated Bernoulli convolution, finite prefix.
            for n in range(1,9):
                vals=[]
                for choices in product([-1,1],repeat=n):
                    x=F(0)
                    for sign in choices:
                        x=rr*x+sign*cc
                    vals.append(x)
                mean=sum(vals,F(0))/len(vals)
                var=sum((x-mean)**2 for x in vals)/len(vals)
                check(mean==0)
                check(var==cc**2*(1-rr**(2*n))/(1-rr**2))

# A direct Monte Carlo check in each qualitatively distinct phase.
random.seed(630921)
for rr,cc,aa in [(F(1,2),F(1,2),F(1,4)),
                 (F(1,2),F(1,2),F(1,2)),
                 (F(1,3),F(2,3),F(3)),
                 (F(1,2),F(1),F(2)),
                 (F(3,4),F(1,2),F(3))]:
    x=0.0
    for k in range(15000):
        z=float(rr)*x
        sign=1 if random.getrandbits(1) else -1
        x=min(float(aa),z+float(cc)) if sign==1 else max(-float(aa),z-float(cc))
        check(-float(aa)-1e-12<=x<=float(aa)+1e-12)

print(f"PASS: {checks} exact-rational and finite numerical assertions")
