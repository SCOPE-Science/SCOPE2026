"""Exact, dependency-free checks for finite multistate noisy q-voter mode theorem.
Run: python check.py  (Python 3.9+)
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial

CHECKS = 0

def require(cond, message):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(message)

def compositions(n,s):
    if s==1:
        yield (n,)
    else:
        for a in range(n+1):
            for tail in compositions(n-a,s-1):
                yield (a,)+tail

def H_table(n,t):
    h=[F(1)]
    for j in range(n):
        h.append(h[-1]*(1+t*j*(j-1)))
    return h

def w_table(n,t):
    h=H_table(n,t)
    return [h[k]/factorial(k) for k in range(n+1)]

def canonical(n,s,k):
    q,r=divmod(n-k,s-1)
    return (k,)+tuple([q+1]*r+[q]*(s-1-r))

def product_weight(arr,w):
    z=F(1)
    for x in arr:z*=w[x]
    return z

def p_to_t(n,s,p):
    return F(s)*(1-p)/(p*(n-1)*(n-2))

def direct_switch_probability(state,position,new_color,p,s):
    if new_color==state[position]:return F(0)
    n=len(state)
    others=[state[j] for j in range(n) if j!=position]
    panel=sum(1 for i in range(n-1) for j in range(i+1,n-1)
              if others[i]==new_color and others[j]==new_color)
    return (p/F(s)+(1-p)*F(panel,comb(n-1,2)))/n

# Exact finite-state detailed balance, calculating the q-panel by independently
# enumerating neighboring unordered pairs rather than using the claimed formula.
for n,s,ps in [(3,3,[F(1,7),F(1,2)]),(4,3,[F(1,5),F(3,5)]),
               (5,3,[F(2,5)]),(6,3,[F(3,7)]),(4,4,[F(1,3)])]:
    for p in ps:
        t=p_to_t(n,s,p)
        H=H_table(n,t)
        for state in product(range(s),repeat=n):
            cnt=[state.count(j) for j in range(s)]
            mass=product_weight(cnt,H)
            for pos in range(n):
                for c in range(s):
                    if c==state[pos]:continue
                    next_state=state[:pos]+(c,)+state[pos+1:]
                    cnt2=[next_state.count(j) for j in range(s)]
                    mass2=product_weight(cnt2,H)
                    forward=direct_switch_probability(state,pos,c,p,s)
                    backward=direct_switch_probability(next_state,pos,state[pos],p,s)
                    require(mass*forward==mass2*backward,
                            ('micro detailed balance',n,s,p,state,pos,c))

# Independently enumerate all finite count compositions and compare their exact
# stationary weights to the one-leader balanced candidate family.
for s in (3,4,5):
    for n in range(3,14):
        if comb(n+s-1,s-1)>3500:continue
        previous_min=None
        for t in (F(0),F(1,100),F(1,25),F(1,10),F(1,5),F(1,4),
                  F(3,10),F(1,2),F(1),F(4),F(40)):
            w=w_table(n,t)
            global_max=max(product_weight(a,w) for a in compositions(n,s))
            candidates=[(k,product_weight(canonical(n,s,k),w))
                        for k in range((n+s-1)//s,n+1)]
            restricted_max=max(z for k,z in candidates)
            require(global_max==restricted_max,('one-leader reduction',n,s,t))
            largest=max(k for k,z in candidates if z==restricted_max)
            if previous_min is not None:
                require(largest>=previous_min,('no mode reentrance',n,s,t))
            previous_min=largest

# q=2,s=3,n=6 exact polynomial numerators; no numeric approximations.
n,s=6,3
for t in (F(0),F(19,100),F(1,5),F(7,25),F(29,100),F(1),F(100)):
    w=w_table(n,t)
    F2=product_weight((2,2,2),w)
    F3=product_weight((3,2,1),w)
    F4=product_weight((4,1,1),w)
    F5=product_weight((5,1,0),w)
    F6=product_weight((6,0,0),w)
    require(F2==F(1,8),('F2',t))
    require(F3==(1+2*t)/12,('F3',t))
    require(F4==(1+2*t)*(1+6*t)/24,('F4',t))
    require(F5==(1+2*t)*(1+6*t)*(1+12*t)/120,('F5',t))
    require(F6==(1+2*t)*(1+6*t)*(1+12*t)*(1+20*t)/720,('F6',t))
    require(F3<max(F2,F4),('skipped k3',t))
    require(F5<max(F4,F6),('skipped k5',t))

# Algebraic root isolation on disjoint rational intervals (unique positive
# roots follow from strict increase of the left polynomial on t>=0).
def P1(t):return 12*t*t+8*t-2
def P2(t):return 240*t*t+32*t-29
require(P1(F(19,100))<0<P1(F(1,5)),'first threshold bracket')
require(P2(F(7,25))<0<P2(F(3,10)),'second threshold bracket')
require(P2(F(1,5))<0,'threshold ordering')
print('PASS',CHECKS,'exact deterministic assertions')
