"""Reproduce finite numerical checks for a two-jet weighted Bergman Gram-kernel theorem.

The universal proof uses gamma log-convexity and angular root counting;
the tests below check normalizations and representative boundary cases.
Requires mpmath; run: python check_twojet.py
"""
import math
import mpmath as mp

mp.mp.dps = 55


def rising(x, n):
    return mp.rf(x, n)


def coeffs(alpha, p, q, c):
    h = mp.mpf(alpha) + 2
    a = mp.mpf(math.factorial(p)) / math.factorial(q)
    A = a * rising(h, p + q) / rising(h, 2 * p)
    B = a * a * rising(h, 2 * q) / rising(h, 2 * p)
    return A, B


def polynomial(alpha, p, q, c, u):
    d = q - p
    A, B = coeffs(alpha, p, q, c)
    return 1 + A * ((-1)**d * c + mp.conj(c)) * u**d + (-1)**d * B * abs(c)**2 * u**(2*d)


def closed_kernel(alpha, p, q, c, z, w):
    h = mp.mpf(alpha) + 2
    delta = z - mp.conj(w)
    u = 1 / delta
    K = 2**mp.mpf(alpha) * (mp.mpf(alpha) + 1) / mp.pi * (-1j * delta)**(-h)
    factor = (-1)**p * rising(h, 2*p) * u**(2*p) / math.factorial(p)**2
    return K * factor * polynomial(alpha, p, q, c, u)


def integral_kernel(alpha, p, q, c, z, w):
    h = mp.mpf(alpha) + 2
    delta = z - mp.conj(w)
    def integrand(t):
        left = (1j*t)**p/math.factorial(p) + c*(1j*t)**q/math.factorial(q)
        right = (-1j*t)**p/math.factorial(p) + mp.conj(c)*(-1j*t)**q/math.factorial(q)
        return t**(h-1) * mp.exp(1j*delta*t) * left * right
    return 2**mp.mpf(alpha)/(mp.pi*mp.gamma(mp.mpf(alpha)+1)) * mp.quad(integrand, [0, mp.inf])


cases = [
    ('0', 0, 2, mp.mpc('1','2'), mp.mpc('.5','1.1'), mp.mpc('1.2','.7')),
    ('-.5', 2, 5, mp.mpc('2','-3'), mp.mpc('.3','2'), mp.mpc('-.4','1.5')),
    ('.75', 1, 4, mp.mpc('.3','.6'), mp.mpc('1','3'), mp.mpc('-1','1')),
    ('.25', 4, 6, mp.mpc('-2','0'), mp.mpc('-.1','1.7'), mp.mpc('1.4','1.1')),
]
for alpha, p, q, c, z, w in cases:
    lhs = integral_kernel(alpha, p, q, c, z, w)
    rhs = closed_kernel(alpha, p, q, c, z, w)
    err = abs(lhs-rhs)/max(abs(rhs), mp.mpf('1e-40'))
    assert err < mp.mpf('1e-25'), (alpha,p,q,err)
print('PASS: 4 high-precision Fourier-integral versus closed-form checks')


def roots_in_halfplane(alpha, p, d, c):
    q = p+d
    A, B = coeffs(alpha, p, q, c)
    assert B > A*A, (alpha, p, q)
    L = A*((-1)**d * c + mp.conj(c))
    H = (-1)**d * B * abs(c)**2
    ud = [(-L + mp.sqrt(L*L - 4*H))/(2*H),
          (-L - mp.sqrt(L*L - 4*H))/(2*H)]
    assert abs(ud[0]-ud[1]) > mp.mpf('1e-20')
    assert all(abs(y)>mp.mpf('1e-20') for y in ud)
    rt = []
    for y in ud:
        r = abs(y)**(mp.mpf(1)/d)
        angle = mp.arg(y)
        for j in range(d):
            rt.append(r*mp.exp(1j*(angle+2*mp.pi*j)/d))
    for u in rt:
        assert abs(polynomial(alpha,p,q,c,u)) < mp.mpf('1e-35')
    neg = sum(mp.im(u)<-mp.mpf('1e-28') for u in rt)
    border = sum(abs(mp.im(u))<=mp.mpf('1e-28') for u in rt)
    expected = d if d%2==0 else (d+1 if mp.im(c)>0 else d-1)
    expected_border = (2 if (d%2==1 and mp.im(c)==0) else 0)
    assert neg == expected and border==expected_border, (alpha,p,d,c,neg,border,expected,expected_border)
    return neg,border

c_grid = [mp.mpc(1,0),mp.mpc(0,1),mp.mpc(0,-1),mp.mpc(2,3),mp.mpc(-2,-4)]
count=0
for alpha in ['-.75','0','.25','2.5']:
    for p in range(4):
        for d in range(2,9):
            for c in c_grid:
                roots_in_halfplane(alpha,p,d,c)
                count+=1
print(f'PASS: {count} root-count checks spanning integer gaps, weights and complex phases')
print('PASS: every checked mixed derivative Gram kernel has the predicted zeros')
