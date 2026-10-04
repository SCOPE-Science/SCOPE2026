from fractions import Fraction as F

# Sparse polynomials in x,y,z,q,beta.
N=5

def mon(*e): return {tuple(e):F(1)}
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

x=mon(1,0,0,0,0); y=mon(0,1,0,0,0); z=mon(0,0,1,0,0)
q=mon(0,0,0,1,0); beta=mon(0,0,0,0,1)
field=[y,z,sub(sub(q,y),mul(beta,z)),con(0),con(0)]
def L(p):
    r={}
    for i in range(N): r=add(r,mul(der(p,i),field[i]))
    return r

assert eq(L(sc(mul(y,y),F(1,2))),mul(y,z))
assert eq(L(sc(mul(x,x),F(1,2))),mul(x,y))
assert eq(L(mul(y,z)),add(add(mul(z,z),mul(q,y)),add(neg(mul(y,y)),neg(mul(beta,mul(y,z))))))
assert eq(L(mul(x,y)),add(mul(y,y),mul(x,z)))
assert eq(L(mul(x,z)),add(add(mul(y,z),mul(x,q)),add(neg(mul(x,y)),neg(mul(beta,mul(x,z))))))

# Exact piecewise checks at rational alpha,mu; the algebraic formulas are parameter-generic.
alpha=F(3,7); mu=F(5,11); r=F(1)+alpha/mu

def f(v):
    if v <= -1: return -mu*v-mu-alpha
    if v >= 1: return -mu*v+mu+alpha
    return alpha*v
assert f(F(-1)) == -alpha
assert f(F(1)) == alpha
assert f(F(0)) == 0
assert f(r) == 0 and f(-r) == 0
assert r-F(1) == alpha/mu

# Harmonic equality branch: with beta=mu and center r, f(x)=-mu(x-r) on x>=1.
R=alpha/mu
for u in [r-R, r-R/F(2), r, r+R/F(2), r+R]:
    assert u >= 1
    assert f(u) == -mu*(u-r)

print('VERIFY_OK')
