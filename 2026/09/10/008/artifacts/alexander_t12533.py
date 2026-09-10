"""Alexander data of t12533 from Teragaito braid word via reduced Burau.
Validated: trefoil s1^3 -> t^2-t+1; fig8 s1 s2^-1 s1 s2^-1 -> -t+3-1/t (up to unit).
Exact sympy arithmetic. Outputs Alexander + Conway a2, a4 + genus bound."""
import sympy as sp

t = sp.Symbol('t')
z = sp.Symbol('z')

def red(n, i):
    """Reduced Burau matrix rho(sigma_i), (n-1)x(n-1).

    Validated: det=-t for all i; braid relations hold (checked for B4).
    s1: [[-t],[1,1,...]]; s_{n-1}: [...,1,t / -t]; interior s_i:
    rows/cols (i-1,i): [[1,t],[0,-t]] with M[i,i-1]=1 coupling to row i+1.
    """
    M = sp.eye(n - 1)
    if i == 1:
        M[0, 0] = -t
        if n - 1 > 1:
            M[1, 0] = 1
    elif i == n - 1:
        M[n - 2, n - 2] = -t
        if n - 1 > 1:
            M[n - 3, n - 2] = t
    else:
        # interior: 2x2 block [[1,t],[0,-t]] at rows/cols (i-1,i) 1-indexed
        # 0-indexed rows a=i-2, b=i-1; cols a=i-2, b=i-1:
        M[i-2, i-2] = 1
        M[i-2, i-1] = t
        M[i-1, i-2] = 0
        M[i-1, i-1] = -t
        # coupling: row b+1 col b = 1
        M[i, i-1] = 1
    return M

def alexander(n, word):
    B = sp.eye(n - 1)
    for i in word:
        assert 1 <= i <= n - 1
        B = red(n, i) * B
    num = (sp.eye(n - 1) - B).det()
    den = sum(t**k for k in range(n)) / 1  # 1+t+...+t^{n-1}
    D = sp.factor(num / den)
    return sp.expand(D)

# validations
D3 = alexander(2, [1, 1, 1])
assert sp.expand(D3 - (t**2 - t + 1)) == 0, D3
Bf = red(3, 1) * red(3, 2).inv() * red(3, 1) * red(3, 2).inv()
# NOTE: matrix product order above is reversed vs alexander(); validate via alexander() path:
Bfv = sp.eye(2)
for i in [1, -2, 1, -2]:
    F = red(3, abs(i))
    Bfv = (F if i > 0 else F.inv()) * Bfv
Df = sp.expand((sp.eye(2) - Bfv).det() / (1 + t + t**2))
assert sp.simplify(Df - (-(t**2 - 3*t + 1) / t**2)) == 0, Df
print("validations OK: trefoil", D3, "; fig8", Df)

word = [1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 3, 2, 1, 1, 2, 2, 1, 3, 2, 2]
print("word length =", len(word))
D = alexander(4, word)
print("Delta(t) =", D)
print("Delta(1) =", D.subs(t, 1))
P = sp.Poly(D, t)
lo = min(e for (e,) in P.monoms())
hi = P.degree()
print("exponent range:", lo, hi)
# symmetrize: Delta_sym(t) = t^{-g} D with g = (hi+lo)/2
assert (hi + lo) % 2 == 0
g = (hi + lo) // 2
Ds = sp.expand(D * t**(-g))
print("symmetric Delta =", Ds)
assert sp.expand(D - t**24 * D.subs(t, 1/t)) == 0
print("symmetric check OK: D(t) = t^24 D(1/t); genus bound g =", 24 // 2)
# Conway: nabla(z) with z = sqrt(t)-1/sqrt(t); Delta(t) = nabla(t^{1/2}-t^{-1/2})
# substitute u = t + 1/t - 2 = z^2; recover Conway coefficients via Chebyshev rewriting
u = sp.Symbol('u')
# express symmetric Laurent poly in u = t + t^-1
gdeg = (hi - lo) // 2
print("half-span g =", gdeg)
# symmetric Laurent: c_g (t^g+t^-g)+...+c_0 ; solve for c by evaluating? Use recurrence T_k.
T = {0: sp.Integer(1), 1: u}
for k in range(2, gdeg + 1):
    T[k] = sp.expand(u * T[k-1] - T[k-2])
# build equations: Ds(t) = sum_{k=0..gdeg} c_k T_k(u), u=t+1/t
cs = sp.symbols('c0:%d' % (gdeg + 1))
expr = sum(cs[k] * T[k] for k in range(gdeg + 1))
# match coefficients of t^0..t^gdeg after substituting u=t+1/t and clearing: compare as Laurent
lhs = sp.expand(expr.subs(u, t + 1/t))
# collect t powers -gdeg..gdeg, match Ds
eqs = []
Pt = sp.Poly(sp.expand(lhs * t**gdeg), t)
Pd = sp.Poly(sp.expand(Ds * t**gdeg), t)
for e in range(2 * gdeg + 1):
    eqs.append(Pt.nth(e) - Pd.nth(e))
sol = sp.solve(eqs, cs, dict=True)[0]
print("t+1/t coeffs:", sol)
# Conway nabla(z) = sum c_k (z^2+2 ... ) no: T_k(u) with u = z^2+2
nabla = sp.expand(sum(sol[cs[k]] * T[k].subs(u, z**2 + 2) for k in range(gdeg + 1)))
print("Conway nabla(z) =", nabla)
Pn = sp.Poly(nabla, z)
a = {e: Pn.nth(e) for e in range(Pn.degree() + 1)}
print("a2 =", a.get(2, 0), " a4 =", a.get(4, 0), " deg nabla =", Pn.degree())
print("det = |Delta(-1)| =", abs(int(Ds.subs(t, -1))))
