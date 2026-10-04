from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,a,b.
N=5

def var(i):
    e=[0]*N; e[i]=1
    return {tuple(e):F(1)}
def con(q): return {(0,)*N:F(q)}
def add(p,q):
    r=dict(p)
    for m,v in q.items():
        r[m]=r.get(m,F(0))+v
        if not r[m]: del r[m]
    return r
def neg(p): return {m:-v for m,v in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r={}
    for e,u in p.items():
        for f,v in q.items():
            g=tuple(e[i]+f[i] for i in range(N))
            r[g]=r.get(g,F(0))+u*v
    return {m:v for m,v in r.items() if v}
def sc(p,s):
    s=F(s); return {m:s*v for m,v in p.items() if s*v}
def der(p,i):
    r={}
    for e,v in p.items():
        if e[i]:
            g=list(e); g[i]-=1; g=tuple(g)
            r[g]=r.get(g,F(0))+v*e[i]
    return {m:v for m,v in r.items() if v}
def eq(p,q): return sub(p,q)=={}
def pow2(p): return mul(p,p)

x,y,z,a,b=[var(i) for i in range(N)]
fx=add(mul(a,y),z)
fy=add(neg(x),pow2(y))
fz=add(x,mul(b,y))
field=[fx,fy,fz,con(0),con(0)]
def L(p):
    r={}
    for i in range(N): r=add(r,mul(der(p,i),field[i]))
    return r

q=mul(y,add(y,b))
assert eq(L(add(y,z)),q)
center=add(y,sc(b,F(1,2)))
assert eq(q,sub(pow2(center),sc(pow2(b),F(1,4))))

# Symbolic substitution helper.
def subst(p,vals):
    out=F(0)
    for e,c in p.items():
        term=c
        for i,k in enumerate(e): term*=vals[i]**k
        out+=term
    return out

# Treat a,b as exact independent rational sample values; algebraic formulas
# were already constructed symbolically above. Check several rational pairs.
for A,B in [(F(27,10),F(1)),(F(-3,2),F(5,3)),(F(0),F(7,4))]:
    for X,Y,Z in [(F(0),F(0),F(0)),(B*B,-B,A*B)]:
        vals=[X,Y,Z,A,B]
        assert subst(fx,vals)==0
        assert subst(fy,vals)==0
        assert subst(fz,vals)==0

# Original Sprott P normalization.
A=F(27,10); B=F(1)
assert (B*B,-B,A*B)==(F(1),F(-1),F(27,10))
print('VERIFY_OK')
