"""Recompute exact two-period variable-coefficient BDF4 stability identities.

Requires Python 3 and SymPy; NumPy is optional for sampled spectra.
Uses exact rational interpolation and symbolic polynomial identities.
"""
import sympy as sp

r = sp.symbols('r', positive=True)
z = sp.Symbol('z')

def difference_step(order, current, preceding):
    """BDF interpolation derivative for the current and previous step lengths.

    With d_n=y_n-y_(n-1), returns the companion matrix on
    (d_n,d_(n-1),...,d_(n-order+2)).
    """
    lengths = [current] + list(preceding)
    assert len(lengths) == order
    t = [sp.Integer(0)]
    for length in lengths:
        t.append(t[-1] - length)
    # Derivatives of the Lagrange cardinal polynomials at t[0]=0.
    weights = [sum(1 / (t[0] - t[k]) for k in range(1,order+1))]
    for j in range(1, order+1):
        weight = (1 / t[j]) * sp.prod(
            (t[0]-t[k])/(t[j]-t[k])
            for k in range(1,order+1) if k != j
        )
        weights.append(sp.factor(weight))
    assert sp.factor(sum(weights)) == 0
    coefficients = [sp.factor(-weights[j] / weights[0])
                    for j in range(1,order+1)]
    assert sp.factor(sum(coefficients)-1) == 0
    top = [sp.factor(-sum(coefficients[j:])) for j in range(1,order)]
    return sp.Matrix([top] + [[int(j == i-1) for j in range(order-1)]
                              for i in range(1,order-1)])

# Periodically extended steps: current r, preceding 1,r,1;
# then current 1, preceding r,1,r.
F_r = difference_step(4, r, (1,r,1))
F_1 = difference_step(4, 1, (r,1,r))
T = F_1 * F_r
A = 24*r**4 + 154*r**3 + 269*r**2 + 154*r + 24
B = 24*r**4 + 34*r**3 + 5*r**2 + 34*r + 24
C = 6*r**3 + 19*r**2 + 6*r
H = 2*r**3 + 5*r**2 + 2*r
polynomial = sp.expand(A*z**3 + B*z**2 + C*z - H)
assert sp.factor(A*T.charpoly(z).as_expr() - polynomial) == 0
assert sp.factor(A - (r+4)*(2*r+3)*(3*r+2)*(4*r+1)) == 0
assert sp.factor(polynomial - r**4*polynomial.subs(r,1/r)) == 0

# Real cubic Schur criterion: |c|<1, P(1)>0, -P(-1)>0,
# 1-b+a*c-c^2>0 for P(z)=z^3+a*z^2+b*z+c.
a,b,c = B/A,C/A,-H/A
certificates = {
  '1+c': (A-H, 8*(3*r**4+19*r**3+33*r**2+19*r+3)),
  '1-c': (A+H, 2*(12*r**4+78*r**3+137*r**2+78*r+12)),
  'P(1)': (A+B+C-H, 48*(r+1)**4),
  '-P(-1)': (A-B+C+H, 32*r*(4*r**2+9*r+4)),
  'Schur': (sp.expand(A**2-A*C-B*H-H**2),
     16*(36*r**8+450*r**7+2191*r**6+5332*r**5+7112*r**4
         +5332*r**3+2191*r**2+450*r+36)),
}
for label,(lhs,rhs) in certificates.items():
    assert sp.factor(lhs-rhs) == 0, label
    assert all(v>0 for v in sp.Poly(rhs,r).all_coeffs() if v),label
assert sp.factor(1+c-(A-H)/A) == 0
assert sp.factor(1-c-(A+H)/A) == 0
assert sp.factor(1+a+b+c-(A+B+C-H)/A) == 0
assert sp.factor(1-a+b-c-(A-B+C+H)/A) == 0
assert sp.factor(1-b+a*c-c*c-(A*A-A*C-B*H-H*H)/A**2) == 0

# At either extreme the normalized polynomial tends to z^2(z+1).
assert sp.factor(sp.limit(polynomial/A, r, 0)-z**2*(z+1)) == 0
assert sp.factor(sp.limit(polynomial/A, r, sp.oo)-z**2*(z+1)) == 0
# The isolated root near -1 is -1+16/(3r)+O(r^-2).
epsilon,u = sp.symbols('epsilon u')
expr = sp.expand((polynomial.subs({r:1/epsilon,z:-1+u*epsilon})*epsilon**4))
assert sp.factor(sp.diff(expr,epsilon).subs(epsilon,0)-24*u+128) == 0

# BDF5 is not unconditionally stable even for a two-periodic mesh:
# at ratio 10, the monic quartic has P(-1)<0, hence a real root <-1.
r10 = sp.Integer(10)
G_r = difference_step(5,r10,(1,r10,1,r10))
G_1 = difference_step(5,1,(r10,1,r10,1))
T5 = G_1*G_r
witness = sp.factor((sp.eye(4)+T5).det())
assert witness == -sp.Rational(8874496,44681585)

# Finite checks support the symbolic identities, not replace the proofs.
import numpy as np
max_sample = 0
for rv in np.logspace(-5,5,301):
    mat = np.array(T.subs(r,sp.Float(float(rv))),float)
    rad = max(abs(x) for x in np.linalg.eigvals(mat))
    assert rad < 1+1e-9
    max_sample = max(max_sample,rad)
print('PASS: exact interpolation, monodromy polynomial, reciprocity,')
print('      positive Schur certificates, sharp root asymptotic,')
print('      exact BDF5 instability witness, 301 sampled matrices.')
print('BDF5 P(-1) =',witness)
print('Maximum sampled BDF4 parasitic radius =',round(max_sample,10))
