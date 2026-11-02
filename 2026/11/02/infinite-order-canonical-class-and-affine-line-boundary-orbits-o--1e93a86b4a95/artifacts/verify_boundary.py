"""Symbolic checks for the boundary geometry of the quotient family.

Run with Python 3 and SymPy 1.14 or newer. This checks identities, not
universality of the orbit or Picard-group arguments, which have proofs.
"""
import sympy as S


def check(n):
    assert n >= 1
    x, y, z, w = S.symbols('x y z w')
    u = S.symbols('u1:' + str(n + 1))
    p = S.sympify(S.prod(t*t for t in u[1:]))
    f = x*x*y + z**3*w**2*u[0]**2*p - 1
    dz = x*x
    dy = -3*z*z*w*w*u[0]**2*p
    assert S.expand(S.diff(f,z)*dz + S.diff(f,y)*dy) == 0
    B = z*w
    C = y*z
    assert S.expand(S.diff(B,z)*dz + S.diff(B,y)*dy - x*x*w) == 0
    dC = S.expand(S.diff(C,z)*dz + S.diff(C,y)*dy)
    assert S.expand(dC + 3 - 4*x*x*y + 3*f) == 0  # equality modulo f
    s, q, rho, eta, b, c, pp = S.symbols('s q rho eta b c P')
    F = s*s*eta + q**3*rho**2*pp - 1
    q_inv = 1/(b*b*pp)
    rho_inv = b**3*pp
    eta_inv = c*b*b*pp
    assert S.simplify(F.subs({s:0,q:q_inv,rho:rho_inv,eta:eta_inv})) == 0
    assert S.simplify(q_inv*rho_inv-b) == 0
    assert S.simplify(q_inv*eta_inv-c) == 0
    q_eta = -S.diff(F,eta)/S.diff(F,q)
    jac = S.factor(q_eta)  # dZ^dW^ds = dq^drho^ds
    assert S.simplify(jac + s*s/(3*q*q*rho*rho*pp)) == 0
    for j in range(1, 3):
        # Weighted coordinate identity under generic numeric values.
        val={x:2,y:3,z:5,w:7}
        for i,v in enumerate(u):
            val[v]=i+2+j
        z0=val[z]/val[x]**2
        w0=val[x]**2*val[w]
        v0=val[x]*val[u[0]]
        assert S.simplify(z0**3*w0**2*v0**2*p.subs(val)-(z**3*w**2*u[0]**2*p).subs(val)) == 0


for n in (1,2,3,5):
    check(n)
print('VERIFY_OK')
