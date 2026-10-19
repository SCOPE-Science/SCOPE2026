"""Reproduction checks for positive first-harmonic kernel quadrature.

Standard-library-only checks; tests finite instances and conditional gap geometry.
The general mathematical statements require the accompanying proof.
"""
import math
import random

PI=math.pi

def point(theta,a,b):
    return (a*math.cos(theta),b*math.sin(theta))

def segment_dist(p,q):
    v=(q[0]-p[0],q[1]-p[1]); v2=v[0]*v[0]+v[1]*v[1]
    if v2 == 0: return math.hypot(*p)
    t=max(0.,min(1.,-(p[0]*v[0]+p[1]*v[1])/v2))
    return math.hypot(p[0]+t*v[0],p[1]+t*v[1])

def dist_hull(angles,a,b):
    angles=sorted((theta%(2*PI)) for theta in angles)
    p=[point(theta,a,b) for theta in angles]
    n=len(p)
    gaps=[(angles[(j+1)%n]-angles[j])%(2*PI) for j in range(n)]
    if max(gaps)<=PI: return 0.
    return min(segment_dist(p[j],p[(j+1)%n]) for j in range(n))

def max_gap(angles):
    angles=sorted(theta%(2*PI) for theta in angles)
    n=len(angles)
    return max((angles[(j+1)%n]-angles[j])%(2*PI) for j in range(n))

def circle_err(angles,r):
    delta=max_gap(angles)-PI
    return r*math.sin(delta/2) if delta>0 else 0.

def formula_tail(n,r,t):
    if t<0: return 1.
    if t>=r: return 0.
    return n/2**(n-1)*(1-2*math.asin(t/r)/PI)**(n-1)

def simpson(f,n):
    if n%2: n+=1
    h=1/n
    return h/3*(f(0)+f(1)+4*sum(f(i*h) for i in range(1,n,2))+2*sum(f(i*h) for i in range(2,n,2)))

def circle_second_moment_exact(n,r):
    # On failure, delta/pi ~ Beta(1,n-1).
    cond=(n-1)*simpson(lambda u: (math.sin(PI*u/2)**2)*(1-u)**(n-2),12000)
    return n/2**(n-1)*r*r*cond

rng=random.Random(274119)
checks=0
for n in range(2,20):
    for _ in range(100):
        theta=[rng.uniform(0,2*PI) for j in range(n)]
        for a,b in [(1.,1.),(3.,1.),(1.,2.)]:
            d=dist_hull(theta,a,b)
            if a==b:
                target=circle_err(theta,a)
                assert abs(d-target)<1e-10,(n,d,target)
            lo=min(a,b)*circle_err(theta,1.)
            hi=max(a,b)*circle_err(theta,1.)
            assert lo-1e-10<=d<=hi+1e-10,(n,a,b,d,lo,hi)
            checks+=1
print('finite geometry checks',checks)

# Exact conditional beta tail, tested as integral of its density via Simpson.
for n in (2,3,4,7,12,24):
    density=lambda u: (n-1)*(1-u)**(n-2)
    for y in (0.05,0.15,0.4,0.7):
        numerical=simpson(lambda x: (1-y)*density(y+(1-y)*x),4000)
        exact=(1-y)**(n-1)
        assert abs(numerical-exact)<1e-8, (n,y,numerical,exact)
        checks+=1
print('beta survival checks',checks)

# Conditional sampling of rare failure removes exponentially unlikely rejection.
# Randomize the start of the unique long gap, then fill the remaining short arc.
for n in (12,40,150,400):
    for a,b in ((1.,1.),(2.,1.),(3.,1.),(0.5,2.)):
        values=[]
        trials=1200
        for _ in range(trials):
            delta=PI*(1-rng.random()**(1/(n-1)))
            phi=rng.uniform(0,2*PI)
            th=[phi,phi+PI+delta]
            th.extend(phi+PI+delta+rng.random()*(PI-delta) for j in range(n-2))
            observed=dist_hull(th,a,b)
            if n>=150:
                # Asymptotic gap chord formula, relative o(1) for typical gap.
                gangle=phi+delta/2
                c=(a*b)/math.hypot(a*math.cos(gangle),b*math.sin(gangle))
                predicted=c*math.sin(delta/2)
                # Boundary support for small delta may not always have foot inside,
                # but large n makes this overwhelmingly likely.
                assert abs(observed-predicted)<4e-10,(n,a,b,observed,predicted)
            values.append((n*observed)**2)
        empirical=sum(values)/trials
        target=PI*PI*a*b/2
        # Loose tolerances because exact second moment is dominated by rare
        # conditional exponential tail observations and finite-N bias.
        if n>=150:
            assert abs(empirical/target-1)<0.27,(n,a,b,empirical,target)
        checks+=1
        print('conditional n,a,b,moment,limit',n,a,b,round(empirical,3),round(target,3))

# A non-elliptic, smooth, strictly convex centrally symmetric feature curve.
# For g(t)=exp(it)+eps exp(3it), eps=0.03, direct curvature bounds
# ensure strict convexity and det(g,gprime)>0 uniformly.
eps=0.03
def smooth_curve(t):
    return (math.cos(t)+eps*math.cos(3*t),math.sin(t)+eps*math.sin(3*t))
def smooth_curve_dist(angles):
    angles=sorted(t%(2*PI) for t in angles)
    p=[smooth_curve(t) for t in angles]
    if max_gap(angles)<=PI: return 0.
    return min(segment_dist(p[i],p[(i+1)%len(p)]) for i in range(len(p)))
for deficit in (0.0005,0.002,0.005):
    for _ in range(100):
        t=rng.uniform(0,2*PI)
        angles=[t,t+PI+deficit]+[t+PI+deficit+rng.random()*(PI-deficit) for j in range(20)]
        actual=smooth_curve_dist(angles)
        gnorm=math.sqrt(1+2*eps*math.cos(2*t)+eps**2)
        det=1+4*eps*math.cos(2*t)+3*eps**2
        first=deficit*det/(2*gnorm)
        assert abs(actual/first-1)<0.02,(t,deficit,actual,first)
        checks+=1
print('nonelliptic chord checks',checks)

# Exact formula in isotropic case and a scale check.
for n in (3,5,10,20,80,160):
    m2=circle_second_moment_exact(n,1.)
    scaled=n*2**n*m2/(PI*PI)
    if n>=80:
        assert abs(scaled-1)<0.1,(n,scaled)
    assert 0<m2<=n/2**(n-1)
    print('isotropic n, mean-square, scaled',n,m2,scaled)
    checks+=1
print('all checks passed',checks)
