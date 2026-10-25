"""Supplementary finite checks for outer-polynomial angular-maxima interpolation.
Execute: python verify.py (numpy required).
This is numerical evidence, not a proof of the all-degree theorem.
"""
import numpy as np


def one_case(angles):
    n = len(angles)
    e = np.exp(1j*np.asarray(angles, dtype=float))
    # Ascending powers of the polynomial with precisely these circle roots.
    q = np.poly(e)[::-1]
    h = [sum(q[j+k]*np.conj(q[j]) for j in range(n+1-k))
         for k in range(n+1)]
    eps = next(s for s in (0.25, -0.25)
               if abs(h[1] + s*(h[0]+h[2])) > 1e-9)
    d = n+1
    coeff = np.zeros(d+1, complex)
    for k in range(d+1):
        coeff[k] = (h[k] if k <= n else 0)
        if k-1 >= 0 and k-1 <= n:
            coeff[k] += eps*h[k-1]
        if k+1 <= n:
            coeff[k] += eps*h[k+1]
    coeff[0] = h[0] + eps*(h[1] + np.conj(h[1]))
    assert abs(coeff[1]) > 1e-10
    assert abs(coeff[d]) > 1e-10
    angles_grid = np.arange(4096)*2*np.pi/4096
    z = np.exp(1j*angles_grid)
    qmod = np.abs(np.polynomial.polynomial.polyval(z, q))**2
    H = (1 + 2*eps*np.cos(angles_grid))*qmod
    M = np.max(H)*8 + 3
    # Trigonometric Laurent coefficients of T(z)=M-H(z), indexed -d..d
    t = np.zeros(2*d+1,complex)
    for k in range(-d,d+1):
        ck = coeff[k] if k >= 0 else np.conj(coeff[-k])
        t[k+d] = (M if k == 0 else 0) - ck
    roots = np.roots(t[::-1])
    out = roots[np.abs(roots)>1.000001]
    assert len(out)==d, (n, roots)
    p = np.poly(out)[::-1]
    p *= np.sqrt(np.real(M - (1+2*eps)*abs(np.polynomial.polynomial.polyval(1,q))**2)
                 /abs(np.polynomial.polynomial.polyval(1,p))**2)
    p *= np.conj(p[0])/abs(p[0])
    assert abs(p[0].imag)<1e-7
    assert min(abs(out))>1
    T = M-H
    P = np.abs(np.polynomial.polynomial.polyval(z,p))**2
    rel = np.max(np.abs(P-T))/M
    assert rel<3e-5, (n, rel)
    assert abs(p[1])>1e-8, (n, p[1])
    for xi in e:
        assert abs(abs(np.polynomial.polynomial.polyval(xi,p))**2-M)/M <3e-5
    assert abs(H.min())<1e-2  # near an exact root on fine grid
    print('N', n, 'epsilon', eps, 'degree', len(p)-1,
          'min_outer_root_modulus', round(min(abs(out)),6),
          'p1_modulus', round(abs(p[1]),8), 'relative_residual',round(rel,10))


if __name__=='__main__':
    one_case([0, np.pi])
    one_case([0.2, 2.5, 4.6])
    one_case([0, 2*np.pi/3,4*np.pi/3])
    one_case([0.13,1.55,3.8,5.4])
    print('VERIFY_OK numerical spectral factors for four independent patterns')
