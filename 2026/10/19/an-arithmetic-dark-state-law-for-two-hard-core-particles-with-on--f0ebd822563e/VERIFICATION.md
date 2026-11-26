---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the ordered hard-core basis no allowed hop crosses the particles, so H is the restriction of H₁⊗I+I⊗H₁ to the antisymmetric product. The sine-mode determinants at the sink have nonzero sine factors and a nonzero difference of cosines. For prime p, writing 2 cos(πk/p)=(-1)^k(ζ^(uk)+ζ^(−uk)), u=(p+1)/2, gives disjoint nonzero residue pairs for 1≤k≤(p−1)/2. A rational relation would be a polynomial of degree at most p−1 with zero constant coefficient divisible by 1+X+···+X^(p−1), hence is zero. Consequently nonzero two-mode sums are simple, and zero has exactly the complementary-mode multiplicity (p−1)/2; the single sink removes one dimension. For the zero-energy projector, sine products vanish on even i+j. On odd i+j use g=j−i and d=i+j; the product with the sink is (cos(gθ)−cos(dθ))(cos θ−cos(3θ))/4 before summing θ=πk/p. Product-to-sum uses even integral frequencies whose half-sums are (p·1_{2p divides frequency}−1)/2. The constants cancel, giving exactly the three indicators in B; the squared-sine sum leaves the extra term only at i+j=p. Subtracting the normalized rank-one projector for Q|1,2⟩ therefore gives the displayed diagonal. The dark subspace reduces the dissipative Hamiltonian; taking imaginary parts in its eigenvector equation excludes any real eigenvalue on the complementary block, so polynomial Jordan prefactors do not prevent decay. This proves rate-independent eventual survival. As a separate finite check, independent_dark_kernel.py constructs the integer hopping matrix from allowed moves, appends the sink constraint, computes a rational nullspace basis U, and compares the diagonal of U(UᵀU)^(-1)Uᵀ exactly at primes 5,7,11,13,17,19 (405 states). This checks the projector evaluation, not simplicity of all other energies; that follows from the prime proof. The frozen verify.py and its recorded numerical evidence were inspected without executing the uploaded code.

## originality

PASS

General dark subspace and hard-core path methods are credited. The surviving distinct result is the evaluated prime-family projector for a single occupied adjacent bond in the hard-core sector, giving both protected dimension and a closed probability for every localized pair and all positive loss rates.

## value

PASS

This is a natural canonical trap on the two-particle configuration graph. The exact survival profile supplies information not contained in dark-state existence: it resolves which localized pairs can retain population, the arithmetic dependence on the path size, and explicit boundary and parity effects. It gives an all-size, all-loss-rate reference for localized annihilation; the underlying general projection principle alone does not provide these probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
