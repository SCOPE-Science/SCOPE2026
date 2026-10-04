from fractions import Fraction
from collections import defaultdict

# Multivariate polynomials in variables x,y,z,w,a,b,c,k,m.
N = 9
X,Y,Z,W,A,B,C,K,M = range(N)

def mon(var):
    e=[0]*N; e[var]=1
    return {tuple(e): 1}

def const(q):
    return {(0,)*N: q}

def add(p,q):
    r=defaultdict(int); r.update(p)
    for e,v in q.items(): r[e]+=v
    return {e:v for e,v in r.items() if v}

def neg(p): return {e:-v for e,v in p.items()}
def sub(p,q): return add(p,neg(q))

def mul(p,q):
    r=defaultdict(int)
    for e,a in p.items():
        for f,b in q.items():
            r[tuple(e[i]+f[i] for i in range(N))]+=a*b
    return {e:v for e,v in r.items() if v}

def scale(p,s): return {e:s*v for e,v in p.items() if s*v}

def deriv(p,j):
    r=defaultdict(int)
    for e,v in p.items():
        if e[j]:
            f=list(e); f[j]-=1
            r[tuple(f)]+=v*e[j]
    return {e:v for e,v in r.items() if v}

x,y,z,w,a,b,c,k,m=[mon(i) for i in range(N)]
fx=add(mul(a,sub(y,x)), add(mul(k,mul(x,z)),w))
fy=neg(add(mul(c,y),mul(x,z)))
fz=add(neg(b),mul(x,y))
fw=neg(mul(m,y))
F=[fx,fy,fz,fw]
Q=add(mul(y,y),mul(z,z))
LQ={}
for j in range(4): LQ=add(LQ,mul(deriv(Q,j),F[j]))
target=add(scale(mul(c,mul(y,y)),-2),scale(mul(b,z),-2))
assert LQ==target, (LQ,target)

div={}
for j in range(4): div=add(div,deriv(F[j],j))
div_target=add(scale(a,-1),add(scale(c,-1),mul(k,z)))
assert div==div_target, (div,div_target)

# Source-parameter specialization: sum = -12.7 + 0.0054 * <y^2>.
coef = -Fraction(-1,5)*Fraction(27,10)/Fraction(100,1)
assert coef == Fraction(27,5000)
base = -Fraction(10,1)-Fraction(27,10)
assert base == -Fraction(127,10)
reported_sum = Fraction(7796,10000)+Fraction(1058,10000)-Fraction(127177,10000)
assert reported_sum == -Fraction(118323,10000)
inferred = (reported_sum-base)/coef
assert inferred == Fraction(43385,270)
print('VERIFY_OK')
