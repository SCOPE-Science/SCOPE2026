#!/usr/bin/env python3
"""Independent numerical probes of the two-channel Hermite Zak energy.

All infinite claims in the accompanying result rely on analytic arguments,
not on finite floating-point checks.
"""
import math
import mpmath as mp
mp.mp.dps = 50
PI = mp.pi

def trunc(a):
    return max(32, int(mp.ceil(mp.sqrt(150*mp.log(10)/(PI*a*a))))+2)

def zak(a,x,w):
    nmax = trunc(a)
    return mp.fsum([(x-a*n)*mp.exp(-PI*(x-a*n)**2)*mp.exp(2j*PI*n*a*w)
                    for n in range(-nmax,nmax+1)])

def energy(a,x,w):
    return a*(abs(zak(a,x,w))**2+abs(zak(a,x,w-1/(2*a)))**2)

def curvatures(a):
    nmax=trunc(a)
    data=[]
    for alt in (0,1):
        A=mp.fsum([(-1 if alt and n%2 else 1)*(1-2*PI*a*a*n*n)*mp.exp(-PI*a*a*n*n) for n in range(-nmax,nmax+1)])
        B=-2*PI*a*a*mp.fsum([(-1 if alt and n%2 else 1)*n*n*mp.exp(-PI*a*a*n*n) for n in range(-nmax,nmax+1)])
        data.append((A,B))
    X=a*sum(pair[0]**2 for pair in data)
    W=a*sum(pair[1]**2 for pair in data)
    return X,W

for s in ('0.3','0.5','0.707106781186547524400844362104849039','1.0','1.4','2.0'):
    a=mp.mpf(s); b=1/(2*a)
    X,W=curvatures(a)
    assert X>0 and W>0
    DX,DW=curvatures(b)
    assert mp.almosteq(X,DW,rel_eps=mp.mpf('1e-27'),abs_eps=mp.mpf('1e-34'))
    assert mp.almosteq(W,DX,rel_eps=mp.mpf('1e-27'),abs_eps=mp.mpf('1e-34'))
    step=mp.mpf('0.00001')
    rx=energy(a,step,0)/step**2/X
    rw=energy(a,0,step)/step**2/W
    assert abs(rx-1)<mp.mpf('2e-7') and abs(rw-1)<mp.mpf('2e-7')
    assert abs(energy(a,0,0))<mp.mpf('1e-90')
    assert abs(energy(a,0,1/(2*a)))<mp.mpf('1e-90')
    print('curvature alpha=',s,'X=',mp.nstr(X,12),'W=',mp.nstr(W,12),
          'duality=PASS','local Taylor=PASS')

# Asymptotic coefficients (the two indicated limits are proved in the text).
for s in ('0.26','0.30'):
    a=mp.mpf(s); X,W=curvatures(a)
    ratioX=X/(PI**2*a**(-5)*mp.exp(-PI/(2*a*a)))
    ratioW=W*a
    assert abs(ratioX-1)<mp.mpf('0.0001') and abs(ratioW-1)<mp.mpf('0.0001')
    print('thin-alpha ',s,'ratios',mp.nstr(ratioX,12),mp.nstr(ratioW,12))
for s in ('1.8','2.1'):
    a=mp.mpf(s); X,W=curvatures(a)
    ratioX=X/(2*a)
    ratioW=W/(32*PI**2*a**5*mp.exp(-2*PI*a*a))
    assert abs(ratioX-1)<mp.mpf('0.0001') and abs(ratioW-1)<mp.mpf('0.0001')
    print('wide-alpha ',s,'ratios',mp.nstr(ratioX,12),mp.nstr(ratioW,12))

# A full radial computation of one LOCAL sublevel area, in whitened coordinates.
a=mp.mpf('0.7'); X,W=curvatures(a)
for level in (mp.mpf('0.002'), mp.mpf('0.0004')):
    pieces=[]
    for j in range(32):
        theta=2*PI*(j+mp.mpf('0.5'))/32
        c=mp.cos(theta)/mp.sqrt(X)
        d=mp.sin(theta)/mp.sqrt(W)
        lo=mp.mpf('0'); hi=2*mp.sqrt(level)
        for _ in range(48):
            mid=(lo+hi)/2
            if energy(a,c*mid,d*mid) < level: lo=mid
            else: hi=mid
        pieces.append(((lo+hi)/2)**2)
    area=PI*sum(pieces)/(32*mp.sqrt(X*W))
    expected=PI*level/mp.sqrt(X*W)
    assert abs(area/expected-1)<mp.mpf('0.007')
    print('local sublevel area level=',str(level),'ratio=',mp.nstr(area/expected,12))
print('ALL NUMERICAL PROBES PASSED')
