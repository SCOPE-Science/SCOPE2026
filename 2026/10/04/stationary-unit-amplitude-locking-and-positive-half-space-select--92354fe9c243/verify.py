from fractions import Fraction as F

# Sparse polynomials in x,y,z,a,b,g,m,l.
N=8

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
            h=tuple(e[i]+f[i] for i in range(N))
            r[h]=r.get(h,F(0))+u*v
    return {k:v for k,v in r.items() if v}
def sc(p,s):
    s=F(s); return {k:s*v for k,v in p.items() if s*v}
def der(p,i):
    r={}
    for e,v in p.items():
        if e[i]:
            h=list(e); h[i]-=1; h=tuple(h)
            r[h]=r.get(h,F(0))+v*e[i]
    return {k:v for k,v in r.items() if v}
def eq(p,q): return sub(p,q)=={}

x=mon(1,0,0,0,0,0,0,0)
y=mon(0,1,0,0,0,0,0,0)
z=mon(0,0,1,0,0,0,0,0)
a=mon(0,0,0,1,0,0,0,0)
b=mon(0,0,0,0,1,0,0,0)
g=mon(0,0,0,0,0,1,0,0)
m=mon(0,0,0,0,0,0,1,0)
l=mon(0,0,0,0,0,0,0,1)

fx=sub(mul(a,mul(x,sub(con(1),y))),mul(b,z))
fy=mul(g,mul(y,sub(mul(x,x),con(1))))
fz=mul(m,x)
field=[fx,fy,fz,con(0),con(0),con(0),con(0),con(0)]

def L(p):
    r={}
    for i in range(N): r=add(r,mul(der(p,i),field[i]))
    return r

assert eq(L(z),fz)
assert eq(L(y),fy)
assert eq(L(mul(z,z)),sc(mul(m,mul(x,z)),2))
assert eq(L(mul(x,x)),sub(sc(mul(a,mul(mul(x,x),sub(con(1),y))),2),sc(mul(b,mul(x,z)),2)))

# det(lambda I - A) for A=[[a,-b],[m,0]] is lambda^2-a lambda+b m.
# Direct 2x2 expansion: (l-a)*l - b*(-m) = l^2-a*l+b*m.
det=add(mul(sub(l,a),l),mul(b,m))
char=add(sub(mul(l,l),mul(a,l)),mul(b,m))
assert eq(det,char)

print('VERIFY_OK')
