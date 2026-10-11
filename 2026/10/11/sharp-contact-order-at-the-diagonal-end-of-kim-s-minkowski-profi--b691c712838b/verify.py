import sympy as sp

alpha,beta,m,n,c = sp.symbols("alpha beta m n c", real=True)
a = sp.pi/2 + alpha
b = sp.pi/4 + beta

Va = -sp.cos(a)*(n*sp.sin(a)*sp.cos(b)+m*sp.sin(b))
Vb = sp.sin(b)*sp.cos(b)*(sp.cos(b)-sp.sin(a)*sp.sin(b))

eps = sp.symbols("eps")
def total_series(expr, order):
    return sp.expand(
        sp.series(expr.subs({alpha:eps*alpha,beta:eps*beta}), eps, 0, order)
        .removeO().subs(eps,1)
    )

Va2 = sp.simplify(total_series(Va,3))
Vb2 = sp.simplify(total_series(Vb,3))
assert sp.simplify(Va2 - sp.sqrt(2)*alpha*(m+n+(m-n)*beta)/2) == 0
assert sp.simplify(Vb2 - sp.sqrt(2)*(alpha**2-4*beta)/8) == 0

C = sp.Rational(1,4)/(2*(m+n)+1)
# invariance at quadratic order
inv = sp.simplify(2*C*alpha*(sp.sqrt(2)*(m+n)*alpha/2) -
                  sp.sqrt(2)*(alpha**2-4*C*alpha**2)/8)
assert sp.factor(inv) == 0

q = 1/sp.sin(sp.pi/2+alpha)
q2 = sp.series(q-1,alpha,0,4).removeO()
assert sp.simplify(q2-alpha**2/2) == 0

r = sp.tan(sp.pi/4 + C*alpha**2)
r2 = sp.series(r-1,alpha,0,4).removeO()
assert sp.simplify(r2-2*C*alpha**2) == 0

ratio = sp.simplify((sp.Rational(1,2))/(2*C))
assert sp.simplify(ratio-(2*(m+n)+1)) == 0

print("VERIFY_OK")
print("unstable_manifold_coefficient=1/[4(2(m+n)+1)]")
print("slope_to_radial_error_ratio=2(m+n)+1")
