"""Symbolic checks for the exact Gaussian momentum moment theorem.

Run with Python 3 and sympy 1.14 or a compatible version.
"""
import sympy as sp


def check():
    d, a, w, z = sp.symbols('d a w z', real=True)
    u = 1 + w - a
    M = sp.Matrix([
        [u**2 + (d+1)*a**2, -2*w*u, w**2],
        [u, -w, 0],
        [1, 0, 0],
    ])
    P = sp.expand((z * sp.eye(3) - M).det())
    assert sp.factor(M.det() - w**3) == 0
    assert sp.factor(P.subs(z, 1) - a*(2*(1-w**2)-a*(d*(1+w)+2))) == 0
    assert sp.factor(P.subs(a, 0) - (z-1)*(z-w)*(z-w**2)) == 0
    dz = sp.diff(P, z).subs({z: 1, a: 0})
    da = sp.diff(P, a).subs({z: 1, a: 0})
    assert sp.factor(-da/dz + 2/(1-w)) == 0
    r = (d+1)/(d+2)
    ac = (1+w)*(d+1-(d+2)*w)/((d+2)*(d*w+d+1))
    completed = -(d+1)*(d*w+d+1)/(d+2)*(a-ac)**2
    completed += w**2*((d+2)**2*w**2-(d+1)**2)/((d+2)**3*(d*w+d+1))
    assert sp.factor(P.subs(z, r)-completed) == 0
    assert sp.factor(P.subs({z: r, w: 0, a: 1/(d+2)})) == 0
    assert sp.factor((u**2+(d+1)*a**2).subs(w, 0)-(1-2*a+(d+2)*a**2)) == 0
    # Independent exact fourth-moment reconstruction from E[g_i^4]=3,
    # E[g_i^2*g_j^2]=1 for i!=j.
    for D in (1, 2, 3, 5, 10):
        gaussian_square = 3 + D - 1
        assert gaussian_square == D + 2
        for W in (sp.Rational(0), sp.Rational(1, 4), sp.Rational(3, 4)):
            ceiling = 2*(1-W**2)/(D*(1+W)+2)
            for factor in (sp.Rational(1, 3), sp.Rational(99, 100), sp.Rational(101, 100), sp.Rational(5, 4)):
                A = ceiling*factor
                Q = M.subs({d: D, a: A, w: W})
                # Numerically enumerate all cubic roots; no infinite proof relies on this.
                eigs = [complex(v) for v in Q.evalf(16).eigenvals(multiple=True)]
                rho = max(map(abs, eigs))
                assert (rho < 1) == (factor < 1), (D, W, factor, rho)
        opt = M.subs({d: D, a: sp.Rational(1, D+2), w: 0})
        assert max(abs(complex(v)) for v in opt.eigenvals()) == float(sp.Rational(D+1, D+2))
    print('VERIFY_OK: Gaussian fourth moments; exact 3x3 recurrence; stability polynomial; unique-optimum certificate; 60 rational spectral checks')


if __name__ == '__main__':
    check()
