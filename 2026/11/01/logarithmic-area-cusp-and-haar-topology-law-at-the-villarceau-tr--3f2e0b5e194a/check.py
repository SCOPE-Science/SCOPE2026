#!/usr/bin/env python3
"""Numerical checks for the area of central planar sections of a solid ring torus.

Requires Python 3, numpy and mpmath. The analytic proof is in RESULT.md;
these finite calculations corroborate selected identities, not their universality.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 45

def section_area(R, r, beta):
    R = mp.mpf(R); r = mp.mpf(r); beta = mp.mpf(beta)
    s = mp.sin(beta)
    lower = mp.mpf(0) if R*s <= r else mp.acos(r/(R*s))
    def f(t):
        h = mp.sqrt(1-s*s*mp.cos(t)**2)
        rad = r*r-R*R*s*s*mp.cos(t)**2
        return h*mp.sqrt(max(mp.mpf(0),rad))
    return 8*R*mp.quad(f,[lower,(lower+mp.pi/2)/2,mp.pi/2])

def raster_area(R,r,beta,gridsize=1600):
    H=R+r
    step=2*H/gridsize
    u=-H+(np.arange(gridsize)+0.5)*step
    c=math.cos(beta);s=math.sin(beta)
    xx=u*c; zz=u*s
    total=0
    for start in range(0,gridsize,100):
        v=u[start:start+100]
        rr=np.sqrt(xx[:,None]**2+v[None,:]**2)
        mask=(rr-R)**2+zz[:,None]**2<=r*r
        total+=int(mask.sum())
    return total*step*step

def test_pair(R, r):
    R=mp.mpf(R);r=mp.mpf(r)
    k=r/R; c=mp.sqrt(1-k*k); b0=mp.asin(k)
    val=4*R*r*c+4*R*R*b0
    a0=section_area(R,r,0)
    a1=section_area(R,r,mp.pi/2)
    ac=section_area(R,r,b0)
    assert abs(a0-4*mp.pi*R*r)<mp.mpf('1e-24')
    assert abs(a1-2*mp.pi*r*r)<mp.mpf('1e-24')
    assert abs(ac-val)<mp.mpf('1e-24')
    C=4*(R*R-r*r)
    E1=mp.mpf('1e-4');E2=mp.mpf('1e-5')
    # Central finite differences of A at two noncritical offsets have
    # logarithmic slope C; the residual is O(epsilon*log epsilon).
    def Q(e): return (section_area(R,r,b0+e)-section_area(R,r,b0-e))/(2*e)
    estimate=(Q(E2)-Q(E1))/mp.log(E2/E1)
    assert abs(estimate/C-1)<mp.mpf('0.002'), (float(estimate),float(C))
    print('R,r',str(R),str(r),'critical angle',mp.nstr(b0,18),
          'critical area',mp.nstr(val,18),'log coefficient',mp.nstr(C,18),
          'slope estimate',mp.nstr(estimate,15))
    for beta in [0.21,0.48,0.72,1.05]:
        radial=float(section_area(R,r,beta))
        grid=raster_area(float(R),float(r),beta)
        assert abs(grid-radial)<0.014*max(1.0,radial), (radial,grid)
    return True

if __name__ == '__main__':
    for R,r in [(2,1),(3,2),(5,1)]:
        test_pair(R,r)
    print('PASS: 3 exact endpoint/critical-area identities per shape; 3 logarithmic coefficient checks; 12 independent raster comparisons.')
