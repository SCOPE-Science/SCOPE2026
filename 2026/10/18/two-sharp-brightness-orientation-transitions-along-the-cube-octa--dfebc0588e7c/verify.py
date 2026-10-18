"""Direct geometric consistency checks for the cube-octahedron brightness theorem.
Standard-library Python 3 only. Infinite-dimensional assertions rely on the written proof.
"""
from itertools import permutations, product
from math import sqrt
import random


def coefficients(c):
    if 1 <= c <= 2:
        return 2*c-1, -2*c*c+6*c-3
    if 2 < c <= 3:
        t=3-c
        return 4-t*t, t*t
    raise ValueError('parameter must be in [1,3]')


def vertices(c):
    base=(1,c-1,0) if c<=2 else (1,1,c-2)
    return list({tuple(v_i*s_i for v_i,s_i in zip(p,s))
                 for p in set(permutations(base))
                 for s in product((-1,1),repeat=3)})


def dot(v,w):
    return sum(a*b for a,b in zip(v,w))


def cross(v,w):
    return (v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0])


def unit(v):
    z=sqrt(dot(v,v))
    return tuple(x/z for x in v)


def direct_projection_area(c,u):
    u=unit(u)
    v=cross(u,(1,0,0) if abs(u[0])<0.8 else (0,1,0))
    v=unit(v)
    w=cross(u,v)
    pts=sorted(set((round(dot(p,v),13),round(dot(p,w),13)) for p in vertices(c)))
    def cross2(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[]
    for p in pts:
        while len(low)>1 and cross2(low[-2],low[-1],p)<=1e-11:
            low.pop()
        low.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>1 and cross2(up[-2],up[-1],p)<=1e-11:
            up.pop()
        up.append(p)
    hull=low[:-1]+up[:-1]
    return abs(sum(x*y2-y*x2 for (x,y),(x2,y2) in zip(hull,hull[1:]+hull[:1])))/2


def predicted(c,u):
    a,b=coefficients(c)
    v=sorted((abs(z) for z in unit(u)),reverse=True)
    return a*sum(v)+b*max(0,v[0]-v[1]-v[2])


def bounds(c):
    a,b=coefficients(c)
    return min(a+b,sqrt(2)*a),max(sqrt(3)*a,sqrt(3*a*a-2*a*b+3*b*b))


def run():
    tmax=(7+sqrt(7))/6
    tmin=(4-sqrt(2)+sqrt(10-6*sqrt(2)))/2
    assert 1<tmax<tmin<2
    assert abs(coefficients(tmax)[1]/coefficients(tmax)[0]-2/3)<1e-13
    assert abs(coefficients(tmin)[1]/coefficients(tmin)[0]-(sqrt(2)-1))<1e-13
    r=random.Random(73421)
    tested=0
    for c in (1,1.02,1.22,1.5,tmax,1.7,1.85,1.9,tmin,1.95,2,2.25,2.5,2.91,3):
        a,b=coefficients(c)
        rr=b/a
        tilted=unit((a+b,a-b,a-b))
        directions=[(1,0,0),(1,1,0),(1,1,1),tilted]
        directions.extend((r.gauss(0,1),r.gauss(0,1),r.gauss(0,1)) for _ in range(360))
        minimum,maximum=bounds(c)
        for direction in directions:
            p=predicted(c,direction)
            geom=direct_projection_area(c,direction)
            assert abs(p-geom)<2e-9,(c,direction,p,geom)
            assert minimum-1e-9<=p<=maximum+1e-9,(c,direction,p,minimum,maximum)
            tested+=1
        assert abs(predicted(c,(1,0,0))-(a+b))<1e-12
        assert abs(predicted(c,(1,1,0))-sqrt(2)*a)<1e-12
        assert abs(predicted(c,(1,1,1))-sqrt(3)*a)<1e-12
        if rr>=2/3-1e-10:
            assert abs(predicted(c,tilted)-maximum)<1e-10
        else:
            assert abs(predicted(c,(1,1,1))-maximum)<1e-10
        if rr>=sqrt(2)-1+1e-10:
            assert abs(predicted(c,(1,1,0))-minimum)<1e-10
        else:
            assert abs(predicted(c,(1,0,0))-minimum)<1e-10
    print('DIRECT_PROJECTED_HULL_AREA_OK',tested,'cases')
    print('TWO_SHARP_ORIENTATION_THRESHOLDS_OK',format(tmax,'.14f'),format(tmin,'.14f'))
    print('ALL_BRIGHTNESS_CHECKS_OK')

if __name__=='__main__':
    run()
