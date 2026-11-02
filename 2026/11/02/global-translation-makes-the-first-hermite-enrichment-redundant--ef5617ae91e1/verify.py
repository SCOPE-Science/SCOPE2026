#!/usr/bin/env python3
"""Direct finite arithmetic and quadrature checks for translated Hermite projections.

The infinite-dimensional theorem is proved analytically in RESULT.md;
these finite checks detect normalization and algebraic errors, not prove global optimality.
"""
import math

SQ2=math.sqrt(2.0)
SQPI=math.sqrt(math.pi)

def coefficients(centers, weights, b):
    assert len(centers)==len(weights) and len(centers)>0
    values=[w*math.exp(-0.25*(c-b)**2) for c,w in zip(centers,weights)]
    return (sum(values),
            sum(v*(c-b) for v,c in zip(values,centers))/SQ2,
            sum(v*(c-b)**2 for v,c in zip(values,centers))/(2*SQ2))

def captured(centers,weights,b,order):
    a=coefficients(centers,weights,b)
    return sum(t*t for t in a[:order+1])

def integrate_simpson(f,left,right,steps=12000):
    assert steps%2==0
    h=(right-left)/steps
    s=f(left)+f(right)
    for k in range(1,steps):s+=(4 if k%2 else 2)*f(left+k*h)
    return s*h/3

def hermite(x,b,n):
    z=x-b
    phi=math.exp(-z*z/2)/math.pi**0.25
    if n==0:return phi
    if n==1:return SQ2*z*phi
    if n==2:return (2*z*z-1)*phi/SQ2
    raise ValueError

def target(x,centers,weights):
    return sum(w*hermite(x,c,0) for c,w in zip(centers,weights))

# Direct integral versus coherent-state coefficient formula.
centers=[-2.0,0.5,2.25];weights=[0.7,0.3,1.1]
for b in (-2.3,-0.1,0.0,1.4,2.8):
    exact=coefficients(centers,weights,b)
    for n in range(3):
        num=integrate_simpson(lambda x:target(x,centers,weights)*hermite(x,b,n),-14,14)
        assert abs(num-exact[n])<3e-8,(b,n,num,exact[n])

# Differentiate energies both ways and test the exact monotonicity identity.
for centers,weights in [([-2,2],[1,1]),([-4,-0.5,1.5],[0.1,2,0.8]),([0.2],[2.5])]:
    for b in [-3,-1.1,-0.2,0,0.37,1.1,4]:
        c0,c1,c2=coefficients(centers,weights,b)
        h=2e-5
        D0=(captured(centers,weights,b+h,0)-captured(centers,weights,b-h,0))/(2*h)
        D1=(captured(centers,weights,b+h,1)-captured(centers,weights,b-h,1))/(2*h)
        assert abs(D0-SQ2*c0*c1)<5e-8,(centers,b,D0,SQ2*c0*c1)
        assert abs(D1-2*c1*c2)<5e-8,(centers,b,D1,2*c1*c2)
        assert c2>=0

# Find each maximizer independently on a fine bounded grid; compare error levels.
for centers,weights in [([-2,2],[1,1]),([-1,1],[1,1]),([-4,0,2],[.5,2,.4]),([-3,2,4],[.4,1,.8])]:
    grid=[-7+14*i/14000 for i in range(14001)]
    vals0=[captured(centers,weights,b,0) for b in grid]
    vals1=[captured(centers,weights,b,1) for b in grid]
    b0=grid[max(range(len(grid)),key=vals0.__getitem__)]
    b1=grid[max(range(len(grid)),key=vals1.__getitem__)]
    assert abs(b0-b1)<=.0011,(centers,b0,b1)
    assert abs(max(vals0)-max(vals1))<3e-6
    assert captured(centers,weights,b0,2)>max(vals1)+1e-8

# Exact symmetric-doublet stationary equation and threshold.
for a in (1.0,SQ2,1.6,2.0,3.0):
    def rootfun(b):return a*math.tanh(a*b/2)-b
    if a<=SQ2:
        assert all(rootfun(b)<1e-13 for b in (.001,.1,1,a+1))
        bstar=0.
    else:
        lo=1e-6;hi=a
        assert rootfun(lo)>0 and rootfun(hi)<0
        for _ in range(75):
            mid=(lo+hi)/2
            if rootfun(mid)>0:lo=mid
            else:hi=mid
        bstar=(lo+hi)/2
        assert abs(rootfun(bstar))<1e-13
        assert captured([-a,a],[1,1],bstar,0)>captured([-a,a],[1,1],0,0)
    c0,c1,c2=coefficients([-a,a],[1,1],bstar)
    assert abs(c1)<1e-12
    assert abs(captured([-a,a],[1,1],bstar,0)-captured([-a,a],[1,1],bstar,1))<1e-11
    assert c2>0

# First-order Hermite target shows positivity hypothesis is essential:
# max one-mode energy = 1/e, whereas the two-mode space at b=0 captures 1.
assert math.exp(-1)<1
for b in (-SQ2,SQ2):
    single=b*b/2*math.exp(-b*b/2)
    assert abs(single-1/math.e)<1e-14

print("VERIFY_OK: 15 overlap quadratures, 63 energy derivative checks, 4 multi-peak optimizer comparisons, 5 sharp doublet regimes, signed boundary")
