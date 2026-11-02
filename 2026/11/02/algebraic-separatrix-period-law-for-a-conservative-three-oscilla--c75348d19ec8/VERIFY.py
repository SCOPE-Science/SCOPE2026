"""Standalone numerical consistency checks for the three-phase reduced period law.

Run: python VERIFY.py
Requires mpmath. Numerical evidence supports but does not prove asymptotics.
"""
import mpmath as mp

mp.mp.dps = 45
pi = mp.pi
one_third = mp.mpf(1)/3
B = mp.beta
K_expected = 2 * B(one_third, mp.mpf(1)/2)
K_equivalent = 2**(mp.mpf(2)/3) * B(one_third, one_third)
K_left = mp.mpf(2)/3 * B(mp.mpf(1)/6,one_third)
K_right = mp.mpf(2)/3 * B(one_third,mp.mpf(1)/2)
assert mp.almosteq(K_expected, K_equivalent)
assert mp.almosteq(K_expected, K_left + K_right)
assert mp.almosteq(K_left,2*K_right)


def period(E):
    E = mp.mpf(E)
    assert 0 < E < 3*mp.sqrt(3)/2
    g = lambda x: 2*mp.sin(x/2)*(1+mp.cos(x/2))-E
    xl = mp.findroot(g, (E/3,E))
    xr = mp.findroot(g, (2*pi-3*E**one_third,2*pi-E**one_third))
    assert 0 < xl < 2*pi/3 < xr < 2*pi
    def q(t):
        x = xl+(xr-xl)*mp.sin(t)**2
        s = mp.sin(x/2)
        c = mp.cos(x/2)-E/(2*s)
        rad = max(mp.mpf('1e-70'),1-c*c)
        return 2*(xr-xl)*mp.sin(t)*mp.cos(t)/(s*mp.sqrt(rad))
    return mp.quad(q,[0,pi/8,pi/4,3*pi/8,pi/2])

values=[]
for string_E in ('0.1','0.01','0.001','0.0001','0.00001'):
    E = mp.mpf(string_E)
    scaled=period(E)*E**one_third
    values.append(scaled)
    print('E:',string_E,'E^(1/3) T(E):',mp.nstr(scaled,20))
assert all(a<b for a,b in zip(values,values[1:]))
assert abs(values[-1]/K_expected-1) < mp.mpf('0.0002')
assert abs(K_expected-mp.mpf('8.4130926319527255671')) < mp.mpf('1e-19')
assert mp.almosteq(mp.sqrt(mp.mpf(9)/4),mp.mpf(3)/2)
print('K:',mp.nstr(K_expected,24))
print('small-center limiting period:',mp.nstr(4*pi/3,20))
print('PASS: beta identity, quadrature scaling, center frequency')
