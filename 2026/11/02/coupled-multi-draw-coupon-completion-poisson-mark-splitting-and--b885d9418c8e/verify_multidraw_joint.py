#!/usr/bin/env python3
"""Finite-state and limiting checks for two coupled coupon-collection rules.
Requires only Python 3's standard library; all exact tests use Fraction.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, exp, log

checks=0

def check(pred, reason):
    global checks
    if not pred: raise AssertionError(reason)
    checks+=1

def transitions(n,d,a,b):
    c=n-a-b
    den=comb(n,d)
    for j in range(min(a,d)+1):
        for h in range(min(b,d-j)+1):
            k=d-j-h
            if 0<=k<=c:
                p=Fraction(comb(a,j)*comb(b,h)*comb(c,k),den)
                if p:
                    yield ((a-j,b+j-1) if j+h else (a,b),p)

def count_step(n,d,dist):
    nxt=defaultdict(Fraction)
    for (a,b),p in dist.items():
        for state,weight in transitions(n,d,a,b):
            nxt[state]+=p*weight
    return dict(nxt)

def masks_step(n,d,dist):
    nxt=defaultdict(Fraction)
    for (seen,chosen),p in dist.items():
        for draw in combinations(range(n),d):
            drawmask=sum(1<<i for i in draw)
            unseen_chosen=[i for i in draw if not (chosen>>i)&1]
            # A deterministic tie choice is sufficient: only COUNT dynamics matter.
            select=unseen_chosen[0] if unseen_chosen else None
            new_seen=seen|drawmask
            new_chosen=chosen|(1<<select) if select is not None else chosen
            nxt[(new_seen,new_chosen)]+=p/Fraction(comb(n,d))
    return dict(nxt)

def summary(n,dist):
    out=defaultdict(Fraction)
    for (seen,chosen),p in dist.items():
        a=n-seen.bit_count()
        b=seen.bit_count()-chosen.bit_count()
        out[(a,b)]+=p
    return dict(out)

def u_dist(n,d,t):
    cur=[Fraction(0) for _ in range(n+1)]
    cur[n]=Fraction(1)
    for _ in range(t):
        nxt=[Fraction(0) for _ in range(n+1)]
        for u,p in enumerate(cur):
            if not p:continue
            q=Fraction(comb(n-u,d),comb(n,d)) if n-u>=d else Fraction(0)
            nxt[u]+=p*q
            if u:nxt[u-1]+=p*(1-q)
        cur=nxt
    return cur

def fall(x,k):
    z=1
    for h in range(k):z*=x-h
    return z

def tagged(n,d,t,a,b):
    # Probability a designated set of size a has not been OFFERED and
    # another disjoint designated set of size b has not been SELECTED.
    keep=Fraction(comb(n-a,d),comb(n,d))**t if n-a>=d else Fraction(int(t==0))
    reduced=u_dist(n-a,d,t) if n-a>=d else None
    if reduced is None:return Fraction(0)
    return keep*sum(p*Fraction(fall(u,b),fall(n-a,b)) for u,p in enumerate(reduced))

def first_unseen_and_seen_unselected(n,d,t,a,b):
    # Exact inclusion-exclusion to force the b unselected coupons to have been seen.
    return sum((-1)**j*comb(b,j)*tagged(n,d,t,a+j,b-j) for j in range(b+1))

def moments(n,d,t,a,b):
    cur={(n,0):Fraction(1)}
    for _ in range(t):cur=count_step(n,d,cur)
    return sum(p*fall(i,a)*fall(j,b) for (i,j),p in cur.items())

@lru_cache(None)
def tie(n,d,a,b):
    if a==0:return Fraction(int(b==0))
    p0=Fraction(0);out=Fraction(0)
    for (aa,bb),p in transitions(n,d,a,b):
        if (aa,bb)==(a,b):p0+=p
        else:out+=p*tie(n,d,aa,bb)
    return out/(1-p0)

def C_d(d,steps=16000):
    if d==1:return 0.0
    if steps%2:steps+=1
    def f(x):
        if x==0:return (d-1)/(2*d)
        return 1/(-__import__('math').expm1(d*__import__('math').log1p(-x))) -1/(d*x) if x<1 else 1-1/d
    h=1/steps
    return h/3*(f(0)+f(1)+4*sum(f(i*h) for i in range(1,steps,2)) +2*sum(f(i*h) for i in range(2,steps,2)))

def float_distribution(n,d,t):
    states={(n,0):1.0}
    cache={}
    for _ in range(t):
        nxt=defaultdict(float)
        for state,p in states.items():
            if state not in cache:
                cache[state]=[(new,float(q)) for new,q in transitions(n,d,*state)]
            for new,q in cache[state]:nxt[new]+=p*q
        states=nxt
    return states

def finish_probabilities(n,d,t):
    v=[0.]*(n+1);v[0]=1.
    for _ in range(t):
        new=v[:]
        for u in range(1,n+1):
            q=1-(comb(n-u,d)/comb(n,d) if n-u>=d else 0)
            new[u]=(1-q)*v[u]+q*v[u-1]
        v=new
    return v

# Exact count transition check versus explicit coupon masks.
for n in range(3,7):
 for d in range(1,min(n,3)+1):
  counts={(n,0):Fraction(1)};masks={(0,0):Fraction(1)}
  for t in range(6):
   reduced=summary(n,masks)
   check(counts==reduced,('mask/count',n,d,t))
   check(sum(counts.values())==1,('mass',n,d,t))
   counts=count_step(n,d,counts)
   masks=masks_step(n,d,masks)

# Exact marked factorial identities. Includes cases where the mark probability is zero.
for n in range(4,10):
 for d in range(1,min(n-1,3)+1):
  for t in range(0,8):
   counts={(n,0):Fraction(1)}
   for _ in range(t):counts=count_step(n,d,counts)
   for a in range(0,3):
    for b in range(0,3):
     if a+b>n-d:continue
     lhs=sum(p*fall(i,a)*fall(j,b) for (i,j),p in counts.items())
     rhs=fall(n,a+b)*first_unseen_and_seen_unselected(n,d,t,a,b)
     check(lhs==rhs,('tagged moment',n,d,t,a,b,lhs,rhs))

# Independent exact d=2 tie identity (from the finite two-type count recurrence).
for n in range(3,20):
 check(tie(n,2,n,0)==Fraction(n-2,2*n-3),('d=2 tie',n))

# Critical independent-Poisson asymptotic checks (no fitted parameter).
for d in (2,3):
 c=exp(d*C_d(d))
 check(abs(c-({2:2.0,3:4.289652925203735}[d]))<3e-8,('c',d,c))
 for n in (30,60,90):
  x=0.0;y=1.0
  tx=round(n/d*(log(n)+x));ty=round(n/d*(log(n)+y))
  st=float_distribution(n,d,tx)
  q=finish_probabilities(n,d,ty-tx)
  pjoint=sum(p*q[a+b] for (a,b),p in st.items() if a==0)
  p0=sum(p for (a,b),p in st.items() if a==0)
  check(abs(pjoint-exp(-exp(-x)-(c-1)*exp(-y)))<.045,('joint limit',d,n,pjoint))
  check(abs(p0-exp(-exp(-x)))<.07,('all-seen limit',d,n,p0))

print('PASS',checks,'exact and numerical assertions')
for d in (2,3,4):
 c=exp(d*C_d(d))
 print('d=%d C_d=%.12f c_d=%.12f tie_limit=%.12f'%(d,C_d(d),c,1/c))
