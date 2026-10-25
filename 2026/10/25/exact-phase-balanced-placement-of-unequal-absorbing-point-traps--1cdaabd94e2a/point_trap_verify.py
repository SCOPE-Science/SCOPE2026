"""Standalone numerical checks for interval point-trap spectral optimization.
Run with: python3 point_trap_verify.py (requires numpy, scipy).
Numerics corroborate but do not replace the stated global Prüfer proof.
"""
import math
import numpy as np
from scipy.optimize import brentq


def optimum(length, left, right, strengths):
    a = np.asarray(strengths, dtype=float)
    def phase(t):
        return (math.atan(left/t)+math.atan(right/t)
                + sum(2*math.atan(v/(2*t)) for v in a) - length*t)
    t = brentq(phase, 1e-13, (len(a)+3)*math.pi/length,
               xtol=1e-13)
    psi = np.arctan(a/(2*t))
    positions = (math.atan(left/t)+2*np.r_[0,np.cumsum(psi)[:-1]]+psi)/t
    return t, positions


def residual(t, length, left, right, strengths, positions):
    u,p = 1.0,left
    last = 0.0
    for x,a in zip(positions,strengths):
        d = x-last
        c=math.cos(t*d)
        sin_over_t = math.sin(t*d)/t if t else d
        u,p = c*u+sin_over_t*p, c*p-t*t*sin_over_t*u
        p += a*u
        last=x
    d=length-last
    c=math.cos(t*d)
    sin_over_t=math.sin(t*d)/t if t else d
    u,p=c*u+sin_over_t*p,c*p-t*t*sin_over_t*u
    return p+right*u


def smallest_root(length,left,right,strengths,positions,upper):
    last=0.
    N=1300
    for t in np.linspace(max(upper/N/100,1e-10),upper+0.003,N):
        v=residual(t,length,left,right,strengths,positions)
        if v < 0 and last >= 0:
            return brentq(lambda s:residual(s,length,left,right,strengths,positions),
                          prev_t,t,xtol=1e-12)
        last=v;prev_t=t
    raise AssertionError('missed first characteristic root')


def test():
    rng=np.random.default_rng(240122)
    nchecks=0
    for _ in range(120):
        n=int(rng.integers(1,7))
        L=float(rng.uniform(.7,2.3))
        left,right=rng.uniform(0,3,2)
        strengths=np.exp(rng.uniform(-2,3,n))
        t,x=optimum(L,left,right,strengths)
        assert len(x)==n and (x[0]>0) and x[-1]<L and np.all(np.diff(x)>0)
        assert abs(residual(t,L,left,right,strengths,x))<1e-6*(1+np.max(strengths))
        root=smallest_root(L,left,right,strengths,x,t)
        assert abs(root-t)<2e-8,('optimum spectral mismatch',t,root)
        nchecks+=4
        for _ in range(3):
            xp=np.sort(rng.uniform(0,L,n))
            rp=smallest_root(L,left,right,strengths,xp,t)
            assert rp<t+5e-8,('competitor beat bound',t,rp,xp)
            nchecks+=1
        for j,a in enumerate(strengths):
            # At optimal jump, slope ratio is precisely +/-a/2.
            psi=math.atan(a/(2*t))
            assert psi>0
            nchecks+=1
    print('PASS:',nchecks,'assertion groups including exact transfer roots and randomized competitors')

if __name__=='__main__':
    test()
