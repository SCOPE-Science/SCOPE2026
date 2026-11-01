"""Exact-algebra and numerical cross-checks for a neutral flip.

Requires Python >=3.10 and SymPy; run: python verification.py
The finite checks are supplementary, not a proof of global statements.
"""
import math
import sympy as S

b, u, d, a = S.symbols('b u d a', real=True)
s = b * (1 - b)
r = 1 - 3 * s
A = 2*b - 1
B = -(1 - 6*s)/3
C = A*(1 - 12*s)/12
D = -(120*b**4 - 240*b**3 + 150*b**2 - 30*b + 1)/60
p = -u + A*u**2 + B*u**3 + C*u**4 + D*u**5
# Derive Taylor coefficients directly from the exact exponential map.
trunc = S.Poly(u**6, u)
expm1jet = S.Poly(sum(u**k/S.factorial(k) for k in range(1, 6)), u)
ratiojet = S.Poly(0, u)
for k in range(5):
    ratiojet += S.Poly((-b)**k, u) * (expm1jet**(k+1)).rem(trunc)
ratiojet = ratiojet.rem(trunc)
exactjet = S.Poly(u,u)-2*ratiojet
for k, ck in enumerate([0,-1,A,B,C,D]):
    assert S.simplify(exactjet.nth(k)-ck)==0
composed = S.Poly(0, u)
for k, ck in enumerate([0, -1, A, B, C, D]):
    if k:
        composed += S.Poly(ck, u) * (S.Poly(p, u)**k).rem(S.Poly(u**6, u))
assert S.simplify(composed.nth(1)-1) == 0
assert S.simplify(composed.nth(2)) == 0
assert S.simplify(composed.nth(3) + 4*r/3) == 0
assert S.simplify(composed.nth(4) - 2*A*r/3) == 0
assert S.simplify(composed.nth(5) - (3-5*s)/15) == 0
assert S.simplify(S.diff(1/(b*(1-b)), b, 2) - 2/b**3 - 2/(1-b)**3)==0

# At b=1/2, the derived fifth-order coefficient gives the logarithmic term.
gamma0 = S.Rational(1, 3)
eta0 = S.Rational(7, 60)
assert S.simplify((3*gamma0**2-2*eta0)/(2*gamma0)-S.Rational(3,20))==0


def logit(x):
    return math.log(x) - math.log1p(-x)

def fmap(x, aa, bb):
    z = logit(x) - aa*(x-bb)
    return 1/(1+math.exp(-z))

def two_cycle_Q(dd, bb):
    return (logit(bb+dd)-logit(bb-dd))/dd

def critical_map_logit(t, bb):
    h = math.expm1(t)
    return t - 2*h/(1+bb*h)

# Confirm uniqueness numerically by bisection and exact two-way return.
cyc_checks=0
for bb in (0.2, 0.35, 0.5, 0.68, 0.8):
    ss=bb*(1-bb)
    ac=2/ss
    maxd=min(bb,1-bb)
    for factor in (0.025, 0.1, 0.7, 2.0):
        aa=ac+factor
        lo, hi=0.0, maxd*(1-1e-12)
        for _ in range(80):
            mid=(lo+hi)/2
            if two_cycle_Q(mid,bb)>aa: hi=mid
            else:lo=mid
        dd=(hi+lo)/2
        assert dd>0
        assert abs(fmap(bb-dd,aa,bb)-(bb+dd))<2e-11
        assert abs(fmap(bb+dd,aa,bb)-(bb-dd))<2e-11
        cyc_checks+=1
    # Cubic pitchfork amplitude from the divided-logit series.
    for gap in (0.001, 0.0001):
        aa=ac+gap
        lo,hi=0.,maxd*(1-1e-12)
        for _ in range(80):
            mid=(lo+hi)/2
            if two_cycle_Q(mid,bb)>aa: hi=mid
            else:lo=mid
        dd=(lo+hi)/2
        theory=3*ss**3/(2*(1-3*ss))
        assert abs((dd*dd/gap)/theory-1)<0.003

# Critical rate and signed inverse-square expansion, including asymmetry.
critical_checks=0
for bb in (0.18, 0.30, 0.50, 0.70, 0.83):
    ss=bb*(1-bb)
    gam=4*(1-3*ss)/3
    delta=2*(2*bb-1)*(1-3*ss)/3
    for x0 in (0.12,0.58,0.89):
        t=logit(x0)-logit(bb)
        for _ in range(160000):
            t=critical_map_logit(t,bb)
        h=math.expm1(t)
        difference=ss*h/(1+bb*h)
        target=ss*ss/gam
        assert abs(160000*difference*difference/target-1)<0.035
        eps=1 if t>0 else -1
        m=80000
        inverse_square=1/(t*t)
        forecast=2*gam*m - 4*delta*eps*math.sqrt(m)/math.sqrt(2*gam)
        assert abs(inverse_square-forecast)<250
        critical_checks+=1
print('PASS: formal quintic 2-iterate jet; logit curvature; symmetric logarithmic coefficient; '
      f'{cyc_checks} two-cycle tests; 10 near-flip amplitude tests; '
      f'{critical_checks} long-trajectory critical-rate checks')
