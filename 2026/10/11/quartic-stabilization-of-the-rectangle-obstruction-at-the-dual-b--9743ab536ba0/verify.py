from fractions import Fraction
from math import comb

# Polynomial utilities, coefficients in ascending powers of t.
def mul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def add(a,b):
    n=max(len(a),len(b))
    c=[Fraction(0)]*n
    for i in range(n):
        c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(c)>1 and c[-1]==0: c.pop()
    return c

a=[Fraction(1),Fraction(1)]
b=[Fraction(1),Fraction(-1)]
a2=mul(a,a); b2=mul(b,b)
ab=mul(a,b)
mu=[Fraction(4,3)*x for x in mul(ab,add(a2,b2))]
assert mu == [Fraction(8,3),0,0,0,Fraction(-8,3)]

# V4 is twice mu.
v4=[2*x for x in mu]
assert v4 == [Fraction(16,3),0,0,0,Fraction(-16,3)]

# Exact rational spot checks of the ratio V4(R_t)/V4(R_0)=1-t^4.
for t in [Fraction(0), Fraction(1,10), Fraction(1,3), Fraction(2,3), Fraction(-1,2)]:
    poly=sum(v4[i]*t**i for i in range(len(v4)))
    assert poly/v4[0] == 1-t**4

# Binomial series: 1-(1-z)^(1/4) has linear coefficient 1/4 in z=t^4.
alpha=Fraction(1,4)
coef_z = -(-alpha)  # subtract coefficient -alpha of (1-z)^alpha
assert coef_z == Fraction(1,4)

print("VERIFY_OK")
print("V4_ratio=1-t^4 exact")
print("critical_normalized_deficit=t^4/4+O(t^8)")
