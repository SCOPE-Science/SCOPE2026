"""Symbolic algebra checks for the critical-periodic Linz--Sprott modulus jerk.

Install the only third-party dependency using the accompanying requirements.txt.
This checks algebraic identities; measure-theoretic and extremal claims are proved
in RESULT.md, not certified by this script.
"""
from sympy import Matrix, Rational, Symbol, cos, diff, factor, simplify, sin, symbols

x, v, w, A = symbols("x v w A", real=True)
zeta, radius, t = symbols("zeta radius t", real=True)
for sign in (-1, 1):
    vector = Matrix([v, w, -A*w - v + sign*x - 1])
    G = v*w + A*v**2/2 - sign*x**2/2 + x
    H = (w**2+v**2)/2 - v*(sign*x-1)
    def lie(expr):
        return simplify(sum(diff(expr, u)*vector[i]
                            for i, u in enumerate((x, v, w))))
    assert simplify(lie(G)-(w**2-v**2)) == 0
    assert simplify(lie(H)+(A*w**2+sign*v**2)) == 0
    assert simplify(lie(H+A*G)+(A+sign)*v**2) == 0
    critical = -sign
    charpoly = zeta**3 + critical*zeta**2+zeta-sign
    assert factor(charpoly) == (zeta-sign)*(zeta**2+1)
    curve = sign + radius*cos(t)
    residual = simplify(diff(curve,t,3) +critical*diff(curve,t,2)
                        +diff(curve,t)-sign*curve + 1)
    assert residual == 0
    assert simplify(diff(curve,t) + radius*sin(t)) == 0
    cv, cw = diff(curve,t), diff(curve,t,2)
    circle_G = G.subs({A:critical, x:curve, v:cv, w:cw})
    circle_H = H.subs({x:curve, v:cv, w:cw})
    assert simplify(circle_H + critical*circle_G - (radius**2 - Rational(1,2))) == 0
    opposite = -sign
    assert simplify(critical*(-opposite*opposite**2/2 + opposite) - Rational(1,2)) == 0
print("PASS: both smooth branches, two conserved-balance identities, critical factors, exact circles, and their Lyapunov levels")
