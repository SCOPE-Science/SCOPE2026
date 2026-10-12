"""Exact polynomial certificate for an integral free conic-line arrangement.

Run: python3 verify.py. Standard-library only; no finite-field extrapolation.
"""
from itertools import product

class P:
    def __init__(self, terms=None):
        self.t = {e: int(c) for e, c in (terms or {}).items() if int(c)}

    @staticmethod
    def of(obj):
        if isinstance(obj, P): return obj
        return P({(0, 0, 0): int(obj)})

    def __add__(self, other):
        other = P.of(other)
        out = self.t.copy()
        for m, c in other.t.items(): out[m] = out.get(m, 0) + c
        return P(out)

    __radd__ = __add__

    def __neg__(self): return P({m: -c for m, c in self.t.items()})
    def __sub__(self, other): return self + (-P.of(other))
    def __rsub__(self, other): return P.of(other) - self

    def __mul__(self, other):
        other = P.of(other)
        out = {}
        for a, v in self.t.items():
            for b, w in other.t.items():
                m = tuple(a[i] + b[i] for i in range(3))
                out[m] = out.get(m, 0) + v * w
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out, base = P.of(1), self
        while n:
            if n & 1: out = out * base
            n >>= 1
            if n: base = base * base
        return out

    def __eq__(self, other): return self.t == P.of(other).t
    def deriv(self, i):
        out = {}
        for m, c in self.t.items():
            if m[i]:
                k = list(m); k[i] -= 1
                out[tuple(k)] = m[i] * c
        return P(out)

    def mod(self, p): return P({m: c % p for m, c in self.t.items()})
    def __repr__(self): return str(self.t)

x, y, z = (P({tuple(int(j == i) for j in range(3)): 1}) for i in range(3))
E = (x, y, z)
C1 = 3*x**2 + y**2 - 3*z**2
C2 = 3*x**2 + y**2 - 12*z**2
F = C1 * C2 * (x-z) * (x+y+2*z) * (-x+y-2*z)
A = y*(3*x-z)
B = 2*x**2 - x*z - 3*y**2
U = (-x*y*z+y**3,
     9*x**3+27*x**2*z+8*y**2*z-36*z**3,
     3*x**2*y+3*x*y*z+y**3-7*y*z**2)
V = (-x**3+8*x**2*z-2*x*y**2+3*y**2*z-12*z**3,
     5*x**2*y-x*y*z,
     3*x**3-x**2*z+x*y**2-7*x*z**2)
G = tuple(F.deriv(i) for i in range(3))

def dot(a,b): return sum((a[i]*b[i] for i in range(3)), P.of(0))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],
                         a[2]*b[0]-a[0]*b[2],
                         a[0]*b[1]-a[1]*b[0])
def add(a,b): return tuple(a[i]+b[i] for i in range(3))
def scale(c,a): return tuple(c*v for v in a)
def check(msg,test):
    if not test: raise AssertionError(msg)

def main():
    check('Euler', dot(E,G) == 7*F)
    check('U tangent', dot(U,G) == A*F)
    check('V tangent', dot(V,G) == B*F)
    check('unimodular determinant', dot(E,cross(U,V)) == -3*F)
    W = add(scale(B,U),scale(-A,V))
    P3 = add(scale(7,U),scale(-A,E))
    Q3 = add(scale(7,V),scale(-B,E))
    check('degree-five global syzygy', dot(W,G) == 0)
    check('first cubic syzygy', dot(P3,G) == 0)
    check('second cubic syzygy', dot(Q3,G) == 0)
    check('cubic cross certificate',cross(P3,Q3)==scale(-21,G))
    check('Euler/fifth cross identity',
          add(add(cross(E,W),scale(3,G)),scale(7,cross(U,V))) == (P.of(0),)*3)
    for p in (5,7,11,13,17,19,23,31):
        check('Saito determinant mod %d' % p,
              (dot(E,cross(U,V)) + 3*F).mod(p) == 0)
        if p == 7:
            check('degree-one characteristic-seven syzygy',dot(E,G).mod(p)==0)
            check('characteristic-seven cross unit',all((cross(E,W)[i]+3*G[i]).mod(p)==0 for i in range(3)))
        else:
            check('cubic cross unit mod %d' % p,all((cross(P3,Q3)[i]+21*G[i]).mod(p)==0 for i in range(3)))
    # Modulo seven A=y(3x-z), B=2x^2-xz-3y^2 are coprime:
    # neither y nor (3x-z) divides B. Check both restrictions.
    check('B not divisible by y modulo seven', B.mod(7) != (B-B).mod(7) and
          (2*x**2-x*z).mod(7) != 0)
    check('B not divisible by 3x-z modulo seven',
          (-(x**2+3*y**2)).mod(7) != 0)
    print('VERIFY_OK: exact integral logarithmic basis, cubic syzygies, and p=7 degree jump')

if __name__ == '__main__':
    main()
