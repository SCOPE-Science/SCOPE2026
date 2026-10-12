from fractions import Fraction
from decimal import Decimal, getcontext

def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,0)+v
        if out[k]==0: del out[k]
    return out
def mul(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            out[i+j]=out.get(i+j,0)+x*y
    return {k:v for k,v in out.items() if v}
def scale(a,c):
    return {k:c*v for k,v in a.items() if c*v}
def sub(a,b):
    return add(a,scale(b,-1))
def pval(x):
    return 3*x**12-7*x**8+5*x**4+x**3-1

# Integer-polynomial replay of
# (1-3t^4)^2 D - [4t^3-(1-3t^4)(1-t^8)]^2 = -16t^3 P.
one={0:1}; t3={3:1}; t4={4:1}; t7={7:1}; t8={8:1}; t16={16:1}
A=add(one,scale(t4,-3))
D={16:1,8:-2,7:-8,3:8,0:1}
B=sub(scale(t3,4),mul(A,add(one,scale(t8,-1))))
lhs=sub(mul(mul(A,A),D),mul(B,B))
P={12:3,8:-7,4:5,3:1,0:-1}
rhs=scale(mul(t3,P),-16)
assert lhs==rhs, (lhs,rhs)

lo=Fraction(6589251988439,10**13)
hi=Fraction(6589251988440,10**13)
assert pval(lo) < 0 < pval(hi)

getcontext().prec=70
def fsign(s):
    t=Decimal(s)
    D=t**16-2*t**8-8*t**7+8*t**3+1
    phi=(1-t**8+D.sqrt())/(2*t**2)
    return (1-3*t**4)*phi-2*t
assert fsign("0.65") > 0
assert fsign("0.67") < 0
print("VERIFY_OK identity=exact root_bracket=0.6589251988439..0.6589251988440 signs=0.65:+,0.67:-")
