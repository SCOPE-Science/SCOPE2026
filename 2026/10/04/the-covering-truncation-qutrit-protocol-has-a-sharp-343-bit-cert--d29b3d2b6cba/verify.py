from fractions import Fraction as F

# Candidate parameters.
s = F(7,120)                 # r^2
L = F(32,45)
U = F(23,30)
eta = 12*s*s*(U-L)
assert U == 1-4*s
assert F(2,3) < L < U
assert eta == F(49,21600)

# Cover cardinality from K <= (2/r)^4 = 16/s^2.
K_real = 16/(s*s)
K = K_real.numerator // K_real.denominator
assert K_real == F(230400,49)
assert K == 4702

# Binary truncation condition.
base = 1 - (1-eta)/18
assert base == F(388800-21551,388800)
delta107 = base**107
assert delta107 < eta
N = 107

# Multi-outcome positivity.  For alpha in [L,U], beta <= 1-L and
# W >= (1-3 beta)/(1-beta) >= (3L-2)/L.
q = (3*L-2)/L
assert q == F(3,16)
eps = F(3,4)**27
assert eps < eta*q
assert eps < F(1,4)
n = 27

# 343-bit upper bound.
dim = K*(N+K)**n
assert dim < 2**343
assert dim >= 2**342

# Global lower bound N >= 97 for every admissible member of the same family.
# eta <= max_{0<s<1/12} 4 s^2(1-12s) = 1/243.
eta_max = F(1,243)
# g(eta)=((17+eta)/18)^96-eta is decreasing on [0,1/243]:
# its derivative is <= (16/3)(19/20)^95 - 1 < 0.
assert F(16,3)*F(19,20)**95 < 1
assert ((17+eta_max)/18)**96 > eta_max

# Any admissible t=eta*q obeys t <= 1/1536, hence n >= 26.
assert F(1,1536) < F(3,4)**25

# Exact helper for T(s0) < (3/4)^n, where T is the maximum of eta*q
# over L for fixed s.  T(s)=12 s^2(3A+2-2 sqrt(6A)), A=1-4s.
# If C-e>0, squaring is equivalence because both sides are positive.
def T_less_eps(s0, n0):
    A = 1-4*s0
    C = 12*s0*s0*(3*A+2)
    D = 24*s0*s0
    e = F(3,4)**n0
    z = C-e
    if z <= 0:
        return True
    return z*z < D*D*6*A

# T is decreasing for s >= 6/125.  Set y=sqrt(6(1-4s));
# T=((6-y^2)(y-2))^2/96 and h'(y)=-3y^2+4y+6.
# At s=6/125, y^2=606/125 < (221/100)^2 and h'(221/100)>0.
assert F(606,125) < F(221,100)**2
assert -3*F(221,100)**2 + 4*F(221,100) + 6 == F(1877,10000) > 0

thresholds = [
    (26, F(6,125), 6944),
    (27, F(293,5000), 4659),
    (28, F(8,125), 3906),
    (29, F(27,400), 3511),
]
for nn, s0, Kmin in thresholds:
    assert s0 >= F(6,125)
    assert T_less_eps(s0, nn)
    # If an admissible member had copy count nn, then t>(3/4)^nn,
    # so monotonicity forces s<s0 and hence floor(16/s^2)>=Kmin.
    assert F(16,1)/(s0*s0) > Kmin
    assert Kmin*(Kmin+97)**nn > 2**342

# For n >= 30, s<1/12 implies floor(16/s^2)>=2304.
assert 2304*(2304+97)**30 > 2**342

print('VERIFY_OK')
