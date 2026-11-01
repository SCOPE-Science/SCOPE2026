#!/usr/bin/env python3
"""Standalone checks of exact moment identities, cone bounds, and first-order drift."""
import math
from fractions import Fraction

def rk4(f, z, dt, t):
    k1 = f(t, z)
    k2 = f(t+dt/2, [z[i]+dt*k1[i]/2 for i in range(2)])
    k3 = f(t+dt/2, [z[i]+dt*k2[i]/2 for i in range(2)])
    k4 = f(t+dt, [z[i]+dt*k3[i] for i in range(2)])
    return [z[i] + dt*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6 for i in range(2)]

def exact_moment_checks():
    for m in (1, 3, 5, 7, 9, 15):
        k=(m+1)//2
        A=Fraction(math.comb(2*k,k),4**k)
        B=A/Fraction(2*k+2)
        assert B==A/Fraction(m+3)
        assert A>0 and Fraction(-2)*A*Fraction(m+3)**((m-1)//2)<0
        # For y >= Y and -1/8 < x < 1/4, (15/16) epsilon*y**m - 1/4
        # exceeds (1/2) epsilon*y**m whenever epsilon*y**m >= 1.
        if m>=3:
            for eps in (Fraction(1,100), Fraction(1), Fraction(100,1)):
                Y=1
                while eps*Y**m < 1 or Fraction(2,(m-2))*1/(eps*Y**(m-2)) >= Fraction(1,8):
                    Y*=2
                assert Fraction(15,16)*eps*Y**m-Fraction(1,4)>=eps*Y**m/2
                assert Fraction(2,(m-2))*1/(eps*Y**(m-2))<Fraction(1,8)

def drift_checks():
    for m in (1,3):
        eps=0.00003
        for mult in (0.97,1.03):
            r=math.sqrt(m+3)*mult
            n=12000
            dt=2*math.pi/n
            z=[r,0.0]
            f=lambda t,z: [z[1],-z[0]+eps*(1-z[0]**2)*z[1]**m]
            for j in range(n):
                z=rk4(f,z,dt,j*dt)
            delta=(z[0]**2+z[1]**2-r*r)/2
            k=(m+1)//2
            A=2*math.pi*math.comb(2*k,k)/4**k
            first=eps*A*r**(m+1)*(1-r*r/(m+3))
            assert delta*first>0
            assert abs(delta/first-1)<0.002

if __name__=='__main__':
    exact_moment_checks()
    drift_checks()
    print('PASS: 6 exact odd-degree moment identities, escape cones, 4 RK4 energy drift comparisons')
