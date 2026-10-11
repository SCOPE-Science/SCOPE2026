#!/usr/bin/env python3
import math, random

def kappa(n):
    return math.pi**(n/2)/math.gamma(n/2+1)

def f(d,t):
    return max(0.0,1-t*t)**((d-1)/2)

def simpson(fun,a,b,n=20000):
    if a==b: return 0.0
    if n%2: n+=1
    h=(b-a)/n
    s=fun(a)+fun(b)
    for i in range(1,n):
        s += (4 if i%2 else 2)*fun(a+i*h)
    return s*h/3

def centered(d,W):
    a=W/2
    return kappa(d-1)*simpson(lambda t:f(d,t),-a,a,6000)

def merge(intervals):
    xs=[]
    for a,b in intervals:
        a=max(-1.0,a); b=min(1.0,b)
        if b>a: xs.append((a,b))
    xs.sort()
    out=[]
    for a,b in xs:
        if out and a<=out[-1][1]: out[-1]=(out[-1][0],max(out[-1][1],b))
        else: out.append((a,b))
    return out

def volume(d, intervals):
    return kappa(d-1)*sum(simpson(lambda t:f(d,t),a,b,1200) for a,b in merge(intervals))

# Exact low-dimensional formulas.
for W in [0.1,0.4,0.9,1.3,1.8]:
    a=W/2
    c2=W*math.sqrt(1-W*W/4)+2*math.asin(W/2)
    c3=math.pi*(W-W**3/12)
    assert abs(centered(2,W)-c2)<2e-9
    assert abs(centered(3,W)-c3)<2e-9

# Ball-volume normalization: integrating the whole slice density gives kappa_d.
for d in range(2,11):
    full=kappa(d-1)*simpson(lambda t:f(d,t),-1,1,10000)
    assert abs(full-kappa(d))<1e-6*max(1,kappa(d))

# Random parallel-plank interval unions never beat the centered interval of total width.
rng=random.Random(20261007)
worst=0.0
for d in range(2,9):
    for _ in range(250):
        n=rng.randint(1,8)
        widths=[rng.random()*0.22 for __ in range(n)]
        W=sum(widths)
        if W>=1.9:
            widths=[w*1.8/W for w in widths]; W=sum(widths)
        intervals=[]
        for w in widths:
            c=rng.uniform(-1.15,1.15)
            intervals.append((c-w/2,c+w/2))
        got=volume(d,intervals)
        opt=centered(d,W)
        worst=max(worst,got-opt)
        assert got<=opt+2e-8

# Sharp layer-swap stability equality.
max_stab_err=0.0
for d in range(2,9):
    for W in [0.4,0.9,1.4,1.8]:
        a=W/2
        cap=min(W,2-W)
        for frac in [0.1,0.35,0.7,1.0]:
            delta=cap*frac
            E=[(-a-delta/2,-a),(-a+delta/2,a-delta/2),(a,a+delta/2)]
            deficit=centered(d,W)-volume(d,E)
            rhs=2*kappa(d-1)*(simpson(lambda t:f(d,t),a-delta/2,a,4000)-simpson(lambda t:f(d,t),a,a+delta/2,4000))
            max_stab_err=max(max_stab_err,abs(deficit-rhs))
            assert abs(deficit-rhs)<3e-6

print('VERIFY_OK')
print('slice_normalization = passed')
print('random_parallel_families = passed')
print('sharp_layer_swap_stability = passed')
print('worst_random_excess = %.3e' % worst)
print('max_stability_error = %.3e' % max_stab_err)
