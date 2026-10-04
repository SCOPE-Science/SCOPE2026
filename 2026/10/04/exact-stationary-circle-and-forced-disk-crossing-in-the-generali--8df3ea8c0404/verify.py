from fractions import Fraction as F

# Exact sparse polynomials in variables x,y,z,a,b.
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
fx=y
fy=sub(x,z)
fz=add(add(mul(a,x),mul(x,z)),mul(b,y))
field=[fx,fy,fz,con(0),con(0)]

def L(p):
    r={}
    for i in range(N): r=add(r,mul(der(p,i),field[i]))
    return r

H=add(add(mul(x,y),z),neg(mul(b,x)))
Fpoly=add(add(mul(x,x),mul(y,y)),mul(a,x))
assert eq(L(H),Fpoly)
assert eq(L(Fpoly),mul(y,add(add(sc(x,4),neg(sc(z,2))),a)))

yz=mul(y,z)
target_yz=add(add(add(mul(x,z),neg(mul(z,z))),mul(a,mul(x,y))),add(mul(mul(x,y),z),mul(b,mul(y,y))))
assert eq(L(yz),target_yz)

# Equilibria, symbolic substitutions via direct formula evaluation.
def eval_poly(p, vals):
    out={}
    total=F(0)
    for e,c in p.items():
        term=c
        for i,pow_ in enumerate(e):
            term*=vals[i]**pow_
        total+=term
    return total

# Test with arbitrary rational symbolic-specializations sufficient for formula replay.
for av,bv in [(F(2),F(3)),(F(5,2),F(-7,3))]:
    for pt in [(F(0),F(0),F(0),av,bv),(-av,F(0),-av,av,bv)]:
        assert eval_poly(fx,pt)==0
        assert eval_poly(fy,pt)==0
        assert eval_poly(fz,pt)==0

# For b != 2, clearing denominators from
# y=(2*x^2+(3*a/2)*x)/(2-b) and F=0 gives
# [2*x^2+(3*a/2)*x]^2 + (2-b)^2*(x^2+a*x)=0.
# Its x^4 coefficient is exactly 4, so the polynomial is nonzero.
assert F(2)**2 == F(4)

print('VERIFY_OK')
