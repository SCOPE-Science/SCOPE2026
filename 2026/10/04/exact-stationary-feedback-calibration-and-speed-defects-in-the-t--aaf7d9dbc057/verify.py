from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,Sx,Sy,Sz,b.
N = 7

def var(i):
    e = [0] * N
    e[i] = 1
    return {tuple(e): F(1)}

def add(a,b):
    r=dict(a)
    for m,c in b.items():
        r[m]=r.get(m,F(0))+c
        if r[m]==0: del r[m]
    return r

def neg(a): return {m:-c for m,c in a.items()}
def sub(a,b): return add(a,neg(b))

def mul(a,b):
    r={}
    for m,c in a.items():
        for n,d in b.items():
            k=tuple(m[i]+n[i] for i in range(N))
            r[k]=r.get(k,F(0))+c*d
    return {m:c for m,c in r.items() if c}

def scale(a,s):
    s=F(s)
    return {m:s*c for m,c in a.items() if s*c}

def eq(a,b): return sub(a,b)=={}

x,y,z,Sx,Sy,Sz,b=[var(i) for i in range(N)]
fx=sub(Sy,mul(b,x))
fy=sub(Sz,mul(b,y))
fz=sub(Sx,mul(b,z))

# residual^2 - (drive^2-b^2 state^2) = -2 b state residual
assert eq(
    sub(mul(fx,fx), sub(mul(Sy,Sy), mul(mul(b,b),mul(x,x)))),
    scale(mul(mul(b,x),fx), -2)
)
assert eq(
    sub(mul(fy,fy), sub(mul(Sz,Sz), mul(mul(b,b),mul(y,y)))),
    scale(mul(mul(b,y),fy), -2)
)
assert eq(
    sub(mul(fz,fz), sub(mul(Sx,Sx), mul(mul(b,b),mul(z,z)))),
    scale(mul(mul(b,z),fz), -2)
)

lhs=add(add(mul(fx,fx),mul(fy,fy)),mul(fz,fz))
drive=add(add(mul(Sx,Sx),mul(Sy,Sy)),mul(Sz,Sz))
states=add(add(mul(x,x),mul(y,y)),mul(z,z))
correction=scale(add(add(mul(mul(b,x),fx),mul(mul(b,y),fy)),mul(mul(b,z),fz)),-2)
rhs=add(sub(drive,mul(mul(b,b),states)),correction)
assert eq(lhs,rhs)

print("VERIFY_OK")
