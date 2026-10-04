#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

# Bivariate exact polynomial: dict[(power_a,power_x)] -> Fraction.
def clean(p):
    return {k:v for k,v in p.items() if v}

def add(p,q):
    r=dict(p)
    for k,v in q.items():
        r[k]=r.get(k,F(0))+v
    return clean(r)

def neg(p): return {k:-v for k,v in p.items()}
def sub(p,q): return add(p,neg(q))

def mul(p,q):
    r={}
    for (ia,ix),u in p.items():
        for (ja,jx),v in q.items():
            k=(ia+ja,ix+jx)
            r[k]=r.get(k,F(0))+u*v
    return clean(r)

def scale(p,c):
    c=F(c)
    return clean({k:c*v for k,v in p.items()})

def power(p,n):
    r={(0,0):F(1)}
    for _ in range(n):
        r=mul(r,p)
    return r

ONE={(0,0):F(1)}
A={(1,0):F(1)}
X={(0,1):F(1)}

def const(c): return {(0,0):F(c)}

# Chebyshev polynomials in x.
T=[ONE,X]
for n in range(1,6):
    T.append(sub(scale(mul(X,T[-1]),2),T[-2]))

# r_a(x)
r=add(add(power(X,3),mul(A,power(X,2))),
      add(mul(sub(scale(power(A,2),2),const(F(5,4))),X),
          scale(power(A,3),-2)))

# Exact Chebyshev identity for 32 r^2.
D0=add(add(scale(power(A,6),128),scale(power(A,2),-20)),const(5))
c1=scale(mul(A,add(add(scale(power(A,4),64),scale(power(A,2),-40)),const(5))),-4)
c4=scale(add(scale(power(A,2),5),const(-1)),4)
rhs=add(add(add(add(mul(D0,T[0]),mul(c1,T[1])),mul(c4,T[4])),mul(scale(A,4),T[5])),T[6])
assert clean(scale(power(r,2),32)) == clean(rhs)

# Polynomial F(a).
Fp=add(add(add(add(add(add(add(scale(power(A,7),256),scale(power(A,6),256)),
                   scale(power(A,5),-96)),scale(power(A,4),-80)),scale(power(A,3),40)),
             scale(power(A,2),30)),scale(A,-15)),const(-5))

# Clear-denominator dual polynomial Qtilde and E.
D=mul(A,add(scale(power(A,4),96),const(-5)))
S=add(add(add(scale(power(A,4),-160),scale(power(A,2),60)),scale(A,5)),const(-2))
twominus=add(scale(A,2),const(-1))
E=scale(mul(twominus,D),4)
Q2=scale(mul(twominus,S),4)
Q1=scale(mul(mul(A,twominus),
                 add(add(add(scale(power(A,4),256),scale(power(A,2),-60)),scale(A,-5)),const(-3))),-4)
Q0=add(add(add(add(add(add(add(scale(power(A,7),-3840),scale(power(A,6),1920)),
                         scale(power(A,5),2432)),scale(power(A,4),-1120)),
                   scale(power(A,3),-640)),scale(power(A,2),250)),scale(A,53)),const(-14))
Q=add(add(Q0,mul(Q1,X)),mul(Q2,power(X,2)))

# Remainder in x modulo monic cubic r.
def degree_x(p):
    return max((ix for (_,ix) in p), default=-1)

def coeff_x(p,k):
    return {(ia,0):v for (ia,ix),v in p.items() if ix==k}

def shift_x(p,k):
    return {(ia,ix+k):v for (ia,ix),v in p.items()}

def rem_x(p,mod):
    p=dict(p)
    while degree_x(p) >= 3:
        d=degree_x(p)
        lead={(ia,0):v for (ia,ix),v in p.items() if ix==d}
        p=sub(p,mul(shift_x(lead,d-3),mod))
    return clean(p)

def x2_as_a_poly(p):
    return clean({(ia,0):v for (ia,ix),v in p.items() if ix==2})

for k in [1,4,5]:
    ck=x2_as_a_poly(rem_x(mul(Q,T[k]),r))
    assert clean(add(ck,E)) == {}

c6=x2_as_a_poly(rem_x(mul(Q,T[6]),r))
factor=scale(mul(mul(mul(twominus,add(scale(A,2),const(1))),
                     add(add(scale(power(A,2),4),scale(A,-6)),const(1))),Fp),-8)
assert clean(sub(add(c6,E),factor)) == {}

# Fraction interval arithmetic.
def ia_add(I,J): return (I[0]+J[0],I[1]+J[1])
def ia_mul(I,J):
    v=[I[0]*J[0],I[0]*J[1],I[1]*J[0],I[1]*J[1]]
    return (min(v),max(v))
def ia_scale(c,I):
    c=F(c)
    return (c*I[0],c*I[1]) if c>=0 else (c*I[1],c*I[0])
def ia_pow(I,n):
    out=(F(1),F(1))
    for _ in range(n): out=ia_mul(out,I)
    return out
def eval_box(p,AI,XI):
    out=(F(0),F(0))
    for (pa,px),c in p.items():
        out=ia_add(out,ia_scale(c,ia_mul(ia_pow(AI,pa),ia_pow(XI,px))))
    return out
def eval_a_exact(p,a):
    out=F(0)
    for (pa,px),c in p.items():
        assert px==0
        out += c*a**pa
    return out

AI=(F(53305,100000),F(53306,100000))
flo=eval_a_exact(Fp,AI[0]); fhi=eval_a_exact(Fp,AI[1])
assert flo < 0 < fhi

# Derivative F'(a), exact.
Fder={}
for (pa,px),c in Fp.items():
    if pa:
        Fder[(pa-1,0)]=c*pa
FderI=eval_box(Fder,AI,(F(0),F(0)))
assert FderI[0] > F(71,1)

# Three root brackets for r and signs of r'.
root_boxes=[
    (F(-9163,10000),F(-9161,10000)),
    (F(-4146,10000),F(-4143,10000)),
    (F(7975,10000),F(7978,10000)),
]
# r' in x
rx={}
for (pa,px),c in r.items():
    if px:
        rx[(pa,px-1)]=c*px

endpoint_signs=[]
der_signs=[]
q_signs=[]
for lo,hi in root_boxes:
    Rlo=eval_box(r,AI,(lo,lo)); Rhi=eval_box(r,AI,(hi,hi))
    endpoint_signs.append((Rlo,Rhi))
    RI=eval_box(rx,AI,(lo,hi))
    der_signs.append(RI)
    QI=eval_box(Q,AI,(lo,hi))
    q_signs.append(QI)

# Required sign patterns establish one simple root in each interval and positive dual weights.
assert endpoint_signs[0][0][1] < 0 and endpoint_signs[0][1][0] > 0
assert endpoint_signs[1][0][0] > 0 and endpoint_signs[1][1][1] < 0
assert endpoint_signs[2][0][1] < 0 and endpoint_signs[2][1][0] > 0
assert der_signs[0][0] > 0
assert der_signs[1][1] < 0
assert der_signs[2][0] > 0
assert q_signs[0][0] > 0
assert q_signs[1][1] < 0
assert q_signs[2][0] > 0
EI=eval_box(E,AI,(F(0),F(0)))
assert EI[0] > 0

# High-precision decimal Newton calculation for display only; proof is exact above.
getcontext().prec=60
def fdec(a):
    return (Decimal(256)*a**7+Decimal(256)*a**6-Decimal(96)*a**5
            -Decimal(80)*a**4+Decimal(40)*a**3+Decimal(30)*a**2
            -Decimal(15)*a-Decimal(5))
def fpdec(a):
    return (Decimal(1792)*a**6+Decimal(1536)*a**5-Decimal(480)*a**4
            -Decimal(320)*a**3+Decimal(120)*a**2+Decimal(60)*a-Decimal(15))
a=Decimal("0.5330518")
for _ in range(12):
    a -= fdec(a)/fpdec(a)
C=Decimal(2)*(Decimal(2)*a+1)**2*(Decimal(4)*a*a-Decimal(6)*a+1)**2/(Decimal(128)*a**6-Decimal(20)*a*a+Decimal(5))
TR=C/Decimal(2)

print("VERIFY_OK")
print("a_interval=(0.53305,0.53306)")
print("a_approx="+str(a))
print("TZ_approx="+str(C))
print("TR_approx="+str(TR))
print("root_brackets=(-0.9163,-0.9161),(-0.4146,-0.4143),(0.7975,0.7978)")
print("dual_weight_signs=positive")
