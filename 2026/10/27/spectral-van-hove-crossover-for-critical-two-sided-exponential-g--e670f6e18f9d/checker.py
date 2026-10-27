#!/usr/bin/env python3
"""Independent finite arithmetic checks for exponential-window Zak spectral formulas.
These tests illustrate constants and algebra; the accompanying proof is unrestricted.
"""
import math, cmath
import numpy as np


def zak_direct(a,x,theta):
    return sum(math.sqrt(a)*math.exp(-a*abs(x-k))*cmath.exp(1j*k*theta)
               for k in range(-80,81))


def zak_closed(a,x,theta):
    q=math.exp(-a)
    d=1-2*q*math.cos(theta)+q*q
    return 2*math.sqrt(a)*q*(math.sinh(a*(1-x))+
             cmath.exp(1j*theta)*math.sinh(a*x))/d


def multiplier(a,x,theta):
    q=math.exp(-a)
    d=1-2*q*math.cos(theta)+q*q
    A=math.sinh(a*(1-x));B=math.sinh(a*x)
    return 4*a*q*q*(A*A+B*B+2*A*B*math.cos(theta))/(d*d)


def spectral_constants(a):
    q=math.exp(-a); M=(1+q)/(1-q)
    L=a*4*q/(1-q)**2
    E=a*(1-q)**2/(1+q)**2
    peak=a*M*M
    rho0=(1+q)**3/(4*a*a*q*(1-q))
    bs=L*(.25+2*q/(1-q)**2)
    logc=1/(2*math.pi*a*math.sqrt(L*bs))
    topc=(1-q)/(math.pi*math.sqrt(2)*a**2.5*M*M*math.sqrt(q))
    Ae=2*a*a*(1-q)/(1+q)
    Be=2*E*q/(1+q)**2
    seamc=2/(math.pi*Ae*math.sqrt(Be))
    return L,E,peak,rho0,logc,topc,seamc


def test():
    errors=[]
    for a in (.7,1.0,2.1225501238100715,3.0):
        for x in (.07,.31,.5,.79):
            for theta in (0.19,1.1,2.7,math.pi):
                zd=zak_direct(a,x,theta);zc=zak_closed(a,x,theta)
                errors.append(abs(zd-zc))
                errors.append(abs(abs(zc)**2-multiplier(a,x,theta)))
        L,E,peak,rho0,lc,tc,sc=spectral_constants(a)
        assert 0<L<peak and 0<E<peak
        assert min(rho0,lc,tc,sc)>0
        # Independent local Taylor coefficients near the unique Zak zero.
        h=1e-4
        q=math.exp(-a)
        zx=a*a*(4*a*q/(1+q)**2)
        zt=a*q*(1-q)**2/(1+q)**4
        assert abs(multiplier(a,.5+h,math.pi)/h**2-zx)<.00005*max(1,zx)
        assert abs(multiplier(a,.5,math.pi+h)/h**2-zt)<.00005*max(1,zt)
        # Midpoint integration of the exact spectral multiplier (Parseval mean=1).
        n=750
        xv=(np.arange(n)+.5)/n
        tv=(np.arange(n)+.5)*2*math.pi/n
        Q=math.exp(-a)
        AA=np.sinh(a*(1-xv))[:,None];BB=np.sinh(a*xv)[:,None]
        D=1-2*Q*np.cos(tv)+Q*Q
        HH=4*a*Q*Q*(AA*AA+BB*BB+2*AA*BB*np.cos(tv))/(D*D)
        mean=float(HH.mean())
        assert abs(mean-1)<2e-5,(a,mean)
        print('a',a,'mean',format(mean,'.12f'),'L_saddle',format(L,'.12f'),
              'E_seam',format(E,'.12f'),'peak',format(peak,'.12f'))
        print('coefficients: low',format(rho0,'.10f'),'log',format(lc,'.10f'),
              'upper',format(tc,'.10f'),'seam',format(sc,'.10f'))
    phi=(1+math.sqrt(5))/2
    ac=2*math.asinh(math.sqrt(phi))
    L,E,*_=spectral_constants(ac)
    assert abs(L-E)<1e-12
    assert spectral_constants(ac-.1)[0]>spectral_constants(ac-.1)[1]
    assert spectral_constants(ac+.1)[0]<spectral_constants(ac+.1)[1]
    assert max(errors)<1e-11,max(errors)
    print('critical a',format(ac,'.15f'))
    print('maximum direct-Zak/algebra residual',format(max(errors),'.3g'))
    print('All arithmetic checks passed; no numerical result is used as an infinite proof.')


if __name__=='__main__':
    test()
