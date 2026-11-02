"""Standalone numerical cross-checks for the near-maximal Reuleaux tetrahedron width law.
Requires Python 3.9+. Exact coefficients are independently derived in RESULT.md.
No finite test is substituted for the analytic proof.
"""
import math
from itertools import combinations

SQ2=math.sqrt(2.0); SQ3=math.sqrt(3.0)
a=SQ2/4.0
r=SQ3/2.0
kappa=(SQ3-SQ2)/4.0
maximum=SQ3-SQ2/2.0
c1=6/(SQ3-SQ2)
c2=3*SQ3/(2*(SQ3-SQ2)**3)
centers=[(a,a,a),(a,-a,-a),(-a,a,-a),(-a,-a,a)]

def dot(a,b): return sum(t*s for t,s in zip(a,b))
def norm(v): return math.sqrt(dot(v,v))
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def scal(v,t): return tuple(x*t for x in v)
def feasible(x):return all(dot(minus(x,c),minus(x,c))<=1+3e-12 for c in centers)

def support(u):
    """Enumerate candidate exposed vertices, circular arcs and spherical faces."""
    points=list(centers)
    for c in centers:
        points.append(plus(c,u))
    for i,j in combinations(range(4),2):
        vi,vj=centers[i],centers[j]
        mid=scal(plus(vi,vj),0.5)
        axis=minus(vj,vi)
        projection=minus(u,scal(axis,dot(u,axis)/dot(axis,axis)))
        h=norm(projection)
        if h>1e-12:points.append(plus(mid,scal(projection,r/h)))
    vals=[dot(x,u) for x in points if feasible(x)]
    assert vals
    return max(vals)

def axial_formula(s,t):
    q=s*s+t*t
    assert q<1
    x=math.sqrt(1-q)
    return -2*a*x+r*(math.sqrt(1-q/2+s*t)+math.sqrt(1-q/2-s*t))

def local_probability(epsilon,angles=8192):
    """Area of six near-axial spherical superlevel components, by angular quadrature."""
    accum=0.0
    for i in range(angles):
        theta=(i+.5)*2*math.pi/angles
        ss=math.sin(2*theta)
        def deficit(q):
            x=math.sqrt(1-q)
            p=q*ss/2
            w=-2*a*x+r*(math.sqrt(1-q/2+p)+math.sqrt(1-q/2-p))
            return maximum-w
        low=0.0; high=min(.5,5*epsilon/kappa)
        assert deficit(high)>epsilon
        for _ in range(65):
            mid=(low+high)/2
            if deficit(mid)>epsilon:high=mid
            else:low=mid
        q=(low+high)/2
        accum+=1-math.sqrt(1-q)
    return 3*accum/angles

def run():
    assert abs(maximum-2*(r-a))<1e-15
    for s,t in [(0.01,0.03),(.06,.02),(-.03,.04),(.08,-.04)]:
        u=(math.sqrt(1-s*s-t*t),s,t)
        width=support(u)+support(tuple(-v for v in u))
        assert abs(width-axial_formula(s,t))<5e-12,(s,t,width,axial_formula(s,t))
        q=s*s+t*t
        assert abs((maximum-width)/q-kappa)<.003
    # Deterministic grid: only a cross-check, not proof of global uniqueness.
    golden=(math.sqrt(5)-1)/2
    observed_max=0
    offaxis_max=0
    for i in range(1400):
        z=1-2*(i+.5)/1400
        th=2*math.pi*((i*golden)%1)
        u=(math.sqrt(1-z*z)*math.cos(th),math.sqrt(1-z*z)*math.sin(th),z)
        w=support(u)+support(tuple(-v for v in u))
        observed_max=max(observed_max,w)
        assert w<maximum+3e-11
        if max(abs(x) for x in u)<.995:offaxis_max=max(offaxis_max,w)
    print('grid max:',observed_max,'off-axis grid max:',offaxis_max)
    for eps in [1e-3,5e-4,1e-4,5e-5]:
        estimate=local_probability(eps)
        pred=c1*eps+c2*eps**2
        print('epsilon:',eps,'six-cap measure:',estimate,'two-term prediction:',pred,'scaled third-order remainder:',(estimate-pred)/eps**3)
        assert abs(estimate-pred)<1500*eps**3
    print('coefficients:',c1,c2,'PASS')
if __name__=='__main__':run()
