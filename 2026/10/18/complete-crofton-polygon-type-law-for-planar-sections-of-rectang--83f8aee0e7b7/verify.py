"""Independent combinatorial and numerical checks for the Crofton section-type law.

Requires Python 3 standard library. Run: python verify.py
Finite checks are supplementary to the analytic proof.
"""
from itertools import product
import math
import random


def closed_form(a, b, c):
    d = [a, b, c]
    if not all(math.isfinite(v) and v > 0 for v in d):
        raise ValueError('all half-edge lengths must be positive and finite')
    sq = math.sqrt((a*b)**2+(a*c)**2+(b*c)**2)
    q = [b*c/sq,a*c/sq,a*b/sq]
    pair_indices = [(0,1,2),(0,2,1),(1,2,0)]
    h_term = sum(math.hypot(d[i],d[j])*math.asin(q[k])
                 for i,j,k in pair_indices)
    min_expectation = sum(d)/2-sum(
        math.hypot(d[i],d[j])*math.acos(q[k])
        for i,j,k in pair_indices)/math.pi
    betas = [math.acos(d[j]*d[k]/(
        math.hypot(d[i],d[j])*math.hypot(d[i],d[k])))
        for i,j,k in [(0,1,2),(1,0,2),(2,0,1)]]
    h_expectation = (math.sqrt(a*a+b*b+c*c)*sum(betas)-2*h_term)/math.pi
    p3=4*min_expectation/sum(d)
    p6=2*h_expectation/sum(d)
    return (p3,1-2*p3+p6,p3-2*p6,p6)


def interval_counts(x, y, z):
    # For a generic normal, vertices are the eight signed sums of x,y,z.
    # Edges of the cuboid connect vertices differing in one sign.
    vals={s:s[0]*x+s[1]*y+s[2]*z for s in product((-1,1),repeat=3)}
    edges=[(s,tuple(-s[k] if k==j else s[k] for k in range(3)))
           for s in vals for j in range(3) if s[j]==-1]
    levels=sorted(vals.values())
    # Separate non-generic coincidences are measure zero, absent in tests.
    lengths={k:0. for k in range(3,7)}
    for lo,hi in zip(levels,levels[1:]):
        if hi-lo < 1.e-12: continue
        t=(hi+lo)*0.5
        sides=sum(min(vals[v],vals[w])<t<max(vals[v],vals[w]) for v,w in edges)
        assert sides in lengths, (x,y,z,t,sides)
        lengths[sides] += hi-lo
    return tuple(lengths[k] for k in range(3,7))


def length_profile(x,y,z):
    X,Y,Z=sorted((x,y,z),reverse=True)
    s=X+Y+Z
    h=max(0.,Y+Z-X)
    return (4*Z,2*s-8*Z+2*h,4*(Z-h),2*h)


def check():
    rand = random.Random(720826)
    cases = [(1,1,1),(1,2,3),(1,1,4),(.3,8,2.7),(1.6,1.1,.81)]
    tested=0
    for a,b,c in cases:
        ps=closed_form(a,b,c)
        assert min(ps) >= -1.e-12 and abs(sum(ps)-1)<1.e-12
        sums=[0.]*4
        denom=0.
        for _ in range(25000):
            gaussian=[rand.gauss(0,1) for j in range(3)]
            norm=math.sqrt(sum(u*u for u in gaussian))
            x,y,z=[v*abs(u)/norm for v,u in zip((a,b,c),gaussian)]
            by_vertices=interval_counts(x,y,z)
            by_formula=length_profile(x,y,z)
            assert all(abs(t-v)<1.e-10 for t,v in zip(by_vertices,by_formula)),(x,y,z,by_vertices,by_formula)
            assert abs(sum(by_vertices)-2*(x+y+z))<1.e-10
            assert abs(by_vertices[2]-by_vertices[0]+2*by_vertices[3])<1.e-10
            for j,v in enumerate(by_vertices): sums[j]+=v
            denom+=2*(x+y+z)
            tested+=1
        approx=[v/denom for v in sums]
        assert max(abs(x-y) for x,y in zip(ps,approx))<0.009,(a,b,c,ps,approx)
        print('halfedges=',(a,b,c),'exact=',tuple(round(v,11) for v in ps),
              'independent_random=',tuple(round(v,6) for v in approx))
    # Symmetric cube exact law and the pointwise invariant are also tested.
    assert abs(closed_form(1,1,1)[3]-0.0464476904201071)<2.e-12
    print('VERIFY_OK configurations=',tested,'independent_edge_counts=',tested*7)


if __name__=='__main__': check()
