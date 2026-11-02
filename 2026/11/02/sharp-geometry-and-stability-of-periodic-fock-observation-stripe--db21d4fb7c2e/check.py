#!/usr/bin/env python3
"""Supplementary finite tests for sharp periodic Gaussian observation stripes.
Run: python3 check.py. Uses only Python's standard library.
The all-measurable-set results require the accompanying analytic proof.
"""
import math
PI=math.pi
C=math.sqrt(2*PI)
checks=0

def near(a,b,tol=1e-9):
    global checks
    checks+=1
    assert math.isfinite(a) and math.isfinite(b) and abs(a-b)<tol, (a,b,tol)

def yes(cond):
    global checks
    checks+=1
    assert cond

def K(x,L):
    return math.sqrt(2)*sum(math.exp(-2*PI*(x+j*L)**2) for j in range(-12,13))

def H(intervals,t,L):
    # Integral of periodized normalized Gaussian over disjoint closed intervals.
    result=0.0
    for a,b in intervals:
        result+=0.5*sum(math.erf(C*(t-a-j*L))-math.erf(C*(t-b-j*L)) for j in range(-10,11))
    return result

def I_intervals(w,L):
    return [(0,w/2),(L-w/2,L)]

def delta_minus(m,L,w):
    if m<=0: return 0
    d=(L-w)/2
    n=1200; h=(m/2)/n
    return 2*h*sum(K(d-(i+.5)*h,L)-K(d+(i+.5)*h,L) for i in range(n))

def delta_plus(m,L,w):
    if m<=0: return 0
    d=w/2
    n=1200; h=(m/2)/n
    return 2*h*sum(K(d-(i+.5)*h,L)-K(d+(i+.5)*h,L) for i in range(n))

for L,rho in [(1.6,.17),(2.7,.42),(4.,.65),(3.,.37)]:
    w=L*rho
    interval=I_intervals(w,L)
    a=H(interval,L/2,L)
    b=H(interval,0,L)
    yes(0<a<rho<b<1)
    for j in range(1,199):
        t=L*j/200
        p=H(interval,t,L)
        yes(a-3e-13<=p<=b+3e-13)
        near(K(t,L),sum(math.exp(-PI*n*n/(2*L*L))*math.cos(2*PI*n*t/L) for n in range(-80,81))/L,2e-10)
    # An arbitrary disconnected mask, using an exact piecewise interval convolution.
    E=[(.04*L,.04*L+.4*w),(.5*L,.5*L+.6*w)]
    for j in range(200):
        t=L*j/200
        h=H(E,t,L)
        yes(a-1e-12<=h<=b+1e-12)
        # Interval minimizing H at t is the arc of length w around t+L/2.
        # Compute exact symmetric difference with that interval by fine Riemann meshes.
        N=20000
        c=0
        for i in range(N):
            x=(i+.5)*L/N
            in_E=any(l<=x<r for l,r in E)
            y=((x-(t+L/2)+L/2)%L)-L/2
            in_min=abs(y)<w/2
            c+=in_E!=in_min
        m_t=c*L/(2*N)
        # Grid error for boundary intersections is at most 4*L/N.
        # Use a conservative lower mismatch bound.
        m_lower=max(0,m_t-5*L/N)
        yes(h>=a+delta_minus(m_lower,L,w)-2e-10)
    for m in [w/7, min(w,L-w)/2, min(w,L-w)*.9]:
        yes(delta_minus(m,L,w)>0 and delta_plus(m,L,w)>0)
    if L==3 and rho==.37:
        for m_cells in [3,4,6,7]:
            ell=L/m_cells
            Es=[]
            for k in range(m_cells):
                Es.append((k*ell,(k+rho)*ell))
            hvals=[H(Es,L*j/997,L) for j in range(997)]
            u=math.exp(-PI*m_cells*m_cells/(2*L*L))
            amp=2*math.sin(PI*rho)/PI*u
            rem=sum(2*abs(math.sin(PI*k*rho))/(PI*k)*u**(k*k) for k in range(2,21))
            yes(abs(max(hvals)-(rho+amp))<=rem+1e-8)
            yes(abs(min(hvals)-(rho-amp))<=rem+1e-8)
            near(sum((max(hvals),min(hvals)))/2,rho,rem+1e-8)

# Large-period erosion: exact erfc-integrated tails, no subtraction near one.
for L in [3.5,4.5,5.5,6.5]:
    rho=.37; w=L*rho; gap=L-w
    lower=sum(math.erfc(C*(gap/2+j*L))-math.erfc(C*(gap/2+w+j*L)) for j in range(8))
    near(lower,H(I_intervals(w,L),L/2,L),max(1e-14,lower*1e-8))
    asym=math.sqrt(2)/(PI*gap)*math.exp(-PI*gap*gap/2)
    yes(.6<lower/asym<1.1)

print('PASS',checks,'supplementary finite assertions')
