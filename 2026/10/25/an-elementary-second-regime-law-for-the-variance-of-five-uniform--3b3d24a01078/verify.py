"""Reproduce finite geometry checks and numerical evaluations of the second-regime formula.

Run: python verify.py   (requires mpmath)
No finite computation substitutes for the geometric proof of the CDF.
"""
import itertools
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 65
n = 5
pairs = list(itertools.permutations(range(n), 2))
checks = 0
least = Fraction(1000, 1)
critical_pairs = []
for i, j in pairs:
    for k, l in pairs:
        if (i, j) == (k, l):
            continue
        c = int(i == k) - int(i == l) - int(j == k) + int(j == l)
        if c == -2:
            assert (i, j) == (l, k)
            checks += 1
            continue
        assert c in (-1, 0, 1)
        # Squared norm of least-norm solution to v_i-v_j=v_k-v_l=1
        # is 1^T G^{-1} 1 = 2/(2+c), with G=[[2,c],[c,2]].
        distance_squared = Fraction(2, 2+c)
        least = min(least, distance_squared)
        if distance_squared == Fraction(2, 3):
            critical_pairs.append(((i,j), (k,l)))
        assert distance_squared >= Fraction(2, 3)
        checks += 1
assert least == Fraction(2, 3)
assert len(critical_pairs) > 0

sqrt2 = mp.sqrt(2)
sqrt5 = mp.sqrt(5)
a = 1/sqrt2
b5 = 8*mp.sqrt(10)*(mp.acos(1/mp.sqrt(3)) - mp.pi/6)
# Independent Gaussian-order-statistic evaluation of the known low-regime coefficient.
phi_cdf = lambda x: (1 + mp.erf(x/mp.sqrt(2)))/2
expected_range = 2*mp.quad(lambda t:1-phi_cdf(t)**5-(1-phi_cdf(t))**5,[0,2,5,10,20])
expected_chi4 = mp.sqrt(2)*mp.gamma(mp.mpf(5)/2)/mp.gamma(2)
b5_independent = sqrt5/mp.mpf(5)*2*mp.pi**2*expected_range/expected_chi4
assert abs(b5_independent-b5) < mp.mpf('1e-44')
checks += 1
const = 80*mp.pi*sqrt5/3

def low(r):
    return sqrt5*(mp.pi**2/2)*r**4-b5*r**5

def primitive(r):
    d = r*r-mp.mpf('0.5')
    if d <= 0:
        return mp.mpf('0')
    return const*(sqrt2*d**mp.mpf('2.5')/5
        - 3*r**4*mp.acos(a/r)/8
        + mp.sqrt(d)*(5*r*r-1)/(8*sqrt2))

def integration(r):
    if r <= a:
        return mp.mpf('0')
    return const*mp.quad(lambda t:(sqrt2*t-1)*(r*r-t*t)**mp.mpf('1.5'), [a,r])

def cdf(y):
    r = mp.sqrt(4*y)
    return low(r) + primitive(r)

# Independent 1D positive-integral evaluation compared with elementary primitive.
ys = [mp.mpf('0.125'),mp.mpf('0.126'),mp.mpf('0.13'),mp.mpf('0.14'),mp.mpf('0.15'),mp.mpf('0.16'),mp.mpf(1)/6]
for y in ys:
    r=mp.sqrt(4*y)
    clos=primitive(r)
    integ=integration(r)
    assert mp.almosteq(clos,integ,rel_eps=mp.mpf('1e-45'),abs_eps=mp.mpf('1e-45')),(y,clos,integ)
    checks+=1
assert abs(cdf(mp.mpf('0.125'))-mp.mpf('0.827937408007051'))<mp.mpf('5e-15')
assert abs(cdf(mp.mpf(1)/6)-mp.mpf('0.966743771690816'))<mp.mpf('5e-15')
checks+=2

# Monotonicity of CDF on this interval follows analytically from original volume.
for left,right in zip(ys,ys[1:]):
    assert cdf(left)<cdf(right)
    checks+=1
# Differentiate the elementary expression w.r.t. r and verify Leibniz's rule.
for y in ys[1:]:
    r=mp.sqrt(4*y)
    lhs=mp.diff(primitive,r)
    rhs=const*3*r*mp.quad(lambda t:(sqrt2*t-1)*(r*r-t*t)**mp.mpf('0.5'),[a,r])
    assert mp.almosteq(lhs,rhs,abs_eps=mp.mpf('1e-37')),(y,lhs,rhs)
    checks+=1
# Leading noninteger onset constant.
leading=4096*mp.pi*mp.sqrt(10)/21
for eps in [mp.mpf('1e-3'),mp.mpf('1e-4'),mp.mpf('1e-5'),mp.mpf('1e-6')]:
    ratio=primitive(mp.sqrt(mp.mpf('0.5')+4*eps))/eps**mp.mpf('3.5')
    assert abs(ratio/leading-1)<100*eps
    checks+=1

print('checks:',checks)
print('least squared radius for overlap:',least)
print('first-branch coefficient b5:',mp.nstr(b5,25))
print('onset coefficient:',mp.nstr(leading,25))
for y in ys:
    print('y',mp.nstr(y,18),'cdf',mp.nstr(cdf(y),25),'correction',mp.nstr(primitive(mp.sqrt(4*y)),20))
print('PASS: pairwise threshold, one-dimensional quadrature, analytic derivative, endpoint CDFs, monotonicity, and onset checks')
