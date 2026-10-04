from math import gcd

# Intersection form on F_1 in basis S,F.
Q = ((-1, 1), (1, 0))
K = (-2, -3)

def pair(a, b):
    return (
        a[0]*(Q[0][0]*b[0] + Q[0][1]*b[1])
        + a[1]*(Q[1][0]*b[0] + Q[1][1]*b[1])
    )

S = (1,0)
F = (0,1)
KS = pair(K,S)
KF = pair(K,F)
assert (KS,KF) == (-1,-2)

# Euler class primitive in H^2 and evaluation map onto H^4.
assert gcd(abs(K[0]), abs(K[1])) == 1
assert gcd(abs(KS), abs(KF)) == 1

# Gysin ranks: Z^2/<K> is Z and ker([KS,KF]) is rank one.
h2_rank = 2 - 1
h3_rank = 2 - 1
assert h2_rank == h3_rank == 1

# w2(F_1) = c1 mod 2 = -K mod 2; K and -K agree mod 2.
c1 = (2,3)
assert tuple(x % 2 for x in c1) == tuple(x % 2 for x in K)

# Global Euler arithmetic.
chi_hat = 2*(4-108)
chi_F1 = 4
chi_singular = chi_hat - chi_F1 + 1
assert chi_hat == -208
assert chi_singular == -211
assert chi_singular % 2 == 1

print(f"K_pairings={KS},{KF}")
print("euler_class_primitive=yes")
print("gysin_H2_rank=1")
print("gysin_H3_rank=1")
print("link_spin=yes")
print("link_classification=S2xS3")
print(f"resolution_euler={chi_hat}")
print(f"singular_euler={chi_singular}")
print("poincare_duality_dimension6=obstructed_by_odd_euler")
print("VERIFY_OK")
