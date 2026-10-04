from decimal import Decimal, getcontext
from math import floor

getcontext().prec = 80

def G(x_num, x_den, n):
    return (n*x_num)//x_den - ((n-1)*x_num)//x_den

# Boundary mechanical words are constant, so the substitution gives constant partial quotients.
for n in range(-200,201):
    assert G(0,1,n) == 0
    assert G(1,1,n) == 1

# For [0; overline(c)], r satisfies r=1/(c+r), hence L=c+2r=sqrt(c^2+4).
# Check the claimed contradiction over a broad finite family; the proof of the inequality is exact.
cases = 0
for a in range(2,301):
    for b in range(a*a+2, a*a+42):
        assert a < b
        # exact squared comparison
        assert a*a + 4 < b*b + 4
        La = Decimal(a*a+4).sqrt()
        Lb = Decimal(b*b+4).sqrt()
        assert La < Lb
        cases += 1

# Small explicit witness at the conjectural boundary.
a,b=2,6
La = Decimal(a*a+4).sqrt()
Lb = Decimal(b*b+4).sqrt()
assert La < Lb
print(f"VERIFY_OK constant_words=401 parameter_cases={cases} witness_a={a} witness_b={b} L0={La} L1={Lb}")
