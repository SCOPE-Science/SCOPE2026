from fractions import Fraction as F
from decimal import Decimal, getcontext


def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b)); c=[F(0)]*n
    for i in range(n): c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return trim(c)

def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def scale(a,s): return trim([F(s)*x for x in a])
def pw(a,n):
    r=[F(1)]; b=a
    while n:
        if n&1: r=mul(r,b)
        b=mul(b,b); n//=2
    return r
def deriv(a): return trim([F(i)*a[i] for i in range(1,len(a))] or [F(0)])
def divmodp(a,b):
    a=trim(a[:]); b=trim(b[:])
    if b==[0]: raise ZeroDivisionError
    if len(a)<len(b): return [F(0)],a
    q=[F(0)]*(len(a)-len(b)+1)
    while len(a)>=len(b) and a!=[0]:
        d=len(a)-len(b); c=a[-1]/b[-1]; q[d]=c
        a=sub(a, [F(0)]*d+scale(b,c))
    return trim(q),trim(a)
def evalp(p,x):
    s=F(0)
    for c in reversed(p): s=s*x+c
    return s

def sturm(p):
    seq=[trim(p), deriv(p)]
    while seq[-1] != [0]:
        _,r=divmodp(seq[-2],seq[-1])
        if r==[0]: break
        seq.append(neg(r))
    return seq

def sign(x): return 1 if x>0 else (-1 if x<0 else 0)
def variations(seq,x):
    vals=[sign(evalp(p,x)) for p in seq]
    vals=[v for v in vals if v]
    return sum(vals[i]!=vals[i-1] for i in range(1,len(vals)))
def roots_between(p,a,b):
    s=sturm(p)
    return variations(s,a)-variations(s,b)

class Rat:
    def __init__(self,n,d=None):
        self.n=trim([F(x) for x in (n if isinstance(n,list) else [n])])
        self.d=trim([F(x) for x in (d if isinstance(d,list) else [d if d is not None else 1])])
    def __add__(self,o):
        o=o if isinstance(o,Rat) else Rat(o)
        return Rat(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
    __radd__=__add__
    def __neg__(self): return Rat(neg(self.n),self.d)
    def __sub__(self,o): return self+(- (o if isinstance(o,Rat) else Rat(o)))
    def __rsub__(self,o): return Rat(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Rat) else Rat(o)
        return Rat(mul(self.n,o.n),mul(self.d,o.d))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,Rat) else Rat(o)
        return Rat(mul(self.n,o.d),mul(self.d,o.n))
    def __rtruediv__(self,o): return Rat(o)/self
    def __pow__(self,n): return Rat(pw(self.n,n),pw(self.d,n))

def poly_multiple_zero_mod_H(r,H):
    _,rem=divmodp(r.n,H)
    return rem==[0]

def rat_gt_on_interval(r,c,lo,hi):
    q=r-Rat(c)
    # denominator must be nonzero in interval, and numerator constant sign.
    assert roots_between(q.d,lo,hi)==0
    assert roots_between(q.n,lo,hi)==0
    mid=(lo+hi)/2
    return evalp(q.n,mid)*evalp(q.d,mid)>0

H=[F(-4),F(96),F(-660),F(1940),F(-2916),F(2187)]
lo=F(23,100); hi=F(6,25)
assert evalp(H,lo)>0 and evalp(H,hi)<0
assert roots_between(H,lo,hi)==1

z=Rat([F(0),F(1)])
eta_num=[F(-68606),F(1053986),F(-4037567),F(6966324),F(-6044868)]
eta=Rat(eta_num,F(5814))
w=z*(eta-1)
b=(eta**3+7)/((eta-1)*(eta+2))
aeq=w**3+3*w**2-b*w+1
bprime=((eta+1)**2*(eta**2-7))/((eta-1)**2*(eta+2)**2)
tan=(eta-1)*bprime-w*(2*w+3-1/(w**2))
assert poly_multiple_zero_mod_H(aeq,H)
assert poly_multiple_zero_mod_H(tan,H)
assert rat_gt_on_interval(eta,F(24,5),lo,hi)
assert rat_gt_on_interval(w,F(1,2),lo,hi)

getcontext().prec=80
def HD(x):
    return Decimal(2187)*x**5-Decimal(2916)*x**4+Decimal(1940)*x**3-Decimal(660)*x**2+Decimal(96)*x-Decimal(4)
a=Decimal(23)/Decimal(100); bD=Decimal(6)/Decimal(25)
fa=HD(a)
for _ in range(260):
    m=(a+bD)/2; fm=HD(m)
    if fm==0: a=bD=m; break
    if (fa>0 and fm>0) or (fa<0 and fm<0): a=m; fa=fm
    else: bD=m
root=(a+bD)/2
theta=root.sqrt()
print('VERIFY_OK roots=1 z=%s theta=%s' % (root,theta))
