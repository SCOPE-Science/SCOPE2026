"""Independent symbolic generator calculation and numerical checks for a time-changed isotropic random flight.

Requires sympy and mpmath. Run: python check.py
"""
import sympy as sym
import mpmath as mp

s, a, v, d = sym.symbols('s a v d', positive=True)

def sphere_moment(j):
    if j % 2:
        return sym.Integer(0)
    return {0: sym.Integer(1), 2: 1/d, 4: 3/(d*(d+2))}[j]

# Laplace-domain generator: p*x^(p-1)*u^(q+1) plus independent
# uniform-direction refreshment with intensity a.
transforms = {(0,j): sphere_moment(j)/s for j in range(5)}
for p in range(1, 5):
    transforms[p,0] = sym.factor(p*v*transforms[p-1,1]/s)
    for q in range(1,5-p):
        transforms[p,q] = sym.factor(
            (p*v*transforms[p-1,q+1] + a*sphere_moment(q)*transforms[p,0])/(s+a)
        )
expected2 = 2*v**2/(d*s**2*(s+a))
expected4 = 24*v**4*(3*s/(d*(d+2))+a/d**2)/(s**3*(s+a)**3)
assert sym.factor(transforms[2,0]-expected2) == 0
assert sym.factor(transforms[4,0]-expected4) == 0
assert sym.limit(s**3*expected2, s, sym.oo) == 2*v**2/d
assert sym.simplify(sym.limit(s**5*expected4, s, sym.oo) - 24*v**4*3/(d*(d+2))) == 0
assert sym.limit(s**2*expected2, s, 0) == 2*v**2/(d*a)
assert sym.simplify(sym.limit(s**3*expected4, s, 0)-24*v**4/(d**2*a**2)) == 0

mp.mp.dps = 50
F = lambda order: mp.gamma(1+4*order)/mp.gamma(1+2*order)**2
K_long = lambda order: 6*mp.gamma(1+order)**2/mp.gamma(1+2*order)-3
assert F(mp.mpf('0.5')) == 2
for dim in (1, 2, 3, 4, 10, 100):
    target = 6*mp.mpf(dim)/(dim+2)
    root = mp.mpf('0.5') if dim == 1 else mp.findroot(
        lambda x: F(x)-target, (mp.mpf('0.5'), mp.mpf('0.999'))
    )
    assert 0 < root < 1
    assert abs(F(root)-target) < mp.mpf('1e-40')
    if dim > 1:
        assert root > mp.mpf('0.5')
for order in (mp.mpf('.1'), mp.mpf('.3'), mp.mpf('.5'), mp.mpf('.7'), mp.mpf('.9')):
    assert K_long(order) > 0

def moment(t, order, dim, j):
    mu2, mu4 = mp.mpf(1)/dim, 3/(mp.mpf(dim)*(dim+2))
    if j == 2:
        transform = lambda z: 2*mu2/(z**(order+1)*(z**order+1))
    elif j == 4:
        transform = lambda z: 24*(mu4*z**order+mu2**2)/(z**(2*order+1)*(z**order+1)**3)
    else:
        raise ValueError('Only orders 2 and 4 are needed')
    return mp.invertlaplace(transform, t, method='dehoog')

def kurtosis(t, order, dim):
    return moment(t,order,dim,4)/moment(t,order,dim,2)**2-3

# These checks are supplementary; the proof, not numerical sampling, establishes
# all dimensions and all fractional orders.
assert kurtosis(mp.mpf('.02'), mp.mpf('.7'), 1) < 0
assert kurtosis(mp.mpf('200'), mp.mpf('.7'), 1) > 0
assert kurtosis(mp.mpf('.02'), mp.mpf('.9'), 2) < 0
assert kurtosis(mp.mpf('200'), mp.mpf('.9'), 2) > 0
assert kurtosis(mp.mpf('.02'), mp.mpf('.4'), 1) > 0
assert kurtosis(mp.mpf('200'), mp.mpf('.4'), 1) > 0
print('All exact-transform, gamma-threshold and inverse-Laplace checks passed.')
