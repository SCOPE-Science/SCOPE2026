"""Exact symbolic reproduction of signed-edge polarization identities."""
import sympy as sp


def base(n, edges, ends, intrinsic):
    H = sp.eye(n)
    for i, j, weight in edges:
        H[i, i] += weight
        H[j, j] += weight
        H[i, j] -= weight
        H[j, i] -= weight
    u = sp.zeros(n, 1)
    u[ends[0]] = 1
    u[ends[1]] = 1
    z0 = H.inv() * sp.Matrix(intrinsic)
    v = H.inv() * u
    c = (u.T * z0)[0]
    d = (z0.T * v)[0]
    e = (v.T * v)[0]
    r = (u.T * v)[0]
    t = sp.symbols('t', positive=True)
    z = (H + t * u * u.T).inv() * sp.Matrix(intrinsic)
    P = sp.factor((z.T * z)[0] / n)
    exact_derivative = 2 * c * (t * (c * e - r * d) - d) / (n * (1 + t * r) ** 3)
    assert sp.simplify(sp.diff(P, t) - exact_derivative) == 0
    assert all(sp.simplify(q) == 0 for q in z - (z0 - t * c * v / (1 + t * r)))
    return H, u, v, r, e, P, exact_derivative


def main():
    t, a, b = sp.symbols('t a b', positive=True)
    det = 3 * a * b + 2 * a + 2 * b + 1
    delta = (a - b) * (2 * a * b - 1)
    common = a * a * b + a * b * b + 4 * a * b + a + b
    weights = [(0, 1, a), (1, 2, b)]
    H, u, v, r, e, _, _ = base(3, weights, (0, 2), [1, 0, 0])
    assert sp.factor(H.det() - det) == 0
    for i, expected in enumerate([-delta, -2 * common, delta]):
        intrinsic = sp.eye(3)[:, i]
        z0 = H.inv() * intrinsic
        c = (u.T * z0)[0]
        d = (z0.T * v)[0]
        assert sp.factor((c * e - r * d) - expected / det ** 2) == 0
    _, _, _, _, _, P3, D3 = base(3, [(0, 1, 3), (1, 2, 1)], (0, 2), [0, 0, 1])
    assert sp.simplify(P3 - (27*t*t+32*t+73)/(6*(13*t+9)**2)) == 0
    assert sp.simplify(D3 - 35*(t-23)/(3*(13*t+9)**3)) == 0
    assert P3.subs(t, 0) == sp.Rational(73, 486)
    assert P3.subs(t, 23) == sp.Rational(7, 264)
    assert sp.limit(P3, t, sp.oo) == sp.Rational(9,338)
    _, _, _, _, _, P4, D4 = base(4, [(0,1,1),(1,2,1),(1,3,1),(2,3,1)], (0,2), [1,0,0,0])
    assert sp.simplify(P4 - 7*(37*t*t+56*t+96)/(4*(51*t+40)**2)) == 0
    assert sp.simplify(D4 - 14*(13*t-944)/(51*t+40)**3) == 0
    assert P4.subs(t, 0) == sp.Rational(21,200)
    assert P4.subs(t, sp.Rational(944,13)) == sp.Rational(173,6952)
    assert sp.limit(P4,t,sp.oo) == sp.Rational(259,10404)
    H3, u3, v3, r3, e3, _, _ = base(3,[(0,1,1),(1,2,1)],(0,2),[1,0,0])
    for i in range(3):
        seed = H3.inv()*sp.eye(3)[:,i]
        c=(u3.T*seed)[0]; d=(seed.T*v3)[0]
        assert sp.simplify((c*e3-r3*d) - (0 if i != 1 else -sp.Rational(1,4)))==0
    print('PASS: general rank-one derivative, complete weighted three-path coefficients, two exact witnesses, unweighted three-path boundary')


if __name__ == '__main__':
    main()
