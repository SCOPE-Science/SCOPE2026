from fractions import Fraction as F

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

X=mon(1,0,0,0,0); Y=mon(0,1,0,0,0); Z=mon(0,0,1,0,0)
a=mon(0,0,0,1,0); c=mon(0,0,0,0,1)
fX=neg(Y); fY=Z
fZ=sub(add(add(mul(X,Y),mul(a,X)),neg(mul(c,Y))),Z)
Fv=[fX,fY,fZ,con(0),con(0)]
def L(p):
    r={}
    for i in range(N): r=add(r,mul(der(p,i),Fv[i]))
    return r

H=add(add(add(add(neg(mul(X,Z)),sc(mul(Y,Y),F(-1,2))),neg(mul(X,Y))),sc(mul(c,mul(X,X)),F(1,2))),sc(mul(mul(X,X),X),F(-1,3)))
assert eq(L(H),sub(mul(Y,Y),mul(a,mul(X,X))))

Xp=fX
Xpp=neg(Z)
Xppp=neg(fZ)
jerk=add(add(add(add(Xppp,Xpp),mul(c,Xp)),mul(a,X)),neg(mul(X,Xp)))
assert jerk=={}

x,y,z,aa,b=X,Y,Z,a,c
gx=sub(aa,y); gy=add(b,z); gz=sub(mul(x,y),z)
assert eq(gx,sub(aa,y))
assert eq(gy,add(b,z))
assert eq(gz,sub(mul(x,y),z))
assert eq(sc(mul(x,gx),2),sub(sc(mul(aa,x),2),sc(mul(x,y),2)))
print("VERIFY_OK")
