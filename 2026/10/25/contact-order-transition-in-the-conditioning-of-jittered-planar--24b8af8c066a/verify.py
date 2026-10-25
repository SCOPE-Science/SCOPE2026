"""Reproduce algebraic and limiting-constant checks for planar jittered observability."""
import math
import random

rng = random.Random(942171)

def smallest(theta):
    m = len(theta)
    c = sum(math.cos(2*x) for x in theta)
    s = sum(math.sin(2*x) for x in theta)
    return math.sqrt(max(0., (m-math.hypot(c,s))/2.))

def matrix_smallest(theta):
    cc = sum(math.cos(x)**2 for x in theta)
    ss = sum(math.sin(x)**2 for x in theta)
    cs = sum(math.cos(x)*math.sin(x) for x in theta)
    return math.sqrt(max(0.,(cc+ss-math.hypot(cc-ss,2*cs))/2.))

count=0
for m in range(2,9):
    for i in range(300):
        theta=[rng.uniform(-.23,.24) for _ in range(m)]
        assert abs(smallest(theta)-matrix_smallest(theta))<1e-9
        count+=1

# The n=2 cone has exact volume 1.  At contact the probability is
# acos(1-t*t)**2/(8*delta**2), provided acos(1-t*t) < 2*delta.
for delta in (.07,.14):
    for t in (.004,.002,.001):
        h=math.acos(1-t*t)
        assert h<2*delta
        exact=h*h/(8*delta*delta)
        asymp=t*t/(4*delta*delta)
        assert abs(exact/asymp-1)<2e-5

# For overlapping windows at m=2, the exact near-zero probability is
# (-Delta)*acos(1-t*t)/(2*delta**2) for h<min(-Delta,Delta+2delta).
for delta, shift in ((.10,-.06),(.14,-.05)):
    for t in (.002,.001):
        h=math.acos(1-t*t)
        assert h<min(-shift,shift+2*delta)
        exact=(-shift)*h/(2*delta*delta)
        asymp=math.sqrt(2)*(-shift)*t/(2*delta*delta)
        assert abs(exact/asymp-1)<5e-6

# Exact 3D contact cone volume V_{1,2}=sqrt(6)/3, via one-dimensional
# integration of the cross-sectional length after difference coordinates.
def integrand(u): return u*(math.sqrt(max(0.,6.-3.*u*u))-u)
L=math.sqrt(3./2.)
N=100000
h=L/N
integral=(integrand(0)+integrand(L)+4*sum(integrand((2*k-1)*h) for k in range(1,N//2+1))+2*sum(integrand(2*k*h) for k in range(1,N//2)))*h/3
assert abs(integral-math.sqrt(6)/3)<1e-9, integral

# Uniform separation: adding rows increases the Gramian in PSD order.
for a,b in ((1,1),(1,2),(2,2),(1,5)):
    delta=.10
    shift=.04
    bound=math.sqrt(1-math.cos(shift))
    for k in range(1000):
        th=[rng.uniform(-2*delta,0) for _ in range(a)]+[rng.uniform(shift,shift+2*delta) for _ in range(b)]
        assert smallest(th)+1e-10>=bound

print('VERIFY_OK exact Gram spectrum:',count,'samples; contact and overlap exact tails; 3D cone integral; separated bound',sum((1,1,1,1)))
