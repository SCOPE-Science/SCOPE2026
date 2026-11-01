"""Exact rational checks for two-frequency great-circle tomography on S^2.

The checks are finite confirmations of the eigenvalue formulas, not a
substitute for the representation-theoretic proof in the accompanying note.
Run: python3 check_spectral_recovery.py
Only Python's standard library is needed.
"""
from fractions import Fraction
from math import factorial, comb


def legendre_coeffs(ell):
    """Coefficients of P_ell(x) in ascending monomial degree."""
    out = {}
    for q in range(ell // 2 + 1):
        j = ell - 2 * q
        out[j] = Fraction((-1)**q * factorial(2*ell-2*q),
                          (2**ell)*factorial(q)*factorial(ell-q)*factorial(j))
    return out


def circle_coefficient_of_zonal(ell, m):
    """Coefficient of exp(i m theta) in P_ell(r cos theta)."""
    out = {}
    for j, pj in legendre_coeffs(ell).items():
        if j >= m and (j-m) % 2 == 0:
            out[j] = pj * Fraction(comb(j, (j-m)//2), 2**j)
    return out


def avg_one_minus_t2(p):
    """E[(1-T^2)^p] for T uniform on [-1,1]."""
    return Fraction(4**p * factorial(p)**2, factorial(2*p+1))


def independent_zonal_energy(ell, m):
    """Average squared Fourier coefficient over Haar circle frames."""
    a = circle_coefficient_of_zonal(ell, m)
    return sum((u*v*avg_one_minus_t2((i+j)//2)
                for i,u in a.items() for j,v in a.items()), Fraction(0))


def odd_double_factorial(n):
    p=1
    for j in range(n,0,-2):p*=j
    return p


def legendre_eigenvalue(ell,m):
    if ell < m or (ell-m)%2:return Fraction(0)
    return Fraction(factorial(ell-m)*odd_double_factorial(ell+m-1)**2,
                    factorial(ell+m)*odd_double_factorial(ell-m)**2)


def closed_eigenvalue(ell,m):
    if ell<m or (ell-m)%2:return Fraction(0)
    if m==2:
        k=ell//2
        a=Fraction(comb(2*k,k),4**k)
        return Fraction(2*k*(2*k+1),(2*k-1)*(2*k+2))*a*a
    if m==3:
        k=(ell-1)//2
        a=Fraction(comb(2*k,k),4**k)
        return (Fraction(2*k*(2*k+3),(2*k-1)*(2*k+4))
                *Fraction(2*k+1,2*k+2)*a*a)
    raise ValueError(m)


def verify():
    n=0
    for ell in range(2,23):
        for m in (2,3):
            exact=independent_zonal_energy(ell,m)
            lam=legendre_eigenvalue(ell,m)
            assert exact==lam/Fraction(2*ell+1), (ell,m,exact,lam)
            assert lam==closed_eigenvalue(ell,m),(ell,m)
            n+=1
    for k in range(1,501):
        a=Fraction(comb(2*k,k),4**k)
        w=(2*k+1)*a*a
        an=Fraction(comb(2*k+2,k+1),4**(k+1))
        wn=(2*k+3)*an*an
        assert wn<w
        for ell,m in ((2*k,2),(2*k+1,3)):
            lam=closed_eigenvalue(ell,m)
            assert (ell+1)*lam>w
            n+=1
    assert legendre_eigenvalue(2,2)==Fraction(3,8)
    assert legendre_eigenvalue(3,3)==Fraction(5,16)
    assert independent_zonal_energy(2,2)==Fraction(3,40)
    assert independent_zonal_energy(3,3)==Fraction(5,112)
    # Last two exact values include the unit-zonal-norm factor 1/(2 ell+1).
    print('SPECTRAL_CHECK_OK: %d exact/finite checks; ell<=22 and k<=500' % n)

if __name__=='__main__':verify()
