#!/usr/bin/env python3
"""Independent finite-state and algebraic checks for tripartite random-edge matching."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from random import Random
import math

assertions=0

def check(condition, msg):
    global assertions
    assertions+=1
    if not condition:
        raise AssertionError(msg)

@lru_cache(None)
def size_pmf(a,b,c):
    """Exact law of (AB,AC,BC) match counts from aggregate state."""
    total=a*b+a*c+b*c
    if not total:
        return {(0,0,0): Fraction(1)}
    out=defaultdict(Fraction)
    for w,ab,ac,bc, delta in [(a*b,1,0,0,(a-1,b-1,c)),
                                (a*c,0,1,0,(a-1,b,c-1)),
                                (b*c,0,0,1,(a,b-1,c-1))]:
        if not w: continue
        for nums,p in size_pmf(*delta).items():
            t=(nums[0]+ab,nums[1]+ac,nums[2]+bc)
            out[t]+=Fraction(w,total)*p
    return dict(out)

@lru_cache(None)
def labeled_pmf(mask,group):
    """Independent labeled graph edge enumeration, no aggregate transition weights."""
    vertices=[v for v in range(len(group)) if mask & (1<<v)]
    edges=[(i,j) for i,j in combinations(vertices,2) if group[i]!=group[j]]
    if not edges:
        return {(0,0,0):Fraction(1)}
    out=defaultdict(Fraction)
    for i,j in edges:
        m2=mask & ~(1<<i) & ~(1<<j)
        k=(min(group[i],group[j]),max(group[i],group[j]))
        idx={(0,1):0,(0,2):1,(1,2):2}[k]
        for nums,p in labeled_pmf(m2,group).items():
            res=list(nums);res[idx]+=1
            out[tuple(res)]+=p/Fraction(len(edges))
    return dict(out)

for a in range(0,4):
 for b in range(0,4):
  for c in range(0,4):
    pmf=size_pmf(a,b,c)
    check(sum(pmf.values())==1,('normalization',a,b,c))
    group=(0,)*a+(1,)*b+(2,)*c
    labeled=labeled_pmf((1<<len(group))-1,group)
    check(pmf==labeled,('labeled agreement',a,b,c))
    for outcome,p in pmf.items():
        unmatched=a+b+c-2*sum(outcome)
        check(unmatched>=0 and p>0,('feasible',a,b,c,outcome))
        check(unmatched==0 or max(a-outcome[0]-outcome[1], b-outcome[0]-outcome[2], c-outcome[1]-outcome[2])==unmatched,('terminal one part',a,b,c,outcome))

# Exact multivariate polynomial identities in (a,b,c,u), no external libraries.
from collections import defaultdict as _dd
ZP=(0,0,0,0)

def monomial(coef, exp):
    return {exp:Fraction(coef)} if coef else {}

def padd(*terms):
    out=_dd(Fraction)
    for term in terms:
        for e,v in term.items():out[e]+=v
    return {e:v for e,v in out.items() if v}

def pneg(term):return {e:-v for e,v in term.items()}

def pmul(*terms):
    out=monomial(1,ZP)
    for term in terms:
        new=_dd(Fraction)
        for i,vi in out.items():
            for j,vj in term.items():new[tuple(x+y for x,y in zip(i,j))]+=vi*vj
        out={e:v for e,v in new.items() if v}
    return out

def pdu(term):
    return {e[:3]+(e[3]-1,):v*e[3] for e,v in term.items() if e[3]}

one=monomial(1,ZP)
a=monomial(1,(1,0,0,0));b=monomial(1,(0,1,0,0))
c=monomial(1,(0,0,1,0));u=monomial(1,(0,0,0,1))
A=padd(one,pneg(pmul(a,u)))
B=padd(one,pneg(pmul(b,u)))
C=padd(one,pneg(pmul(c,u)))
Q=pmul(A,B,C)
X=pmul(a,B,C);Y=pmul(b,A,C);Z=pmul(c,A,B)
for v,other in [(X,padd(Y,Z)),(Y,padd(X,Z)),(Z,padd(X,Y))]:
    check(padd(pmul(pdu(v),Q),pmul(v,other))=={},'symbolic ODE')
for prod,expected in [
    (pmul(X,Y),pmul(Q,a,b,C)),
    (pmul(X,Z),pmul(Q,a,c,B)),
    (pmul(Y,Z),pmul(Q,b,c,A)),
]:
    check(padd(prod,pneg(expected))=={},'symbolic rate identity')
for aa in range(1,8):
 for bb in range(1,aa+1):
  for cc in range(1,bb+1):
   a0,b0,c0=Fraction(aa),Fraction(bb),Fraction(cc)
   # Integrals of ab(1-cu), ac(1-bu), bc(1-au)
   check(a0*b0*(1/a0-c0/(2*a0*a0))==b0*(1-c0/(2*a0)),'AB integral')
   check(a0*c0*(1/a0-b0/(2*a0*a0))==c0*(1-b0/(2*a0)),'AC integral')
   check(b0*c0*(1/a0-1/(2*a0))==b0*c0/(2*a0),'BC integral')
   check(a0*(1-b0/a0)*(1-c0/a0)==(a0-b0)*(a0-c0)/a0,'terminal')

# Exact rational algebraic minimization: normalized b=x*a,c=y*a.
for m in range(2,25):
 for j in range(1,m+1):
  for k in range(1,j+1):
   x=Fraction(j,m);y=Fraction(k,m);s=x+y
   U=(1-x)*(1-y)
   matched=Fraction(1,2)*(1+s-U)
   opt=min(Fraction(1+s,2),s)
   check(matched/opt>=Fraction(7,8),('ratio lower bound',x,y))
check(Fraction(7,8)==(Fraction(1,1)+Fraction(1,1)-Fraction(1,4))/2,'sharp witness')

rng=Random(532817)
def sample(a,b,c):
    sizes=[a,b,c];typ=[0,0,0]
    while True:
        w=[sizes[0]*sizes[1],sizes[0]*sizes[2],sizes[1]*sizes[2]]
        total=sum(w)
        if not total: break
        pick=rng.randrange(total)
        t=0 if pick<w[0] else (1 if pick<w[0]+w[1] else 2)
        i,j=[(0,1),(0,2),(1,2)][t]
        sizes[i]-=1;sizes[j]-=1;typ[t]+=1
    return sizes,typ

for (a,b,c) in [(2000,1000,1000),(1800,1000,500),(1500,1500,500)]:
   trials=80
   samplecounts=[sample(a,b,c)[1] for _ in range(trials)]
   avg=[sum(v[i] for v in samplecounts)/trials for i in range(3)]
   targets=[b*(1-c/(2*a)),c*(1-b/(2*a)),b*c/(2*a)]
   for i in range(3):
      check(abs(avg[i]-targets[i])<80,('simulation diagnostic',a,b,c,i,avg,targets))
print(f'PASS {assertions} exact and symbolic assertions plus bounded Monte Carlo diagnostics; finite tests are not asymptotic proofs.')
