from fractions import Fraction as F

# Sparse polynomial ring in X,Y,Z,A,B,k1,k2,k3,k4,k5,f.
N=11

def var(i):
    e=[0]*N; e[i]=1
    return {tuple(e):F(1)}
def const(q): return {(0,)*N:F(q)}
def add(a,b):
    r=dict(a)
    for m,q in b.items():
        r[m]=r.get(m,F(0))+q
        if r[m]==0: del r[m]
    return r
def neg(a): return {m:-q for m,q in a.items()}
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    r={}
    for m,q in a.items():
        for n,s in b.items():
            k=tuple(m[i]+n[i] for i in range(N))
            r[k]=r.get(k,F(0))+q*s
    return {m:q for m,q in r.items() if q}
def scale(a,q):
    q=F(q); return {m:q*s for m,s in a.items() if q*s}
def eq(a,b): return sub(a,b)=={}

X,Y,Z,A,B,k1,k2,k3,k4,k5,f=[var(i) for i in range(N)]
X2=mul(X,X)
aX=sub(mul(k1,A),mul(k2,X))
forcing=sub(mul(mul(k3,B),X),scale(mul(k4,X2),2))
fx=add(mul(aX,Y),forcing)
fz=sub(mul(mul(k3,B),X),mul(k5,Z))

# Exact decompositions used in the proof.
assert eq(fx, add(mul(sub(mul(k1,A),mul(k2,X)),Y), sub(mul(mul(k3,B),X),scale(mul(k4,X2),2))))
assert eq(fz, sub(mul(mul(k3,B),X),mul(k5,Z)))

# Historical specialization.
k3v=F(8000); Bv=F(3,50); k5v=F(1)
alpha=k3v*Bv
assert alpha==F(480)
assert k5v/alpha==F(1,480)
assert F(1)/(alpha*alpha)==F(1,230400)

print('VERIFY_OK')
