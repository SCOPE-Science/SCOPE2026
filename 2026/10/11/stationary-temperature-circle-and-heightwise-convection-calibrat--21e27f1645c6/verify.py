from fractions import Fraction as F

# Minimal exact polynomial arithmetic in x,y,z,sigma,zeta,alpha,rho.
N = 7
def mon(*e):
    return {tuple(e): F(1)}
def con(c):
    return {tuple([0]*N): F(c)} if c else {}
def add(p,q):
    r = dict(p)
    for k,v in q.items():
        r[k] = r.get(k,F(0)) + v
        if not r[k]:
            del r[k]
    return r
def neg(p):
    return {k:-v for k,v in p.items()}
def sub(p,q):
    return add(p,neg(q))
def mul(p,q):
    r = {}
    for e,u in p.items():
        for f,v in q.items():
            g = tuple(e[i]+f[i] for i in range(N))
            r[g] = r.get(g,F(0)) + u*v
    return {k:v for k,v in r.items() if v}
def sc(p,s):
    s = F(s)
    return {k:s*v for k,v in p.items() if s*v}
def der(p,i):
    r = {}
    for e,v in p.items():
        if e[i]:
            g = list(e)
            g[i] -= 1
            g = tuple(g)
            r[g] = r.get(g,F(0)) + v*e[i]
    return {k:v for k,v in r.items() if v}

x = mon(1,0,0,0,0,0,0)
y = mon(0,1,0,0,0,0,0)
z = mon(0,0,1,0,0,0,0)
sigma = mon(0,0,0,1,0,0,0)
zeta = mon(0,0,0,0,1,0,0)
alpha = mon(0,0,0,0,0,1,0)
rho = mon(0,0,0,0,0,0,1)

fx = add(add(neg(mul(sigma,x)), mul(zeta,z)), mul(alpha,mul(y,z)))
fy = add(add(rho,neg(y)),neg(mul(x,z)))
fz = add(neg(z),mul(x,y))
field = [fx,fy,fz,{},{},{},{}]

def L(p):
    r = {}
    for i in range(3):
        r = add(r,mul(der(p,i),field[i]))
    return r

circle = add(mul(y,y),mul(z,z))
target = add(add(sc(mul(rho,y),2),sc(mul(y,y),-2)),sc(mul(z,z),-2))
assert L(circle) == target

assert sub(mul(x,y),z) == fz
assert sub(mul(x,z),sub(rho,y)) == neg(fy)
assert sub(add(mul(zeta,z),mul(alpha,mul(y,z))),mul(sigma,x)) == fx

# Moment-shell algebra at exact rational test values.
r = F(17,5)
m = F(9,7)
Ey2_plus_Ez2 = r*m
centered = Ey2_plus_Ez2 - r*m + r*r/F(4)
assert centered == r*r/F(4)

# Orthogonal-regression variance/covariance algebra.
EZ = F(3,8)
EZ2 = F(7,10)
ER = F(0)
ER2 = F(11,13)
EZR = F(0)
varZ = EZ2-EZ*EZ
Eprod = EZ+ER
Eprod2 = EZ2+2*EZR+ER2
varProd = Eprod2-Eprod*Eprod
assert varProd == varZ+ER2
cov = (EZ2+EZR)-EZ*Eprod
assert cov == varZ

print("VERIFY_OK")
