#!/usr/bin/env python3
"""Deterministic geometry checks for regular-polygon angular widths."""
import math
from statistics import mean

PI = math.pi

def geom_width(n, R, theta):
    pts = [(R*math.cos(2*PI*j/n), R*math.sin(2*PI*j/n)) for j in range(n)]
    vals = [x*math.cos(theta) + y*math.sin(theta) for x,y in pts]
    return max(vals)-min(vals)

def params(n, R=1.0):
    m = n if n % 2 == 0 else 2*n
    a = PI/m
    C = 2*R if n % 2 == 0 else 2*R*math.cos(a)
    return a,C

def prediction(n,R,theta):
    a,C=params(n,R)
    offset=a if n%2 else 0.0
    x=((theta-offset+a)%(2*a))-a
    return C*math.cos(x)

def mean_and_cov(a,t):
    mu=math.sin(a)/a
    e=((2*a-t)*math.cos(t)+t*math.cos(2*a-t)+math.sin(2*a-t)+math.sin(t))/(4*a)
    return mu,e-mu*mu

def area_cdf(n,R,z):
    a,C=params(n,R)
    if n%4 == 0:
        lo,hi = C*C*math.cos(a)**2,C*C
        if z <= lo:return 0.
        if z >= hi:return 1.
        return 1-math.acos(math.sqrt(z)/C)/a
    lo,hi=C*C*math.cos(a),C*C*(1+math.cos(a))/2
    if z <= lo:return 0.
    if z >= hi:return 1.
    return 1-math.acos(2*z/(C*C)-math.cos(a))/a

def trap_mean(values):
    return sum(values)/len(values)

def run():
    checked=0
    for n in range(3,31):
        a,C=params(n,1.6)
        for j in range(401):
            t=2*PI*(j+0.19)/401
            v=geom_width(n,1.6,t)
            u=prediction(n,1.6,t)
            assert abs(v-u)<2e-12,('profile',n,j,v,u)
            checked+=1
        for f in (0,0.125,0.34,0.48,0.64,0.98,1.0):
            t=a*f
            M=32768
            xs=[(2*a*(j+.5)/M)-a for j in range(M)]
            widths=[prediction(n,1.6,x) for x in xs]
            shifted=[prediction(n,1.6,x+t) for x in xs]
            joint=trap_mean([x*y for x,y in zip(widths,shifted)])
            mu,cov=mean_and_cov(a,t)
            assert abs(joint-C*C*(cov+mu*mu))<2e-9,('corr',n,t,joint,cov)
            checked+=1
        for p in (.05,.25,.5,.75,.95):
            M=12000
            zs=sorted(geom_width(n,1.6,2*a*(j+.37)/M)*geom_width(n,1.6,2*a*(j+.37)/M+PI/2) for j in range(M))
            # analytic quantile read off CDF numerical from observed quantile
            empirical=zs[int(p*M)]
            cdf=area_cdf(n,1.6,empirical)
            assert abs(cdf-p)<0.002,('area cdf',n,p,cdf)
            checked+=1
    print('PASS',checked,'independent vertex/continuum-correlation/random-rectangle checks')
    # high precision edge correlation and limiting quartic
    import mpmath as mp
    mp.mp.dps=90
    for m in (6,10,18,30,100,300,1000):
        a=mp.pi/m
        mu=mp.sin(a)/a
        variance=mp.mpf('0.5')+mp.sin(2*a)/(4*a)-mu*mu
        covariance=mp.cos(a)/2+mp.sin(a)/(2*a)-mu*mu
        rho=covariance/variance
        assert rho < -mp.mpf(7)/8
        print('m=',m,'anticorrelation=',mp.nstr(rho,25))
    def Q(u):return 1-mp.mpf(15)/8*u**4+mp.mpf(15)/2*u**3-mp.mpf(15)/2*u**2
    root=mp.findroot(Q,(mp.mpf('.45'),mp.mpf('.55')))
    print('universal zero=',mp.nstr(root,35))
    print('universal antipodal correlation=',Q(1))
if __name__ == '__main__': run()
