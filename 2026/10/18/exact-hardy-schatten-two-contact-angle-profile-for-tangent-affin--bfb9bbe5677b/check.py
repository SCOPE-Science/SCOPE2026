"""Independent numerical diagnostics for an exact Hardy-space Hilbert--Schmidt norm."""
import math
import numpy as np


def exact(a: float, b: float, delta: float) -> float:
    h = 1.0 - math.cos(delta)
    return 1.0 / (2.0 * math.sqrt((1-a)*(1-b)*h * (2*a*b+(1-a)*(1-b)*h)))


def integrate_once(a: float, b: float, delta: float, n: int) -> float:
    t = 2*math.pi*np.arange(n)/n
    p = 1-a+a*np.exp(1j*t)
    den = np.abs(1-(1-b)*np.exp(-1j*delta)*p)**2-b*b*np.abs(p)**2
    assert np.min(den) > 0
    return float(np.mean(1/den))


def integrate_twice(a: float, b: float, delta: float, n: int) -> float:
    t = 2*math.pi*np.arange(n)/n
    ph = (1-a+a*np.exp(1j*t))[:,None]
    ps = np.conjugate(np.exp(1j*delta)*(1-b+b*np.exp(1j*t)))[None,:]
    return float(np.mean(1/np.abs(1-ph*ps)**2))


def check():
    count=0
    for a,b in [(.21,.77),(.4,.6),(.5,.5),(.71,.29),(.92,.88)]:
        for d in [.2,.55,1.2,2.2,math.pi]:
            target=exact(a,b,d)
            val1=integrate_once(a,b,d,65536)
            assert abs(val1/target-1)<2e-11,(a,b,d,target,val1)
            count+=1
            if a<.8 and b<.8:
                val2=integrate_twice(a,b,d,1024)
                assert abs(val2/target-1)<5e-8,(a,b,d,target,val2)
                count+=1
            mirror=exact(b,a,-d)
            assert abs(mirror/target-1)<1e-12
            count+=1
    for a,b in [(.2,.3),(.5,.5),(.7,.8)]:
        coeff=1/(2*math.sqrt(a*(1-a)*b*(1-b)))
        for d in [.05,.025,.0125,.00625]:
            scaled=d*exact(a,b,d)
            assert abs(scaled/coeff-1)<2*d*d
            count+=1
    print(f'PASS: {count} numerical diagnostics; all integrals use independent grids and normalizations.')
    print('Finite diagnostics are not a proof of the operator identity or limiting theorem.')

if __name__=='__main__':
    check()
