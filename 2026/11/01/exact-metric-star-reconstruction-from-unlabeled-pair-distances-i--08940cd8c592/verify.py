"""Independent exact checks of one-dimensional metric-star distance-density identities.
Run: python verify.py
Uses only Python standard library; all exact computations use Fraction.
"""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
from random import Random

def direct_density(arms,t):
    """Counts distances by conditioning on same or distinct arms (ordered sample pairs)."""
    a=[F(x) for x in arms]; t=F(t); L=sum(a)
    same=sum(2*max(F(0),x-t) for x in a)
    cross=sum(2*(max(F(0),t)-max(F(0),t-x)-max(F(0),t-y)+max(F(0),t-x-y)) for x,y in combinations(a,2))
    return (same+cross)/L**2

def hinge_density(arms,t):
    a=[F(x) for x in arms];t=F(t);L=sum(a);n=len(a)
    h=L+F(n*(n-3),2)*t-(n-2)*sum(max(F(0),t-x) for x in a)+sum(max(F(0),t-x-y) for x,y in combinations(a,2))
    return 2*h/L**2

def curvature(arms):
    a=list(map(F,arms));n=len(a);v=Counter()
    for x in a:v[x]-=n-2
    for x,y in combinations(a,2):v[x+y]+=1
    return Counter({k:c for k,c in v.items() if c})

def recover_from_curvature(curv,n):
    """Exact signed-measure peeling. Pair sums of recovered arms are removed."""
    rem=Counter(curv); seen=[]
    while len(seen)<n:
        rem=Counter({x:y for x,y in rem.items() if y!=0})
        assert rem,('insufficient residual',seen)
        t=min(rem)
        mass=rem[t]
        assert mass<0 and (-mass)%(n-2)==0,(t,mass,seen,dict(rem))
        m=-mass//(n-2)
        assert len(seen)+m<=n
        for _ in range(m):
            # Subtract each new negative single-arm curvature and new pair with all older arms
            rem[t]+=n-2
            for old in seen:
                rem[old+t]-=1
            seen.append(t)
        rem=Counter({x:y for x,y in rem.items() if y})
    assert not rem,('remaining unexplained curvature',rem)
    return seen

examples=[(1,2,3),(1,1,1),(1,1,2,3),(1,2,3,5),(1,2,3,3),(F(1,2),F(3,2),F(5,2)),(1,4,7,8,12), (1,2,3,4,5,6)]
for arms in examples:
    a=list(map(F,arms)); L=sum(a);n=len(a)
    assert recover_from_curvature(curvature(a),n)==sorted(a)
    assert direct_density(a,0)==F(2,L)
    assert hinge_density(a,0)==F(2,L)
    for k in range(161):
        t=F(k,20)
        assert direct_density(a,t)==hinge_density(a,t),(arms,t)
    # density integrates to one exactly by trapezoids over all knot positions
    knots=sorted(set([F(0)]+a+[x+y for x,y in combinations(a,2)]))
    area=sum((hinge_density(a,u)+hinge_density(a,v))*(v-u)/2 for u,v in zip(knots,knots[1:]))
    assert area==1,(arms,area)
    # Right derivative at zero
    t=min(a)/100
    slope=(hinge_density(a,t)-hinge_density(a,0))/t
    assert slope==F(n*(n-3), L**2)
print('DIRECT_CONDITIONING_VERSUS_HINGE_DENSITY_EXACT')
print('SIGNED_CURVATURE_PEELING_WITH_COLLISIONS_EXACT')
print('NORMALIZATION_AND_END_SLOPES_EXACT')
# A completely invisible arm length in the second derivative is still recovered
special=(F(1),F(2),F(3));nu=curvature(special)
assert F(3) not in nu and recover_from_curvature(nu,3)==list(special)
print('HIDDEN_ARM_LENGTH_RECOVERED_EXACT')
# Independent pair sampling; conditional arm lengths via arclength points
rng=Random(28720);a=[1.,2.,3.];L=sum(a); knots=[0.,1.,2.,3.,4.,5.,6.]
N=240000;cnt=[0]*(len(knots)-1)
for _ in range(N):
    u=rng.random()*L;v=rng.random()*L
    def point(w):
        for j,x in enumerate(a):
            if w<=x:return j,w
            w-=x
        return len(a)-1,a[-1]
    i,x=point(u);j,y=point(v)
    d=abs(x-y) if i==j else x+y
    for k in range(len(cnt)):
        if knots[k]<=d<knots[k+1]:cnt[k]+=1;break
# exact CDF by integration of hinge density, supports piecewise linear
expected=[]
for lo,hi in zip(knots,knots[1:]):
    mass=(float(hinge_density(a,F(str(lo))))+float(hinge_density(a,F(str(hi)))))*(hi-lo)/2
    expected.append(mass)
    assert abs(cnt[len(expected)-1]/N-mass)<.008,(lo,hi,cnt[len(expected)-1]/N,mass)
print('INDEPENDENT_UNIFORM_ARCLENGTH_PAIR_SAMPLING_PASSED')
print('ALL_CHECKS_PASSED')
