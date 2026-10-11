#!/usr/bin/env python3
"""Standalone finite arithmetic and quadrature checks for a four-frequency torus phase inequality.

The continuous-exponent statements are established by an analytic rearrangement
argument. This script is a finite, supplementary consistency test only.
"""
import cmath
import math
import random
from collections import defaultdict

S = ((0,0),(1,0),(0,1),(1,1))

def moment_even(coeffs, order):
    cur={(0,0):1}
    for _ in range(order):
        nxt=defaultdict(int)
        for (i,j), v in cur.items():
            for (k,l),a in zip(S,coeffs):
                nxt[i+k,j+l]+=v*a
        cur=dict(nxt)
    return sum(abs(v)**2 for v in cur.values())

def moment_grid(amplitudes, phase, p, n=96):
    a,b,c,d=amplitudes
    z_list=[cmath.exp(2j*math.pi*k/n) for k in range(n)]
    dcomplex=d*cmath.exp(1j*phase)
    total=0.0
    for w in z_list:
        aw=a+c*w
        bw=b+dcomplex*w
        for z in z_list:
            total+=abs(aw+bw*z)**p
    return total/(n*n)

def main():
    assertions=0
    assert moment_even((1,1,1,1),2)==36; assertions+=1
    assert moment_even((1,1,1,-1),2)==20; assertions+=1
    assert moment_even((1,1,1,1),3)==400; assertions+=1
    assert moment_even((1,1,1,-1),3)==112; assertions+=1
    rng=random.Random(20261010)
    ps=(.3,.8,1.,1.5,1.999,2.001,2.4,3.,4.,5.,6.5)
    for amplitudes in [(1,1,1,1),(.4,3,2,1.1),(2,1,.7,2.2)] + [tuple(.2+2.8*rng.random() for _ in range(4)) for _ in range(18)]:
        for p in ps:
            sample=[moment_grid(amplitudes, t, p, 64) for t in (0.,math.pi/4,math.pi/2,3*math.pi/4,math.pi)]
            step=[sample[i+1]-sample[i] for i in range(4)]
            assert all(v>1e-10 for v in step) if p<2 else all(v<-1e-10 for v in step), (amplitudes,p,sample)
            assertions+=4
    for amplitudes in [(1.,0.,3.,1.),(0.,1.,2.,3.),(1.,2.,0.,3.),(1.,2.,3.,0.)]:
        for p in (0.3,1.,3.,5.):
            vals=[moment_grid(amplitudes,t,p,64) for t in (0,math.pi/2,math.pi)]
            assert max(vals)-min(vals)<1e-11, (p,amplitudes,vals)
            assertions+=1
    print('FINITE_CHECK_PASS',assertions,'supplementary assertions')

if __name__=='__main__': main()
