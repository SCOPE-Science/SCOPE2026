#!/usr/bin/env python3
"""Self-contained finite checks for an exact capped-simplex flow/projection comparison.
Finite checks corroborate but do not replace the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def clip(z): return max(F(0),min(F(1),z))
def project(y,s):
    for status in product('LFU',repeat=len(y)):
        ix=[i for i,k in enumerate(status) if k=='F']
        if not ix: continue
        lam=(sum(y[i] for i in ix)+sum(k=='U' for k in status)-s)/len(ix)
        z=[clip(y[i]-lam) for i in range(len(y))]
        if sum(z)==s and all((z[i]==0 if k=='L' else z[i]==1 if k=='U' else F(0)<z[i]<F(1)) for i,k in enumerate(status)):
            return tuple(z)
    # Handle end-point ties by clipped bisection over breakpoints.
    levels=sorted([v for q in y for v in (q,q-1)])
    for lo,hi in zip(levels[:-1],levels[1:]):
        m=(lo+hi)/2
        ids=[i for i,v in enumerate(y) if 0<v-m<1]
        if not ids: continue
        count_upper=sum(v-m>=1 for v in y)
        lam=(sum(y[i] for i in ids)+count_upper-s)/len(ids)
        z=tuple(clip(v-lam) for v in y)
        if sum(z)==s: return z
    raise AssertionError((y,s))

def state(p,b,a,H,t,which):
    tg=2*b/H
    tp=b/a
    start=tg if which=='flow' else tp
    finish=start+2*(1-p-b)/a
    if t<=tg:
        return (p+H*t/2,F(1),b-H*t/2)
    if which=='projection' and t<=tp:
        return (p+b,F(1),F(0))
    if t<=finish:
        z=min(1-p-b,max(F(0),a*(t-start)/2))
        return (p+b+z,F(1)-z,F(0))
    return (F(1),p+b,F(0))

def truth_max(p,b,a,H): return min(b*(1-2*a/H)/2,1-p-b)

rng=Random(34)
checks=0
for _ in range(500):
    a=F(rng.randint(1,6),rng.randint(1,6))
    H=a*F(rng.randint(21,100),10)
    p=F(rng.randint(1,8),20)
    b=F(rng.randint(1,8),20)
    if p+b>=1: continue
    s=1+p+b
    tg=2*b/H;tp=b/a
    tf=tg+2*(1-p-b)/a;tfp=tp+2*(1-p-b)/a
    times=[F(0),tg/2,tg,(tg+tp)/2,tp,tf,tfp,max(tf,tfp)+1]
    times+=[F(rng.randrange(200),100)*max(tfp,tf) for i in range(5)]
    for t in times:
        z=state(p,b,a,H,t,'projection')
        assert project((p,1-a*t,b-H*t),s)==z,(p,b,a,H,t,z)
        g=state(p,b,a,H,t,'flow')
        assert sum(g)==s and all(0<=v<=1 for v in g)
        error=max(abs(g[i]-z[i]) for i in range(3))
        assert error<=truth_max(p,b,a,H)
        checks+=1
    # Verify the exact maximum is attained at the earlier of the onset or completion of the flow ramp.
    tstar=min(tp,tf)
    assert max(abs(state(p,b,a,H,tstar,'flow')[j]-state(p,b,a,H,tstar,'projection')[j]) for j in range(3)) == truth_max(p,b,a,H)
    checks+=1

# Discretized tangent gradient flow: iterate a local projection rather than
# projecting the cumulative unconstrained ray. Exact-rational calculation.
p=b=F(1,4);a=F(1);H=F(8);s=1+p+b;h=F(1,1024)
x=(p,F(1),b)
for k in range(128):
    x=project(tuple(xi-h*ci for xi,ci in zip(x,(0,a,H))),s)
assert x==state(p,b,a,H,F(1,8),'flow'),(x,state(p,b,a,H,F(1,8),'flow'))
assert x!=state(p,b,a,H,F(1,8),'projection')
assert truth_max(p,b,a,H)==F(3,32)
checks+=3

# Limiting sharpness 1/3 of the natural three-site family.
for n in (10,100,1000,10000):
    p=F(1,n+10);b=F(2,3);a=F(1);H=F(n)
    err=truth_max(p,b,a,H)
    assert err<=F(1,3)
    if n==10000: assert abs(err-F(1,3))<F(1,1000)
    checks+=1
print('VERIFY_OK',checks,'exact-rational comparisons')

# In two cells the feasible set is an interval, so one-step ray projection
# and projected tangent-cone dynamics coincide; test across exact rational data.
for _ in range(300):
    s=F(rng.randrange(1,39),20)
    lo=max(F(0),s-1);hi=min(F(1),s)
    t=F(rng.randrange(0,60),10)
    x=lo+(hi-lo)*F(rng.randrange(0,101),100)
    ca=F(rng.randrange(-20,21),7);cb=F(rng.randrange(-20,21),7)
    speed=(cb-ca)/2
    truth=(min(hi,max(lo,x+t*speed)),)
    z=project((x-t*ca,s-x-t*cb),s)
    assert z[0]==truth[0] and z[1]==s-truth[0]
    checks+=1
print('VERIFY_2CELL_OK',300,'exact-rational comparisons')
