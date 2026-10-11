from sympy import symbols, sqrt, chebyshevt, expand, simplify, diff, discriminant

x = symbols("x")
s5 = sqrt(5)
a = s5 / 2
b = (7 * s5 - 12) / 20
c = (3 * s5 - 8) / 20
r = -(1 + s5) / 4

assert simplify(b + c - (a - 1)) == 0
assert simplify(4 * b - 6 * c - a) == 0
assert simplify(-1 / r - (s5 - 1)) == 0

q = expand(1 + a * x + b * chebyshevt(4, x) + c * chebyshevt(6, x))
R = ((24 * s5 - 64) / 5) * x**3 + ((36 - 4 * s5) / 5) * x**2 + ((9 - 15 * s5) / 5) * x + (14 - 2 * s5) / 5
assert simplify(q - (x + 1) * (x - r)**2 * R) == 0
assert simplify(q.subs(x, -1)) == 0
assert simplify(q.subs(x, r)) == 0
assert simplify(diff(q, x).subs(x, r)) == 0
assert simplify(R.subs(x, 1) - (-1 + 3 * s5 / 5)) == 0

Rp = diff(R, x)
D = simplify(discriminant(Rp, x))
assert simplify(D - 32 * (1063 - 477 * s5) / 25) == 0
assert 3**2 * 5 < 8**2
assert 1063**2 - 5 * 477**2 == -7676
assert 3**2 * 5 > 5**2

print("VERIFY_OK", "a=sqrt(5)/2", "b=(7*sqrt(5)-12)/20", "c=(3*sqrt(5)-8)/20", "disc=32*(1063-477*sqrt(5))/25")
