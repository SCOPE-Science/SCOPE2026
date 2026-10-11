import sympy as sp

l = sp.symbols("l", real=True)
s = sp.sqrt(2)
r = s - 1
T = 1 - (2 - s) * l

x = sp.Matrix([-r, 1])
y = sp.Matrix([1, r])
p = sp.simplify(l * x + (1 - l) * y)
q = sp.simplify(l * x - (1 - l) * y)

assert sp.simplify((r + 1) / s - 1) == 0
assert sp.simplify(p[0] - (1 - s*l)) == 0
assert sp.simplify(p[1] - (r + (2-s)*l)) == 0
assert sp.simplify((p[0] + p[1]) / s - T) == 0
assert sp.factor(T - p[0]) == 2*l*(s-1)
assert sp.factor(T - p[1]) == (s-2)*(2*l-1)

assert sp.simplify(q[0] + T) == 0
assert sp.simplify(q[1] - (s*l-r)) == 0
b = sp.simplify(r/s)
assert sp.simplify(b - (1-s/2)) == 0
neg_branch = sp.factor(r*T - (r-s*l))
pos_branch = sp.factor(r*T - (s*l-r))
assert neg_branch == -2*l*(-2+s)
assert sp.simplify(pos_branch - (-2*(-1+s)*(2*l-1))) == 0

# Endpoint checks certify the affine nonnegative factors on their stated intervals.
for expr, pts in [
    (T-p[0], [0, sp.Rational(1,2)]),
    (T-p[1], [0, sp.Rational(1,2)]),
    (neg_branch, [0, b]),
    (pos_branch, [b, sp.Rational(1,2)]),
]:
    for pt in pts:
        assert sp.N(expr.subs(l, pt), 50) >= 0

hilbert_gap = sp.factor(T**2 - (l**2 + (1-l)**2))
assert hilbert_gap == -2*l*(s-1)*(2*l-1)

# Published upper estimate on this half interval: lambda*sqrt(2)+1-2*lambda.
assert sp.simplify(l*s + 1 - 2*l - T) == 0
print("VERIFY_OK")
