"""Exact rational finite checks of induced-rotation period and area formulas.

Run with python3 check_period_spectrum.py; no third-party dependencies.
The mathematical statements for all parameters follow from the accompanying proof,
not from the finite range of these tests.
"""
from fractions import Fraction as Q
from math import gcd


def interval_map(t, p, q, s):
    lam = Q(p,q)
    length = 1 + lam - s
    assert Q(0) <= t < length
    if t < 1-s:
        return t + lam
    if t < 1:
        return t + lam - 1
    return t - 1


def rotate_return(t,p,q,s):
    lam=Q(p,q)
    circumference=1+lam
    length=circumference-s
    v=t
    for steps in range(1,4):
        v=(v+lam)%circumference
        if v<length:
            return v,steps
    raise AssertionError('unexpected return time')


def clipped_area_for_m(p,q,m):
    """Shoelace area of clipped parameter rectangle in (s,r)-plane."""
    poly=[(Q(0),Q(0)),(Q(p,q),Q(0)),(Q(p,q),Q(1,q)),(Q(0),Q(1,q))]
    def clip(poly, level, greater):
        if not poly:return []
        def fn(pt):return (pt[0]+pt[1]-level)*(1 if greater else -1)
        out=[]
        for u,v in zip(poly,poly[1:]+poly[:1]):
            fu,fv=fn(u),fn(v)
            if fu>=0:out.append(u)
            if (fu<0 and fv>0) or (fu>0 and fv<0):
                ratio=fu/(fu-fv)
                out.append(tuple(u[k]+ratio*(v[k]-u[k]) for k in range(2)))
        return out
    poly=clip(poly,Q(m,q),True)
    poly=clip(poly,Q(m+1,q),False)
    if not poly:return Q(0)
    return abs(sum(((a[0]*b[1]-a[1]*b[0]) for a,b in zip(poly,poly[1:]+poly[:1])),Q(0)))/2


def test():
    sampled_orbits=0
    integrated_polygons=0
    geometric_checks=0
    for q in range(2,32):
        for p in range(1,q):
            if gcd(p,q)>1:continue
            lam=Q(p,q)
            for k in range(p):
                s=Q(3*k+1,3*q)
                for r in (Q(1,5*q),Q(4,5*q)):
                    m=(q*(s+r)).numerator//(q*(s+r)).denominator
                    n=p+q-m
                    start=r
                    v=start
                    seen=set()
                    for step in range(n):
                        assert v not in seen, (p,q,k,r,step,n)
                        seen.add(v)
                        w,rt=rotate_return(v,p,q,s)
                        assert 1<=rt<=2 and w==interval_map(v,p,q,s)
                        # With symmetric 45-degree outer cones the physical
                        # horizontal coordinate is x=t-1+y, where y=s/2.
                        y=s/2
                        x=v-1+y
                        if x < -y:
                            xx=x+lam
                        elif x < y:
                            xx=x-(1-lam)
                        else:
                            xx=x-1
                        assert xx+1-y==w
                        geometric_checks+=1
                        v=w
                    assert v==start and len(seen)==n
                    # Each congruence class of the circle visits exactly n survivors.
                    circle={r+Q(j,q) for j in range(p+q)}
                    survivors={z for z in circle if z<1+lam-s}
                    assert survivors==seen
                    sampled_orbits+=1
            areas=[]
            for m in range(p+1):
                measure=clipped_area_for_m(p,q,m)
                assert measure==(Q(1,2) if m in (0,p) else Q(1))/q**2, (p,q,m,measure)
                areas.append((p+q-m)*measure)
                integrated_polygons+=1
            area=sum(areas,Q(0))
            assert area==lam*(1+lam/Q(2))
            weighted_period=sum((p+q-m)*a for m,a in enumerate(areas))
            claimed_mean=Q(2*q+p,2)+Q(p*p+2,6*(2*q+p))
            assert weighted_period/area==claimed_mean,(p,q,weighted_period/area,claimed_mean)
    return sampled_orbits,integrated_polygons,geometric_checks

if __name__=='__main__':
    print('PASS exact orbit samples, area polygons:',*test())
