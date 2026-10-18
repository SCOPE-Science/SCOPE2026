"""Exact cross-section certificates and numerical area sanity checks.

Only Python's standard library is required. This checker is supplementary to
an analytic all-dimensional proof.
"""
from fractions import Fraction as F
from itertools import product
from math import atanh, pi, tanh


def hull(points):
    pts = sorted(set(points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    low=[]
    for p in pts:
        while len(low)>=2 and cross(low[-2],low[-1],p)<=0: low.pop()
        low.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0: up.pop()
        up.append(p)
    return low[:-1]+up[:-1]


def area(vertices):
    v=hull(vertices)
    return abs(sum(x[0]*y[1]-x[1]*y[0] for x,y in zip(v,v[1:]+v[:1])))/2


def ratio_exact(y,z):
    p=[(1/(1-y),F(0)),(-1/(1+y),F(0)),
       (F(0),1/(1-z)),(F(0),-1/(1+z))]
    half_difference=[((x[0]-w[0])/2,(x[1]-w[1])/2) for x,w in product(p,p)]
    return area(half_difference)/area(p)


def integrate_simpson(f,lo,hi,n=800):
    assert n%2==0
    h=(hi-lo)/n
    return h/3*(f(lo)+f(hi)+4*sum(f(lo+(2*k-1)*h) for k in range(1,n//2+1))
             +2*sum(f(lo+2*k*h) for k in range(1,n//2)))


def main():
    coords=[F(-4,5),F(-2,3),F(-1,3),F(0),F(1,5),F(1,2),F(3,4)]
    for y,z in product(coords,repeat=2):
        observed=ratio_exact(y,z)
        expected=1+max(abs(y),abs(z))/2
        assert observed==expected,(y,z,observed,expected)
    print(f'exact rational 2D projected polar and difference-body certificates: {len(coords)**2} PASS')
    for t in [0.1,0.5,0.75,0.9]:
        a=atanh(t)
        profile=1+integrate_simpson(lambda s:s*tanh(a*s),0,1)
        u_points=72;du=2*a/u_points
        weighted_sum=0
        for i in range(u_points):
            u=-a+(i+0.5)*du
            for j in range(u_points):
                v=-a+(j+0.5)*du
                weighted_sum+=1+max(abs(tanh(u)),abs(tanh(v)))/2
        direct=weighted_sum/u_points**2
        assert abs(profile-direct)<4e-4,(t,profile,direct)
        f_area=48*a*a/pi
        h_area=f_area*profile
        assert f_area>0 and f_area<h_area<1.5*f_area
        print(f't={t}: F={f_area:.12g}, H/F={profile:.12g}, independent midpoint={direct:.12g} PASS')
    print('Analytic proof required for the arbitrary-dimensional limit and global inequalities.')

if __name__=='__main__':main()
