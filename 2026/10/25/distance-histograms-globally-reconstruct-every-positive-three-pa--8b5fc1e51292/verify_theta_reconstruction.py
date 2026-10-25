"""Exact rational intersection and independent sampling checks for three-path theta graphs.

This script is self-contained (Python 3, standard library). It does not
stand in for the analytic proof, which applies to arbitrary real edge lengths.
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random
from math import sqrt


def clip(poly, ax, ay, rhs):
    """Intersect a rational polygon with ax*x+ay*y>=rhs."""
    if not poly:
        return []
    result=[]
    for u,v in zip(poly, poly[1:]+poly[:1]):
        du=ax*u[0]+ay*u[1]-rhs
        dv=ax*v[0]+ay*v[1]-rhs
        if du >= 0:
            result.append(u)
        if (du<0<dv) or (dv<0<du):
            t=du/(du-dv)
            result.append((u[0]+t*(v[0]-u[0]),u[1]+t*(v[1]-u[1])))
    return result


def polygon_area(poly):
    if len(poly)<3:
        return Q(0)
    return abs(sum(u[0]*v[1]-u[1]*v[0]
                   for u,v in zip(poly,poly[1:]+poly[:1])))/2


def ordered_cross_tail(u,v,w,r):
    """Measure of ordered pairs on distinct u,v arms at distance > r."""
    poly=[(Q(0),Q(0)),(u,Q(0)),(u,v),(Q(0),v)]
    # Direct paths through either common vertex, then shortcuts using arm w.
    halfplanes=[(1,1,r),(-1,-1,r-u-v),(1,-1,r-w-v),(-1,1,r-u-w)]
    for ax,ay,rhs in halfplanes:
        poly=clip(poly,ax,ay,rhs)
    return polygon_area(poly)


def ordered_same_tail(u,w,r):
    """Area of ordered pairs on one arm, alternate pole path length w."""
    low=max(Q(0),r)
    high=min(u,u+w-r)
    if low>=high:
        return Q(0)
    return 2*(u*(high-low)-(high*high-low*low)/2)


def unnormalized_tail(lens,r):
    """L^2 * Pr(distance>r), exactly, for positive rational edge lengths."""
    total=Q(0)
    for i in range(3):
        other=min(lens[j] for j in range(3) if j!=i)
        total+=ordered_same_tail(lens[i],other,r)
    for i,j in combinations(range(3),2):
        k=3-i-j
        total+=2*ordered_cross_tail(lens[i],lens[j],lens[k],r)
    return total


def sample_distance(lens,i,x,j,y):
    """Independent shortest-path enumerator for any two sampled edge positions."""
    if i==j:
        z=abs(x-y)
        w=min(lens[t] for t in range(3) if t!=i)
        return min(z,lens[i]+w-z)
    k=3-i-j
    return min(x+y,lens[i]-x+lens[j]-y,
               x+lens[k]+lens[j]-y,lens[i]-x+lens[k]+y)


def run():
    n=0
    strict=[]
    for a in range(1,7):
        for b in range(a,10):
            for c in range(b,12):
                lengths=(Q(a),Q(b),Q(c))
                D=Q(b+c,2)
                h=Q(b-a,2)
                if a<b:
                    for e in (h/10,h/2,h-Q(1,1000)):
                        if e>0:
                            actual=unnormalized_tail(lengths,D-e)
                            predicted=4*e*(a+e)
                            assert actual==predicted,(lengths,e,actual,predicted)
                            n+=1
                    delta=Q(1,10000)
                    gap=unnormalized_tail(lengths,D-h-delta)-4*(h+delta)*(a+h+delta)
                    assert gap>0,(lengths,gap)
                    expected=2*(a+c)*(2 if b==c else 1)
                    assert abs(gap/delta-expected)<Q(1,50),(lengths,gap,expected)
                    n+=2
                    strict.append((lengths,gap))
                else:
                    e=Q(1,100000)
                    actual=unnormalized_tail(lengths,D-e)
                    coeff=12*a if a==b==c else 2*c+6*a
                    assert abs(actual/e-coeff)<Q(1,100),(lengths,actual,e,coeff)
                    n+=1
    rng=Random(104729)
    comparisons=[]
    for triplet,rr in [((1,2,5),Q(3)),((1,1,5),Q(5,2)),((1,1,1),Q(3,4)),((2,3,3),Q(5,2))]:
        ls=list(triplet);L=sum(ls);m=110000
        matches=0
        for _ in range(m):
            def draw():
                z=rng.random()*L
                for i,edge in enumerate(ls):
                    if z<edge:return (i,z)
                    z-=edge
                return (2,float(ls[-1]))
            i,x=draw();j,y=draw()
            matches+=(sample_distance(ls,i,x,j,y)>float(rr))
        exact=float(unnormalized_tail(tuple(map(Q,ls)),rr)/Q(L*L))
        observed=matches/m
        tol=6*sqrt(max(exact*(1-exact),0.0001)/m)+0.001
        assert abs(exact-observed)<tol,(triplet,rr,exact,observed,tol)
        comparisons.append((triplet,str(rr),round(exact,7),round(observed,7)))
    print('EXACT_CASES',n)
    print('POSITIVE_ONSET_CASES',len(strict))
    print('RANDOM_CHECKS',comparisons)
    print('ALL_CHECKS_OK')

if __name__=='__main__':
    run()
