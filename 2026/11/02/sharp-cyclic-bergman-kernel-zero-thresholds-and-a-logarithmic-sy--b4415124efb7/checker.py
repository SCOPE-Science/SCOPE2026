"""Finite reproducibility checks for cyclic Bergman kernel thresholds.

Requires Python 3 and mpmath. Execute: python checker.py.
"""
import mpmath as mp
mp.mp.dps = 45
checks = 0

def assert_close(a, b, tol=mp.mpf('1e-27')):
    global checks
    assert abs(a-b) < tol, (a,b)
    checks += 1

def border(d, lam):
    t = mp.e**(mp.j*mp.pi/d)
    return mp.re(sum((1-t*mp.e**(2j*mp.pi*k/d))**(-lam) for k in range(d))/d)

def power_kernel(d, lam, x):
    # |x|<1; rapidly convergent for the radii selected below.
    return sum(mp.rf(lam,d*n)*x**n/mp.factorial(d*n) for n in range(450))

for d in range(2, 11):
    for x in [mp.mpf('-0.3'),mp.mpf('0.4'),mp.mpf('-0.7')]:
        assert_close(power_kernel(d,2,x),(1+(d-1)*x)/(1-x)**2)
    assert_close(border(d,1),mp.mpf('0.5'))
    assert_close(border(d,2),mp.mpf(2-d)/4)
    if d>2:
        root=mp.findroot(lambda L:border(d,L),(mp.mpf('1.03'),mp.mpf('1.99')))
        assert 1<root<2
        checks+=1
        assert_close(border(d,root),0)
        middle=(root+2)/2
        rho=mp.findroot(lambda r:power_kernel(d,middle,-r),(mp.mpf('0.05'),mp.mpf('0.95')))
        assert 0<rho<1
        checks+=1
        assert_close(power_kernel(d,middle,-rho),0)
        assert power_kernel(d,middle,-rho/2)>0
        assert power_kernel(d,middle,-(rho+1)/2)<0
        checks+=2
    else:
        assert border(d,mp.mpf('1.8'))>0
        checks+=1
for d in [16,32,64]:
    root=mp.findroot(lambda L:border(d,L),(1+mp.mpf('.35')/mp.log(d),1+mp.mpf('.9')/mp.log(d)))
    scaled=(root-1)*mp.log(d)
    assert mp.mpf('.68')<scaled<mp.mpf('.75')
    checks+=1
assert_close(2*mp.cos(mp.pi*mp.mpf('1.6525214566647722')/3)+2**(-mp.mpf('1.6525214566647722')),0,mp.mpf('1e-14'))
print('PASS:',checks,'finite assertions')
