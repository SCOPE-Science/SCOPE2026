from fractions import Fraction
from math import comb

def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,Fraction(0))+v
        if out[k]==0:
            del out[k]
    return out

def scale(a,c):
    return {k:v*c for k,v in a.items() if v*c}

def mul(a,b):
    out={}
    for (i,j),u in a.items():
        for (k,l),v in b.items():
            key=(i+k,j+l)
            out[key]=out.get(key,Fraction(0))+u*v
    return {k:v for k,v in out.items() if v}

ONE={(0,0):Fraction(1)}
X={(0,1):Fraction(1)}
S={(1,0):Fraction(1)}

def power(a,n):
    out=ONE
    for _ in range(n):
        out=mul(out,a)
    return out

one_minus_x=add(ONE,scale(X,-1))
one_minus_s=add(ONE,scale(S,-1))
xs2=mul(X,power(S,2))
D=power(add(ONE,scale(xs2,-1)),3)

P={}
def term(si,xj,c):
    global P
    P=add(P,{(si,xj):Fraction(c)})

for si,xj,c in [
    (1,0,4),
    (0,1,1),(1,1,-7),(2,1,1),(3,1,-3),
    (0,2,1),(1,2,5),(2,2,-6),(3,2,2),(4,2,1),(5,2,1),
    (2,3,1),(3,3,-3),(4,3,1),(5,3,1)
]:
    term(si,xj,c)

A=one_minus_x
q=xs2
base=add(power(X,2), scale(mul(X,power(A,2)),4))
N=mul(base,D)
N=add(N, mul(power(A,4), add(ONE,q)))
N=add(N, scale(mul(mul(mul(power(A,3),X),S), add(ONE,scale(q,-1))), -4))
N=add(N, scale(mul(mul(mul(power(A,2),power(X,2)),power(S,2)), power(add(ONE,scale(q,-1)),2)), 4))

lhs=add(D,scale(N,-1))
rhs=mul(mul(mul(X,one_minus_x),one_minus_s),P)
assert lhs==rhs

B = [
    [Fraction(0),Fraction(1,3),Fraction(1),Fraction(2)],
    [Fraction(4,5),Fraction(2,3),Fraction(6,5),Fraction(12,5)],
    [Fraction(8,5),Fraction(31,30),Fraction(19,15),Fraction(12,5)],
    [Fraction(12,5),Fraction(4,3),Fraction(16,15),Fraction(8,5)],
    [Fraction(16,5),Fraction(22,15),Fraction(8,15),Fraction(0)],
    [Fraction(4),Fraction(4,3),Fraction(0),Fraction(0)]
]

def bernstein_var(i,n,var,one_minus_var):
    return scale(mul(power(var,i),power(one_minus_var,n-i)), Fraction(comb(n,i)))

PB={}
for i in range(6):
    Bi=bernstein_var(i,5,S,one_minus_s)
    for j in range(4):
        Bj=bernstein_var(j,3,X,one_minus_x)
        PB=add(PB,scale(mul(Bi,Bj),B[i][j]))

assert PB==P
assert all(c>=0 for row in B for c in row)
assert any(c>0 for row in B for c in row)
print("VERIFY_OK deficit_identity=1 bernstein_identity=1 nonnegative_coefficients=24")
