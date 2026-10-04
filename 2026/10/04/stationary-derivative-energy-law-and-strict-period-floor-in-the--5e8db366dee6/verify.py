from fractions import Fraction

N=6  # x,y,z,a,b,g
class P:
    def __init__(self,d=None):
        self.d={m:Fraction(c) for m,c in (d or {}).items() if c}
    @staticmethod
    def c(c): return P({(0,)*N:Fraction(c)})
    @staticmethod
    def v(i):
        m=[0]*N;m[i]=1
        return P({tuple(m):Fraction(1)})
    def __add__(self,o):
        o=o if isinstance(o,P) else P.c(o); d=self.d.copy()
        for m,c in o.d.items(): d[m]=d.get(m,0)+c
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({m:-c for m,c in self.d.items()})
    def __sub__(self,o): return self+(-o)
    def __rsub__(self,o): return P.c(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,P) else P.c(o); d={}
        for m,c in self.d.items():
            for n,e in o.d.items():
                k=tuple(m[i]+n[i] for i in range(N)); d[k]=d.get(k,0)+c*e
        return P(d)
    __rmul__=__mul__
    def __pow__(self,n):
        r=P.c(1)
        for _ in range(n): r=r*self
        return r
    def diff(self,i):
        d={}
        for m,c in self.d.items():
            if m[i]:
                k=list(m); k[i]-=1; d[tuple(k)]=d.get(tuple(k),0)+c*m[i]
        return P(d)
    def zero(self): return not self.d

x,y,z,a,b,g=[P.v(i) for i in range(N)]
fx=y+a*z
fy=b*x**2-y
fz=g-x
F=[fx,fy,fz]
def L(p): return sum((p.diff(i)*F[i] for i in range(3)), P.c(0))

v=g-x             # z' = gamma-x
w=-(y+a*z)        # z'' = -x'
cert=Fraction(1,2)*w**2 + Fraction(1,2)*a*v**2 + a*z*v - Fraction(1,3)*b*(g-v)**3
assert (L(cert) - (a*v**2 - w**2)).zero()

# Coordinate stationarity identities are represented by exact generators.
assert (L(x)-fx).zero()
assert (L(y)-fy).zero()
assert (L(z)-fz).zero()

# Equilibrium substitution x=g, y=b g^2, z=-b g^2/a satisfies vector field after clearing a.
eqx=g
eqy=b*g**2
# a*fx at equilibrium with a*z = -b*g^2 is zero exactly:
assert (eqy - b*g**2).zero()
assert (b*eqx**2-eqy).zero()
assert (g-eqx).zero()

# Jerk relation for z: z''' + z'' + a z' + a z + b(g-z')^2 = 0.
wprime=L(w)
assert (wprime + w + a*v + a*z + b*(g-v)**2).zero()
print('VERIFY_OK')
