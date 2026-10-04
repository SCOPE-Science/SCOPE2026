from fractions import Fraction as F

# Sparse polynomial ring in x,y,z,a,b,c,d,r,s,xR,I.
N = 11

def var(i):
    e=[0]*N; e[i]=1
    return {tuple(e):F(1)}

def add(p,q):
    out=dict(p)
    for m,v in q.items():
        out[m]=out.get(m,F(0))+v
        if out[m]==0: del out[m]
    return out

def neg(p): return {m:-v for m,v in p.items()}
def sub(p,q): return add(p,neg(q))

def mul(p,q):
    out={}
    for m,a in p.items():
        for n,b in q.items():
            k=tuple(m[i]+n[i] for i in range(N))
            out[k]=out.get(k,F(0))+a*b
    return {m:v for m,v in out.items() if v}

def scale(p,q):
    q=F(q)
    return {m:q*v for m,v in p.items() if q*v}

def der(p,i):
    out={}
    for m,a in p.items():
        if m[i]:
            n=list(m); n[i]-=1; n=tuple(n)
            out[n]=out.get(n,F(0))+a*m[i]
    return {m:v for m,v in out.items() if v}

def eq(p,q): return sub(p,q)=={}

x,y,z,a,b,c,d,r,s,xR,I=[var(i) for i in range(N)]
fx=add(add(sub(y,mul(a,mul(mul(x,x),x))),mul(b,mul(x,x))),sub(I,z))
fy=sub(sub(c,mul(d,mul(x,x))),y)
fz=mul(r,sub(mul(s,sub(x,xR)),z))
field=[fx,fy,fz]+[{}]*(N-3)

def L(p):
    out={}
    for i in range(N):
        out=add(out,mul(der(p,i),field[i]))
    return out

assert eq(L(scale(mul(y,y),F(1,2))),mul(y,fy))
assert eq(L(scale(mul(z,z),F(1,2))),mul(z,fz))

res_y=add(sub(mul(d,mul(x,x)),c),y)
assert eq(res_y,neg(fy))
res_z=mul(r,sub(mul(s,sub(x,xR)),z))
assert eq(res_z,fz)

assert F(5)**2 == 25
assert F(4)**2 == 16

print('VERIFY_OK')
