"""Exact-rational reproducibility checks for the Braess moment frontier.
Run: python3 checker.py
All arithmetic in the assertions is rational; no external modules are used.
"""
from fractions import Fraction as F
from random import Random

a, b, k = F(2,3), F(2), F(3,4)
rng = Random(20261027)
checks = 0

def verify(condition):
    global checks
    assert condition
    checks += 1

def extra(d):
    if d <= 1: return F(3,2)*d*d-d
    if d <= 2: return d-d*d/2
    return F(0)

def bound(d):
    return k*(d-a)*(b-d)

def cost_no(d):
    return d*(1+d/2)

def cost_yes(d):
    if d <= 1: return 2*d*d
    if d <= 2: return 2*d
    return cost_no(d)

def expect(pts):
    return sum((w*extra(d) for d,w in pts), F(0))

def mv(pts):
    m = sum((w*d for d,w in pts), F(0))
    v = sum((w*(d-m)**2 for d,w in pts), F(0))
    return m,v

def two_point(m,v,low):
    assert low<m and v>0
    high=m+v/(m-low)
    p_low=(high-m)/(high-low)
    return [(low,p_low),(high,1-p_low)]

# Exact Wardrop complementarity and two-route baseline verification.
for i in range(0,601):
    d=F(i,100)
    c=max(F(0),min(d,2-d))
    u=(d-c)/2
    v=u
    cu=u+c+1
    cv=v+c+1
    cc=d+c
    # Available routes must not have a lower cost than any route used.
    used=[(u,cu),(v,cv),(c,cc)]
    mincost=min(t for mass,t in used if mass>0) if d>0 else 0
    for mass,t in used:
        verify(mass>=0)
        if d>0:
            verify(t>=mincost)
            if mass>0: verify(t==mincost)
    physical=u*cu+v*cv+c*cc
    verify(physical==cost_yes(d))
    verify(physical-cost_no(d)==extra(d))
    verify(extra(d)>=bound(d))
    if d<=1: verify(extra(d)-bound(d)==(1-F(3,2)*d)**2)
    elif d<=2: verify(extra(d)-bound(d)==(1-d/2)**2)
    else: verify(extra(d)-bound(d)==F(3,4)*(d-a)*(d-2))

# Equality points on the 0..6 rational grid.
verify([F(i,300) for i in range(0,1801) if extra(F(i,300))==bound(F(i,300))]==[a,b])

# The variance inequality is exact for arbitrary mixtures (not just two points).
for _ in range(2000):
    n=rng.randint(1,6)
    vals=[F(rng.randrange(0,901),100) for _ in range(n)]
    raw=[rng.randint(1,20) for _ in range(n)]
    pts=list(zip(vals,[F(x,sum(raw)) for x in raw]))
    m,v=mv(pts)
    verify(expect(pts)>=k*((m-a)*(b-m)-v))
    verify(expect(pts)==sum((w*extra(d) for d,w in pts),F(0)))

# Construct exact witnesses both sides of the moment boundary at each tested mean.
for j in range(1,300):
    m=a+F(j,300)*(b-a) # strictly within (a,b)
    threshold=(m-a)*(b-m)
    verify(threshold>0)
    # Small variance: every two-point support chosen below m tests positive expected difference.
    v=threshold/2
    low=m/2
    if low<m:
        pts=two_point(m,v,low)
        M,V=mv(pts)
        verify(M==m and V==v)
        verify(expect(pts)>0)
    # Equality witness, unique two-atom zero-difference law.
    pts=[(a,(b-m)/(b-a)),(b,(m-a)/(b-a))]
    M,V=mv(pts)
    verify(M==m and V==threshold)
    verify(expect(pts)==0)
    # Above the threshold, construct same-moment opposite-sign two-point laws.
    excess=F(1,7)
    v=threshold+excess
    eps=min(a/2,(m-a)/2,excess/(4*(b-m)))
    lo_negative=a-eps
    lo_positive=a+eps
    for lo,sign in [(lo_negative,-1),(lo_positive,1)]:
        pts=two_point(m,v,lo)
        M,V=mv(pts)
        verify(M==m and V==v)
        verify(pts[1][0]>2)
        verify(sign*expect(pts)>0)

# At m=3/2, variance=1/2, same moments have strictly opposite planning consequences.
minus=[(F(1,2),F(1,3)),(F(2),F(2,3))]
plus=[(F(1),F(2,3)),(F(5,2),F(1,3))]
for pts in [minus,plus]:
    verify(mv(pts)==(F(3,2),F(1,2)))
verify(expect(minus)==-F(1,24))
verify(expect(plus)==F(1,3))
print('PASS',checks,'exact-rational assertions')
