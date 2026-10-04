from fractions import Fraction as Q
from math import comb
from decimal import Decimal, getcontext

# Exact arithmetic in Q(sqrt(2)): values are pairs a+b*sqrt(2).
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(x,q): return (x[0]*q,x[1]*q)
def inv(x):
    d=x[0]*x[0]-2*x[1]*x[1]
    if d == 0: raise ZeroDivisionError
    return (x[0]/d,-x[1]/d)
def div(x,y): return mul(x,inv(y))
def powq(x,n):
    out=(Q(1),Q(0)); base=x
    while n:
        if n&1: out=mul(out,base)
        base=mul(base,base); n//=2
    return out

def eq(x,a,b):
    assert x==(Q(a),Q(b)), (x,(Q(a),Q(b)))

ONE=(Q(1),Q(0)); SQ2=(Q(0),Q(1))
rho=(Q(17),Q(-12))

# F(t)=sum_{m>=0} a_m t^m with a_m=binom(m+3,3)/(1-rho^(m+2)).
a=[]
for m in range(4):
    den=sub(ONE,powq(rho,m+2))
    a.append(scale(inv(den),Q(comb(m+3,3))))

# Reciprocal coefficients b_m for 1/F(t)=sum b_m t^m.
b=[]
b0=inv(a[0]); b.append(b0)
for n in range(1,4):
    s=(Q(0),Q(0))
    for k in range(1,n+1): s=add(s,mul(a[k],b[n-k]))
    b.append(neg(mul(inv(a[0]),s)))

eq(b[0],-576,408)
eq(b[1],Q(2304,35),Q(-1728,35))
eq(b[2],0,Q(88008,20825))
eq(b[3],Q(-1663057152,866632375),Q(-1247292864,866632375))

# Coefficients of the inverse tail are b_m/1024 multiplying t^(m-2).
inv_m2=scale(b[0],Q(1,1024))
inv_m1=scale(b[1],Q(1,1024))
const=scale(b[2],Q(1,1024))
inv_p1=scale(b[3],Q(1,1024))

eq(inv_m2,Q(-9,16),Q(51,128))
eq(inv_m1,Q(9,140),Q(-27,560))
eq(const,0,Q(11001,2665600))

# B_n^4-B_{n-1}^4 has these t^-2 and t^-1 coefficients.
base_m2=(Q(-9,16),Q(51,128))
base_m1=(Q(1,16),Q(-3,64))
assert inv_m2==base_m2

# B_{2n-1}=h*t^-1 + O(t), h=lambda^-1/(4sqrt(2)).
h=(Q(-1,2),Q(3,8))
# The unique cancellation coefficient is c=1/280.
assert sub(base_m1,inv_m1)==scale(h,Q(1,280))

# For c=1/280 the t coefficient of the smooth approximant is g1.
g1=(Q(9,140),Q(27,560))
kappa=neg(sub(inv_p1,g1))
eq(kappa,Q(114672321,1733264750),Q(344016963,6933059000))

# Numerical replay against direct balancing tails for n=2,...,12.
getcontext().prec=80
sqrt2=Decimal(2).sqrt()
C=Decimal(11001)*sqrt2/Decimal(2665600)
K=(Decimal(114672321)/Decimal(1733264750)
   +Decimal(344016963)*sqrt2/Decimal(6933059000))
rhoD=Decimal(17)-Decimal(12)*sqrt2

def B(n):
    a,b=0,1
    for _ in range(n): a,b=b,6*b-a
    return a

def residual(n):
    # 25 terms are far more than needed at this growth rate.
    s=Decimal(0)
    for k in range(n,n+25):
        bk=Decimal(B(k)); s += Decimal(1)/(bk**4)
    gsm=(Decimal(B(n)**4-B(n-1)**4)-Decimal(B(2*n-1))/Decimal(280))
    return Decimal(1)/s-gsm

prev=Decimal(0)
for n in range(2,13):
    R=residual(n)
    assert R>Decimal(1)/Decimal(280)
    assert R<C
    assert R>prev
    prev=R
    # First-order asymptotic error is O(rho^(2n)); a generous certified replay bound.
    approx=C-K*(rhoD**n)
    assert abs(R-approx) < Decimal(3)*(rhoD**(2*n))

print('VERIFY_OK exact_series_coefficients=4 unique_c=1/280 residual_cases=11 n=2..12')
