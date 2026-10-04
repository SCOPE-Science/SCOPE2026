from fractions import Fraction as F

N = 5
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

fx=neg(add(x,mul(a,y)))
fy=add(x,mul(z,z))
fz=add(b,x)
field=[fx,fy,fz,con(0),con(0)]

def L(p):
    r={}
    for i in range(N):
        r=add(r,mul(der(p,i),field[i]))
    return r

v=add(x,b)
w=neg(add(x,mul(a,y)))
Fcert=add(
    add(mul(v,w),sc(mul(v,v),F(1,2))),
    mul(a,add(sc(mul(mul(z,z),z),F(1,3)),neg(mul(b,z))))
)

assert eq(L(z),add(b,x))
assert eq(L(y),add(x,mul(z,z)))
assert eq(L(Fcert),sub(mul(w,w),mul(a,mul(v,v))))
assert add(add(add(L(w),w),mul(a,v)),mul(a,sub(mul(z,z),b)))=={}

twoz_minus_one=add(sc(z,2),con(-1))
assert eq(
    add(neg(mul(a,v)),sc(mul(a,mul(z,v)),2)),
    mul(a,mul(twoz_minus_one,v))
)

print("VERIFY_OK")
