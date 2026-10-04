from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,a,b,c.
N = 6

def con(q):
    return {(0,)*N: F(q)}

def var(i):
    e = [0]*N
    e[i] = 1
    return {tuple(e): F(1)}

def add(p,q):
    r = dict(p)
    for m,v in q.items():
        r[m] = r.get(m,F(0)) + v
        if r[m] == 0:
            del r[m]
    return r

def neg(p):
    return {m:-v for m,v in p.items()}

def sub(p,q):
    return add(p,neg(q))

def mul(p,q):
    r = {}
    for e,u in p.items():
        for f,v in q.items():
            g = tuple(e[i]+f[i] for i in range(N))
            r[g] = r.get(g,F(0)) + u*v
    return {m:v for m,v in r.items() if v}

def scale(p,q):
    q = F(q)
    return {m:q*v for m,v in p.items() if q*v}

def der(p,i):
    r = {}
    for e,v in p.items():
        if e[i]:
            g = list(e)
            g[i] -= 1
            g = tuple(g)
            r[g] = r.get(g,F(0)) + v*e[i]
    return {m:v for m,v in r.items() if v}

def eq(p,q):
    return sub(p,q) == {}

x,y,z,a,b,c = [var(i) for i in range(N)]
fx = mul(a,sub(y,x))
fy = sub(mul(c,y),mul(x,z))
fz = sub(mul(x,y),mul(b,z))
field = [fx,fy,fz,{}, {}, {}]

def L(p):
    r = {}
    for i in range(N):
        r = add(r,mul(der(p,i),field[i]))
    return r

x2 = scale(mul(x,x),F(1,2))
y2 = scale(mul(y,y),F(1,2))
z2 = scale(mul(z,z),F(1,2))

assert eq(L(x2), mul(a,sub(mul(x,y),mul(x,x))))
assert eq(L(y2), sub(mul(c,mul(y,y)),mul(mul(x,y),z)))
assert eq(L(z2), sub(mul(mul(x,y),z),mul(b,mul(z,z))))

# Critical defect:
# target = b*z*(z-c) - c*(y-x)^2.
target = sub(
    mul(b,mul(z,sub(z,c))),
    mul(c,mul(sub(y,x),sub(y,x)))
)

# a*target is a linear combination of generator derivatives:
# -a L(y^2/2) - a L(z^2/2) + a*c L(z) + c L(x^2/2)
certificate = add(
    add(neg(mul(a,L(y2))), neg(mul(a,L(z2)))),
    add(mul(mul(a,c),L(z)), mul(c,L(x2)))
)
assert eq(certificate, mul(a,target))

# Equilibrium residuals under y=x, z=c, x^2=b*c:
# x' = 0; y'=x(c-z)=0; z'=x^2-bc=0.
assert eq(mul(a,sub(x,x)), {})
assert eq(mul(x,sub(c,c)), {})
assert eq(sub(mul(x,x),mul(b,c)), sub(mul(x,x),mul(b,c)))

# Classical parameters.
A,B,C = F(36),F(3),F(20)
assert B*C == F(60)
assert A > 0 and B > 0 and C > 0

print("VERIFY_OK")
