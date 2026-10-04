from fractions import Fraction as F

# Sparse polynomials in x,y,u,C,S,c.
N=6
def v(i):
    e=[0]*N; e[i]=1; return {tuple(e):F(1)}
def add(p,q):
    r=dict(p)
    for m,a in q.items():
        r[m]=r.get(m,F(0))+a
        if r[m]==0: del r[m]
    return r
def neg(p): return {m:-a for m,a in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    r={}
    for e,a in p.items():
        for f,b in q.items():
            g=tuple(e[i]+f[i] for i in range(N))
            r[g]=r.get(g,F(0))+a*b
    return {m:a for m,a in r.items() if a}
def scale(p,s):
    s=F(s); return {m:s*a for m,a in p.items() if s*a}
def eq(p,q): return sub(p,q)=={}

x,y,u,C,S,c=[v(i) for i in range(N)]
X=add(c,mul(u,sub(mul(x,C),mul(y,S))))
Y=mul(u,add(mul(x,S),mul(y,C)))
lhs=add(mul(sub(X,c),sub(X,c)),mul(Y,Y))
rhs=mul(mul(u,u),mul(add(mul(x,x),mul(y,y)),add(mul(C,C),mul(S,S))))
assert eq(lhs,rhs)

U=F(9,10); C0=F(1)
R=C0/(1-U); d=C0/(1-U*U); rho=U*C0/(1-U*U)
assert R==10
assert d==F(100,19)
assert rho==F(90,19)
# Source coefficient equation divided by 1-u^2 matches completed-square coefficients.
a=1-U*U
assert F(1)==a/a
assert F(-2)*C0/a == -2*d
assert C0*C0/a == d*d-rho*rho
print('VERIFY_OK')
