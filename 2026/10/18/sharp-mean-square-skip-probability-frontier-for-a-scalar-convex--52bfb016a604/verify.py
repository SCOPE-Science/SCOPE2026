#!/usr/bin/env python3
"""Exact second-moment algebra for a scalar Bernoulli proximal splitting scheme."""
import sympy as sp

p = sp.Symbol("p", positive=True)
I = sp.eye(2)
M_skip = sp.Matrix([[sp.Rational(1, 2), -sp.Rational(1, 2)], [0, 1]])
M_update = sp.Matrix([
    [sp.Rational(1, 2) - 1/(4*p), -sp.Rational(1, 2) + 3/(4*p)],
    [sp.Rational(1, 4), sp.Rational(1, 4)],
])
D = 6*p**2 + 7*p - 1
W = sp.Matrix([
    [p*(15*p + 13), 9*p - 5],
    [9*p - 5, (12*p**2 + 7*p + 9)/p],
])

def average_congruence(X):
    return (1-p)*M_skip.T*X*M_skip + p*M_update.T*X*M_update

checks = 0

def check_matrix_equal(X, Y):
    global checks
    Z = X - Y
    assert all(sp.cancel(z) == 0 for z in Z), sp.simplify(Z)
    checks += 1

check_matrix_equal(W - average_congruence(W), 2*D*I)
check_matrix_equal((W/(2*D)) - average_congruence(W/(2*D)), I)
assert sp.simplify(W.det() - 4*(3*p+1)*(15*p**2+10*p+23)) == 0
checks += 1
critical = (sp.sqrt(73) - 7)/12
assert sp.simplify(D.subs(p, critical)) == 0
assert 0 < float(critical) < 1
checks += 2

# The covariance lift independently checks the exact critical polynomial.
def moment_map(M):
    a,b,c,d = M[0,0],M[0,1],M[1,0],M[1,1]
    return sp.Matrix([
        [a*a, 2*a*b, b*b],
        [a*c, a*d+b*c, b*d],
        [c*c, 2*c*d, d*d],
    ])

B = (1-p)*moment_map(M_skip) + p*moment_map(M_update)
assert sp.simplify((sp.eye(3)-B).det() - D/16) == 0
checks += 1

# Exactly enumerate every Bernoulli history through six iterations.
# Compare direct path sums with the independently assembled second-moment lift.
for sample_p in [sp.Rational(1,16), sp.Rational(1,8), sp.Rational(1,4),
                 sp.Rational(1,2), sp.S.One]:
    skip = M_skip
    update = M_update.subs(p, sample_p)
    lift = B.subs(p, sample_p)
    for initial in [sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([2, -3])]:
        moment = sp.Matrix([initial[0]**2, initial[0]*initial[1], initial[1]**2])
        paths = [(sp.S.One, initial)]
        for k in range(7):
            direct = sp.Matrix([
                sum(prob*z[0]**2 for prob,z in paths),
                sum(prob*z[0]*z[1] for prob,z in paths),
                sum(prob*z[1]**2 for prob,z in paths),
            ])
            check_matrix_equal(direct, moment)
            paths = [(prob*(1-sample_p), skip*z) for prob,z in paths] + [
                (prob*sample_p, update*z) for prob,z in paths]
            moment = lift*moment

print(f"PASS: {checks} exact algebraic / exhaustive finite-horizon consistency checks")
print(f"Critical probability = {sp.simplify(critical)} = {float(critical):.12f}")
print("The all-iteration theorem is justified by the positive Lyapunov identities, not finite enumeration.")
