#!/usr/bin/env python3
"""Finite corroboration for the Bessel-weighted Dirichlet series boundary law."""
import math
import mpmath as mp
from scipy.special import i0e

def K(a):
    return (4*math.pi)**(-len(a)/2)*math.prod(x**(-0.5) for x in a)

def h(u,a):
    return math.prod(float(i0e(2*x*u)) for x in a)

def check():
    tests=0
    for a in [[0.75],[0.5,0.9],[0.5,0.7,1.1],[0.5,0.8,1.1,1.3],[0.5,0.7,0.9,1.1,1.5]]:
        beta=len(a)/2
        norms=[]
        for u in [8,16,32,64,128]:
            v=h(u,a)*u**beta/K(a)
            assert v>0 and math.isfinite(v)
            norms.append(abs(v-1))
            tests+=2
        assert norms[-1]<norms[0], (a,norms)
        tests+=1
        assert norms[-1]<0.08, (a,norms[-1])
        tests+=1
    mp.mp.dps=55
    for d in (1,2,3,4):
        beta=mp.mpf(d)/2
        vals=[]
        for delta in (mp.mpf('1e-3'),mp.mpf('1e-5'),mp.mpf('1e-7')):
            if d in (1,2):
                val=delta**(beta-1)*mp.gammainc(1-beta,delta,mp.inf)
                target=mp.sqrt(mp.pi)*delta**(-mp.mpf('0.5')) if d==1 else mp.log(1/delta)
            else:
                val=mp.quad(lambda u: (1-mp.exp(-delta*u))*u**(-beta),[1,1/delta,mp.inf])
                target=2*mp.sqrt(mp.pi)*mp.sqrt(delta) if d==3 else delta*mp.log(1/delta)
            vals.append(float(abs(val/target-1)))
            tests+=1
        assert vals[-1]<vals[0],(d,vals)
        assert vals[-1]<0.10,(d,vals)
        tests+=2
    for n in (2,3,5,11,97):
        for a in ([0.5],[0.6,1.2],[0.5,0.9,1.1]):
            u=math.log(n)
            exact=math.prod(float(mp.besseli(0,2*x*u))*math.exp(-2*x*u) for x in a)
            assert abs(exact-h(u,a))<5e-13
            tests+=1
            for x in a:
                b=float(mp.besseli(0,2*x*u))
                t=sum((x*u)**(2*m)/math.factorial(m)**2 for m in range(45))
                assert abs(t/b-1)<5e-12
                tests+=1
    print(f'PASS: {tests} finite analytical-identity and asymptotic corroborations.')
if __name__=='__main__':check()
