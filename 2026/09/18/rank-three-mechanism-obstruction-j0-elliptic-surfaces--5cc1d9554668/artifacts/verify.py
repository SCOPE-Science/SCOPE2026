from sympy import Rational, symbols, factor, together

n, t = symbols("n t", nonzero=True)
m = Rational(3, 1) / (32*n**3 - 1)
A = 16*n**6
B = 1 + 3*m
C = 16*m**3
F = A*t**6 + B*t**3 + C
Delta = factor(B**2 - 4*A*C)

assert factor(Delta - (1-m)**3) == 0
assert factor(((1-m)/(4*n**2))**3 - Delta/(4*A)) == 0
assert factor(((1-m)/(4*m))**3 - Delta/(4*C)) == 0

# Two rational sections of E0.
x1 = (1-m)/(4*n**2)
y1 = 4*n**3*t**3 + B/(8*n**3)
x2 = 2*t + 16*m**2/t**2
y2 = -4*n**3*t**3 - 12*m - 64*m**3/t**3

assert factor(together(y1**2 - x1**3 - F)) == 0
assert factor(together(y2**2 - x2**3 - F)) == 0

# If m were a rational square, lowest terms force 32*n^3-1=3*b^2.
# The left side is 7 mod 8, while 3*b^2 mod 8 lies in {0,3,4}.
assert {3*(b*b) % 8 for b in range(8)} == {0, 3, 4}

print("delta and cube identities: OK")
print("two E0 section identities: OK")
print("mod-8 nonsquare obstruction: OK")
