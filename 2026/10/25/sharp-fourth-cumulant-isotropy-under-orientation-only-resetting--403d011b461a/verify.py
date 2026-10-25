"""Independent angular-Fourier moment-hierarchy checks for orientation-only resetting.

Requires numpy and scipy. Run: python orientation_cumulant_verify.py
"""
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import solve_ivp


def prediction(q, r, delta, d0, t, phi):
    lam = r + 4*q
    a = r/lam
    b = r/(r + 16*q)
    variance_f = (1 - a*a + (b-a*a)*math.cos(4*phi))/2
    bracket = t/lam + math.expm1(-lam*t)/(lam*lam)
    return (2*(d0+delta*a*math.cos(2*phi))*t,
            24*delta*delta*variance_f*bracket)


def hierarchy(q, r, delta, d0, t, phi):
    # Moments E[Z^2 exp(ik theta)], k=0,+2,-2, and E[Z^4].
    # Reset sends theta to 0 without affecting Z.
    u = lambda k: r/(r+q*k*k)
    ks = (0, 2, -2)
    def rhs(time, y):
        z = [complex(y[2*j], y[2*j+1]) for j in range(3)]
        ans = np.zeros(7)
        for j,k in enumerate(ks):
            force = 2*(d0*u(k) + delta/2*(np.exp(-2j*phi)*u(k+2)+np.exp(2j*phi)*u(k-2)))
            der = -(r+q*k*k)*z[j] + r*z[0] + force
            ans[2*j:2*j+2] = der.real,der.imag
        ans[6] = (12*(d0*z[0] + delta/2*(np.exp(-2j*phi)*z[1] + np.exp(2j*phi)*z[2]))).real
        return ans
    sol = solve_ivp(rhs, (0,t), np.zeros(7),rtol=2e-12,atol=2e-13)
    assert sol.success
    m2, m4 = sol.y[0,-1], sol.y[6,-1]
    return m2, m4 - 3*m2*m2


def main():
    for r in [Fraction(1,3),Fraction(2,1),Fraction(4,1),Fraction(7,1)]:
        q=Fraction(1,1)
        a=r/(r+4*q)
        b=r/(r+16*q)
        assert b-a*a == 8*r*q*(2*q-r)/((r+16*q)*(r+4*q)**2)
    count=0
    for q,r in [(0.4,0.6),(0.4,0.8),(0.4,1.6), (1.3,0.2), (1.3,2.6),(1.3,5.0)]:
        for t in (0.2,1.0,4.5):
            for phi in (0,0.21,math.pi/4,math.pi/2,0.99):
                p=prediction(q,r,0.43,1.19,t,phi)
                h=hierarchy(q,r,0.43,1.19,t,phi)
                for x,y in zip(p,h):
                    assert abs(x-y) <= 2e-8*max(1,abs(x)), (q,r,t,phi,p,h)
                count += 1
    for q in (.3,1.0,2.0):
        for r in (q,2*q,4*q):
            a=r/(r+4*q)
            b=r/(r+16*q)
            caxis=prediction(q,r,.43,1.19,1.1,0)[1]
            cdiag=prediction(q,r,.43,1.19,1.1,math.pi/4)[1]
            diff=caxis-cdiag
            if r==2*q: assert abs(diff)<1e-13
            else: assert diff*(2*q-r)>0
    for angle in np.linspace(0,2*math.pi,33):
        v=prediction(1.0,2.0,0.43,1.19,1.7,float(angle))[1]
        v0=prediction(1.0,2.0,0.43,1.19,1.7,0)[1]
        assert abs(v-v0)<1e-12
    print(f"PASS: {count} independent Fourier-moment ODE comparisons; exact rational threshold identity; direction-switch tests; critical angular invariance.")

if __name__=='__main__': main()
