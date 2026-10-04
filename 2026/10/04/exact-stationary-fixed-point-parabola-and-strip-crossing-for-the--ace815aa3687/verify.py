from fractions import Fraction as F

# A tiny sparse polynomial ring in formal variables a,b,m,s2.
N=4

def var(i):
    e=[0]*N; e[i]=1
    return {tuple(e):F(1)}

def const(q):
    return {(0,)*N:F(q)}

def add(p,q):
    r=dict(p)
    for m,c in q.items():
        r[m]=r.get(m,F(0))+c
        if r[m]==0: del r[m]
    return r

def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))

def mul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items():
            g=tuple(e[i]+f[i] for i in range(N))
            r[g]=r.get(g,F(0))+c*d
    return {m:c for m,c in r.items() if c}

def eq(p,q): return sub(p,q)=={}

a,b,m,s2=[var(i) for i in range(N)]
one=const(1)
stationarity=sub(add(mul(a,s2),mul(sub(one,b),m)),one)
variance=sub(s2,mul(m,m))
cleared_rhs=sub(sub(one,mul(sub(one,b),m)),mul(a,mul(m,m)))
# a*Var - rhs is exactly the stationarity residual.
assert eq(sub(mul(a,variance),cleared_rhs),stationarity)

# Exact arithmetic in Q(sqrt(609)) for the classical map.
D=609
class QD:
    def __init__(self,p=0,q=0): self.p=F(p); self.q=F(q)
    def __add__(self,o):
        o=o if isinstance(o,QD) else QD(o)
        return QD(self.p+o.p,self.q+o.q)
    __radd__=__add__
    def __neg__(self): return QD(-self.p,-self.q)
    def __sub__(self,o): return self+(- (o if isinstance(o,QD) else QD(o)))
    def __rsub__(self,o): return QD(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,QD) else QD(o)
        return QD(self.p*o.p+D*self.q*o.q,self.p*o.q+self.q*o.p)
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,QD):
            den=o.p*o.p-D*o.q*o.q
            return QD((self.p*o.p-D*self.q*o.q)/den,(self.q*o.p-self.p*o.q)/den)
        return QD(self.p/F(o),self.q/F(o))
    def __eq__(self,o):
        o=o if isinstance(o,QD) else QD(o)
        return self.p==o.p and self.q==o.q
    def __repr__(self): return f'QD({self.p},{self.q})'

A=F(7,5); B=F(3,10)
s=QD(0,1)
rminus=(QD(-7)-s)/28
rplus=(QD(-7)+s)/28

def qroot(r):
    return A*r*r+(1-B)*r-1
assert qroot(rminus)==0
assert qroot(rplus)==0
assert rminus+rplus==F(-1,2)
assert rminus*rplus==F(-5,7)
assert -(1-B)/A==F(-1,2)
assert -1/A==F(-5,7)
# Fixed points are (r,b r).
for r in (rminus,rplus):
    y=B*r
    xnext=1-A*r*r+y
    ynext=B*r
    assert xnext==r
    assert ynext==y

print('VERIFY_OK')
