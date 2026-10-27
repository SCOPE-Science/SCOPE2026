"""Deterministic quadrature cross-checks for an asymmetric periodic capture process."""
import math
import numpy as np
from scipy.special import erfc
from scipy.integrate import quad
from scipy.optimize import brentq


def exact(D, L, r, c):
    x = L*math.sqrt(r/D)/2
    s = math.sinh(c*x)/math.sinh(x)
    ds = (c*math.cosh(c*x)*math.sinh(x)-math.sinh(c*x)*math.cosh(x))/math.sinh(x)**2
    en = s/2
    en2 = math.cosh(c*x)*math.cosh(x)/(2*math.sinh(x)**2)
    v = r*L*en
    de = D*(x*x*math.cosh(c*x)*math.cosh(x)/math.sinh(x)**2 + x**3*s*ds/2)
    ent = en/r - (x/(4*r))*ds  # E[N T] = E[N]/r - d E[N]/dr
    return en, en2, ent, v, de


def integrated(D,L,r,c):
    a=L*(1+c)/2
    b=L*(1-c)/2
    def moment(u, order):
        t=u/r
        if not t: return 0.0
        # Tail series for positive and negative integer steps.
        K=max(25,int(math.ceil(7*math.sqrt(2*D*t)/L))+10)
        n=np.arange(1,K+1)
        den=math.sqrt(4*D*t)
        plus=0.5*erfc(((n-1)*L+b)/den)
        minus=0.5*erfc(((n-1)*L+a)/den)
        w=(2*n-1) if order==2 else 1
        return float(np.sum(w*(plus+minus if order==2 else plus-minus)))
    # independent numerical Laplace integrals in u=r*t
    en=quad(lambda z:math.exp(-z)*moment(z,1),0,90,epsabs=2e-11,limit=350)[0]
    en2=quad(lambda z:math.exp(-z)*moment(z,2),0,90,epsabs=2e-11,limit=350)[0]
    ent=quad(lambda z:math.exp(-z)*(z/r)*moment(z,1),0,90,epsabs=2e-11,limit=350)[0]
    v=r*L*en
    de=0.5*r*(L*L*en2-2*v*L*ent+2*v*v/(r*r))
    return en,en2,ent,v,de


def f(x,c):
    return 2/x+c/math.tanh(c*x)-1/math.tanh(x)


def main():
    tests=0
    for D,L,r,c in [(1,1,0.3,0.2), (1,1,3,0.5), (0.8,1.7,2.1,0.7), (3,2,0.4,0.1),(1,1,7,0.9)]:
        e=exact(D,L,r,c)
        q=integrated(D,L,r,c)
        for aa,bb in zip(e,q):
            assert abs(aa-bb)<5e-7*max(1,abs(aa),abs(bb)), (D,L,r,c,aa,bb)
            tests+=1
        xstar=brentq(lambda x:f(x,c),0.1,1000)
        assert f(xstar*0.8,c)>0 and f(xstar*1.2,c)<0
        tests+=1
    for c in [0.05,0.15,0.3,0.55,0.8,0.95]:
        star=brentq(lambda x:f(x,c),0.1,200)
        assert f(star*0.9,c)>0 and f(star*1.1,c)<0
        tests+=1
    for c in [0,0.2,0.5,0.9]:
        D,L=1.0,1.0
        small=exact(D,L,1e-4,c)[4]
        assert small>D
        large=exact(D,L,1e5 if c>0.8 else 1e3,c)[4]
        assert 0<large<D
        tests+=2
    print(f'PASS {tests} independent quadrature, optimization, and crossover assertions')
    for c in (0.1,0.5,0.9):
        xstar=brentq(lambda x:f(x,c),0.1,250)
        print('c=',c,'optimal x=',xstar,'rL2/D=',4*xstar*xstar,'vL/D=',2*xstar*xstar*math.sinh(c*xstar)/math.sinh(xstar))

if __name__=='__main__':main()
