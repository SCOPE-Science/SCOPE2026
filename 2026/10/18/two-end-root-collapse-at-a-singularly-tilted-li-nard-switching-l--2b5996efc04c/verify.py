#!/usr/bin/env python3
"""Numerical diagnostics for a planar crossing-averaging formula.
The universal result is proved analytically; sampled checks do not prove it.
Requires Python 3 standard library only.
"""
from math import sin,cos,pi,comb,sqrt

def alpha(j):
    return comb(2*j,j)/(4**j*(j+1))

def average(r,phi,f_even,g_even):
    s=sin(phi)
    odd=sum(.5*alpha(j)*c*r**(2*j+1) for j,c in enumerate(f_even))
    even=sum((2/pi)*c*s**(2*j+1)*r**(2*j)/(2*j+1) for j,c in enumerate(g_even))
    return odd+even

def integrate_piecewise(func,cut1,cut2,steps=6000):
    # Smooth panels separated at both switching events.
    cuts=sorted({0.0, 2*pi, cut1%(2*pi), cut2%(2*pi)})
    z=0.0
    for u,v in zip(cuts,cuts[1:]):
        h=(v-u)/steps
        z+=h*sum(func(u+(k+.5)*h) for k in range(steps))
    return z

def raw_average(r,phi,f_even,g_even):
    def func(t):
        xx=r*cos(t)
        damp=r*sin(t)**2*sum(c*xx**(2*j) for j,c in enumerate(f_even))
        force=sin(t)*(1 if cos(t-phi)>=0 else -1)*sum(c*xx**(2*j) for j,c in enumerate(g_even))
        return damp+force
    return integrate_piecewise(func,phi-pi/2,phi+pi/2)/(2*pi)

def bisect(f,a,b,iterations=100):
    fa=f(a);fb=f(b)
    assert fa*fb<0,(a,b,fa,fb)
    for _ in range(iterations):
        m=(a+b)/2; fm=f(m)
        if fa*fm<=0:b=m;fb=fm
        else:a=m;fa=fm
    return (a+b)/2

counter=0
for phi in (0.07,0.3,1.0,pi/2,-0.27):
    for j in range(7):
        for r in (0.4,1.2):
            v=average(r,phi,[0],[0]*j+[1]); w=raw_average(r,phi,[0],[0]*j+[1]);
            assert abs(v-w)<8e-7*(1+abs(v)),('g',phi,j,r,v,w)
            counter+=1
    for j in range(5):
        for r in (0.4,1.2):
            v=average(r,phi,[0]*j+[1],[0]); w=raw_average(r,phi,[0]*j+[1],[0]);
            assert abs(v-w)<8e-7*(1+abs(v)),('f',phi,j,r,v,w)
            counter+=1

# Fixed f=1 and g=-1-x^(2q) produce one collapsing and one escaping root.
for q in (1,2,3,4):
    for s in (0.02,0.008,0.003):
        phi=__import__('math').asin(s)
        gg=[-1]+[0]*(q-1)+[-1]
        f=lambda r:average(r,phi,[1],gg)
        inn=bisect(f,.001*s,10*s)
        predicted_inner=4/pi*s
        assert abs(inn/predicted_inner-1)<.04,(q,s,inn,predicted_inner)
        predicted_outer=(pi*(2*q+1)/4)**(1/(2*q-1))*s**(-(2*q+1)/(2*q-1))
        out=bisect(f,predicted_outer*.6,predicted_outer*1.4)
        assert abs(out/predicted_outer-1)<.06,(q,s,out,predicted_outer)
        assert inn>0 and out>inn
        assert f(inn*.8)<0 and f(inn*1.2)>0
        assert f(out*.8)>0 and f(out*1.2)<0
        counter+=6

# Generic even damping f(x)=1-5x^2+4x^4, g(x)=-1-x^8:
# two finite damping roots plus one inner and one outer (p=2, q=4).
f_even=[1,-10,4]; g_even=[-1,0,0,0,-1]
for s in (0.03,0.015):
    phi=__import__('math').asin(s)
    f=lambda r:average(r,phi,f_even,g_even)
    # damping polynomial 1-5*(alpha_1/alpha_0)*r^2+4*(alpha_2/alpha_0)*r^4
    import math
    A1=alpha(1)*(-10); A2=alpha(2)*4
    discr=A1*A1-4*A2
    assert discr>0
    roots=[sqrt((-A1 +sign*sqrt(discr))/(2*A2)) for sign in (-1,1)]
    positions=[bisect(f,.01*s,10*s)]
    for rf in roots:
        positions.append(bisect(f,rf*.9,rf*1.1))
    exponent=(2*4+1)/(2*(4-2)-1)
    target=(-.5*alpha(2)*4/((2/pi)*(-1)/9))**(1/3)*s**(-exponent)
    positions.append(bisect(f,.5*target,1.5*target))
    assert len(positions)==4 and positions==sorted(positions)
    counter+=6
print(f'PASS {counter} diagnostic assertions; universal statements rely on analytical proof')
