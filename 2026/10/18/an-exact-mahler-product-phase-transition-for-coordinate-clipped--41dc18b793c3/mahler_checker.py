"""Independent numerical checks for the exact volume-product phase law.
Run: python mahler_checker.py (requires scipy). The proof is analytic;
these finite tests are diagnostics, not substitutes for the proof.
"""
from math import gamma, cos, sin, pi
from scipy.integrate import quad
from scipy.optimize import brentq

def ball_volume(n,p):
    return (2*gamma(1+1/p))**n/gamma(1+n/p)

def components(n,p,a):
    m=n-1; q=p/(p-1); v=1-a**p
    F=quad(lambda x:(1-x**p)**(m/p),0,a,epsabs=2e-12)[0]
    G=quad(lambda x:(1-x**q)**(m/q),0,a**(p-1),epsabs=2e-12)[0]
    H=G+v**(1+m/q)/(n*a)
    return F,G,H

def volume_product(n,p,a):
    F,G,H=components(n,p,a)
    return 4*ball_volume(n-1,p)*ball_volume(n-1,p/(p-1))*F*H

def stationarity(n,p,a):
    F,G,H=components(n,p,a)
    return n*a*a*(1-a**p)**((n-1)*(2-p)/p)*H-F

def polar_area_angular(p,a):
    q=p/(p-1)
    def integrand(theta):
        x,y=cos(theta),sin(theta)
        h0=(x**q+y**q)**(1/q)
        xopt= (x/h0)**(q-1)
        h=h0 if xopt<=a else x*a+y*(1-a**p)**(1/p)
        return 1/(h*h)
    return 2*quad(integrand,0,pi/2,epsabs=1e-11,points=[0.0,pi/4,pi/2])[0]

if __name__=='__main__':
    for n,p in [(2,1.1),(2,1.5),(2,1.9),(2,2.0),(2,3.0),(3,1.5),(3,2.0),(4,1.5)]:
        if p<2:
            a=brentq(lambda a:stationarity(n,p,a),0.02,0.9999999999,xtol=1e-13)
            step=min(1e-4,(1-a)/4)
            assert stationarity(n,p,a-step)>0
            assert stationarity(n,p,a+step)<0
            if step>=1e-5:
                assert volume_product(n,p,a)>volume_product(n,p,a+step)-1e-11
                assert volume_product(n,p,a)>volume_product(n,p,a-step)-1e-11
        else:
            a=None
            assert all(stationarity(n,p,x)>0 for x in [0.02,0.2,0.5,0.8,0.98])
        print('n=%d p=%g a*=%s P=%0.12f'%(n,p, 'none' if a is None else '%.12f'%a,volume_product(n,p,a or 0.8)))
    for p,a in [(1.1,0.4),(1.5,0.75),(2,0.3),(3,0.9),(6,0.65)]:
        F,G,H=components(2,p,a)
        polar_formula=4*H
        polar_independent=polar_area_angular(p,a)
        print('polar p=%g a=%g two_methods=%.12f %.12f'%(p,a,polar_formula,polar_independent))
        assert abs(polar_formula-polar_independent)<2e-8
    from math import pi
    for a in [0.2,0.3,0.6,0.9]:
        assert abs(volume_product(3,2,a)-(4*pi*pi/9)*(3+2*a*a-a**4))<2e-11
    print('all checks passed')
