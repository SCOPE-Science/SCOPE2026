"""Reproduce finite numerical checks for the dephased lattice-gas Fourier response.

Requires mpmath; all mathematical limit claims are proved analytically in RESULT.md.
"""
import mpmath as mp

mp.mp.dps = 32
count = 0


def near(x, y, atol=mp.mpf("1e-18"), rtol=mp.mpf("1e-18")):
    global count
    count += 1
    assert abs(x-y) <= atol+rtol*max(abs(x), abs(y)), (x, y)


def sinc_hyper(z):
    z = mp.mpf(z)
    if z == 0:
        return mp.mpf(1)
    if z > 0:
        return mp.sinh(mp.sqrt(z))/mp.sqrt(z)
    return mp.sin(mp.sqrt(-z))/mp.sqrt(-z)


def poles(lam, k, t):
    return 2*lam*t*sinc_hyper((lam*lam-k*k)*t*t)


def laplace_response(lam, k, t):
    return mp.invertlaplace(
        lambda s: 1/(mp.sqrt((s+lam)**2+k*k)-lam), t, method="dehoog"
    )


def renewal_response(lam, k, t):
    # Exact inverse of h via a Laplace-factorized Bessel convolution.
    a2 = lam*lam-k*k
    def S(z): return z*sinc_hyper(a2*z*z)
    def kernel(s): return k*mp.besselj(1,k*s)/s if s else k*k/2
    a = mp.sqrt(a2)
    c = mp.cosh(a*t) if a2 != 0 else 1
    return mp.re(c + lam*S(t) + mp.quad(lambda s: kernel(s)*S(t-s), [0,t]))


# Verify the exact separated-mode identity and independent Bessel reconstruction.
for lam in (mp.mpf('0.8'), mp.mpf('1.0')):
    for ratio in (mp.mpf('.55'), mp.mpf('1'), mp.mpf('1.6')):
        k = lam * ratio
        for t in (mp.mpf('1.5'), mp.mpf('3.25'), mp.mpf('6')):
            response = laplace_response(lam,k,t)
            h = mp.exp(lam*t)*response
            reconstructed = renewal_response(lam,k,t)
            near(h, reconstructed, atol=mp.mpf('3e-21'), rtol=mp.mpf('3e-21'))
            # Compute the branch complement by an independent Laplace inversion.
            residual = mp.invertlaplace(lambda u: 1/(mp.sqrt(u*u+k*k)+lam),t,method='dehoog')
            near(h,poles(lam,k,t)+residual,atol=mp.mpf('2e-21'),rtol=mp.mpf('2e-21'))

# Check asymptotic sign and coefficient at late time for several branches.
for ratio in (mp.mpf('.7'),mp.mpf('1'),mp.mpf('1.4')):
    lam=mp.mpf('1');k=ratio
    for t in (mp.mpf('18'),mp.mpf('29')):
        residual=mp.invertlaplace(lambda u:1/(mp.sqrt(u*u+k*k)+lam),t,method='dehoog')
        predicted=mp.sqrt(2*k/mp.pi)/(lam**2*t**mp.mpf('1.5'))*mp.sin(k*t+3*mp.pi/4)
        # Absolute tail-error bound chosen generously; this is not the asymptotic proof.
        count += 1
        assert abs(residual-predicted) < mp.mpf('.15')*t**(-mp.mpf('1.5'))

# Directly test the normalized t^-2 transition layer against exact Laplace inversion.
for eta in (mp.mpf('-5'),mp.mpf('-1'),mp.mpf('0'),mp.mpf('1'),mp.mpf('4')):
    lam=mp.mpf('1')
    t=mp.mpf('24')
    k=mp.sqrt(lam*lam-eta/(t*t))
    exact=mp.exp(lam*t)*laplace_response(lam,k,t)/t
    near(exact,2*lam*sinc_hyper(eta),atol=mp.mpf('.003'),rtol=mp.mpf('.003'))

print(f'PASS: {count} finite Bessel/transform/asymptotic comparisons')
