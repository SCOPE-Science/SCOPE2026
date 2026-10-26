"""Numerical checks for Fourier zeros of two equal-mass spherical shells.
The symbolic and all-parameter arguments are provided in RESULT.md.
"""
import mpmath as mp

mp.mp.dps = 70


def H(t, r):
    return mp.sin(t) + mp.sin(r*t)/r


def D1(t, r):
    return mp.cos(t) + mp.cos(r*t)


def D2(t, r):
    return -mp.sin(t) - r*mp.sin(r*t)


def D3(t, r):
    return -mp.cos(t) - r*r*mp.cos(r*t)


def phi(t, r):
    return (mp.sinc(t) + mp.sinc(r*t))/2


# Verify the analytic transform against direct integration over sphere latitude.
for r in [mp.mpf(1)/2, mp.mpf(2)/3, mp.mpf(1)/3, mp.sqrt(2)/3]:
    for t in [mp.mpf('0.33'), mp.mpf('2.7'), mp.mpf('8.15')]:
        direct = (mp.quad(lambda x: mp.cos(t*x), [-1, 1])+
                  mp.quad(lambda x: mp.cos(r*t*x), [-1, 1]))/4
        assert abs(direct-phi(t, r)) < mp.mpf('1.e-62')
print('Fourier integral normalization: 12 high-precision comparisons passed')

# Resonances at reduced ratios with numerator and denominator of opposite parity.
for p, q in [(1,2), (2,3), (1,4), (3,4), (4,5)]:
    r = mp.mpf(p)/q
    for odd in [1, 3, 5]:
        t = odd*q*mp.pi
        scale = max(1, abs(t))
        assert abs(H(t,r)) < mp.mpf('1.e-62')*scale
        assert abs(D1(t,r)) < mp.mpf('1.e-62')
        assert abs(D2(t,r)) < mp.mpf('1.e-62')
        assert abs(D3(t,r)) > mp.mpf('0.05')
    for even in [2,4]:
        t = even*q*mp.pi
        assert abs(H(t,r)) < mp.mpf('1.e-62')*max(1,abs(t))
        assert abs(D1(t,r)) > 1
print('Parity resonance and exact multiplicity: 25 sampled cases passed')

# Odd/odd ratios have shared sinc roots but no triple root.
for p,q in [(1,3),(3,5),(1,5)]:
    r = mp.mpf(p)/q
    for k in range(1,5):
        t = k*q*mp.pi
        assert abs(H(t,r)) < mp.mpf('1.e-62')*max(1,abs(t))
        assert abs(D1(t,r)) > 1
print('Same-parity shared-root exclusion: 12 sampled cases passed')

# Three complex local branches near the lowest resonance.
r0 = mp.mpf(1)/2
t0 = 2*mp.pi
C = mp.sign(6*t0/(r0*(r0*r0-1))) * abs(6*t0/(r0*(r0*r0-1)))**(mp.mpf(1)/3)
omega = mp.exp(2j*mp.pi/3)
for delta in [mp.mpf('1.e-3'),mp.mpf('1.e-4'),mp.mpf('1.e-5'),mp.mpf('-1.e-4')]:
    dr = mp.sign(delta)*abs(delta)**(mp.mpf(1)/3)
    r = r0+delta
    roots = []
    for k in range(3):
        center = t0 + C*dr*omega**k
        root = mp.findroot(lambda z:H(z,r), (center*(1-mp.mpf('1.e-6')),center*(1+mp.mpf('1.e-6'))), tol=mp.mpf('1.e-60'), maxsteps=100)
        assert abs(H(root,r)) < mp.mpf('1.e-55')
        assert abs(root - center) < 8*abs(delta)**(mp.mpf(2)/3)
        assert all(abs(root - other) > mp.mpf('0.01') for other in roots)
        roots.append(root)
    assert sum(abs(mp.im(z))<mp.mpf('1.e-40') for z in roots) == 1
    assert abs(roots[1]-mp.conj(roots[2])) < mp.mpf('1.e-45')
    print('delta=',mp.nstr(delta,8),'shift(real)=',mp.nstr(mp.re(roots[0]-t0),13),'triple roots=',len(roots))
print('Cubic-root unfolding: 4 three-branch tests passed')
