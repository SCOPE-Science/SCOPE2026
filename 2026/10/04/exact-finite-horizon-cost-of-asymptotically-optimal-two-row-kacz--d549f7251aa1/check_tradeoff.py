import sympy as sp

s, w = sp.symbols("s w", positive=True)
c = sp.symbols("c", positive=True)
# Work with c^2 = 1-s^2 after matrix construction.
T = sp.Matrix([
    [(1-w)*(1-w*c**2), -w*c*s],
    [-(1-w)*w*c*s, 1-w*s**2],
])
subs_unit = {c**2: 1-s**2}

# One-sweep witness on a-perp=e2.
e2 = sp.Matrix([0, 1])
witness = sp.expand((T*e2).dot(T*e2)).subs(c**2, 1-s**2)
witness = sp.factor(witness)
assert sp.simplify(witness - ((1-s**2) + s**2*(w-1)**2)) == 0

tr = sp.expand(sp.trace(T)).subs(c**2, 1-s**2)
det = sp.factor(T.det().subs(c**2, 1-s**2))
assert sp.simplify(tr - ((1-s**2)*w**2 - 2*w + 2)) == 0
assert sp.simplify(det - (1-w)**2) == 0

disc = sp.factor(tr**2 - 4*det)
target_disc = sp.factor(w**2*(1-s**2)*(2-w*(1-s))*(2-w*(1+s)))
assert sp.simplify(disc-target_disc) == 0

wstar = sp.simplify(2/(1+s))
q = sp.simplify((1-s)/(1+s))
Tstar = sp.simplify(T.subs(w, wstar).subs(c, sp.sqrt(1-s**2)))
N = sp.simplify(Tstar - q*sp.eye(2))
assert all(sp.simplify(x)==0 for x in N*N)
assert sp.simplify(sp.trace(N)) == 0
nf2 = sp.factor(sum(sp.expand(x**2) for x in N))
assert sp.simplify(nf2 - 16*s**2*(1-s)/(1+s)**3) == 0
assert sp.simplify(nf2/q**2 - 16*s**2/(1-s**2)) == 0

# Exact rational replays of the closed-form power norm.
for sv in [sp.Rational(1,10), sp.Rational(1,3), sp.Rational(3,5), sp.Rational(4,5)]:
    cv = sp.sqrt(1-sv**2)
    qv = (1-sv)/(1+sv)
    Tv = sp.simplify(Tstar.subs(s, sv))
    for kval in [1,2,3,5,8]:
        P = sp.simplify(Tv**kval)
        gram = sp.simplify(P.T*P)
        eigs = list(gram.eigenvals().keys())
        lammax = max([sp.N(x, 50) for x in eigs])
        closed = sp.simplify(qv**kval*(sp.sqrt(1+4*kval**2*sv**2/cv**2)+2*kval*sv/cv))
        assert abs(float(sp.sqrt(lammax) - sp.N(closed,50))) < 1e-11

# Verify the algebra used to reduce the quotient of the two norm formulas.
k = sp.symbols("k", positive=True, integer=True)
assert sp.simplify(q/(1-s**2) - 1/(1+s)**2) == 0
radicand_reduction = sp.expand((1-s**2)*(1+4*k**2*s**2/(1-s**2)))
assert sp.simplify(radicand_reduction - (1-s**2+4*k**2*s**2)) == 0

# Horizon-one strictness reduces to a positive polynomial on 0<s<1.
strict_poly = sp.expand((1+3*s**2) - (1+s**2)**2)
assert sp.simplify(strict_poly - s**2*(1-s)*(1+s)) == 0

# Nearly-parallel scaling: s=t^2, k=alpha/t.
t, alpha = sp.symbols("t alpha", positive=True)
ss = t**2
kk = alpha/t
Rscale = (sp.sqrt(1-ss**2+4*kk**2*ss**2)+2*kk*ss)/(1+ss)**(2*kk)
series = sp.series(sp.log(Rscale), t, 0, 5).removeO()
expected_lead = alpha*(1-sp.Rational(4,3)*alpha**2)*t**3
assert sp.expand(series).coeff(t,3) == sp.expand(expected_lead).coeff(t,3)

print("PASS one-sweep witness identity")
print("PASS trace/determinant/discriminant factorization")
print("PASS defective-optimum nilpotent identities")
print("PASS exact rational power-norm replays")
print("PASS exact ratio-reduction identities")
print("PASS horizon-one strictness polynomial")
print("PASS near-parallel leading crossover coefficient")
print("SERIES", sp.series(sp.log(Rscale), t, 0, 6))
