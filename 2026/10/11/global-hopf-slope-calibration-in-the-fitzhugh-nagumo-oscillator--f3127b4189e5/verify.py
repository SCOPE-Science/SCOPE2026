from fractions import Fraction as F

# Sparse polynomial ring in v,w,a,b,eps,I.
N=6

def var(i):
    e=[0]*N; e[i]=1
    return {tuple(e):F(1)}

def const(q): return {(0,)*N:F(q)}
def add(p,q):
    out=dict(p)
    for m,c in q.items():
        out[m]=out.get(m,F(0))+c
        if out[m]==0: del out[m]
    return out

def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    out={}
    for m,c in p.items():
        for n,d in q.items():
            k=tuple(m[i]+n[i] for i in range(N))
            out[k]=out.get(k,F(0))+c*d
    return {m:c for m,c in out.items() if c}
def scale(p,q):
    q=F(q)
    return {m:q*c for m,c in p.items() if q*c}
def powp(p,n):
    out=const(1)
    for _ in range(n): out=mul(out,p)
    return out

def der(p,i):
    out={}
    for m,c in p.items():
        if m[i]:
            n=list(m); n[i]-=1; n=tuple(n)
            out[n]=out.get(n,F(0))+c*m[i]
    return {m:c for m,c in out.items() if c}
def eq(p,q): return sub(p,q)=={}

v,w,a,b,eps,I=[var(i) for i in range(N)]
one=const(1)
f=sub(v,scale(powp(v,3),F(1,3)))
g=add(sub(f,w),I)
h=mul(eps,sub(add(v,a),mul(b,w)))
field=[g,h,{}, {}, {}, {}]

def L(p):
    out={}
    for i in range(N): out=add(out,mul(der(p,i),field[i]))
    return out

U=add(add(scale(mul(sub(one,b),powp(v,2)),F(1,2)),scale(mul(b,powp(v,4)),F(1,12))),mul(sub(a,mul(b,I)),v))
E=add(scale(powp(g,2),F(1,2)),mul(eps,U))
expected=mul(sub(sub(one,mul(eps,b)),powp(v,2)),powp(g,2))
assert eq(L(E),expected)

# Regression residuals.
assert eq(sub(w,add(f,I)),neg(g))
# eps*(v-(bw-a)) = h
assert eq(mul(eps,sub(v,sub(mul(b,w),a))),h)

# Abstract conditional-regression variance algebra.
EA=F(7,5); EB=EA; EB2=F(19,6); EAB=EB2; EA2=F(23,5)
assert EA2-2*EAB+EB2 == (EA2-EA*EA)-(EB2-EB*EB)

# Standard parameters.
e0=F(2,25); b0=F(4,5)
assert 1-e0*b0 == F(117,125)

print('VERIFY_OK')
