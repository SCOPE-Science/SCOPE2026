from fractions import Fraction as F
from itertools import permutations

# Q(q), where q satisfies 35 q^2 - 52 q - 1995 = 0.
class Q:
    __slots__=('a','b')
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=asQ(o); return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,o): return self+(-asQ(o))
    def __rsub__(self,o): return asQ(o)-self
    def __mul__(self,o):
        o=asQ(o)
        # q^2=(52 q+1995)/35
        return Q(self.a*o.a + self.b*o.b*F(1995,35),
                 self.a*o.b + self.b*o.a + self.b*o.b*F(52,35))
    __rmul__=__mul__
    def __eq__(self,o):
        o=asQ(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return f'Q({self.a},{self.b})'
def asQ(x): return x if isinstance(x,Q) else Q(x,0)

# Q(q,sqrt(2)) = A + B*sqrt(2)
class K:
    __slots__=('A','B')
    def __init__(self,A=0,B=0): self.A=asQ(A); self.B=asQ(B)
    def __add__(self,o):
        o=asK(o); return K(self.A+o.A,self.B+o.B)
    __radd__=__add__
    def __neg__(self): return K(-self.A,-self.B)
    def __sub__(self,o): return self+(-asK(o))
    def __rsub__(self,o): return asK(o)-self
    def __mul__(self,o):
        o=asK(o)
        return K(self.A*o.A + 2*self.B*o.B,
                 self.A*o.B + self.B*o.A)
    __rmul__=__mul__
    def __eq__(self,o):
        o=asK(o); return self.A==o.A and self.B==o.B
    def __repr__(self): return f'K({self.A},{self.B})'
def asK(x): return x if isinstance(x,K) else K(x,0)

q=Q(0,1)
s2=K(0,Q(1,0))
zero=K(0); one=K(1)

def padd(a,b):
    n=max(len(a),len(b)); out=[zero for _ in range(n)]
    for i in range(n):
        out[i]=(a[i] if i<len(a) else zero)+(b[i] if i<len(b) else zero)
    return out

def pmul(a,b):
    out=[zero for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]=out[i+j]+x*y
    return out

def pneg(a): return [-x for x in a]

def invcount(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def det_poly(M):
    total=[zero]
    for perm in permutations(range(4)):
        prod=[one]
        for i,j in enumerate(perm): prod=pmul(prod,M[i][j])
        total=padd(total,pneg(prod) if invcount(perm)%2 else prod)
    return total

def const(x): return [asK(x)]
def lin(c): return [asK(c), one]  # lambda + c

# Exact equilibrium elimination checks.
assert 265*265 < 70501 < 266*266
assert 282004 == 4*70501
# q roots solve 35q^2-52q-1995=0 by quadratic formula.
# Coarse exact bounds enough for Routh signs: -7 < q_- < q_+ < 9.
assert F(26-266,35) > -7
assert F(26+266,35) < 9

for eps in (1,-1):
    # lambda I - J at a nonzero equilibrium, with p=eps*sqrt(2)*q and r=5eps*sqrt(2)
    e=F(eps)
    J=[
        [K(5), -5*e*s2, -K(q), K(0)],
        [5*e*s2, K(-10), e*s2*K(q), K(0)],
        [K(q)*F(1,3), e*s2*K(q)*F(1,3), K(F(-19,5)), K(F(1,5))],
        [K(F(1,10)), 5*e*s2*F(1,2), K(q)*F(1,2), K(F(21,20))],
    ]
    M=[]
    for i in range(4):
        row=[]
        for j in range(4):
            if i==j: row.append(lin(-J[i][j]))
            else: row.append(const(-J[i][j]))
        M.append(row)
    cp=det_poly(M)
    expected=[
        K(Q(F(-798),F(-52,5))),
        K(Q(F(760),F(9896,525))),
        K(Q(F(-231,25),F(-25,42))),
        K(F(31,4)),
        K(1),
    ]
    assert cp==expected, (eps,cp)

# Routh first-column identities for P_q(lambda).
a1=F(31,4)
# b1 = -98543*q/32550 - 83161/775
B_const=F(-83161,775); B_q=F(-98543,32550)
# On q>-7, b1 < b1(-7) = -400423/4650 < 0.
B_at_neg7=B_const+B_q*F(-7)
assert B_at_neg7 == F(-400423,4650) and B_at_neg7 < 0
# constant coefficient a4=-798-(52/5)q is < a4(-7)=-3626/5<0.
a4_at_neg7=F(-798)+F(-52,5)*F(-7)
assert a4_at_neg7 == F(-3626,5) and a4_at_neg7 < 0
# c1 equals N(q)/D(q) on the equilibrium quadratic.
N0=47022920375235; N1=2588408117026
D0=64179501750; D1=1810727625
assert N0-7*N1 == 28904063556053 > 0
assert D0-7*D1 == 51504408375 > 0
# Since N,D increase with q and q>-7, c1>0. Thus Routh signs +,+,-,+,- -> 3 RHP roots.

# Origin spectrum is exactly {5,-10,-19/5,21/20}: two RHP roots.
origin=[F(5),F(-10),F(-19,5),F(21,20)]
assert sum(x>0 for x in origin)==2 and all(x!=0 for x in origin)
print('VERIFY_OK')
