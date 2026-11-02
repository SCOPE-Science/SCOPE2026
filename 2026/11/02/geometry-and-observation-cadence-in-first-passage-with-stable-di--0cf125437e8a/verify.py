"""Independent numerical checks for stable-diffusivity wedge first passage.

Requires Python 3.10+, scipy, numpy. The proof is analytical and does not
rely on finite numerical sampling.
"""
import math
from scipy.integrate import quad
from scipy.special import erf, gamma

pi=math.pi

def average_erfs(b, c=None):
    def integrand(t):
        p = erf(b*t)
        if c is not None:
            p *= erf(c*t)
        return 2/math.sqrt(pi)*math.exp(-t*t)*p
    return quad(integrand, 0, 12, epsabs=1e-12, epsrel=1e-12, limit=250)[0]

def wedge_constant(theta, radius, phi, D=1):
    p=pi/(2*theta)
    return (4/pi)*gamma(1+p)/gamma(1+2*p)*(radius*radius/(4*D))**p*math.sin(pi*phi/theta)

def halfplane_survival(t, y, D, sigma, tau):
    n=int(t//tau)
    u=t-n*tau
    h=sigma*(n*math.sqrt(tau)+math.sqrt(max(u,0)))
    return 1.0 if t==0 else (2/pi)*math.atan(y/(math.sqrt(D)*h))

def quadrant_survival(t,x,y,D,sigma,tau):
    n=int(t//tau)
    u=t-n*tau
    h=sigma*(n*math.sqrt(tau)+math.sqrt(max(u,0)))
    if h==0:
        return 1.0
    q=D*h*h
    return (2/pi)*math.atan(x*y/math.sqrt(q*(q+x*x+y*y)))

def check():
    count=0
    for b in [0.01,0.06,0.2,0.5,1,2,5,12]:
        h=(2/pi)*math.atan(b)
        assert abs(average_erfs(b)-h)<8e-12
        count+=1
        for c in [0.02,0.2,0.7,1.7,6.0]:
            q=(2/pi)*math.atan(b*c/math.sqrt(1+b*b+c*c))
            assert abs(average_erfs(b,c)-q)<8e-12, (b,c,q,average_erfs(b,c))
            count+=1
    for x,y,D in [(0.3,1.5,0.5),(1,1,1),(1.5,4,3),(3,2,0.7)]:
        r=math.hypot(x,y)
        ang=math.atan2(y,x)
        assert abs(wedge_constant(pi/2,r,ang,D) - x*y/(pi*D))<1e-11
        assert abs(wedge_constant(pi,r,ang,D) - y/math.sqrt(pi*D))<1e-11
        count+=2
    for x,y,D,sigma,tau in [(1,2,1,1,1),(0.3,3,2,0.7,4),(4,1,1.5,2,0.3)]:
        for n in [20,40,80,160,320,640]:
            t=n*tau
            khalf=2*y*math.sqrt(tau)/(pi*sigma*math.sqrt(D))
            kquad=2*x*y*tau/(pi*D*sigma*sigma)
            s1=halfplane_survival(t,y,D,sigma,tau)
            s2=quadrant_survival(t,x,y,D,sigma,tau)
            assert 0<s1<=1 and 0<s2<=1
            if n>=320:
                assert abs(t*s1/khalf-1)<0.22, (t,s1,khalf)
                assert abs(t*t*s2/kquad-1)<0.22, (t,s2,kquad)
            count+=4
    for n in [1,2,3,5,10,20,50,100,200]:
        # Sparre Andersen lower bound for sensing only at block endpoints.
        b=math.comb(2*n,n)/4**n
        assert b>0 and abs((n**0.5)*b-1/math.sqrt(pi))<0.16
        count+=2
    return count

if __name__=='__main__':
    print('passed', check(), 'independent deterministic numerical and algebraic checks')
