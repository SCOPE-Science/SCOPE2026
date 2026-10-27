#!/usr/bin/env python3
"""Reproducible numerical checks for fidelity hitting and weak stochastic restart.

All mathematical constants and initial states are defined within this file.
The program is self-contained apart from the standard Python mpmath package.
"""
import mpmath as mp
mp.mp.dps = 60
checks = 0

def assert_close(a, b, tol=mp.mpf('3e-29')):
    global checks
    a, b = mp.mpf(a), mp.mpf(b)
    scale = max(mp.mpf(1), abs(a), abs(b))
    assert abs(a-b) < tol*scale, (a, b, a-b)
    checks += 1

def moments(x, b, c=1):
    x, b, c = mp.mpf(x), mp.mpf(b), mp.mpf(c)
    assert 0 <= x < b < 1 and c > 0
    d, y = 1-b, 1-x
    mean = mp.log(y/d)/c
    variance = (mp.log(d)**2 - mp.log(y)**2 +
                2*(mp.polylog(2, b)-mp.polylog(2, x)) +
                2*mp.log(d/y))/c**2
    return mean, variance

def criterion(x, b):
    d, y = 1-mp.mpf(b), 1-mp.mpf(x)
    return (mp.polylog(2, b)-mp.polylog(2, x)
            -(1+mp.log(y))*mp.log(y/d))

def threshold(b):
    b = mp.mpf(b)
    d = 1-b
    lo, hi = d, mp.mpf(1)
    # The function starts at zero at lo, becomes positive, and ends negative.
    # Use the unique derivative maximizer to bracket the interior zero.
    A = lambda y: -mp.log(y)/(1-y)-1
    l, h = d, mp.mpf(1)
    for _ in range(160):
        mid = (l+h)/2
        if A(mid) > mp.log(mid/d): l=mid
        else: h=mid
    lo = (l+h)/2
    f = lambda y: criterion(1-y, b)
    assert f(lo) > 0 and f(hi) < 0
    for _ in range(170):
        mid = (lo+hi)/2
        if f(mid) > 0: lo=mid
        else: hi=mid
    return 1-(lo+hi)/2

def generator(f, x, c):
    return c*(x*(1-x)*mp.diff(f, x, 2)+(1-2*x)*mp.diff(f, x))

# The first two hitting-time moment equations are checked by differentiating
# the separately evaluated closed forms in the original fidelity coordinate.
for btxt in ['0.09','0.3','0.6','0.91','0.997']:
    b = mp.mpf(btxt)
    for fractxt in ['0.04','0.23','0.62','0.88']:
        x=b*mp.mpf(fractxt)
        for c in [mp.mpf('.7'),mp.mpf('2.3')]:
            mean = lambda z: moments(z,b,c)[0]
            second = lambda z: sum([moments(z,b,c)[1], moments(z,b,c)[0]**2])
            assert_close(generator(mean,x,c), -1)
            assert_close(generator(second,x,c), -2*mean(x))
            assert moments(x,b,c)[1] > 0
            checks += 1

# Laplace transform solved by the distinct hypergeometric boundary-value
# problem; numerical differentiation recovers both moments.
for x,b,c in [('0.05','0.32','1.1'),('0.25','0.8','1.7'),('0.54','0.9','2.3'),('0.0','0.97','0.8')]:
    x,b,c=map(mp.mpf,(x,b,c))
    def LT(r):
        discriminant=mp.sqrt(1-4*r/c)
        a=(1-discriminant)/2; z=(1+discriminant)/2
        return mp.hyp2f1(a,z,1,x)/mp.hyp2f1(a,z,1,b)
    m,v=moments(x,b,c)
    assert_close(-mp.diff(LT,0),m,mp.mpf('2e-25'))
    assert_close(mp.diff(LT,0,2),v+m*m,mp.mpf('2e-24'))
    for r in [mp.mpf('0.0001'),mp.mpf('0.002')]:
        restarted=(1-LT(r))/(r*LT(r))
        assert restarted > 0
        checks+=1
    # Negative derivative is equivalent to the exact dilogarithmic sign.
    derivative= -criterion(x,b)/c**2
    assert_close(derivative,(m*m-v)/2)

# The derivative has a unique interior zero; demonstrate correct signs on both
# sides and at a model selection boundary for a range of target fidelities.
for btxt in ['0.001','0.01','0.1','0.3','0.5','0.8','0.99','0.9999']:
    b=mp.mpf(btxt)
    root=threshold(b)
    assert 0 < root < b
    assert abs(criterion(root,b)) < mp.mpf('2e-45')
    assert criterion(root/2,b) < 0
    assert criterion((root+b)/2,b) > 0
    checks+=4

# Verify the two endpoint laws at successively smaller parameter values.
for btxt in ['0.001','0.003','0.01']:
    b=mp.mpf(btxt)
    delta=(threshold(b)-b/3)/b**2
    assert abs(delta-mp.mpf(14)/243) < mp.mpf('.0003')
    checks+=1

A = mp.zeta(2)-mp.polylog(2,1-mp.exp(-1))
for dtxt in ['0.0000001','0.0000000001','0.000000000000001']:
    d=mp.mpf(dtxt)
    xc=threshold(1-d)
    asympt=1-mp.exp(-1) - A/(mp.e*mp.log(1/d))
    assert abs(xc-asympt)*mp.log(1/d)**2 < mp.mpf('5')
    checks+=1

print('PASS',checks,'analytical/numerical identities and threshold diagnostics')
for b in ['0.1','0.5','0.9','0.9999']:
    print('target_fidelity',b,'critical_initial_fidelity',mp.nstr(threshold(b),18))
