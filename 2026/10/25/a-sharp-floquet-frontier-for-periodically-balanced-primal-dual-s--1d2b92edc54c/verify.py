"""Exact identities for the two-periodic dual-extrapolated primal-dual update.

Requires SymPy. Run with: python verify.py
"""
import sympy as sp


def companion(r, q):
    return sp.Matrix([[1 + q - 2 * r, r - q], [1, 0]])


def strongly_convex_step(tau, sigma, epsilon):
    a = 1 / (1 + epsilon * tau)
    b = 1 / (1 + epsilon * sigma)
    return sp.Matrix([
        [a, -2 * a * tau, a * tau],
        [b * sigma * a, b * (1 - 2 * sigma * a * tau), b * sigma * a * tau],
        [0, 1, 0],
    ])


def verify():
    r, t = sp.symbols('r t', positive=True)
    z = sp.symbols('z')
    S = t + 1 / t
    B = companion(r, 1 / t) * companion(r, t)
    Tr = 2 * (1 + 2 * r**2 - r * (1 + S))
    Det = 1 + r**2 - r * S
    assert sp.factor(sp.trace(B) - Tr) == 0
    assert sp.factor(B.det() - Det) == 0
    assert sp.factor(1 - Tr + Det - r * (S + 2 - 3 * r)) == 0
    assert sp.factor(1 - Det - r * (S - r)) == 0
    assert sp.factor(1 + Tr + Det - (4 + 5 * r**2 - 2 * r - 3 * r * S)) == 0
    critical = (4 + 5 * r**2 - 2 * r) / (3 * r)
    minimizer = 2 / sp.sqrt(5)
    assert sp.simplify(sp.diff(critical, r).subs(r, minimizer)) == 0
    assert sp.simplify(critical.subs(r, minimizer) - (4 * sp.sqrt(5) - 2) / 3) == 0
    assert sp.simplify(sp.diff(critical, r, 2) - 8 / (3 * r**3)) == 0

    r0 = sp.Rational(1, 2)
    B0 = companion(r0, sp.Rational(1, 3)) * companion(r0, 3)
    assert B0 == sp.Matrix([[sp.Rational(7, 6), -sp.Rational(5, 6)], [3, -sp.Rational(5, 2)]])
    assert sp.factor(B0.charpoly(z).as_expr() - (z**2 + 4*z/3 - sp.Rational(5,12))) == 0
    lam = -(4 + sp.sqrt(31)) / 6
    Y1 = (11 - sp.sqrt(31)) / 18
    assert sp.simplify(B0*sp.Matrix([Y1, 1]) - lam*sp.Matrix([Y1, 1])) == sp.zeros(2, 1)
    x0 = (2-sp.sqrt(31))/18
    assert sp.simplify((1-r0)*1+x0 - Y1) == 0

    # Independently verify the direct three-state implementation against
    # the eliminated second-order recurrence for rational initial data.
    x = sp.Rational(2, 7)
    y = sp.Rational(1, 3)
    yprev = y
    pairs = [(y, yprev)]
    for k in range(14):
        sig = sp.Rational(1) if k % 2 == 0 else sp.Rational(3)
        tau = r0 / sig
        extrap = y if k == 0 else 2*y-yprev
        xn = x - tau*extrap
        yn = y + sig*xn
        if k >= 1:
            assert sp.simplify(sp.Matrix([yn, y]) - companion(r0, sig/(sp.Rational(1) if (k-1)%2==0 else sp.Rational(3)))*sp.Matrix([y,yprev])) == sp.zeros(2,1)
        pairs.append((yn, y))
        x,y,yprev = xn,yn,y
    for j in range(1, 6):
        assert sp.simplify(sp.Matrix(pairs[2*j+1])- B0**j*sp.Matrix(pairs[1])) == sp.zeros(2, 1)

    epsilon = sp.Rational(1, 100)
    P = strongly_convex_step(sp.Rational(1, 6), 3, epsilon) * strongly_convex_step(sp.Rational(1, 2), 1, epsilon)
    poly = z * (1256692803*z**2 + 1571570000*z - 500000000) / 1256692803
    assert sp.factor(P.charpoly(z).as_expr() - poly) == 0
    quadratic_at_minus_one = 1256692803 - 1571570000 - 500000000
    assert quadratic_at_minus_one == -814877197
    w1 = P[:,0]
    w2 = P*w1
    minor = sp.factor(w1[0]*w2[1] - w1[1]*w2[0])
    assert minor == sp.Rational(3638000000000000000, 1579276801111996809)
    assert minor > 0
    print('VERIFY_OK: Floquet polynomial, exact Schur margins, dimension-free threshold,')
    print('  bilinear unstable mode, fourteen direct updates, strongly convex rational certificate')


if __name__ == '__main__':
    verify()
