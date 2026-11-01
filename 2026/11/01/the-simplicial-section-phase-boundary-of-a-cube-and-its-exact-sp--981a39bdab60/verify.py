"""Finite exact and numerical corroboration of a cube-section theorem."""
from fractions import Fraction as F
from itertools import product
import math, random
from scipy.integrate import quad

def vertex_count(d,z,g):
    vertices=list(product((-1,1),repeat=d))
    heights={v: sum(g[i]*(F(v[i])-z[i]) for i in range(d)) for v in vertices}
    assert all(h for h in heights.values())
    count=0
    for v in vertices:
        for i in range(d):
            if v[i]==1:
                w=tuple((-v[j] if j==i else v[j]) for j in range(d))
                count+= (heights[v]*heights[w]<0)
    return count

def predicted(d,z,g):
    hits=[]
    for sig in product((-1,1),repeat=d):
        c=[F(1)-sig[i]*z[i] for i in range(d)]
        h=(F(2)-sum(c))/2
        if h<=0:continue
        a=[sig[i]*g[i] for i in range(d)]
        H=sum(c[i]*a[i] for i in range(d))
        if H>0 and all(a[i]>H/2 for i in range(d)):
            hits.append((sig,1))
        if H<0 and all(-a[i]>-H/2 for i in range(d)):
            hits.append((sig,-1))
    return hits

rng=random.Random(1729)
tests=0
for d in (3,4,5,6):
    for iteration in range(700):
        z=[F(rng.randrange(-8,9),10) for _ in range(d)]
        g=[F(rng.randrange(-60,61),1) for _ in range(d)]
        # Skip normals that pass through vertices.
        if any(sum(g[i]*(F(v[i])-z[i]) for i in range(d))==0 for v in product((-1,1),repeat=d)):
            continue
        k=vertex_count(d,z,g)
        hits=predicted(d,z,g)
        assert (k==d)==(len(hits)==1),(d,z,g,k,hits)
        tests+=1
print('exact face-count/vertex-cone equivalence checks:',tests)

def p3(t):
    if t<=F(1,3):return 0.
    lam=(1-float(t))/2
    delta=1-3*lam
    rho=math.sqrt((lam+delta)**2+2*lam**2)
    inner=3*lam**2+2*lam*delta
    return math.atan2(delta**2,rho**3+3*inner*rho)/math.pi

for t in (0.34,0.4,0.55,0.7,0.9,0.99):
    # Independent 1D integral using the polar azimuth: for u1,u2,u3>0,
    # the simplex cone is symmetric around (1,1,1); integrate over x-simplex
    # with scipy dblquad in barycentric coordinates.
    from scipy.integrate import dblquad
    c=1-t
    h=1-3*c/2
    integrand=lambda y,x: ((.5+h*x/c)**2+(.5+h*y/c)**2+(.5+h*(1-x-y)/c)**2)**(-1.5)
    integral=dblquad(integrand,0,1,lambda x:0,lambda x:1-x,epsabs=1e-11)[0]
    p_integral=2/(4*math.pi) * h**2/c**3*integral
    assert abs(p3(t)-p_integral)<2e-12,(t,p3(t),p_integral)
    print('trihedral formula vs independent quadrature:',t,round(p3(t),12))

coef=3**3.5/(16*math.pi)
for gap in (0.02,0.01,0.003):
    t=1/3+gap
    ratio=p3(t)/gap**2
    print('critical onset coefficient check:',gap,ratio,'target',coef)
print('all checks passed')
