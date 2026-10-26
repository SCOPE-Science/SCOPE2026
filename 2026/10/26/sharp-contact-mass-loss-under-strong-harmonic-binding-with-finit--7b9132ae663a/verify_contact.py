#!/usr/bin/env python3
"""Independent finite checks for the analytic finite-tumble contact-mass asymptotic.

Run: python verify_contact.py
No numerical test replaces the proof of the limiting claim.
"""
from fractions import Fraction as F
from math import exp, log1p, pi

states = ('+2', '+1', '0s', '0t', '-1', '-2')

def model(a, b):
    zero=F(0)
    Q=[[zero for _ in states] for _ in states]
    for i,j,r in [(0,1,2*a),(1,0,b/2),(1,2,b/2),(1,3,a),
                  (2,1,a),(2,4,a),(3,1,b),(3,4,b),
                  (4,2,b/2),(4,3,a),(4,5,b/2),(5,4,2*a)]:
        Q[i][j]=r
    for i in range(6):Q[i][i]=-sum(Q[i])
    den=(a+b)**2
    stationary=[b*b/(4*den),a*b/den,b*b/(2*den),a*a/den,
                a*b/den,b*b/(4*den)]
    return Q,stationary

def simpson(f, lo, hi, n=4000):
    assert n%2==0
    h=(hi-lo)/n
    return (f(lo)+f(hi)+sum((4 if k%2 else 2)*f(lo+h*k) for k in range(1,n)))*h/3

def integral_dilog(k):
    return simpson(lambda u: log1p(k*exp(-u)),0,40)

def k_closed(a,b):
    af=float(a);bf=float(b)
    return pi*pi*af*af*bf*bf/(32*(af+bf)**2)*(1+bf/(4*af)+af/(2*bf))

def k_flux(a,b):
    Q,stationary=model(a,b)
    B=1+Q[4][2]/(-Q[2][2])+Q[4][3]/(-Q[3][3])
    return float(stationary[1]*(Q[1][2]*Q[2][4]+Q[1][3]*Q[3][4])*B)*integral_dilog(1)/4

def main():
    tests=0
    for ni in range(1,11):
      for nj in range(1,11):
        a=F(ni,4);b=F(nj,5)
        Q,p=model(a,b)
        assert sum(p)==1; tests+=1
        assert all(sum(row)==0 for row in Q);tests+=1
        assert all(sum(p[i]*Q[i][j] for i in range(6))==0 for j in range(6));tests+=1
        assert p[0]+p[1]==p[4]+p[5];tests+=1
        assert abs(k_closed(a,b)-k_flux(a,b))<1e-8;tests+=1
    assert abs(integral_dilog(1)-pi*pi/12)<3e-9;tests+=1
    assert k_closed(F(1),F(1))>0;tests+=1
    print('PASS',tests,'exact rational/numerical checks')
    print('K(alpha=beta=1)=',repr(k_closed(F(1),F(1))))
    print('Integral log(1+e^-u)=',repr(integral_dilog(1)))

if __name__=='__main__':main()
