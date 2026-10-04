#!/usr/bin/env python3
import math, cmath
from math import gcd

def shift(n,p,q):
    return (2*p+math.sqrt(2*n*q*q-2*(n-2)*p*p))**2/(q*q-p*p)

def params(n,D):
    a=math.sqrt(4*n*n-4*(n-4)*D+D*D)
    b=(D-2*n)/a
    return a,b

def reduced_amplitudes(n,D,t):
    # Basis a=(1,-1)/sqrt2 and symmetric block (s,r).
    la=D-2.0
    h11=D+2.0
    h22=2.0*(n-3)
    v=2.0*math.sqrt(2.0*(n-2))
    tau=(h11+h22)/2.0
    gap=math.sqrt((h11-h22)**2+4*v*v)
    z=gap*t/2.0
    c=math.cos(z); s=math.sin(z)
    u_ss=cmath.exp(-1j*tau*t)*(c-1j*((h11-h22)/gap)*s)
    u_rs=cmath.exp(-1j*tau*t)*(-1j*(2*v/gap)*s)
    u_aa=cmath.exp(-1j*la*t)
    amp_target=(u_ss-u_aa)/2.0
    amp_source=(u_ss+u_aa)/2.0
    amp_rest_norm=abs(u_rs)/math.sqrt(2.0)
    return amp_target,amp_source,amp_rest_norm,gap

def main():
    exact=0
    rejected=0
    for n in range(4,13):
        pairs=[(0,1)]
        for q in range(2,9):
            for p in range(-q+1,q):
                if gcd(abs(p),q)==1 and ((p-q)&1):
                    pairs.append((p,q))
        for p,q in pairs:
            D=shift(n,p,q)
            assert D>0
            a,b=params(n,D)
            assert abs(b-p/q)<2e-12,(n,p,q,D,b)
            t=2*math.pi*q/a
            at,asrc,leak,gap=reduced_amplitudes(n,D,t)
            assert abs(abs(at)-1)<2e-10,(n,p,q,D,t,at)
            assert abs(asrc)<2e-10 and leak<2e-10
            assert abs(gap-a)<2e-11
            exact+=1
        # Same-parity reduced p,q are both odd; they cannot satisfy phase parity.
        for p,q in ((1,3),(-1,3),(1,5),(3,5)):
            if abs(p)>=q: continue
            D=shift(n,p,q)
            a,b=params(n,D)
            assert abs(b-p/q)<2e-12
            for s in range(1,10):
                k=q*s
                t=2*math.pi*k/a
                at,asrc,leak,_=reduced_amplitudes(n,D,t)
                assert abs(abs(at)-1)>1e-7
                assert leak<3e-10
                rejected+=1
        D0=shift(n,0,1)
        assert abs(D0-2*n)<3e-12
    print('VERIFY_OK')
    print('exact_parameter_checks =',exact)
    print('same_parity_rejection_checks =',rejected)
    print('source_shift_cases = 9')

if __name__=='__main__':
    main()
