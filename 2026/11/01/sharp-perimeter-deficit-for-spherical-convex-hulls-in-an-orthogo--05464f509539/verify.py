"""Numerical cross-checks for the sharp spherical-wedge perimeter theorem.

Run with Python 3.10+ and the standard library. Numerical experiments are
corroboration, not a replacement for the analytic proof in RESULT.md.
"""
import math
import random

PI = math.pi


def hemisphere_fraction(z, theta):
    r = math.sqrt(max(0.0, 1.0-z*z))
    p = 0.5 + (math.asin(r*math.cos(theta))+
               math.asin(r*math.sin(theta)))/PI
    return max(0.0, min(1.0, p))


def deficit_integral(n, nz=900, nt=720):
    # D_n = integral_{z=-1}^1 integral_{theta=0}^{2pi} p(z,theta)^n dtheta dz.
    # Midpoint quadrature integrates full latitude/longitude domain.
    dz = 2.0/nz
    dt = 2*PI/nt
    total = 0.0
    for j in range(nz):
        z = -1+(j+0.5)*dz
        r = math.sqrt(max(0.0, 1-z*z))
        s = 0.0
        for k in range(nt):
            t = (k+0.5)*dt
            p = 0.5+(math.asin(r*math.cos(t))+math.asin(r*math.sin(t)))/PI
            s += max(0.0, min(1.0, p))**n
        total += s
    return total*dz*dt


def spherical_perimeter(points):
    # Central/gnomonic projection to a plane perpendicular to (1,1,0).
    data = []
    for j, (x,y,z) in enumerate(points):
        a=(x+y)/math.sqrt(2)
        data.append(((x-y)/(math.sqrt(2)*a),z/a,j))
    data.sort()

    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

    lower=[]
    for x in data:
        while len(lower)>=2 and cross(lower[-2],lower[-1],x)<=0: lower.pop()
        lower.append(x)
    upper=[]
    for x in reversed(data):
        while len(upper)>=2 and cross(upper[-2],upper[-1],x)<=0: upper.pop()
        upper.append(x)
    hull=lower[:-1]+upper[:-1]
    result=0.0
    for i,p in enumerate(hull):
        a=points[p[2]]
        b=points[hull[(i+1)%len(hull)][2]]
        d=sum(ai*bi for ai,bi in zip(a,b))
        result+=math.acos(max(-1,min(1,d)))
    return result


def geometric_mean(n,reps,seed):
    rng=random.Random(seed)
    s=0.0
    for i in range(reps):
        pts=[]
        for j in range(n):
            theta=rng.random()*PI/2
            z=2*rng.random()-1
            r=math.sqrt(1-z*z)
            pts.append((r*math.cos(theta),r*math.sin(theta),z))
        s+=spherical_perimeter(pts)
    return s/reps


def main():
    beta=math.gamma(0.75)*math.gamma(0.5)/math.gamma(1.25)
    coefficient=PI*beta/2
    assert 3.76406<coefficient<3.76408

    for z in [-.94,-.53,0,.32,.92]:
        for theta in [0.01,0.9,1.7,3.2,5.4]:
            p=hemisphere_fraction(z,theta)
            assert 0<=p<=1
            assert 1-p+1e-12 >= math.asin(z*z)/PI

    checked={}
    for n in (3,10,100,2500):
        d=deficit_integral(n)
        checked[n]=d
        assert 0<d<2*PI
    assert abs(checked[3]-3.356136842729647)<0.003
    assert abs(checked[10]-1.489863806080073)<0.003
    assert abs(checked[100]-0.387716401157468)<0.003
    assert abs(math.sqrt(2500)*checked[2500]-coefficient)<0.03
    assert checked[3]>checked[10]>checked[100]>checked[2500]

    # Independently compute geodesic hull boundaries, without great-circle quadrature.
    for n,reps in ((3,4000),(10,2500),(30,1800)):
        empirical=geometric_mean(n,reps,194739+n)
        quadrature=2*PI-(checked[n] if n in checked else deficit_integral(n))
        print('hull_samples',n,reps,'empirical_perimeter',round(empirical,7),
              'integral_perimeter',round(quadrature,7))
        assert abs(empirical-quadrature)<0.075
    print('limit_constant',format(coefficient,'.12f'))
    print('scaled_deficit_n2500',format(math.sqrt(2500)*checked[2500],'.12f'))
    print('ALL_CHECKS_PASSED')


if __name__=='__main__':
    main()
