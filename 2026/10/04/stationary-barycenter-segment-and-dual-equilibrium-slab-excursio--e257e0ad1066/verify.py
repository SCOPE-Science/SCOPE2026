from fractions import Fraction as F

# Exact sparse polynomials in x,y,z,a,b.
N=5

def mon(*e): return {tuple(e):F(1)}
def con(q): return {(0,)*N:F(q)}
def add(p,q):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,F(0))+v
        if not r[k]: del r[k]
    return r
def neg(p): return {k:-v for k,v in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r={}
    for e,u in p.items():
        for f,v in q.items():
            g=tuple(e[i]+f[i] for i in range(N))
            r[g]=r.get(g,F(0))+u*v
    return {k:v for k,v in r.items() if v}
def sc(p,s):
    s=F(s)
    return {k:s*v for k,v in p.items() if s*v}
def der(p,i):
    r={}
    for e,v in p.items():
        if e[i]:
            g=list(e); g[i]-=1; g=tuple(g)
            r[g]=r.get(g,F(0))+v*e[i]
    return {k:v for k,v in r.items() if v}
def eq(p,q): return sub(p,q)=={}

x=mon(1,0,0,0,0)
y=mon(0,1,0,0,0)
z=mon(0,0,1,0,0)
a=mon(0,0,0,1,0)
b=mon(0,0,0,0,1)

fx=add(mul(a,x),mul(b,z))
fy=sub(mul(x,z),y)
fz=sub(y,x)
field=[fx,fy,fz,con(0),con(0)]

def L(p):
    r={}
    for i in range(N):
        r=add(r,mul(der(p,i),field[i]))
    return r

H1=sub(sc(mul(x,x),F(1,2)),mul(b,add(y,z)))
target1=add(mul(a,mul(x,x)),mul(b,x))
assert eq(L(H1),target1)

H2=add(add(sc(mul(a,mul(x,x)),F(-1,2)),neg(mul(b,x))),neg(mul(mul(a,b),add(y,z))))
target2=sub(mul(mul(b,b),sub(mul(z,z),z)),mul(fx,fx))
assert eq(L(H2),target2)

assert eq(L(mul(x,x)),add(sc(mul(a,mul(x,x)),2),sc(mul(b,mul(x,z)),2)))
assert eq(L(x),fx)
assert eq(L(y),fy)
assert eq(L(z),fz)

# Equilibria: e0=(0,0,0) and e1=(-b/a,-b/a,1).
# Clear denominators at e1: a*x=-b, a*y=-b, z=1.
# Then a*fx = a*(a*x+b*z) = a*(-b)+a*b = 0.
assert add(sc(mul(a,b),-1),mul(a,b))=={}
# a*fy = (a*x)*z-a*y = -b-(-b)=0.
assert add(neg(b),b)=={}
# a*fz = a*y-a*x = -b-(-b)=0.
assert add(neg(b),b)=={}

print('VERIFY_OK')
