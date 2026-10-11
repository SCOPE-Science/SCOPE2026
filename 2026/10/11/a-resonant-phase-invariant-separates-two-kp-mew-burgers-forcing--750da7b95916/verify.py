from fractions import Fraction as F

N=5  # w,p,z,q,o

def clean(a):
    return {m:c for m,c in a.items() if c}
def C(c): return {(0,0,0,0,0):F(c)}
def X(i):
    e=[0]*N; e[i]=1
    return {tuple(e):F(1)}
def add(a,b):
    r=dict(a)
    for m,c in b.items(): r[m]=r.get(m,F(0))+c
    return clean(r)
def neg(a): return {m:-c for m,c in a.items()}
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    r={}
    for ma,ca in a.items():
        for mb,cb in b.items():
            m=tuple(x+y for x,y in zip(ma,mb))
            r[m]=r.get(m,F(0))+ca*cb
    return clean(r)
def scale(c,a): return clean({m:F(c)*v for m,v in a.items()})
def powp(a,n):
    r=C(1)
    for _ in range(n): r=mul(r,a)
    return r
def deriv(a,i):
    r={}
    for m,c in a.items():
        if m[i]:
            mm=list(m); k=mm[i]; mm[i]-=1
            mm=tuple(mm); r[mm]=r.get(mm,F(0))+c*k
    return clean(r)
def lie(a,Fv):
    r={}
    for i,fi in enumerate(Fv): r=add(r,mul(deriv(a,i),fi))
    return clean(r)

def ev(a,vals):
    s=F(0)
    for m,c in a.items():
        t=c
        for e,v in zip(m,vals): t*=v**e
        s+=t
    return s

w,p,z,q,o=[X(i) for i in range(N)]
field=[neg(mul(o,p)),mul(o,w),scale(2,mul(o,q)),scale(-2,mul(o,z)),C(0)]
I1=add(powp(w,2),powp(p,2))
I2=add(powp(z,2),powp(q,2))
Kr=add(mul(q,sub(powp(w,2),powp(p,2))),scale(2,mul(mul(z,w),p)))
Ki=sub(mul(z,sub(powp(w,2),powp(p,2))),scale(2,mul(mul(q,w),p)))
for name,P in [('I1',I1),('I2',I2),('ReK',Kr),('ImK',Ki)]:
    assert lie(P,field)=={}, name
assert sub(add(powp(Kr,2),powp(Ki,2)),mul(powp(I1,2),I2))=={}
vals=[F(4,5),F(3,5),F(4,5),F(3,5),F(5,4)]
assert ev(I1,vals)==1 and ev(I2,vals)==1
assert ev(Kr,vals)==F(117,125)
assert ev(Ki,vals)==F(-44,125)
canon=[F(1),F(0),F(0),F(1),F(5,4)]
assert ev(Kr,canon)==1 and ev(Ki,canon)==0
print('VERIFY_OK')
