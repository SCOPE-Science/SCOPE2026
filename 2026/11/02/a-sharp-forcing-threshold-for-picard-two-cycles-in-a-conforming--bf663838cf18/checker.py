"""Exact checks for a one-node Kirchhoff finite-element Picard phase transition.

Run: python checker.py
Requires: sympy >= 1.11.  No external data files.
"""
from fractions import Fraction
from sympy import Matrix, Rational, Symbol, sqrt, simplify, factor, diff, solve, N


def triangle_area(a, b, c):
    return abs((b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0]))/2


def main():
    corners = [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)),
               (Fraction(1), Fraction(1)), (Fraction(0), Fraction(1))]
    center = (Fraction(1, 2), Fraction(1, 2))
    areas = [triangle_area(center, corners[i], corners[(i+1)%4]) for i in range(4)]
    assert areas == [Fraction(1, 4)]*4
    # Center nodal hat is barycentric on each cell: integrate lambda^2 as A/6.
    mass = sum((t/6 for t in areas), Fraction(0))
    # Center altitude on every triangle is 1/2, so its local gradient norm is 2.
    stiffness = sum((t*4 for t in areas), Fraction(0))
    assert mass == Fraction(1, 6)
    assert stiffness == Fraction(4)
    assert stiffness/mass == Fraction(24)

    x, g, a = Symbol('x', real=True), Symbol('g', real=True), Symbol('a', positive=True)
    alpha, beta, eig, theta, tau = Rational(1,12), Rational(1,72), 24, Rational(1,2), 1
    Gamma = alpha + beta*Rational(1,2)*eig*x**2
    denominator = 1+tau**2*theta*Gamma*eig
    assert simplify(Gamma-(Rational(1,12)+x**2/6))==0
    assert simplify(denominator -2*(1+x**2))==0
    Fg = (g+2)/denominator
    assert simplify(Fg - ((g+2)/2)/(1+x**2)) == 0

    F = a/(1+x**2)
    F2 = a/(1+F**2)
    assert simplify((F2-x) + (x**3+x-a)*(x**2-a*x+1)/((1+x**2)**2+a**2)) == 0
    assert factor(F2-x) == factor(-(x**3+x-a)*(x**2-a*x+1)/((1+x**2)**2+a**2))
    assert simplify(diff(x+x**3-a,x)) == 1+3*x**2

    delta = sqrt(a*a-4)
    p, q = (a-delta)/2, (a+delta)/2
    assert simplify(p+q-a) == 0
    assert simplify(p*q-1) == 0
    assert simplify((F.subs(x,p)-q))==0
    assert simplify((F.subs(x,q)-p))==0
    assert simplify((diff(F,x).subs(x,p)*diff(F,x).subs(x,q))-4/a**2)==0

    # Specific forced Picard system, initial iterate 1, parameter g=4 -> a=3.
    p3,q3=(3-sqrt(5))/2,(3+sqrt(5))/2
    assert simplify(Fg.subs({x:1,g:4})-Rational(3,2))==0
    assert simplify((x+x**3-3).subs(x,p3) - (15-9*sqrt(5))/2)==0
    assert simplify((x+x**3-3).subs(x,q3) - (15+9*sqrt(5))/2)==0
    assert simplify((diff(F,x).subs({x:p3,a:3}) * diff(F,x).subs({x:q3,a:3}))-Rational(4,9))==0
    assert N(p3)<1<N(q3)
    assert p3<1 and N(q3)>2
    # For g=4, fixed root lies between the two cycle values.
    root=solve(x+x**3-3,x)
    roots_real=[float(N(r)) for r in root if abs(float(N(r).as_real_imag()[1]))<1e-10]
    assert len(roots_real)==1 and float(N(p3))<roots_real[0]<float(N(q3))

    # Verify the scalar map and full implicit equation agree for exact rationals.
    for gv in [0, 1, 2, 3, 4, 10, 50]:
        aa=Rational(gv+2,2)
        for xv in [Rational(0), Rational(1,4), Rational(1), Rational(5,3), Rational(7)]:
            z=simplify(Fg.subs({g:gv,x:xv}))
            assert z == aa/(1+xv**2)
            assert simplify((1+theta*Gamma.subs(x,xv)*eig)*z -(gv+2))==0
        if gv>2:
            pp,qq=[simplify(v.subs(a,aa)) for v in (p,q)]
            assert simplify(F.subs({a:aa,x:pp})-qq)==0
            assert simplify(F.subs({a:aa,x:qq})-pp)==0
            assert 0<float(N(4/aa**2))<1
    print('PASS: mesh integrals, exact reduction, global-dynamics factorization,')
    print('      cycle identities, residuals, multiplier, and sampled rational checks.')

if __name__=='__main__':
    main()
