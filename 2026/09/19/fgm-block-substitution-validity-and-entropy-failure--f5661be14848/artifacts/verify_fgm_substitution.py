from fractions import Fraction
import sympy as sp
import mpmath as mp


def threshold(r, s):
    A = 2**r - 1
    B = 2**s - 1
    return Fraction(-1, A * B), Fraction(1, max(A, B))


def symbolic_density(r, s):
    theta = sp.symbols('theta', real=True)
    xs = sp.symbols(f'x0:{r}', positive=True)
    ys = sp.symbols(f'y0:{s}', positive=True)
    U = sp.prod(xs)
    V = sp.prod(ys)
    G = U * V * (1 + theta * (1-U) * (1-V))
    g = G
    for q in xs + ys:
        g = sp.diff(g, q)
    target = 1 + theta * (1 - 2**r * U) * (1 - 2**s * V)
    return sp.simplify(g - target) == 0, sp.factor(g)


def I(a):
    if abs(a) < mp.mpf('1e-25'):
        return mp.mpf('0')
    F = lambda t: t*t*mp.log(t)/2 - t*t/4
    return (F(1+a) - F(1-a))/(2*a)


def entropies(theta):
    # For r=s=1, average over U~Unif(0,1).
    H_outer = -mp.quad(lambda u: I(theta*(1-2*u)), [0, 1])
    # For r=2,s=1, W=X1*X2 has density -log(w) on (0,1).
    H_comp = -mp.quad(lambda w: I(theta*(1-4*w))*(-mp.log(w)), [0, 1])
    return H_outer, H_comp


if __name__ == '__main__':
    for r, s in [(1,1), (2,1), (2,2), (3,2)]:
        ok, density = symbolic_density(r, s)
        print(f'r={r}, s={s}, formula_ok={ok}, admissible_theta={threshold(r,s)}')
        print(f'  density={density}')

    # Explicit failure of closure: r=2,s=1, theta=1 at (9/10,9/10,1/10).
    x = Fraction(9,10)
    y = Fraction(9,10)
    z = Fraction(1,10)
    bad_density = 1 + (1 - 4*x*y)*(1 - 2*z)
    print('closure_counterexample_density=', bad_density, float(bad_density))

    # Entropy counterexample inside the valid range: theta=1/4.
    mp.mp.dps = 30
    theta = mp.mpf('0.25')
    Ho, Hc = entropies(theta)
    print('theta=1/4')
    print('H_outer=', mp.nstr(Ho, 24))
    print('H_composite_r2_s1=', mp.nstr(Hc, 24))
    print('H_composite_minus_outer=', mp.nstr(Hc-Ho, 24))

    q1 = (mp.mpf(4)/3)**1 - 1
    q2 = (mp.mpf(4)/3)**2 - 1
    print('H_outer_second_derivative_at_0=', mp.nstr(-q1*q1, 24))
    print('H_r2_s1_second_derivative_at_0=', mp.nstr(-q2*q1, 24))
