from fractions import Fraction as F

N = 9  # q1,q2,q3,p1,p2,p3,L,beta,eta
ZERO = (0,) * N

class P:
    def __init__(self, d=None):
        self.d = {m:F(c) for m,c in (d or {}).items() if c}
    @staticmethod
    def c(c):
        return P({ZERO:F(c)})
    @staticmethod
    def v(i):
        m = [0]*N
        m[i] = 1
        return P({tuple(m):F(1)})
    def __add__(self, o):
        o = o if isinstance(o,P) else P.c(o)
        d = dict(self.d)
        for m,c in o.d.items():
            d[m] = d.get(m,F(0)) + c
            if not d[m]: del d[m]
        return P(d)
    __radd__ = __add__
    def __neg__(self):
        return P({m:-c for m,c in self.d.items()})
    def __sub__(self,o): return self + (-o)
    def __rsub__(self,o): return P.c(o) - self
    def __mul__(self,o):
        o = o if isinstance(o,P) else P.c(o)
        d = {}
        for m,c in self.d.items():
            for n,e in o.d.items():
                k = tuple(a+b for a,b in zip(m,n))
                d[k] = d.get(k,F(0)) + c*e
        return P(d)
    __rmul__ = __mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n >= 0
        r = P.c(1)
        a = self
        while n:
            if n & 1: r = r*a
            a = a*a
            n //= 2
        return r
    def __eq__(self,o):
        o = o if isinstance(o,P) else P.c(o)
        return self.d == o.d

q1,q2,q3,p1,p2,p3,L,beta,eta = [P.v(i) for i in range(N)]
psq = p1**2 + p2**2 + p3**2
qsq = q1**2 + q2**2 + q3**2
B1 = -beta*q1**3 + eta**2*q1 - eta*q2 - eta*q3
B2 = -beta*q2**3 - eta*q1
B3 = -beta*q3**3 - eta*q1
qB = q1*B1 + q2*B2 + q3*B3

F1 = (-L**2*beta*q1**3 + beta*q1**5 + beta*q1*q2**4 + beta*q1*q3**4
      + L**2*eta**2*q1 - eta**2*q1**3 - L**2*eta*q2 - L**2*eta*q3
      + 2*eta*q1**2*q2 + 2*eta*q1**2*q3 - psq*q1)
F2 = (-L**2*beta*q2**3 + beta*q1**4*q2 + beta*q2**5 + beta*q2*q3**4
      - eta**2*q1**2*q2 - eta*q1*L**2 + 2*eta*q1*q2**2
      + 2*eta*q1*q2*q3 - psq*q2)
F3 = (-L**2*beta*q3**3 + beta*q1**4*q3 + beta*q2**4*q3 + beta*q3**5
      - eta**2*q1**2*q3 - eta*q1*L**2 + 2*eta*q1*q2*q3
      + 2*eta*q1*q3**2 - psq*q3)

assert F1 == L**2*B1 - q1*(qB + psq)
assert F2 == L**2*B2 - q2*(qB + psq)
assert F3 == L**2*B3 - q3*(qB + psq)

# L^2*Sdot = L^2*|p|^2 + q dot F.
left = L**2*psq + q1*F1 + q2*F2 + q3*F3
right = -(qsq - L**2)*(qB + psq)
assert left == right

ell = F(1,100)
p = (F(11,1000), F(51,1000), F(51,1000))
states = {
    'blue': ((F(0),F(0),F(1,100)),p),
    'magenta': ((F(0),F(1,100),F(0)),p),
    'green': ((F(1,100),F(0),F(0)),p),
}
expected = {
    'blue': F(51,100000),
    'magenta': F(51,100000),
    'green': F(11,100000),
}
for name,(qv,pv) in states.items():
    radius2 = sum(x*x for x in qv)
    tangent = sum(x*y for x,y in zip(qv,pv))
    assert radius2 == ell*ell
    assert tangent == expected[name]
    print(f'{name}_radius_squared = {radius2}')
    print(f'{name}_tangent_defect = {tangent}')
    print(f'{name}_radial_derivative = {2*tangent}')

print('vector_field_factorization = exact')
print('defect_dynamics_after_clearing_L2 = exact')
print('VERIFY_OK')
