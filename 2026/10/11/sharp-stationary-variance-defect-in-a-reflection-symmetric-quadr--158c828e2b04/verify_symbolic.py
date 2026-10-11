"""Exact symbolic checks for a reflection-symmetric quadratic flow.

Requires Python 3 and SymPy. This verifies polynomial differential
identities and Hopf solvability coefficients. The invariant-measure
argument and analytic equality rigidity are proved in RESULT.md.
"""
import sympy as sp

x, y, z, a = sp.symbols('x y z a', real=True)
F = sp.Matrix((x*(1-y), z, x**2-y-a*z))
V = sp.Matrix((x, y, z))
lie = lambda f: sp.expand(sum(sp.diff(f, v)*F[k] for k, v in enumerate(V)))
checks = {
    'x2': lie(x**2)-2*x**2*(1-y),
    'y2': lie(y**2)-2*y*z,
    'yz': lie(y*z)-(z**2+x**2*y-y**2-a*y*z),
    'z2': lie(z**2)-2*z*(x**2-y-a*z),
    'divergence': sp.trace(F.jacobian(V))-(1-y-a),
}
g = x**2-1-a*z
checks['strictness_tangency'] = lie(g)-((2*x**2-a)*(1-y)-a*g)
for name, error in checks.items():
    assert sp.simplify(error) == 0, (name, error)

lam = sp.symbols('lam')
J = F.jacobian(V).subs({x: 1, y: 1, z: 0, a: 2})
assert sp.factor(J.charpoly(lam).as_expr()) == (lam+2)*(lam**2+1)

t, amp, omega2 = sp.symbols('t amp omega2', real=True)
D = lambda f: sp.diff(f, t)
L = lambda f: D(D(D(f)))+2*D(D(f))+D(f)+2*f
q1 = amp*sp.cos(t)
q2 = -amp**2/sp.Integer(2) + amp**2/sp.Integer(12)*(sp.cos(2*t)+sp.sin(2*t))
assert sp.trigsimp(L(q2)+2*q1*q1) == 0
order3 = sp.expand_trig(
    omega2*(3*D(D(D(q1)))+4*D(D(q1))+D(q1))
    -D(D(q1)) + 4*q1*q2 + sp.Rational(4,3)*q1**3
)
cos1 = sp.factor(sp.integrate(order3*sp.cos(t), (t,0,2*sp.pi))/sp.pi)
sin1 = sp.factor(sp.integrate(order3*sp.sin(t), (t,0,2*sp.pi))/sp.pi)
assert sp.simplify(cos1 - amp*(6-5*amp**2-24*omega2)/6) == 0
assert sp.simplify(sin1 - amp*(amp**2+12*omega2)/6) == 0
assert cos1.subs({amp:sp.sqrt(2), omega2:-sp.Rational(1,6)}) == 0
assert sin1.subs({amp:sp.sqrt(2), omega2:-sp.Rational(1,6)}) == 0

u1 = sp.sqrt(2)*sp.cos(t)
u2 = -1 + sp.Rational(1,6)*(sp.cos(2*t)+sp.sin(2*t))
g2 = sp.trigsimp(2*u2 + 2*u1**2 + 2*D(D(u2)))
assert sp.trigsimp(g2-(sp.cos(2*t)-sp.sin(2*t))) == 0
assert sp.integrate(g2**2, (t,0,2*sp.pi))/(2*sp.pi) == 1
print('PASS: five moment generators, divergence, tangency, Hopf spectrum,')
print('      order-two equation, order-three solvability, defect coefficient 1.')
