"""Numerical sanity checks for sharp real-part envelopes of polylogarithmic kernels.

The continuum theorem is analytic; finite floating-point tests are not its proof.
Requires mpmath, Python 3.
"""
import mpmath as mp
mp.mp.dps = 55

def F(a,z):
    if z==0: return mp.mpf(1)
    return mp.polylog(-a,z)/z

def H(a,z):
    return (1-z)**2*F(a,z)

def bound(a):
    if a==1: return mp.mpf(1)
    if 1<a<2: return 4*mp.altzeta(-a)
    if 0<=a<=2: return mp.mpf(0)
    return -mp.inf

for a in [mp.mpf('0'),mp.mpf('.2'),mp.mpf('.75'),mp.mpf('1'),mp.mpf('1.1'),mp.mpf('1.5'),mp.mpf('1.9'),mp.mpf('2')]:
    m=bound(a)
    for r in [mp.mpf('.2'),mp.mpf('.7'),mp.mpf('.95')]:
        for j in range(13):
            z = r*mp.e**(2j*mp.pi*1j/13)
            if mp.re(H(a,z)) < m - mp.mpf('1e-40'):
                raise AssertionError(('lower_bound',str(a),str(z)))
    if 1<a<2:
        assert abs(mp.re(H(a,-mp.mpf('.99999')))-m)<mp.mpf('.003')
    if a==1:
        assert abs(H(a,mp.mpf('.5')+.4j)-1)<mp.mpf('1e-40')
print('POLYLOG_CARATHEODORY_GRID_OK')

for a in [mp.mpf('2.1'),mp.mpf('2.3'),mp.mpf('3'),mp.mpf('4.4'),mp.mpf('8')]:
    b=a-1
    theta=(mp.pi/(2*b)+min(mp.pi/2,3*mp.pi/(2*b)))/2
    assert mp.cos(b*theta)<0
    values=[]
    for eps in [mp.mpf('1e-2'),mp.mpf('1e-3'),mp.mpf('1e-4')]:
        z=mp.e**(-eps*mp.e**(1j*theta))
        values.append(mp.re(H(a,z)))
    assert all(v<0 for v in values)
    assert values[2]<values[1]<values[0]
print('POLYLOG_NEGATIVE_SECTOR_GROWTH_OK')

for a in [mp.mpf('2.01'),mp.mpf('2.5'),mp.mpf('3'),mp.mpf('4.1'),mp.mpf('7')]:
    vals=[F(a,-mp.mpf(j)/200) for j in range(1,201)]
    signs=[mp.sign(mp.re(v)) for v in vals]
    assert signs[0]==1 and -1 in signs
print('POLYLOG_REAL_ZERO_SIGN_CHANGE_OK')
