"""Reproducibility checks for convex-polygon diameter graph limit law.

Finite computations check geometric constants and positivity; the limiting
weak convergence and Poisson convergence are justified analytically.
"""
import math
from itertools import combinations


def subtract(a,b):return (a[0]-b[0],a[1]-b[1])
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def norm(a):return math.sqrt(dot(a,a))
def unit(a):return (a[0]/norm(a),a[1]/norm(a))
def close(a,b,tol=1e-11):
    assert math.isclose(a,b,abs_tol=tol,rel_tol=tol),(a,b)

def geometry(poly):
    m=len(poly)
    assert m>=3
    area=sum(cross(poly[j],poly[(j+1)%m]) for j in range(m))/2
    assert area>0
    dist={(i,j):norm(subtract(poly[j],poly[i])) for i,j in combinations(range(m),2)}
    diameter=max(dist.values())
    edges=[(i,j) for (i,j),d in dist.items() if abs(d-diameter)<1e-11]
    gamma={}
    for i,j in edges:
        for v,w in [(i,j),(j,i)]:
            a=unit(subtract(poly[(v-1)%m],poly[v])); b=unit(subtract(poly[(v+1)%m],poly[v]))
            u=unit(subtract(poly[w],poly[v]))
            pa=dot(u,a);pb=dot(u,b)
            assert pa>0 and pb>0
            sin_theta=abs(cross(a,b))
            gamma[(v,w)]=sin_theta/(2*area*pa*pb)
    tail_small=sum(gamma[(i,j)]*gamma[(j,i)] for i,j in edges)
    return area,diameter,edges,gamma,tail_small/6,tail_small/3

# Nonregular isosceles example: two diameters sharing the apex.
iso=[(-1.,0.),(1.,0.),(0.,2.)]
a,d,edges,g,cf,cp=geometry(iso)
close(a,2);close(d,math.sqrt(5));assert edges==[(0,2),(1,2)]
close(g[(2,0)],1/3);close(g[(2,1)],1/3)
close(g[(0,2)],1/2);close(g[(1,2)],1/2)
close(cf,1/18);close(cp,1/9)

# Equilateral triangle: old independent special-case normalization.
equilateral=[(0.,0.),(1.,0.),(0.5,math.sqrt(3)/2)]
a,d,edges,g,cf,cp=geometry(equilateral)
close(a,math.sqrt(3)/4);close(d,1)
assert len(edges)==3
for rate in g.values():close(rate,2.)
close(cf,2.);close(cp,4.)

# Rectangle with a matching diameter graph and anisotropic corner rates.
rect=[(-2.,-1.),(2.,-1.),(2.,1.),(-2.,1.)]
a,d,edges,g,cf,cp=geometry(rect)
assert edges==[(0,2),(1,3)]
assert len(set([v for pair in edges for v in pair]))==4
close(a,8);close(d,math.sqrt(20))
assert all(rate>0 for rate in g.values())

# Joint apex wedge deficits are not independent.  At t=1 the overlap of
# positive-measure triangles is bounded below by a positive rectangle.
# In inward ray coordinates r,s at the apex of the isosceles example,
# directions give (5r+3s)/sqrt(5), (3r+5s)/sqrt(5).
t0=1.0
rmax=smax=math.sqrt(5)/8
assert (5*rmax+3*smax)/math.sqrt(5)<=t0+1e-12
assert (3*rmax+5*smax)/math.sqrt(5)<=t0+1e-12
assert 2*rmax*smax>0 # PPP intensity in (r,s) is 2 dr ds
print('ALL_CHECKS_PASSED')
