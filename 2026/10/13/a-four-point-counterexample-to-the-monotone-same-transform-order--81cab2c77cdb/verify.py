from fractions import Fraction
from itertools import product


def corr_same(values):
    pairs = [(values[min(t)-1], values[max(t)-1]) for t in product(range(1,5), repeat=3)]
    n = Fraction(len(pairs), 1)
    ex = sum(x for x, _ in pairs) / n
    ey = sum(y for _, y in pairs) / n
    ex2 = sum(x*x for x, _ in pairs) / n
    ey2 = sum(y*y for _, y in pairs) / n
    exy = sum(x*y for x, y in pairs) / n
    vx = ex2 - ex*ex
    vy = ey2 - ey*ey
    cov = exy - ex*ey
    assert vx == vy
    return cov / vx

raw = corr_same([Fraction(1), Fraction(2), Fraction(3), Fraction(4)])
assert raw == Fraction(41,143)

a = Fraction(7,20)
witness = corr_same([Fraction(0), a, 1-a, Fraction(1)])
assert witness == Fraction(1817,6335)
assert witness - raw == Fraction(96,905905) > 0

# Polynomial identity for q(a)-41/143.
# q(a)=(-7a^2+4a+4)/(95a^2-68a+28).
# Cross-multiplication must equal -96(3a-1)(17a-6).
# Coefficients are listed in ascending powers.
def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,pi in enumerate(p):
        for j,qj in enumerate(q):
            out[i+j]+=pi*qj
    return out

def sub(p,q):
    m=max(len(p),len(q)); out=[0]*m
    for i in range(m):
        out[i]=(p[i] if i<len(p) else 0)-(q[i] if i<len(q) else 0)
    return out

num=[4,4,-7]
den=[28,-68,95]
lhs=sub([143*c for c in num],[41*c for c in den])
rhs=[-96*c for c in mul([-1,3],[-6,17])]
assert lhs==rhs

# Derivative numerator identity: n'd-nd' = 96(a^2-12a+4).
np=[4,-14]
dp=[-68,190]
der_num=sub(mul(np,den),mul(num,dp))
assert der_num == [384,-1152,96,0]

print('VERIFY_OK', raw, witness, witness-raw)
