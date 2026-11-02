#!/usr/bin/env python3
"""Exact polynomial certificate for characteristic-seven genus-four curve strata."""
import sympy as sp
from collections import Counter

p = 7
a, b, x, z = sp.symbols('a b x z')

def eq7(f, g):
    return sp.Poly(sp.expand(f-g), a, b, modulus=p).is_zero

f = x**10+x**7+a*x**4+b*x
c = sp.Poly(sp.expand(f**3), x)
H = sp.Matrix([[sp.Poly(c.nth(7*i-j), a, b, modulus=p).as_expr()
                for j in range(1, 5)] for i in range(1, 5)])
want = sp.Matrix([[3*a*b**2, 0, 0, b**3],
                  [0, a**3-a*b+3*b**2, 0, 0],
                  [0, 0, 3*a*a+3*a-b, 0],
                  [3, 0, 0, 3*a+3]])
assert all(eq7(H[i,j], want[i,j]) for i in range(4) for j in range(4))
L = a**3-a*b+3*b*b
R = 3*a*a+3*a-b
D = sp.discriminant(z**3+z**2+a*z+b, z)
assert eq7(D, 3*a**3+a*a-3*a*b+b*b+3*b)
assert eq7(H.det(), 3*b*b*L*R*R)
# Elliptic quotient: Y^2 = X(X^3+X^2+aX+b).
fE = x**4+x**3+a*x*x+b*x
assert eq7(sp.Poly(sp.expand(fE**3),x).nth(6), L)
parabola = 3*a*(a+1)
assert eq7(L.subs(b,parabola), -a*a*(a+2)**2)
assert eq7(D.subs(b,parabola), 2*a*(a+2)**3)
# In rank-one block u v^t, zero second iterate iff v^{(7)t}u=0.
S = a*b*b+(a+1)**7
factor = (a-2)*(a-3)*(a+1)**2*(a**3+3*a*a-1)
assert eq7(S.subs(b,parabola),factor)
assert not any((r**3+3*r*r-1)%7==0 for r in range(7))
# Original a-number for differential space rank H; stable Cartier ranks are below.
counts = Counter()
for aa in range(7):
    for bb in range(7):
        discr = (3*aa**3+aa*aa-3*aa*bb+bb*bb+3*bb)%7
        if bb == 0 or discr == 0:
            continue
        lv = (aa**3-aa*bb+3*bb*bb)%7
        rv = (3*aa*(aa+1)-bb)%7
        sv = (aa*bb*bb+(aa+1)**7)%7
        if rv==0: pair=(2,1 if sv==0 else 2)
        elif lv==0: pair=(1,3)
        else: pair=(0,4)
        counts[pair]+=1
assert dict(counts)=={(0,4):29,(1,3):4,(2,2):2,(2,1):2},counts
print('EXACT_GENUS4_C6_P7_IDENTITIES_OK')
print('F7_MARKED_STRATA',dict(sorted(counts.items())))
