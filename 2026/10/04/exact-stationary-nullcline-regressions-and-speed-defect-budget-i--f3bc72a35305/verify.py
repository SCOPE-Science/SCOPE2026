from fractions import Fraction as F

# Sparse polynomial ring in v,w,a,b,I,eps.
N=6

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
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(m[i]+n[i] for i in range(N))
            r[k]=r.get(k,F(0))+c*d
    return {m:c for m,c in r.items() if c}

def scale(p,q):
    q=F(q)
    return {m:q*c for m,c in p.items() if q*c}

def eq(p,q): return sub(p,q)=={}

v,w,a,b,I,eps=[var(i) for i in range(N)]
v2=mul(v,v); v3=mul(v2,v)
Fv=add(sub(v,scale(v3,F(1,3))),I)
fdot=sub(Fv,w)
wdot=mul(eps,sub(add(v,a),mul(b,w)))

assert eq(sub(Fv,w),fdot)
assert eq(sub(add(v,a),mul(b,w)), sub(add(v,a),mul(b,w)))

# Equilibrium polynomial after w=F(v): v+a-bF(v).
eqpoly=sub(add(v,a),mul(b,Fv))
target=add(add(scale(v3,F(1,3)), {}), {})
target=add(add(scale(mul(b,v3),F(1,3)), mul(sub(const(1),b),v)), sub(a,mul(b,I)))
assert eq(eqpoly,target)

b0=F(4,5); e0=F(2,25)
assert b0*b0==F(16,25)
assert F(1)/(e0*e0)==F(625,4)

print('VERIFY_OK')
