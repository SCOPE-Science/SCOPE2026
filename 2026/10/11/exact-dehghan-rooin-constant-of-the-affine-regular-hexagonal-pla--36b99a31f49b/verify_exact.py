from fractions import Fraction as F

# The six permutations of (0,s,1), grouped by the proof's symmetries.
permutations = {
    (0, 1, 2): "identity",
    (2, 1, 0): "reversal",
    (0, 2, 1): "transposition",
    (1, 0, 2): "transposition",
    (1, 2, 0): "cycle",
    (2, 0, 1): "cycle",
}
assert len(permutations) == 6
assert sorted(permutations.values()).count("identity") == 1
assert sorted(permutations.values()).count("reversal") == 1
assert sorted(permutations.values()).count("transposition") == 2
assert sorted(permutations.values()).count("cycle") == 2

# Exact maximum certificate for F(q)=q(2-q)^2 on 0<q<=1.
q = F(2, 3)
Fmax = q * (2 - q) ** 2
assert Fmax == F(32, 27)
# Polynomial identity: 32/27 - q(2-q)^2 = (8-3q)(3q-2)^2/27.
for z in [F(1,100),F(1,4),F(1,2),F(2,3),F(3,4),F(1,1)]:
    lhs = F(32,27) - z*(2-z)**2
    rhs = (8-3*z)*(3*z-2)**2/F(27,1)
    assert lhs == rhs and lhs >= 0

# Equality configuration in triple/range coordinates.
def rng(t):
    return max(t)-min(t)
U=(F(0),F(0),F(1))       # u=(0,1)
V=(F(0),F(1),F(2,3))     # v=(1,2/3)
assert rng(U)==1 and rng(V)==1
num = rng(tuple(U[i]-V[i] for i in range(3)))
den_sq = F(3,2)           # N(a u-a^{-1}v)^2 at a^2=2/3
assert num == F(4,3)
ratio_sq = num*num/den_sq
assert ratio_sq == F(32,27)

print("VERIFY_OK")
