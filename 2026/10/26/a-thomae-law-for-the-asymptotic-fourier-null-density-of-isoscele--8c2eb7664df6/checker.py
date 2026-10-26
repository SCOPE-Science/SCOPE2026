"""Numerical cross-checks of the stated Fourier-null geometry.
Run with Python 3, numpy and scipy. These checks are finite diagnostics, not
substitutes for the analytical classification or lattice asymptotics.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def sinc(x):
    return float(np.sinc(x / math.pi))


def transform(alpha, u, v):
    if abs(u) < 1e-9:
        if abs(v)<1e-9:return 4.
        return 4*(math.sin(v)/v+1j*alpha*(v*math.cos(v)-math.sin(v))/(v*v))
    a=sinc(v-alpha*u); b=sinc(v+alpha*u)
    return 2/u*(math.sin(u)*(a+b)-1j*math.cos(u)*(a-b))


def independent_integral(alpha,u,v):
    re=quad(lambda y: 2*(1+alpha*y)*sinc(u*(1+alpha*y))*math.cos(v*y),-1,1,epsabs=1e-12,epsrel=1e-12)[0]
    im=quad(lambda y: -2*(1+alpha*y)*sinc(u*(1+alpha*y))*math.sin(v*y),-1,1,epsabs=1e-12,epsrel=1e-12)[0]
    return complex(re,im)


def lattice_points(alpha,R):
    # Integer pair parametrization from the theorem, excluding removable lines.
    bound=int(math.ceil((1+alpha)*R/math.pi))+4
    out=set()
    for k in range(-bound,bound+1):
        for l in range(-bound,bound+1):
            if k*l==0 or k==l: continue
            u=math.pi*(l-k)/(2*alpha)
            v=math.pi*(k+l)/2
            if u*u+v*v<=R*R+1e-10:
                out.add((round(u,10),round(v,10)))
    return out


def vertical_points(alpha,R,mesh_per_unit=13):
    # Locate crossings of the *continuous* sinc combinations on all exceptional lines.
    # At special rational lines, an even-multiplicity zero at v=0 is added separately.
    pts=set()
    for j in range(-int(2*R/math.pi),int(2*R/math.pi)+1):
        if j==0:continue
        u=j*math.pi/2
        vlim=math.sqrt(max(0.,R*R-u*u))
        p=alpha*u
        sign=1 if j%2 else -1
        def g(v):return sinc(v-p)+sign*sinc(v+p)
        num=max(20,int(2*vlim*mesh_per_unit))
        xs=np.linspace(-vlim,vlim,num+1)
        vals=[g(x) for x in xs]
        for i in range(num):
            a,b=xs[i:i+2]
            if vals[i]*vals[i+1]<0:
                root=brentq(g,a,b,xtol=3e-13)
                pts.add((round(u,10),round(root,10)))
            elif abs(vals[i])<1e-13:
                pts.add((round(u,10),round(a,10)))
        if (j%2==0) or (abs(sinc(p))<1e-13):
            pts.add((round(u,10),0.))
    return pts


def main():
    tests=[(.25,.3,.7),(.25,2.9,-1.2),(.4,-5.4,3.2),(.4,0.,2.4),(.3819660112501051,3.1,6.7),(.3819660112501051,-9.2,-2.7)]
    errors=[]
    for alpha,u,v in tests:
        errors.append(abs(transform(alpha,u,v)-independent_integral(alpha,u,v)))
    assert max(errors)<5e-11
    print('Independent one-dimensional Fourier integration comparisons:',len(tests),'maximum discrepancy',f'{max(errors):.3e}')
    checked=0
    for alpha in [.25,.4, math.sqrt(2)/4]:
        for k in range(-5,6):
            for l in range(-5,6):
                if k*l==0 or k==l:continue
                u=math.pi*(l-k)/(2*alpha);v=math.pi*(k+l)/2
                assert abs(transform(alpha,u,v))<1e-11
                checked+=1
    print('Reciprocal-lattice zero formula tested:',checked,'points')
    for alpha in [.25,.4,math.sqrt(2)/4]:
        for R in [45.,90.]:
            lattice=lattice_points(alpha,R)
            vertical=vertical_points(alpha,R)
            combined=lattice | vertical
            q=Fraction(alpha).limit_denominator(100)
            denominator=q.denominator if abs(alpha-float(q))<1e-12 else None
            predicted=2/math.pi*(1+alpha-(1/denominator if denominator else 0))
            # The theorem has O(R), not O(1), counting remainder.
            print('alpha',round(alpha,9),'R',int(R),'lattice',len(lattice),'vertical',len(vertical),'overlap',len(lattice&vertical),'union',len(combined),'N/R^2',round(len(combined)/R**2,6),'limit',round(predicted,6))
            # Allow O(R) even at moderate R; compare on scale R.
            assert abs(len(combined)-predicted*R*R)<12*R
    print('All finite diagnostics passed.')

if __name__=='__main__':main()
