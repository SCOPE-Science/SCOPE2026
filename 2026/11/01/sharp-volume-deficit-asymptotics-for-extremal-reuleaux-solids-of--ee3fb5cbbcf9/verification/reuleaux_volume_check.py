#!/usr/bin/env python3
"""Independent numerical checks of regular Reuleaux revolution volumes.

This finite computation corroborates but does not prove the all-order asymptotic.
Requires numpy and scipy; no network, no external data.
"""
import math
import numpy as np
from scipy.integrate import quad
P=math.pi

def fourier_deficit(n,terms=120):
    def f(theta):
        return sum(-2*(-1)**((j-1)//2)*math.cos(n*j*theta)
                   /(P*j*(1-(n*j)**2)) for j in range(1,2*terms,2))
    def fp(theta):
        return sum(2*n*(-1)**((j-1)//2)*math.sin(n*j*theta)
                   /(P*(1-(n*j)**2)) for j in range(1,2*terms,2))
    knots=np.linspace(0,P,max(4*n+1,101))
    I=sum(quad(lambda t:(fp(t)**2-2*f(t)**2)*math.sin(t),a,b,
               epsabs=3e-10,limit=300)[0] for a,b in zip(knots[:-1],knots[1:]))
    return P*I/2

def disk_volume(n):
    R=1/(2*math.cos(P/(2*n)))
    points=[(R*math.sin(2*P*i/n),R*math.cos(2*P*i/n)) for i in range(n)]
    def radius(z):
        return min(x+math.sqrt(max(0,1-(z-y)**2)) for x,y in points)
    # The defining disk inequality is y-dependent; every disk intersects
    # each axial level in this range. Numerical quadrature is piecewise smooth.
    zlo,zhi=R-1,R
    knots=np.linspace(zlo,zhi,10*n+1)
    volume=P*sum(quad(lambda z:radius(z)**2,a,b,epsabs=3e-10,
                      limit=250)[0] for a,b in zip(knots[:-1],knots[1:]))
    return volume

if __name__=='__main__':
    target=P**3/48
    errors=[]
    for n in (3,5,7,9,11):
        v=disk_volume(n)
        vf=P/6-fourier_deficit(n)
        err=abs(v-vf)
        errors.append(err)
        print(f'n={n}: disk_volume={v:.10f}, support_volume={vf:.10f}, '
              f'absolute_discrepancy={err:.2e}, scaled_gap={(P/6-v)*n*n:.9f}')
        assert err<8e-6, (n,err)
    assert abs((P/6-disk_volume(11))*121-target)<0.005
    print(f'PASS: five independent profile comparisons; target coefficient {target:.10f}')
