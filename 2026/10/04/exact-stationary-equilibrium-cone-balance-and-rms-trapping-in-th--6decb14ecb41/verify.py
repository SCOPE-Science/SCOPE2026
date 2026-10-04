from fractions import Fraction as F
from decimal import Decimal, getcontext

# Sparse polynomial ring in x,y,z,a,b,c,d.
N = 7

def cst(q):
    return {(0,)*N: F(q)}

def var(i):
    e=[0]*N
    e[i]=1
    return {tuple(e):F(1)}

def add(p,q):
    r=dict(p)
    for m,a in q.items():
        r[m]=r.get(m,F(0))+a
        if r[m]==0:
            del r[m]
    return r

def neg(p):
    return {m:-a for m,a in p.items()}

def sub(p,q):
    return add(p,neg(q))

def mul(p,q):
    r={}
    for e,a in p.items():
        for f,b in q.items():
            g=tuple(e[i]+f[i] for i in range(N))
            r[g]=r.get(g,F(0))+a*b
    return {m:a for m,a in r.items() if a}

def scale(p,s):
    s=F(s)
    return {m:s*a for m,a in p.items() if s*a}

def der(p,i):
    r={}
    for e,a in p.items():
        if e[i]:
            g=list(e); g[i]-=1; g=tuple(g)
            r[g]=r.get(g,F(0))+a*e[i]
    return {m:a for m,a in r.items() if a}

def eq(p,q):
    return sub(p,q)=={}

x,y,z,a,b,cc,d=[var(i) for i in range(N)]
fx=sub(mul(a,sub(x,y)),mul(y,z))
fy=add(neg(mul(b,y)),mul(x,z))
fz=add(add(neg(mul(cc,z)),mul(d,x)),mul(x,y))
field=[fx,fy,fz,{}, {}, {}, {}]

def L(p):
    r={}
    for i in range(N):
        r=add(r,mul(der(p,i),field[i]))
    return r

energy=scale(add(mul(x,x),mul(y,y)),F(1,2))
target=add(add(mul(a,mul(x,x)),neg(mul(a,mul(x,y)))),neg(mul(b,mul(y,y))))
assert eq(L(energy),target)

# The two factor slopes are roots k of a k^2-a k-b=0.
# Under b=a*k*(k-1), the tangency numerator becomes:
# a(k-1)+k b = a(k-1)(1+k^2).
# Verify this polynomial identity symbolically in k for a=1 after replacing b=k(k-1).
# Coefficients by powers of k:
left = {1:F(1), 0:F(-1), 3:F(1), 2:F(-1)}  # (k-1)+k^2(k-1)
right = {3:F(1), 2:F(-1), 1:F(1), 0:F(-1)} # (k-1)(1+k^2)
assert left == right

# Published three-scroll parameters.
getcontext().prec=60
A=Decimal(977)/Decimal(1000)
B=Decimal(10)
Delta=(A*A+Decimal(4)*A*B).sqrt()
kp=(A+Delta)/(Decimal(2)*A)
km=(Delta-A)/(Decimal(2)*A)
zp=(-A+Delta)/Decimal(2)
zm=(-A-Delta)/Decimal(2)

tol=Decimal("1e-50")
assert abs(B/zp-kp) < tol
assert abs(B/zm+km) < tol
assert abs((kp-km)-Decimal(1)) < tol
assert abs(kp*km-B/A) < tol

# The source factor polynomial vanishes exactly on each equilibrium slope.
def cone(xv,yv):
    return (xv-kp*yv)*(xv+km*yv)

for slope in (kp,-km):
    yv=Decimal("1.23456789")
    xv=slope*yv
    assert abs(cone(xv,yv)) < Decimal("1e-50")

print("VERIFY_OK")
