from fractions import Fraction as F

# Polynomials use ascending coefficients.
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def add(a,b):
    n=max(len(a),len(b))
    return trim([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n)])

def scale(a,c):
    return trim([c*x for x in a])

def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(out)

def deriv(a):
    return trim([F(i)*a[i] for i in range(1,len(a))] or [F(0)])

def val(a,x):
    out=x*0
    p=x*0+1
    for c in a:
        out=out+c*p
        p=p*x
    return out

def subst_one_minus_t(a):
    # Horner composition a(1-t).
    out=[F(0)]
    u=[F(1),F(-1)]
    for c in reversed(a):
        out=add(mul(out,u),[c])
    return trim(out)

class Q3:
    # a + b sqrt(3), exact rational a,b.
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        return Q3(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q3(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Q3) else Q3(o)))
    def __rsub__(self,o): return Q3(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        return Q3(self.a*o.a+3*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        den=o.a*o.a-3*o.b*o.b
        return Q3((self.a*o.a-3*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        return self.a==o.a and self.b==o.b
    def sign(self):
        if self.a==0:
            return (self.b>0)-(self.b<0)
        if self.b==0:
            return (self.a>0)-(self.a<0)
        if self.a>0 and self.b>0: return 1
        if self.a<0 and self.b<0: return -1
        aa=self.a*self.a
        bb=3*self.b*self.b
        if aa==bb: return 0
        if self.a>0 and self.b<0:
            return 1 if aa>bb else -1
        return -1 if aa>bb else 1
    def __repr__(self): return f"Q3({self.a},{self.b})"

t=[F(0),F(1)]
one=[F(1)]
tm1=[F(-1),F(1)]
tm2=[F(-2),F(1)]
tp1=[F(1),F(1)]

L0=scale(mul(mul(t,tm1),tm2),F(-1,6))
L1=scale(mul(mul(tp1,tm1),tm2),F(1,2))
L2=scale(mul(mul(t,tp1),tm2),F(-1,2))
L3=scale(mul(mul(t,tm1),tp1),F(1,6))
assert add(add(L0,L1),add(L2,L3)) == one

q0=add(one,scale(L0,-1))
q1=add(L2,L3)
q2=L3
assert q0 == add(one,scale(mul(mul(t,tm1),tm2),F(1,6)))
assert q1 == scale(mul(mul(t,tp1),[F(5),F(-2)]),F(1,6))
assert q2 == scale(mul(mul(t,tm1),tp1),F(1,6))

one_minus_q1=add(one,scale(q1,-1))
factor=scale(mul(mul(tm2,tm1),[F(3),F(2)]),F(1,6))
assert one_minus_q1 == factor

lower_defect=scale(q2,-1)
upper_defect=add(q0,[-1])
assert lower_defect == [F(0),F(1,6),F(0),F(-1,6)]
assert upper_defect == subst_one_minus_t(lower_defect)
assert deriv(lower_defect) == [F(1,6),F(0),F(-1,2)]

s=Q3(0,F(1,3))  # 1/sqrt(3) = sqrt(3)/3
assert s*s == Q3(F(1,3))
assert val(lower_defect,s) == Q3(0,F(1,27))
assert val(upper_defect,Q3(1)-s) == Q3(0,F(1,27))

# Strict-positive witness (eps,2eps,3eps,1), eps=1/100.
eps=F(1,100)
expr=eps + val(q0,s)*eps + val(q1,s)*eps + val(q2,s)*(1-3*eps)
expected=Q3(F(1,50),F(-29,900))  # (18-29 sqrt(3))/900
assert expr == expected
assert expr.sign() < 0
assert 18*18 < 3*29*29

# Threshold epsilon = (18 sqrt(3)-13)/803 is positive and below 1/3.
thresh=Q3(F(-13,803),F(18,803))
assert thresh.sign()>0
assert (Q3(F(1,3))-thresh).sign()>0

print('VERIFY_OK')
