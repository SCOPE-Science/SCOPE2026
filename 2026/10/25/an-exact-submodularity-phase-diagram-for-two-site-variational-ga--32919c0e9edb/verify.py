"""Reproduce the two-site Gaussian-process variational-gain classification.

Requires Python 3 standard library only. This program supplements the proof;
it does not replace the analytic argument for all admissible parameters.
"""
import math
import random


def d2(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def f(k, z, s):
    # The kernel is already normalized by the observational variance.
    if len(s) == 0:
        q = [[0., 0.], [0., 0.]]
    elif len(s) == 2:
        q = [row[:] for row in k]
    else:
        j = s[0]
        q = [[k[i][j]*k[j][h]/k[j][j] for h in range(2)] for i in range(2)]
    b = [[q[i][j] + (1. if i == j else 0.) for j in range(2)] for i in range(2)]
    det = d2(b)
    inv = [[b[1][1]/det,-b[0][1]/det],[-b[1][0]/det,b[0][0]/det]]
    quadratic = sum(z[i]*inv[i][j]*z[j] for i in range(2) for j in range(2))
    return -.5*(math.log(det)+quadratic + k[0][0]+k[1][1]-q[0][0]-q[1][1])


def coefficients(t, r):
    d = 1+t*(1+r*r)
    hp, hm = 1+t*(1+r), 1+t*(1-r)
    c = t*r*r-math.log(d)+.5*math.log(hp*hm)
    ap = r*t*(1+r)*(2*t+1)/(2*hp*d)
    am = r*t*(1-r)*(2*t+1)/(2*hm*d)
    return c, ap, am


def trial(t,r,z):
    k = [[t,t*r],[t*r,t]]
    vals = {():f(k,z,()),(0,):f(k,z,(0,)),(1,):f(k,z,(1,)),(0,1):f(k,z,(0,1))}
    g = vals[(0,)]+vals[(1,)]-vals[()]-vals[(0,1)]
    c,ap,am = coefficients(t,r)
    zp=(z[0]+z[1])/math.sqrt(2.)
    zm=(z[0]-z[1])/math.sqrt(2.)
    expected = c+ap*zp*zp-am*zm*zm
    assert abs(g-expected) < 2.e-10*(1+abs(g)+abs(expected)), (t,r,z,g,expected)
    assert all(vals[tup]>=vals[()]-1.e-10 for tup in [(0,),(1,),(0,1)])
    assert vals[(0,1)]>=max(vals[(0,)],vals[(1,)])-1.e-10
    assert c>0 and ap>0 and am>0
    assert (g>=-1.e-10)==(zm*zm<=(c+ap*zp*zp)/am+1.e-8) or abs(g)<1.e-8
    return g


def run():
    count=0
    for t in [.001,.03,.1,.5,1.,3.,20.,150.]:
        for r in [.0005,.02,.125,.5,.75,.95,.999]:
            for z in [[0.,0.],[1.,1.],[1.,-1.],[3.,-2.],[-2.,3.],[.05,4.]]:
                trial(t,r,z)
                count+=1
    rng=random.Random(260601821)
    for _ in range(1000):
        t=10**rng.uniform(-2.5,2)
        r=rng.uniform(.01,.99)
        z=[rng.uniform(-5,5),rng.uniform(-5,5)]
        trial(t,r,z)
        count+=1
    g=trial(1.,.5,[1.,-1.]); count+=1
    exact=1/36+math.log(20/27)/2
    assert abs(g-exact)<1.e-12 and exact<0
    for r in [1.e-3,2.e-4,5.e-5]:
        t=.7
        for z in [[1,2],[1,-2]]:
            g=trial(t,r,z)
            predicted=t*(2*t+1)/(1+t)**2*z[0]*z[1]
            assert abs(g/r-predicted)<.03, (r,g/r,predicted)
            count+=1
    print(f'PASS: {count} independent deterministic direct-matrix checks, monotonicity, signs, and weak-coupling limits')


if __name__=='__main__':run()
