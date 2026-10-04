from math import asin, asinh, cos, exp, fsum, pi, sin, sqrt, sinh, cosh


def Dk(s, kappa):
    y = sin(pi*s)
    if kappa > 0:
        return asin(sqrt(kappa)*y)/(sqrt(kappa)*pi)
    if kappa < 0:
        return asinh(sqrt(-kappa)*y)/(sqrt(-kappa)*pi)
    return y/pi


def qn(n, ell, kappa):
    return fsum(exp(-ell*Dk(j/n, kappa)) for j in range(n))/n


def simpson_q(ell, kappa, N=20000):
    assert N % 2 == 0
    h = 1.0/N
    vals = [exp(-ell*Dk(j*h, kappa)) for j in range(N+1)]
    return h/3.0*(vals[0]+vals[-1]+4.0*fsum(vals[1:N:2])+2.0*fsum(vals[2:N-1:2]))


def smooth_coeffs(ell, kappa):
    c2 = ell/6.0
    c4 = ell*(pi*pi*(1.0-kappa)-ell*ell)/360.0
    return c2, c4


def intrinsic_exact(n, ell):
    E = exp(-ell/2.0)
    x = ell/(2.0*n)
    coth = cosh(x)/sinh(x)
    if n % 2 == 0:
        return (1.0-E)*coth/n
    csch = 1.0/sinh(x)
    return (coth-E*csch)/n

# Smooth round metrics: compare direct samples with the two-term expansion.
for ell in (0.4, 1.3, 3.0):
    for kappa in (-2.0, 0.0, 0.5, 0.9):
        qinf = simpson_q(ell, kappa)
        c2, c4 = smooth_coeffs(ell, kappa)
        e1 = abs(qn(80, ell, kappa) - (qinf + c2/80**2 + c4/80**4))
        e2 = abs(qn(160, ell, kappa) - (qinf + c2/160**2 + c4/160**4))
        # Sixth-order decay should improve by roughly 64 when n doubles.
        assert e2 < e1/20.0 + 2e-13, (ell, kappa, e1, e2)

# Euclidean specialization agrees with the regular-polygon chord formula.
for ell in (0.7, 2.0, 5.0):
    a = ell/(2*pi)
    for n in (7, 16, 31):
        direct = fsum(exp(-2*a*sin(pi*j/n)) for j in range(n))/n
        assert abs(direct-qn(n,ell,0.0)) < 2e-15

# Intrinsic endpoint: exact parity formulas agree with direct sampling.
for ell in (0.4, 1.7, 4.0):
    E = exp(-ell/2.0)
    qinf = 2.0*(1.0-E)/ell
    for n in range(3, 31):
        direct = qn(n, ell, 1.0)
        exact = intrinsic_exact(n, ell)
        assert abs(direct-exact) < 3e-14, (ell,n,direct,exact)
    # Check the parity-dependent leading coefficients numerically.
    for n in (200, 400):
        even = intrinsic_exact(n, ell)
        odd = intrinsic_exact(n+1, ell)
        ce = ell*(1.0-E)/6.0
        co = ell*(2.0+E)/12.0
        assert abs(n*n*(even-qinf)-ce) < 2e-4
        assert abs((n+1)**2*(odd-qinf)-co) < 2e-4

print('VERIFY_OK round-circle magnitude sampling law')
