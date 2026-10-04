#!/usr/bin/env python3
import math

SQRT2=math.sqrt(2.0)
SQRT2PI=math.sqrt(2.0*math.pi)

def Phi(x):
    return 0.5*(1.0+math.erf(x/SQRT2))

def phi(x):
    return math.exp(-0.5*x*x)/SQRT2PI

def simpson(f,a,b,n=200000):
    if n%2: n+=1
    h=(b-a)/n
    s=f(a)+f(b)
    for k in range(1,n):
        s += (4.0 if k%2 else 2.0)*f(a+k*h)
    return s*h/3.0

def coverage(B):
    assert B>=2
    c=math.sqrt(B-2.0)
    val=simpson(lambda u: phi(u)*(Phi(c*u)**B),-10.0,10.0)
    return 1.0-2.0*val

anchors={
    2:0.5,
    3:0.5,
    6:0.45291882956353047,
    10:0.40548979311044375,
    20:0.33768262443956143,
    100:0.1997773730047565,
}
for B,target in anchors.items():
    got=coverage(B)
    if abs(got-target)>2e-8:
        raise SystemExit(f'coverage anchor failed B={B}: {got} vs {target}')

# Samplewise range identity: LOFO_i=(sum(g)-g_i)/(B-1), hence its
# range is exactly range(g)/(B-1).
g=[-1.25,0.1,2.0,0.75,-0.4,1.2]
B=len(g); s=sum(g)
lofo=[(s-x)/(B-1.0) for x in g]
r1=max(lofo)-min(lofo)
r0=max(g)-min(g)
if abs(r1-r0/(B-1.0))>1e-14:
    raise SystemExit('range identity failed')

# The asymptotic leading term is approached from below at these finite B.
for B in (100,1000):
    got=coverage(B)
    lead=2.0*math.sqrt(math.log(B)/(math.pi*B))
    ratio=got/lead
    if not (0.80 < ratio < 0.95):
        raise SystemExit(f'asymptotic sanity failed B={B}, ratio={ratio}')

# Independent symmetric fold means have hull coverage 1-2^(1-B).
if abs((1.0-2.0**(1-6))-0.96875)>1e-15:
    raise SystemExit('independent-hull anchor failed')
print('VERIFY_OK')
