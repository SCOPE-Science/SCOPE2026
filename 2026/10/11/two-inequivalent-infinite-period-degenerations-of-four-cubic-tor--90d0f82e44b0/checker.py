"""Standalone numerical checks for an exact cubic-torus return theorem.

The analytic proof is contained in RESULT.md; finite checks do not certify all parameters.
"""
import math


def fields(x, y, z, a, lam, eta, c):
    k = lam + eta * z
    return (k*z*x/4 + c*x*y*y,
            k*z*y/4 - c*x*x*y,
            k*(-a*a*(x*x+y*y) + z*z + a**4-1)/2)


def period(a, lam, eta):
    A = a*a
    D = lam*lam + (A*A-1)*eta*eta
    return 4*math.pi/D*(lam/math.sqrt(A*A-1) + A*eta*eta/math.sqrt(lam*lam-eta*eta))


def quadrature(a, lam, eta, n=12000):
    h = 2*math.pi/n
    def f(phi):
        return 2/((a*a+math.cos(phi))*(lam+eta*math.sin(phi)))
    total = f(0) + f(2*math.pi)
    for k in range(1,n):
        total += (4 if k%2 else 2)*f(k*h)
    return total*h/3


def main():
    for a, lam, eta, c in [(2.,3.,1.,1.),(1.2,2.,1.5,.3),(1.01,4.,2.,1.),(2.,1.01,1.,2.)]:
        # Confirm polynomial invariance as an identity at several off-torus points.
        for x,y,z in [(.3,.7,-.2),(1.8,-1.2,.4),(-.9,.4,-.6)]:
            P,Q,R=fields(x,y,z,a,lam,eta,c)
            r2=x*x+y*y
            F=(r2-a*a)**2+z*z-1
            dotF=4*(r2-a*a)*(x*P+y*Q)+2*z*R
            assert abs(dotF-(lam+eta*z)*z*F) < 2.e-10*max(1,abs(dotF))
        T=period(a,lam,eta)
        Tn=quadrature(a,lam,eta)
        assert abs(T-Tn) < 1.e-8*max(1,abs(T))
        # Exact holonomy exponent is the integral of log(tan theta) derivative.
        mu=-4*math.pi*c/math.sqrt(lam*lam-eta*eta)
        h=2*math.pi/12000
        I=h/3*(1/(lam+eta*math.sin(0))+1/(lam+eta*math.sin(2*math.pi))+
               sum((4 if j%2 else 2)/(lam+eta*math.sin(j*h)) for j in range(1,12000)))
        assert abs(mu+2*c*I) < 1.e-8*max(1,abs(mu))
    a,eta,c=2.0,1.0,1.0
    constant=4*math.pi/(a*a*math.sqrt(2*eta))
    for delta in [1.e-3,1.e-4,1.e-5]:
        T=period(a,eta+delta,eta)
        assert abs(T*math.sqrt(delta)/constant -1)< 0.045
        chi=(-4*math.pi*c/math.sqrt((eta+delta)**2-eta**2))/T
        assert abs(chi+c*a*a)<0.045*c*a*a
    lam,eta=3.,1.
    for a in [1.01,1.001,1.0001]:
        scaled=period(a,lam,eta)*math.sqrt(a**4-1)
        assert abs(scaled/(4*math.pi/lam)-1)<0.05
        chi=(-4*math.pi*c/math.sqrt(lam*lam-eta*eta))/period(a,lam,eta)
        assert abs(chi)<0.3
    print('CHECK_OK')


if __name__=='__main__':
    main()
