"""Independent numerical normalization and asymptotic checks for the stated two-shell Fourier theorem.
Run: python checker.py (requires mpmath). Finite checks are not an all-degree proof.
"""
import mpmath as mp

mp.mp.dps = 180


def mode_matrix(d, a, b, u, v, ell):
    nu = mp.mpf(d) / 2 - 1
    alpha = ell + nu
    const = mp.power(2, nu) * mp.gamma(nu + 1)
    def phi(z):
        return const * mp.power(z, -nu) * mp.besselj(alpha, z)
    return (phi(a*u), phi(b*u), phi(a*v), phi(b*v))


def predictions(d, a, b, u, v, ell):
    nu = mp.mpf(d) / 2 - 1
    kap = mp.gamma(nu + 1) / (mp.power(2, ell) * mp.gamma(ell + nu + 1))
    delta = (b*b-a*a) * (v*v-u*u)
    assert delta > 0
    det = -kap**2 * (a*b*u*v)**ell * delta / (4*(ell+nu+1))
    svmax = kap * (b*v)**ell
    svmin = kap * (a*u)**ell * delta / (4*(ell+nu+1))
    return det, svmax, svmin


print('mpmath_dps', mp.mp.dps)
cases = [('plane', 2, '.7', '1.3', '.4', '.6'),
         ('space', 3, '.9', '1.4', '.2', '.9'),
         ('five-dimensional', 5, '1', '2', '.3', '.8')]
for name, dim, a, b, u, v in cases:
    a, b, u, v = [mp.mpf(k) for k in (a,b,u,v)]
    nu = mp.mpf(dim)/2 - 1
    assert b*v < mp.besseljzero(nu, 1), 'frequency outside stated safe region'
    print('case', name, 'dimension', dim)
    for ell in (0,1,2,6,12,24,36,48):
        A,B,C,D = mode_matrix(dim,a,b,u,v,ell)
        det = A*D-B*C
        assert det < 0, (name,ell,'nonsingularity/sign')
        tr = A*A+B*B+C*C+D*D
        largest = mp.sqrt((tr+mp.sqrt(tr*tr-4*det*det))/2)
        smallest = -det/largest
        pred_det,pred_big,pred_small=predictions(dim,a,b,u,v,ell)
        ratios = [det/pred_det,largest/pred_big,smallest/pred_small]
        if ell == 48:
            assert all(abs(r-1) < mp.mpf('.04') for r in ratios), (name,ell,ratios)
        if ell in (0,12,48):
            print(' ell',ell,'det/pred',mp.nstr(ratios[0],12),
                  'smax/pred',mp.nstr(ratios[1],12),
                  'smin/pred',mp.nstr(ratios[2],12))

# Directly integrate an independent axisymmetric spherical mode at dimension 3.
z=mp.mpf('0.87')
nu=mp.mpf('.5')
for ell in (0,1,2,3,4):
    direct=mp.quad(lambda x: mp.legendre(ell,x)*mp.exp(-1j*z*x)/2,[-1,1])
    analytic=(-1j)**ell * 2**nu*mp.gamma(nu+1)*z**(-nu)*mp.besselj(ell+nu,z)
    assert abs(direct-analytic)<mp.mpf('1e-95')
    print('plane_wave_order',ell,'relative_error',mp.nstr(abs(direct-analytic)/abs(analytic),8))
print('PASS: Bessel sign, large-degree constants, and independent Fourier normalization checks')
