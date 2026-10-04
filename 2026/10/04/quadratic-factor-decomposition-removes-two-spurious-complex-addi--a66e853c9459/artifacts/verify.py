from fractions import Fraction as F
from itertools import product

# Basis e1,e2,e3. A_t products from Bekbaev--Rakhimov As_{1,1}^8(3)(t).
def mulQ(x,y,t):
    # bilinear via basis table
    a,b,c=x; d,e,f=y
    # e1 unit; e2^2=e1; e2e3=e3e2=e3; e3^2=t(e1+e2)+e3
    return (
        a*d + b*e + t*c*f,
        a*e + b*d + t*c*f,
        a*f + c*d + b*f + c*e + c*f,
    )

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(a,x): return tuple(a*b for b in x)

e1=(F(1),F(0),F(0)); e2=(F(0),F(1),F(0)); e3=(F(0),F(0),F(1))
p=scale(F(1,2),add(e1,e2)); q=scale(F(1,2),sub(e1,e2))
for t in [F(-7,11), F(0), F(5,3)]:
    assert mulQ(p,p,t)==p and mulQ(q,q,t)==q and mulQ(p,q,t)==(F(0),)*3
    assert mulQ(p,e3,t)==e3 and mulQ(q,e3,t)==(F(0),)*3
    w=sub(scale(F(2),e3),p)
    assert mulQ(w,w,t)==scale(F(1)+F(8)*t,p)

# t=0: q,e3,p-e3 are 3 orthogonal idempotents summing to 1 (U_2^3).
r=e3; s=sub(p,e3)
B=[q,r,s]
for i,x in enumerate(B):
    for j,y in enumerate(B):
        expected=x if i==j else (F(0),)*3
        assert mulQ(x,y,F(0))==expected
assert add(add(q,r),s)==e1

# t=-1/8: q,p,epsilon with epsilon^2=0 and p epsilon=epsilon (U_3^3).
eps=sub(e3,scale(F(1,2),p))
assert mulQ(q,q,F(-1,8))==q
assert mulQ(p,p,F(-1,8))==p
assert mulQ(p,eps,F(-1,8))==eps == mulQ(eps,p,F(-1,8))
assert mulQ(eps,eps,F(-1,8))==(F(0),)*3
assert mulQ(q,p,F(-1,8))==(F(0),)*3 and mulQ(q,eps,F(-1,8))==(F(0),)*3

# Finite-field exhaustive automorphism count for q=5, fixing the identity e1.
def inv(a,p): return pow(a,p-2,p)
def det3(cols,p):
    # columns vectors
    a,b,c=cols
    m00,m10,m20=a; m01,m11,m21=b; m02,m12,m22=c
    return (m00*(m11*m22-m12*m21)-m01*(m10*m22-m12*m20)+m02*(m10*m21-m11*m20))%p

def madd(x,y,p): return tuple((a+b)%p for a,b in zip(x,y))
def mscale(a,x,p): return tuple((a*b)%p for b in x)
def mmul(x,y,t,pmod):
    a,b,c=x; d,e,f=y; t%=pmod
    return ((a*d+b*e+t*c*f)%pmod,
            (a*e+b*d+t*c*f)%pmod,
            (a*f+c*d+b*f+c*e+c*f)%pmod)

def lin(cols,x,p):
    return tuple(sum(cols[j][i]*x[j] for j in range(3))%p for i in range(3))

def aut_count(t,pmod):
    one=(1,0,0); basis=[one,(0,1,0),(0,0,1)]
    count=0
    # bijective algebra endomorphisms fix the identity; enumerate images of e2,e3.
    for v2 in product(range(pmod), repeat=3):
      for v3 in product(range(pmod), repeat=3):
        cols=[one,v2,v3]
        if det3(cols,pmod)==0: continue
        ok=True
        for x in basis:
          for y in basis:
            if lin(cols,mmul(x,y,t,pmod),pmod)!=mmul(lin(cols,x,pmod),lin(cols,y,pmod),t,pmod):
                ok=False; break
          if not ok: break
        if ok: count+=1
    return count

q0=5
squares={x*x%q0 for x in range(1,q0)}
rows=[]
for t in range(q0):
    delta=(1+8*t)%q0
    typ='zero' if delta==0 else ('square' if delta in squares else 'nonsquare')
    c=aut_count(t,q0)
    expected={'square':6,'zero':q0-1,'nonsquare':2}[typ]
    assert c==expected, (t,delta,typ,c,expected)
    rows.append((t,delta,typ,c))
assert [r[2] for r in rows].count('zero')==1
assert [r[2] for r in rows].count('square')==(q0-1)//2
assert [r[2] for r in rows].count('nonsquare')==(q0-1)//2
print('F5 rows:', rows)
print('CHECK_OK')
