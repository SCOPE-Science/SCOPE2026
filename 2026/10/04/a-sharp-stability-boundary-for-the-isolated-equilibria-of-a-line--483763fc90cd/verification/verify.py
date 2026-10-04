from fractions import Fraction
import cmath

class Q2:
    # Exact numbers u + v*sqrt(10).
    __slots__ = ("u", "v")
    def __init__(self, u=0, v=0):
        self.u = Fraction(u)
        self.v = Fraction(v)
    def __add__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.u + o.u, self.v + o.v)
    __radd__ = __add__
    def __neg__(self): return Q2(-self.u, -self.v)
    def __sub__(self, o): return self + (- (o if isinstance(o,Q2) else Q2(o)))
    def __rsub__(self, o): return Q2(o) - self
    def __mul__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.u*o.u + 10*self.v*o.v, self.u*o.v + self.v*o.u)
    __rmul__ = __mul__
    def __eq__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return self.u == o.u and self.v == o.v
    def __repr__(self): return f"Q2({self.u},{self.v})"

# Polynomials in lambda, ascending coefficients, with Q2 coefficients.
def padd(p,q):
    n=max(len(p),len(q)); r=[Q2() for _ in range(n)]
    for i in range(n):
        if i<len(p): r[i]=r[i]+p[i]
        if i<len(q): r[i]=r[i]+q[i]
    return r

def pneg(p): return [-x for x in p]
def psub(p,q): return padd(p,pneg(q))
def pmul(p,q):
    r=[Q2() for _ in range(len(p)+len(q)-1)]
    for i,x in enumerate(p):
        for j,y in enumerate(q): r[i+j]=r[i+j]+x*y
    return r

def det3_poly(M):
    t1=pmul(M[0][0], psub(pmul(M[1][1],M[2][2]), pmul(M[1][2],M[2][1])))
    t2=pmul(M[0][1], psub(pmul(M[1][0],M[2][2]), pmul(M[1][2],M[2][0])))
    t3=pmul(M[0][2], psub(pmul(M[1][0],M[2][1]), pmul(M[1][1],M[2][0])))
    return padd(psub(t1,t2),t3)

# a=5, b=2, c=34; s=sqrt(10); E+=(34s/25,s,34/5).
s=Q2(0,1)
x=Fraction(34,25)*s
y=s
z=Fraction(34,5)
a=Fraction(5); b=Fraction(2)
# lambda*I - J at E+.
L=[Q2(0),Q2(1)]
def const(x): return [x if isinstance(x,Q2) else Q2(x)]
def lin_minus_const(k): return [-(k if isinstance(k,Q2) else Q2(k)), Q2(1)]
M=[
    [lin_minus_const(-a), const(-z), const(-y)],
    [const(0), L, const(a*x)],
    [const(-y), const(-x), lin_minus_const(-b)],
]
p=det3_poly(M)
expected=[Q2(Fraction(4624,5)),Q2(Fraction(2312,25)),Q2(7),Q2(1)]
assert p==expected, (p,expected)
assert all(co.v==0 for co in p)
routh = Fraction(7)*Fraction(2312,25)-Fraction(4624,5)
assert routh == Fraction(-6936,25) and routh < 0

# Independent numeric root check by Durand--Kerner.
co=[1.0,7.0,2312.0/25.0,4624.0/5.0]
def f(z): return ((co[0]*z+co[1])*z+co[2])*z+co[3]
roots=[1+0j, -0.4+0.9j, -0.7-1.1j]
for _ in range(200):
    new=[]
    for i,r in enumerate(roots):
        d=1+0j
        for j,sr in enumerate(roots):
            if i!=j: d*=r-sr
        new.append(r-f(r)/d)
    if max(abs(new[i]-roots[i]) for i in range(3)) < 1e-14:
        roots=new; break
    roots=new
assert max(abs(f(r)) for r in roots) < 1e-8
assert sum(r.real>1e-9 for r in roots)==2
assert sum(r.real<-1e-9 for r in roots)==1
roots=sorted(roots,key=lambda z:(z.real,z.imag))
print('exact_coefficients=', [str(c.u) for c in p])
print('routh_delta=', routh)
print('roots=', [complex(round(r.real,10),round(r.imag,10)) for r in roots])
print('VERIFY_OK')
