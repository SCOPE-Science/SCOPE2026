"""Torsion-freeness of J(Q) from the two verified Jacobian orders.
Run: python3 torsion_trivial.py
Uses: #J(F5)=71, #J(F11)=136 (recomputed in counts.py by exact F_{p^2}
enumeration; re-asserted here as integer inputs with factor checks).
Lemma (reduction injectivity on prime-to-p torsion): for good p, the kernel
of J(Q)->J(Fp) is a pro-p group, so any prime-to-p divisor of |J(Q)[tors]|
divides #J(Fp).
Proof coded: let n = |J(Q)[tors]| (finite). Any prime l|n with l not in {5,11}:
  l-part of n divides both 71 and 136 (apply lemma at p=5 and p=11), hence
  divides gcd(71,136)=1, impossible. So n = 5^a*11^b. If a>=1: reduce mod 11;
  the 5-part injects (5 != 11) into J(F11) of order 136 = 8*17, but 5 not |
  136, so a=0. If b>=1: reduce mod 5; 11-part injects into J(F5) of order 71
  (prime != 11), so 11^b | 71, impossible; b=0. Hence n=1: J(Q) torsion-free.
Prints TORSION_TRIVIAL_OK.
"""
from math import gcd

def main():
    J5, J11 = 71, 136
    assert J5 == 71 and J11 == 136
    # factor checks (exact)
    assert J5 not in (0, 1) and all(J5 % k for k in range(2, J5))
    tmp = J11
    fac = {}
    for q in [2, 3, 5, 7, 11, 13, 17]:
        while tmp % q == 0:
            fac[q] = fac.get(q, 0)+1
            tmp //= q
    assert tmp == 1, tmp
    print("factorizations: 71 prime;", "136 =", fac)
    assert fac == {2: 3, 17: 1}
    g = gcd(J5, J11)
    print("gcd(71,136) =", g)
    assert g == 1
    # prime-divisor elimination (finite check over candidate primes)
    # any l | n, l not in {5,11}: l-part | gcd = 1 -> contradiction
    print("l-part argument: l not in {5,11} divides both orders -> divides 1.")
    # exponent elimination
    assert J11 % 5 != 0  # so 5^a | 136 impossible for a>=1
    assert J5 % 11 != 0  # so 11^b | 71 impossible for b>=1
    print("5 not | 136 -> a=0; 11 not | 71 -> b=0. n=1.")
    print("TORSION_TRIVIAL_OK")

if __name__ == "__main__":
    main()
