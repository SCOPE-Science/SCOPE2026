from fractions import Fraction as F

# Sparse polynomials in variables x,y,z,a,b.
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

x=mon(1,0,0,0,0); y=mon(0,1,0,0,0); z=mon(0,0,1,0,0)
a=mon(0,0,0,1,0); b=mon(0,0,0,0,1)
fx=add(neg(y),mul(z,z))
fy=add(x,mul(a,y))
fz=sub(x,mul(b,z))
field=[fx,fy,fz,con(0),con(0)]
def L(p):
    r={}
    for i in range(N): r=add(r,mul(der(p,i),field[i]))
    return r

h1=add(add(mul(a,x),y),neg(z))
t1=add(mul(a,mul(z,z)),mul(b,z))
assert eq(L(h1),t1)

# H2 = a*b*z^2 + a*b^2*x + b^2*y
b2=mul(b,b)
h2=add(add(mul(mul(a,b),mul(z,z)),mul(mul(a,b2),x)),mul(b2,y))
# Target = a*x^2 + b^2*x - a*(x-b*z)^2
xbz=sub(x,mul(b,z))
t2=add(add(mul(a,mul(x,x)),mul(b2,x)),neg(mul(a,mul(xbz,xbz))))
assert eq(L(h2),t2)

# Canonical equilibrium checks a=1/2,b=1 at E0 and E1=(-2,4,-2).
def eval_poly(p, vals):
    s=F(0)
    for e,c in p.items():
        term=c
        for power,val in zip(e,vals): term*=F(val)**power
        s+=term
    return s
for pt in [(F(0),F(0),F(0),F(1,2),F(1)), (F(-2),F(4),F(-2),F(1,2),F(1))]:
    assert eval_poly(fx,pt)==0
    assert eval_poly(fy,pt)==0
    assert eval_poly(fz,pt)==0

print('VERIFY_OK')
