#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 90

Q = [729, 8289, 26784, 14904, -34128, -82944, -300448, 174168, -140086, 530922, 208224, 210728, 23864, -102168, -93792, -51128, -13707, -1331]
RS = [343, -24478, -322208, -1446786, -3270135, -3897152, -1459896, 3197232, 6674718, 6330356, 764456, -5167620, -7047478, -4152240, -1251752, 1222272, 1430587, 567962, 57560, -4650, 125]
RM = [343, 20922, 157036, 604990, 1543121, 2718936, 3182000, 1329480, -2879162, -7744644, -9795992, -8788652, -5133918, -2042856, 34800, 2312, 55155, 45018, 7820, -22754, 125]
H = [8,0,7,-1]


def strip(p):
    p = list(p)
    while len(p) > 1 and p[0] == 0:
        p.pop(0)
    return p


def deriv(p):
    n = len(p)-1
    return strip([p[i]*(n-i) for i in range(n)]) if n else [Fraction(0)]


def divrem(a,b):
    a = [Fraction(x) for x in strip(a)]
    b = [Fraction(x) for x in strip(b)]
    if b == [0]:
        raise ZeroDivisionError
    while len(a) >= len(b) and a != [0]:
        k = len(a)-len(b)
        q = a[0]/b[0]
        sub = [q*x for x in b] + [Fraction(0)]*k
        a = strip([x-y for x,y in zip(a, sub)])
    return a


def sturm(p):
    p0 = [Fraction(x) for x in strip(p)]
    p1 = deriv(p0)
    seq = [p0,p1]
    while seq[-1] != [0]:
        r = divrem(seq[-2],seq[-1])
        if r == [0]:
            break
        seq.append([-x for x in r])
    return seq


def peval(p,x):
    y = Fraction(0)
    for a in p:
        y = y*x + a
    return y


def variations(seq,x):
    signs=[]
    for p in seq:
        v=peval(p,x)
        if v>0: signs.append(1)
        elif v<0: signs.append(-1)
        else: raise AssertionError('endpoint is a root')
    return sum(signs[i] != signs[i-1] for i in range(1,len(signs)))


def root_count(p,a,b):
    s=sturm(p)
    return variations(s,a)-variations(s,b)


def cube_root(x):
    x = Decimal(x)
    if x == 0: return Decimal(0)
    y = x if x >= 1 else Decimal(1)
    for _ in range(120):
        yn = (2*y + x/(y*y))/3
        if abs(yn-y) < Decimal('1e-80'):
            return yn
        y=yn
    return y


def poly_dec(coeffs,x):
    y=Decimal(0)
    for a in coeffs:
        y=y*x+Decimal(a)
    return y


def relation_c(t):
    return cube_root((1+t**3)/(1+t**6))

# A tiny two-variable dual-number evaluator for exact formula differentiation.
class D2:
    __slots__=('v','dt','dc')
    def __init__(self,v,dt=0,dc=0):
        self.v=Decimal(v); self.dt=Decimal(dt); self.dc=Decimal(dc)
    def __add__(self,o):
        if not isinstance(o,D2): o=D2(o)
        return D2(self.v+o.v,self.dt+o.dt,self.dc+o.dc)
    __radd__=__add__
    def __neg__(self): return D2(-self.v,-self.dt,-self.dc)
    def __sub__(self,o): return self+(-o if isinstance(o,D2) else -Decimal(o))
    def __rsub__(self,o): return D2(o)-self
    def __mul__(self,o):
        if not isinstance(o,D2): o=D2(o)
        return D2(self.v*o.v,self.dt*o.v+self.v*o.dt,self.dc*o.v+self.v*o.dc)
    __rmul__=__mul__
    def inv(self):
        return D2(1/self.v,-self.dt/(self.v*self.v),-self.dc/(self.v*self.v))
    def __truediv__(self,o):
        if not isinstance(o,D2): o=D2(o)
        return self*o.inv()
    def __rtruediv__(self,o): return D2(o)/self
    def __pow__(self,n):
        if n==0: return D2(1)
        out=D2(1)
        for _ in range(n): out=out*self
        return out


def implicit_derivative_sign(tval, branch):
    t=Decimal(str(tval)); c=relation_c(t)
    T=D2(t,1,0); C=D2(c,0,1)
    if branch=='small_plus':
        E1=(1-C*T**2)**3+(T+C)**3
        E2=(2+C*T**2)**3+(C-2*T)**3
    elif branch=='large_plus':
        E1=(1-C*T**2)**3+(T+C)**3
        E2=(2+C*T**2)**3+(2*T-C)**3
    elif branch=='minus':
        E1=(1+C*T**2)**3+(C-T)**3
        E2=(2-C*T**2)**3+(2*T+C)**3
    else:
        raise ValueError(branch)
    P=(E1*E2)/(1+T**3)**2
    R=C**3*(1+T**6)-(1+T**3)
    D=P.dt*R.dc-P.dc*R.dt
    return D


def P_large_u(u):
    u=Decimal(u)
    r=cube_root(u*(1+u)**2/(1+u*u)**2)
    A=Decimal(2)/(1+u*u)+3*r
    B=(Decimal(7)+9*u*u)/(1+u*u)+6*r
    return A*B

# Exact Sturm checks.
assert root_count(H, Fraction(0), Fraction(7,50)) == 1
assert peval(H,Fraction(7,50)) > 0
assert root_count(RS, Fraction(0), Fraction(7,50)) == 0
assert root_count(Q, Fraction(0), Fraction(1)) == 1
assert root_count(Q, Fraction(7578975,10_000_000), Fraction(7578976,10_000_000)) == 1
assert root_count(RM, Fraction(0), Fraction(1)) == 1
assert root_count(RM, Fraction(5,1000), Fraction(6,1000)) == 1

# Sign checks for the actual implicit derivative on each smooth branch.
assert implicit_derivative_sign('0.4','small_plus') > 0
assert implicit_derivative_sign('0.8','large_plus') > 0
assert implicit_derivative_sign('0.95','large_plus') < 0
assert implicit_derivative_sign('0.1','minus') < 0
assert implicit_derivative_sign('0.2','minus') > 0

# Isolate u_* by bisection of the exact polynomial sign.
lo=Decimal('0.7578975'); hi=Decimal('0.7578976')
for _ in range(180):
    mid=(lo+hi)/2
    if poly_dec(Q,lo)*poly_dec(Q,mid) <= 0: hi=mid
    else: lo=mid
u=(lo+hi)/2
P=P_large_u(u)
Tconst=P ** (Decimal(1)/Decimal(6))
# Decimal power is checked against a cube/square reconstruction.
assert abs(Tconst**6-P) < Decimal('1e-65')
assert Decimal('1.9639614189191') < Tconst < Decimal('1.9639614189193')
# Negative-orientation endpoint maximum is 56^(1/6), and a rational interior
# plus-branch witness already beats it.
end_minus=Decimal(56) ** (Decimal(1)/Decimal(6))
assert P_large_u(Decimal(3)/4) > Decimal(56)
assert Tconst > end_minus

print('VERIFY_OK')
print('u_star=',u)
print('T_perp_l3_2=',Tconst)
