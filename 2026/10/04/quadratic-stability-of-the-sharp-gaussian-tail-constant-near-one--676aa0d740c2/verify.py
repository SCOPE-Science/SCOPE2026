import math
from itertools import product

SQRT3 = math.sqrt(3.0)
SQRT2PI = math.sqrt(2.0 * math.pi)

def phi(x):
    return math.exp(-0.5*x*x)/SQRT2PI

def barphi(x):
    return 0.5*math.erfc(x/math.sqrt(2.0))

def Q(t):
    return 2.0*barphi(SQRT3*t)

def h(t):
    return barphi(SQRT3*t)/(SQRT3*phi(SQRT3*t))

def bisect(fun, lo, hi, it=120):
    flo, fhi = fun(lo), fun(hi)
    assert flo*fhi <= 0.0
    for _ in range(it):
        mid=(lo+hi)/2.0
        fm=fun(mid)
        if flo*fm <= 0.0:
            hi=mid; fhi=fm
        else:
            lo=mid; flo=fm
    return (lo+hi)/2.0

def tail_weighted_uniform(t, weights):
    # Exact inclusion-exclusion CDF formula for a finite sum of independent uniforms.
    w=[abs(float(x)) for x in weights]
    n=len(w)
    L=[2.0*x for x in w]
    W=sum(w)
    x=W+t
    den=math.factorial(n)
    for ell in L:
        den*=ell
    total=0.0
    for bits in product((0,1), repeat=n):
        shift=sum(ell*b for ell,b in zip(L,bits))
        z=x-shift
        if z>0.0:
            total += (-1.0 if sum(bits)%2 else 1.0)*(z**n)
    F=total/den
    return min(1.0,max(0.0,2.0*(1.0-F)))

def golden_max(fun, lo, hi, it=100):
    gr=(math.sqrt(5.0)-1.0)/2.0
    x1=hi-gr*(hi-lo); x2=lo+gr*(hi-lo)
    f1=fun(x1); f2=fun(x2)
    for _ in range(it):
        if f1 < f2:
            lo=x1; x1=x2; f1=f2; x2=lo+gr*(hi-lo); f2=fun(x2)
        else:
            hi=x2; x2=x1; f2=f1; x1=hi-gr*(hi-lo); f1=fun(x1)
    x=(lo+hi)/2.0
    return x,fun(x)

t0=bisect(lambda t:(1.0-t)-h(t), 0.5,0.8)
Cstar=(1.0-t0)/Q(t0)
kappa=t0/(2.0*Q(t0))
shift=1.0/(6.0*t0*(1.0-t0))

assert abs(t0-0.6429083350319992) < 2e-14
assert abs(Cstar-1.3451182120491874) < 2e-14
assert abs(kappa-1.2108763588856896) < 3e-14
assert abs(shift-0.7259721828638811) < 3e-14

# Check h'(t)=3 t h(t)-1 numerically at several points.
for t in (0.2,0.5,t0,0.8):
    eps=1e-6
    num=(h(t+eps)-h(t-eps))/(2*eps)
    rhs=3.0*t*h(t)-1.0
    assert abs(num-rhs) < 2e-8

# Exact finite-sum stress cases. In each case the optimizer lies in the dominant-uniform plateau,
# where the theorem predicts dependence only on a1, not on how the residual l2 mass is split.
cases=[[0.04,0.03],[0.05,0.02,0.01],[0.08,0.06],[0.10,0.05,0.03]]
for rest in cases:
    eps2=sum(x*x for x in rest)
    a1=math.sqrt(1.0-eps2)
    weights=[a1]+rest
    ta=bisect(lambda t:t+h(t)-a1,0.4,0.8)
    predicted=(a1-ta)/(a1*Q(ta))
    assert ta < a1-sum(rest)
    xmax=sum(weights)
    # global search by dense partition + local golden refinement
    grid=[xmax*j/4000.0 for j in range(4000)]
    vals=[tail_weighted_uniform(t,weights)/Q(t) for t in grid]
    j=max(range(len(vals)),key=vals.__getitem__)
    lo=grid[max(0,j-4)]; hi=grid[min(len(grid)-1,j+4)]
    tn,kn=golden_max(lambda t:tail_weighted_uniform(t,weights)/Q(t),lo,hi)
    assert abs(kn-predicted) < 2e-9
    assert abs(tn-ta) < 2e-6

# Second-order coefficients from a small perturbation.
for b in (0.02,0.01,0.005):
    a1=math.sqrt(1.0-b*b)
    ta=bisect(lambda t:t+h(t)-a1,0.5,0.75)
    Ka=(a1-ta)/(a1*Q(ta))
    assert abs((Cstar-Ka)/(b*b)-kappa) < 6e-4
    assert abs((t0-ta)/(b*b)-shift) < 6e-4

print('VERIFY_OK')
print('t0=%.16f' % t0)
print('Cstar=%.16f' % Cstar)
print('kappa=%.16f' % kappa)
print('threshold_shift_coefficient=%.16f' % shift)
