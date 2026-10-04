#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

class E:
    # a + b*w, where w^2 + w + 1 = 0
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a = Fraction(a)
        self.b = Fraction(b)
    def __add__(self, o):
        o = coerce(o); return E(self.a+o.a, self.b+o.b)
    __radd__ = __add__
    def __neg__(self): return E(-self.a,-self.b)
    def __sub__(self, o): return self + (-coerce(o))
    def __rsub__(self, o): return coerce(o) - self
    def __mul__(self, o):
        o = coerce(o)
        # (a+bw)(c+dw) = ac-bd + (ad+bc-bd)w
        return E(self.a*o.a-self.b*o.b,
                 self.a*o.b+self.b*o.a-self.b*o.b)
    __rmul__ = __mul__
    def inv(self):
        n = self.a*self.a-self.a*self.b+self.b*self.b
        if n == 0: raise ZeroDivisionError
        return E((self.a-self.b)/n, -self.b/n)
    def __truediv__(self,o): return self*coerce(o).inv()
    def __eq__(self,o):
        o=coerce(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return f"E({self.a},{self.b})"

def coerce(x): return x if isinstance(x,E) else E(x,0)

ZERO=E(0); ONE=E(1); W=E(0,1); W2=W*W
assert W2 == E(-1,-1)
assert W*W*W == ONE

def cr(a,b,c,d):
    return (a-c)*(b-d)/((a-d)*(b-c))

base = cr(ZERO, ONE, W, W2)
assert base == -W
vals=[]
for p in permutations((ONE,W,W2)):
    vals.append(cr(ZERO,*p))
assert vals.count(-W) == 3
assert vals.count(-W2) == 3
# In lexicographic permutation order of (1,w,w^2), the cross-ratio-preserving
# permutations are exactly identity and the two 3-cycles.
assert [i for i,v in enumerate(vals) if v == -W] == [0,3,4]

# Character check for the six monomials of
# 27*x^5 + 18*x^3*y*z - 2*x^2*y^3 - x^2*z^3 + 2*x*y^2*z^2 - y^4*z.
# Under x->w*x, y->w^2*y, z->z, a monomial x^a y^b z^c
# has character exponent a+2b mod 3.
monomials=[(5,0,0),(3,1,1),(2,3,0),(2,0,3),(1,2,2),(0,4,1)]
assert { (a+2*b)%3 for a,b,c in monomials } == {2}

# Parametrization weights under s->w*s:
# x=s^4 t has exponent 4 = 1 mod 3;
# both terms of y=s^2 t^3-s^5 have exponent 2 mod 3;
# both terms of z=t^5+2s^3 t^2 have exponent 0 mod 3.
assert 4 % 3 == 1
assert {2%3,5%3} == {2}
assert {0,3%3} == {0}

print('VERIFY_OK')
