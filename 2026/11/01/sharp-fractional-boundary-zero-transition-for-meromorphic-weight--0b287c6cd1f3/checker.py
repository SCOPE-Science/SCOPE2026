"""Finite reproducibility checks for a fractional-weight Bergman kernel transition.
The infinite zero classification is proved analytically, not by this script.
Requires mpmath and standard Python.
"""
import mpmath as mp

mp.mp.dps = 42
checks = 0

def assert_close(a, b, tol=mp.mpf('1e-29')):
    global checks
    assert abs(a-b) < tol, (a, b, a-b)
    checks += 1

def scalar_Q(theta, b, z):
    # beta=-b; Euler-transformed hypergeometric analytic numerator.
    return mp.hyp2f1(-theta, -b, 1-b, z)

def scalar_series(theta, b, z, count=190):
    # Reproducing-kernel monomial coefficients for alpha=theta-1 and beta=-b.
    return mp.fsum(mp.rf(1-b+theta,n)/mp.rf(1-b,n) * z**n for n in range(count))

for theta in [mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.8')]:
    for b in [mp.mpf('0.23'), mp.mpf('0.67'), mp.mpf('0.83')]:
        for z in [-mp.mpf('0.37'), mp.mpf('0.43'), mp.mpc('0.2', '0.3')]:
            lhs = scalar_series(theta,b,z)
            rhs = scalar_Q(theta,b,z)/(1-z)**(theta+1)
            assert_close(lhs,rhs, mp.mpf('5e-29'))
        assert_close(scalar_Q(theta,b,0),1)
    # Bisection is numerical evidence of a root, not proof of uniqueness.
    lo,hi=mp.mpf('0.2'),mp.mpf('0.99')
    assert scalar_Q(theta,lo,-1)>0 and scalar_Q(theta,hi,-1)<0
    checks+=1
    for _ in range(155):
        mid=(lo+hi)/2
        if scalar_Q(theta,mid,-1)>0: lo=mid
        else:hi=mid
    bc=(lo+hi)/2
    assert_close(scalar_Q(theta,bc,-1),0,mp.mpf('2e-37'))
    assert mp.im(scalar_Q(theta, bc, mp.mpc(-0.5,0.2)))>0
    checks+=1
    b=(bc+1)/2
    lo_r,hi_r=mp.mpf('0'),mp.mpf('1')
    assert scalar_Q(theta,b,-lo_r)>0 and scalar_Q(theta,b,-hi_r)<0
    checks+=1
    for _ in range(155):
        r=(lo_r+hi_r)/2
        if scalar_Q(theta,b,-r)>0:lo_r=r
        else:hi_r=r
    assert_close(scalar_Q(theta,b,-(lo_r+hi_r)/2),0,mp.mpf('2e-37'))
    print('theta=',mp.nstr(theta,7),'critical b=',mp.nstr(bc,23),'interior scalar root=',mp.nstr(-(lo_r+hi_r)/2,23))

# For theta=1, the numerator is elementary and the critical value is 1/2.
for b in [mp.mpf('0.25'),mp.mpf('0.5'),mp.mpf('0.75')]:
    for z in [-mp.mpf('.4'),mp.mpf('.2'),mp.mpc('.1','.3')]:
        assert_close(scalar_Q(mp.mpf('1'),b,z),1+b*z/(1-b))
print('PASS:', checks, 'finite numerical identities and root checks')
