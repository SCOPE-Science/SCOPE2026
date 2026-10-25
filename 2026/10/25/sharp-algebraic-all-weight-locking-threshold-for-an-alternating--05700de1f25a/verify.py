#!/usr/bin/env python3
"""Finite numerical diagnostics for an exact alternating-frequency four-cycle theorem.

The infinite/all-parameter assertions are proved analytically in the accompanying
result; these finite checks are only reproducible consistency tests.
"""
import math
from fractions import Fraction


def zroot(c):
    if not 0.0 < c < 1.0:
        raise ValueError('requires 0<c<1')
    # Monotone crossing of (1+c)(z*z-1)/(1+c*z)^(3/2) = 1.
    def f(z):
        return (1.0 + c)*(z*z - 1.0)/(1.0+c*z)**1.5
    low, high = 1.0, 2.0
    while f(high) < 1.0:
        high *= 2.0
    for _ in range(120):
        mid = (low + high)/2.0
        if f(mid) < 1.0:
            low = mid
        else:
            high = mid
    return (low+high)/2.0


def threshold(a):
    if a == 0:
        return .5, None
    c = a/(2.0+a)
    z = zroot(c)
    f = math.sqrt(z/(z+c))*(1+(1+c)/math.sqrt(1+c*z))
    return 1.0/f, z


def stationary_angles(a,K):
    kc,z = threshold(a)
    assert K > kc
    if a == 0:
        phi = math.asin(1.0/(2.0*K))
        return (0.0, phi, 0.0, phi)
    c = a/(2.0+a)
    tcrit = math.sqrt(z/c)
    def T(t):
        return t/math.sqrt(1+t*t)*(1+(1+c)/math.sqrt(1+c*c*t*t))
    low,high=0.0,tcrit
    for _ in range(120):
        mid=(low+high)/2.0
        if T(mid)<1.0/K:
            low=mid
        else:
            high=mid
    phi=math.atan((low+high)/2.0)
    delta=math.atan(c*math.tan(phi))
    return (0.0,phi,delta,phi+delta)


def field(theta,a,K):
    omega=(-1.,1.,-1.,1.)
    edges=[(0,1,1.),(1,2,1.+a),(2,3,1.),(3,0,1.)]
    dy=list(omega)
    for i,j,w in edges:
        inc=K*w*math.sin(theta[j]-theta[i])
        dy[i]+=inc
        dy[j]-=inc
    return dy


def gauge_hessian(theta,a):
    edges=[(0,1,1.),(1,2,1.+a),(2,3,1.),(3,0,1.)]
    m=[[0.]*3 for _ in range(3)]
    for i,j,w in edges:
        g=w*math.cos(theta[j]-theta[i])
        for k in range(1,4):
            for l in range(1,4):
                ek=(int(j==k)-int(i==k))
                el=(int(j==l)-int(i==l))
                m[k-1][l-1]+=g*ek*el
    return m


def det2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def main():
    identities=0
    for ni in range(1,18):
        c=Fraction(ni,20)
        for mi in range(1,18):
            t=Fraction(mi,3)
            # Trig-free identity for equality of the two flux balances.
            # (1+a) sin(phi-delta) = sin(phi+delta) when tan(delta)=c*tan(phi).
            a=2*c/(1-c)
            assert (1+a)*(1-c) == 1+c
            assert ((1+c*t*t)**2-(1-c*t*t)**2)==4*c*t*t
            identities+=2
    num=0
    for a in (0.001,0.05,0.3,1.,5.,100.):
        c=a/(2.+a)
        for j in range(1,151):
            phi=(math.pi/2.)*j/152.
            delta=math.atan(c*math.tan(phi))
            g2=(1.+a)*math.cos(phi-delta)
            g4=math.cos(phi+delta)
            h=math.cos(phi)
            delta_prime=c/(math.cos(phi)**2+c*c*math.sin(phi)**2)
            determinant=2*h*(g2+g4)+4*g2*g4
            slope=math.cos(phi)+(1+delta_prime)*math.cos(phi+delta)
            assert abs(determinant-2*(g2+g4)*slope)<1.e-10
            assert g2+g4>0
            num+=2
    prior=.5
    for a in (0., .0001, .001, .01, .1, .5, 1., 2., 3., 10., 100., 10000.):
        kc,z=threshold(a)
        assert kc >= prior-2.e-13, (a,kc,prior)
        if a>0:
            assert kc>prior
            c=a/(a+2.)
            assert z>1.
            assert abs((1.+c*z)**1.5-(1.+c)*(z*z-1.))<1.e-8
            phi=math.atan(math.sqrt(z/c))
            delta=math.atan(c*math.tan(phi))
            assert abs((math.sin(phi)+math.sin(phi+delta))*kc-1.)<1.e-12
            num+=3
        prior=kc
        for mult in (1.0001, 1.01, 1.3, 3.0):
            K=kc*mult
            theta=stationary_angles(a,K)
            residual=max(abs(v) for v in field(theta,a,K))
            assert residual<1.e-10,(a,K,theta,residual)
            H=gauge_hessian(theta,a)
            assert H[0][0] >0 and det2(H)>0 and det3(H)>0,(a,K,H)
            num+=2
    lim_z=(9+math.sqrt(33))/8
    lam=1/((1+2*(math.sqrt(33)-1)/8)*math.sqrt(1-((math.sqrt(33)-1)/8)**2))
    assert abs(lam-.5681261053323405)<1.e-10
    assert abs(threshold(1.e8)[0]-lam)<2.e-8
    slope=(math.sqrt(2)-1)/8
    assert abs((threshold(1.e-5)[0]-.5)/1.e-5-slope)<1.e-5
    print('RATIONAL_FLUX_IDENTITIES_PASS',identities)
    print('STATIONARY_ORBIT_HESSIAN_AND_ALGEBRA_PASS',num)
    print('SMALL_WEIGHT_SLOPE_AND_LIMIT_PASS',round(slope,12),round(lam,12))
    print('ALL_WEIGHT_EXCLUSIONS_AND_GLOBAL_STABILITY_REQUIRE_ANALYTIC_PROOF')

if __name__=='__main__':main()
