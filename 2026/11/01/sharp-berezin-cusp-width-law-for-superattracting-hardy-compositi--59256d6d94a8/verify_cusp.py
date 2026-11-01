"""Supplementary numerical test of Hardy composition Berezin cusp cross-sections.
No finite run is asserted to certify the asymptotic theorem.
"""
import math
import cmath
import numpy as np
from scipy.optimize import brentq

def berezin(r, theta, coefficients):
    z = r*cmath.exp(1j*theta)
    phi = sum(c*z**k for k,c in coefficients.items())
    return (1-r*r)/(1-z.conjugate()*phi)

def section(delta, coefficients, ntheta=720):
    hs=[]
    for theta in np.linspace(0,2*math.pi,ntheta,endpoint=False):
        r=brentq(lambda r: 1-berezin(r,theta,coefficients).real-delta,0,0.85,xtol=1e-14)
        hs.append(berezin(r,theta,coefficients).imag)
    return min(hs),max(hs)

def run():
    count=0
    cases=[{2:.45+0.20j,3:.06-0.08j},{3:-.52j,4:.09+.02j},{4:.6,5:-.12j},{5:-.31+.22j,6:.1}]
    for coeff in cases:
        m=min(coeff)
        a=abs(coeff[m]); gamma=(m+1)/2
        values=[]
        for delta in (1e-2,3e-3,1e-3,3e-4,1e-4):
            lo,hi=section(delta,coeff)
            x=(hi-lo)/(2*delta**gamma)
            # finite-grid and finite-delta errors, not a proof of limits
            assert x>0 and abs(x-a)<.25
            assert lo<0<hi
            values.append((delta,x))
            count+=2
        assert abs(values[-1][1]-a)<abs(values[0][1]-a)+.03
        count+=1
        print(f'order={m} |first|={a:.9f} width-scaled-endpoint={values[-1][1]:.9f} deviation={values[-1][1]-a:+.3g}')
    print(f'passed assertions: {count}')
if __name__=='__main__':run()
