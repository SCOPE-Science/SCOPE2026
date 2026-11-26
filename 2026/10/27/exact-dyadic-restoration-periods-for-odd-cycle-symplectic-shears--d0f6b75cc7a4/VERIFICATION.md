---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two factors are integral symplectic shears with symmetric couplings. Modulo 2 the shift diagonalizes over a splitting field since n is odd, and the nonconstant mode with shift eigenvalue λ has distinct map eigenvalues λ and λ^(-1). A primitive n-th root forces odd part n, and the constant-mode unipotent block has order 2. The circulant Laurent representation is faithful: the matrices S^j have distinct shifts of one basis vector for 0≤j<n. In that ring, the Laurent sum for U_m hits each residue twice for m=2n and omits one exponent congruent to zero for m=2n−1. The even polynomial U_{2n−1} has zero derivative modulo 2, while differentiating U_{2n}=w U_n² modulo 2 gives U_n². Since Σ²=nΣ, shifting b to b+2 leaves U_{2n}(b+2)=0 modulo 4, and T^(2n)=I+2ΣI modulo 4. Nonzero Σ modulo 2 gives exact order 4n modulo 4. Squaring gives identity modulo 8: the unknown multiple of 4 contributes only a multiple of 8 because T^(2n)=I modulo 2, and Σ+Σ² is even. On the constant mode H has trace 4 and determinant 1, so H²=4H−I gives H⁴−I=8(2H²−H), not zero modulo 16. Raising this to odd n preserves the mod-16 obstruction, proving exact valuation three of T^(4n)−I. Squaring raises that valuation exactly by one, and raising to any odd power leaves it unchanged. Every identity exponent for higher moduli must already be a multiple of 4n, giving the claimed least exponent. This is the global order since a linear map fixes all vectors exactly when it fixes the coordinate basis.

## originality

PASS

The supported novelty is the exact all-odd-size dyadic matrix order for the unequal-shear nearest-neighbor map, especially its common mod-4 and mod-8 order and the exact onset of lifting. Equal-shear cat maps and generic matrix-order lifting are prior tools, not this order law. The closest inspected works differ in the update map or the underlying graph and size class.

## value

PASS

The recurrence order gives an exact return-to-identity time for all states of a natural spatially local symplectic torus update, uniformly in odd composite as well as prime circumference. The mod-4/mod-8 plateau distinguishes this arithmetic from automatic dyadic doubling; the uniform projector congruence explains it and the constant mode proves where it ends. This is more than an isolated numerical instance or a general lifting recipe.

The dated certificate retains the supplied scientific assessment, sources and limitations.
