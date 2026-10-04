#!/usr/bin/env python3
import math
from fractions import Fraction

P0 = 2.0/5.0
P1 = 3.0/5.0
ALPHA = 1.0/20.0
T = 30
ELL = math.log(1.0/ALPHA)
R1 = P1/P0
R0 = (1.0-P1)/(1.0-P0)
DELTA = math.log(R1/R0)


def kappa(beta):
    return math.log(P0*R1**beta + (1.0-P0)*R0**beta)


def kappa_prime(beta):
    a = P0*R1**beta
    b = (1.0-P0)*R0**beta
    return (a*math.log(R1) + b*math.log(R0))/(a+b)


def g(beta):
    return beta*kappa_prime(beta) - kappa(beta)


def q(beta, s):
    return (ELL + s*kappa(beta) - beta*s*math.log(R0))/(beta*DELTA)


def beta_minimum(s):
    target = ELL/s
    if target >= -math.log(P0):
        return None
    lo, hi = 1e-12, 1.0
    while g(hi) < target:
        hi *= 2.0
    for _ in range(160):
        mid = (lo+hi)/2.0
        if g(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0


def bisect_level(s, level, lo, hi, descending):
    for _ in range(180):
        mid = (lo+hi)/2.0
        value = q(mid, s)-level
        if descending:
            if value > 0.0:
                lo = mid
            else:
                hi = mid
        else:
            if value < 0.0:
                lo = mid
            else:
                hi = mid
    root=(lo+hi)/2.0
    assert abs(q(root,s)-level) < 2e-11
    return root


def effective_boundary(beta):
    out=[]
    for s in range(1,T+1):
        # Roots are kept away from cell sample points; tiny tolerance only prevents
        # accidental upward rounding from floating representation.
        m=math.ceil(q(beta,s)-1e-12)
        out.append(min(s+1,m))
    return tuple(out)


def survival(boundary):
    p=Fraction(3,5)
    dp={0:Fraction(1,1)}
    for s,m in enumerate(boundary,1):
        nd={}
        for j,prob in dp.items():
            if j < m:
                nd[j]=nd.get(j,Fraction(0,1))+prob*(1-p)
            if j+1 < m:
                nd[j+1]=nd.get(j+1,Fraction(0,1))+prob*p
        dp=nd
    return sum(dp.values(),Fraction(0,1))

# Analytically, q_s has at most one minimum. Enumerate every effective integer
# crossing. For s with no finite minimum, q_s decreases to s from above, so its
# effective boundary is always s+1 and it creates no effective crossing.
critical=[]
for s in range(1,T+1):
    bm=beta_minimum(s)
    if bm is None:
        continue
    qmin=q(bm,s)
    for level in range(math.floor(qmin)+1, s+1):
        if qmin >= level:
            continue
        left=bisect_level(s,level,1e-12,bm,True)
        critical.append((left,s,level,'left'))
        if level < s:
            lo=bm
            hi=max(1.0,2.0*bm)
            while q(hi,s) < level:
                hi*=2.0
            right=bisect_level(s,level,lo,hi,False)
            critical.append((right,s,level,'right'))

critical.sort()
roots=[x[0] for x in critical]
assert min(b-a for a,b in zip(roots,roots[1:])) > 1e-8

# Evaluate every open cell. The event is constant on a cell; endpoint inclusion
# is handled after identifying the minimizing adjacent roots.
bounds=[0.0]+roots+[math.inf]
records=[]
for a,b in zip(bounds,bounds[1:]):
    x=b/2.0 if a==0.0 else (a*2.0 if math.isinf(b) else (a+b)/2.0)
    bd=effective_boundary(x)
    records.append((a,b,survival(bd),bd))

best=min(r[2] for r in records)
best_cells=[r for r in records if r[2]==best]
assert len(best_cells)==1
left,right,best_prob,best_bd=best_cells[0]

EXPECTED=Fraction(424022988283968360448,931322574615478515625)
assert best_prob==EXPECTED
assert abs(left-1.4377067867164328) < 2e-13
assert abs(right-1.5201316458803258) < 2e-13

left_info=[x for x in critical if abs(x[0]-left)<1e-12]
right_info=[x for x in critical if abs(x[0]-right)<1e-12]
assert any(s==10 and level==8 and side=='left' for _,s,level,side in left_info)
assert any(s==21 and level==14 and side=='right' for _,s,level,side in right_info)
assert abs(q(left,10)-8.0)<2e-11
assert abs(q(right,21)-14.0)<2e-11

# Endpoints have the same effective event because the rejection inequality is >=
# and ceil(q) equals the interior boundary at these roots.
assert survival(effective_boundary(left*(1+2e-13)))==EXPECTED
assert survival(effective_boundary(right*(1-2e-13)))==EXPECTED

# Smooth stationary point: g(beta)=ell/T.
lo,hi=1e-12,4.0
target=ELL/T
for _ in range(180):
    mid=(lo+hi)/2.0
    if g(mid)<target:
        lo=mid
    else:
        hi=mid
beta_smooth=(lo+hi)/2.0
assert abs(beta_smooth-1.1136398811625186)<2e-14
smooth_prob=survival(effective_boundary(beta_smooth))
assert smooth_prob==Fraction(448493759336008032256,931322574615478515625)
assert smooth_prob>best_prob

lr_prob=survival(effective_boundary(1.0))
assert lr_prob==Fraction(92343913543124885504,186264514923095703125)
assert lr_prob>smooth_prob>best_prob

print('critical_roots',len(critical))
print('optimizer_interval',repr(left),repr(right))
print('optimum_probability',best_prob,float(best_prob))
print('smooth_beta',repr(beta_smooth))
print('smooth_probability',smooth_prob,float(smooth_prob))
print('likelihood_ratio_probability',lr_prob,float(lr_prob))
print('VERIFY_OK')
