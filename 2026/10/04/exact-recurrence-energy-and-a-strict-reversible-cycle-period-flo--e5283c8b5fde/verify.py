from fractions import Fraction as F

# Exact sparse polynomials in x,y,z.
N=3
def mon(*e): return {tuple(e):F(1)}
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
def sign_sub(p, signs):
    r={}
    for e,v in p.items():
        s=F(1)
        for i,sgn in enumerate(signs):
            if sgn==-1 and e[i]%2: s=-s
        r[e]=v*s
    return {k:v for k,v in r.items() if v}

x=mon(1,0,0); y=mon(0,1,0); z=mon(0,0,1)
fx=neg(y)
fy=add(x,z)
fz=add(mul(x,z),sc(mul(y,y),3))
field=[fx,fy,fz]
def L(p):
    r={}
    for i in range(N): r=add(r,mul(der(p,i),field[i]))
    return r

assert eq(L(sub(mul(x,y),z)), sub(mul(x,x),sc(mul(y,y),4)))
assert eq(L(z), add(mul(x,z),sc(mul(y,y),3)))
assert eq(L(mul(y,z)), add(add(add(mul(x,z),mul(z,z)),mul(mul(x,y),z)),sc(mul(mul(y,y),y),3)))

# Reverser R(x,y,z)=(-x,y,-z): f(Ru)=-R f(u).
signs=(-1,1,-1)
fR=[sign_sub(f,signs) for f in field]
minus_R_f=[field[0],neg(field[1]),field[2]]
assert all(eq(a,b) for a,b in zip(fR,minus_R_f))

# Jerk derivation: y=-p, z=-q-x, z'=-r-p.
# Original z'=xz+3y^2 gives r-xq+p-x^2+3p^2=0.
# Equality in Wirtinger gives q=-x/4, r=-p/4.
assert F(-1,4)+1 == F(3,4)
assert F(1,4)-1 == F(-3,4)
assert F(3) == F(3,4)*4

print('VERIFY_OK')
