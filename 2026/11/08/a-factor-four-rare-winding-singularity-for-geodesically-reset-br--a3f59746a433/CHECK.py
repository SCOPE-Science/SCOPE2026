#!/usr/bin/env python3
"""Finite diagnostics for a Brownian ring with shortest-arc Poisson returns.
This is a numerical consistency check, not an infinite-time proof.
"""
import math


def transform(s, rate, diffusivity, circumference):
    if rate == 0:
        return 1 / math.cosh(circumference * math.sqrt(s / diffusivity))
    z = circumference * math.sqrt((rate + s) / diffusivity) / 2
    return (rate * math.cosh(z) + s) / (rate * math.cosh(z) + s * math.cosh(2*z))


def spectral_exponent(k, rate, diffusivity, circumference):
    if k == 0: return 0.
    if rate == 0: return diffusivity * (k / circumference)**2
    objective = 1 / math.cosh(k)
    low, high = 0., 1.
    while transform(high, rate, diffusivity, circumference) > objective:
        high *= 2
    for _ in range(85):
        middle = (low + high)/2
        if transform(middle, rate, diffusivity, circumference) > objective:
            low = middle
        else:
            high = middle
    return (low + high)/2


def thomas(a,b,c,d):
    n=len(b)
    b=b[:];c=c[:];d=d[:]
    for i in range(1,n):
        m=a[i]/b[i-1]
        b[i] -= m*c[i-1]
        d[i] -= m*d[i-1]
    out=[0.]*n
    out[-1]=d[-1]/b[-1]
    for i in range(n-2,-1,-1):
        out[i]=(d[i]-c[i]*out[i+1])/b[i]
    return out


def finite_difference_transform(s,r,D,L,N=600):
    h=L/N;v=D/h**2
    a=[0.]*N;b=[0.]*N;c=[0.]*N;d=[0.]*N;e=[0.]*N
    b[0]=2*v+s;c[0]=-2*v
    for i in range(1,N):
        a[i]=-v;b[i]=2*v+s+r
        if i<N-1: c[i]=-v
        if i*h<L/2: e[i]=r
        else: d[i]=r
    d[-1]+=v
    independent=thomas(a,b,c,d)
    response=thomas(a,b,c,e)
    return independent[0]/(1-response[0])


def main():
    count=0
    def check(condition,message):
        nonlocal count
        assert condition,message
        count+=1
    cases=[(1.,2.,1.,1.),(1.,2.,0.,1.),(2.,3.,.4,.7),(.7,3.7,.4,.8),
           (3.,2.,2.,4.),(1.5,4.5,.2,.1),(.8,1.2,2.5,3.)]
    for D,L,r,s in cases:
        exact=transform(s,r,D,L)
        approx=finite_difference_transform(s,r,D,L)
        check(0<exact<1,"range of Laplace transform")
        check(abs(approx-exact)<0.006,"independent numerical boundary-value solution")
        check(transform(2*s,r,D,L)<exact,"strict Laplace monotonicity")
        for k in (0.3,1.1,3.5):
            v=spectral_exponent(k,r,D,L)
            check(abs(transform(v,r,D,L)*math.cosh(k)-1)<1.e-11,"renewal-pole equation")
            check(v>=0,"nonnegative scaled CGF")
            check(abs(v-spectral_exponent(-k,r,D,L))<1.e-12,"reflection symmetry")
        if r==0:
            for k in (1.0,2.0,3.0):
                check(abs(spectral_exponent(k,0,D,L)-D*(k/L)**2)<1.e-12,"free-ring exponent")
    for D,L,r in [(1.,2.,.1),(1.,2.,1.),(1.,4.,.6),(2.,3.,.4)]:
        k=180.
        v=spectral_exponent(k,r,D,L)
        a=4*D/L**2
        q=(L/2)*math.sqrt((v+r)/D)
        estimate=k-2*math.log(k)+math.log(r/(2*a))
        check(abs(q-estimate)<.3,"high-current log-corrected scale")
        check(0.7 < v/(a*k*k) < 1.02,"positive-reset leading coefficient")
        check(v > spectral_exponent(k,0,D,L),"asymptotic enhancement")
    for k in (.4,1.3,3.):
        v0=spectral_exponent(k,0,1.,2.)
        v=spectral_exponent(k,1.e-7,1.,2.)
        check(abs(v-v0)<1.e-5,"fixed-tilt zero-rate limit")
    for D,L,r in [(1.,2.,.1),(1.,2.,2.),(2.,3.,.4)]:
        z=L*math.sqrt(r/D)/2
        mean=2*(math.sinh(z)**2)/(r*math.cosh(z))
        k=.0005
        check(abs(2*spectral_exponent(k,r,D,L)/k**2-1/mean)<0.001,"mean inter-turn time and CLT coefficient")
    print('PASS:',count,'finite numerical assertions (not an infinite-time proof)')

if __name__=='__main__': main()
