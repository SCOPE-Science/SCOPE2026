from fractions import Fraction as F
from itertools import product

# Regular tetrahedron represented by integer vectors divided by sqrt(3).
V = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
M = [[sum(F(v[i]*v[j],3) for v in V) for j in range(3)] for i in range(3)]
assert M == [[F(4,3) if i==j else F(0) for j in range(3)] for i in range(3)]
G = [[x/F(4) for x in row] for row in M]
assert G == [[F(1,3) if i==j else F(0) for j in range(3)] for i in range(3)]
assert F(1,8)*(1-F(1,3)) == F(1,12)

w1=(1,1,-1,-1)
w2=(1,-1,1,-1)
max_norm2=F(0)
max_sum_indicator=False
for s in product((1,-1), repeat=4):
    # Equality-class Gram matrix H_ab = 1 on diagonal, -(s_a s_b)/3 off diagonal.
    H=[[F(1) if a==b else -F(s[a]*s[b],3) for b in range(4)] for a in range(4)]
    for w in (w1,w2):
        q=sum(F(w[a])*H[a][b]*F(w[b]) for a in range(4) for b in range(4))
        d=sum(w[a]*s[a] for a in range(4))
        assert q == F(16,3)-F(d*d,3)
        assert q <= F(16,3)
        max_norm2=max(max_norm2,q)
    if sum(w1[a]*s[a] for a in range(4))==0 and sum(w2[a]*s[a] for a in range(4))==0:
        max_sum_indicator=True
assert max_norm2 == F(16,3)
assert max_sum_indicator
# Strict ceiling comparison: 1/sqrt(3) < 1/sqrt(2), equivalent for positives to 1/3 < 1/2.
assert F(1,3) < F(1,2)
print('VERIFY_OK')
