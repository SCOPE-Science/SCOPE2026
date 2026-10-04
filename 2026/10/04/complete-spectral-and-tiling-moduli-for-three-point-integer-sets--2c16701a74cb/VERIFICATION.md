---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof is analytic and exact. The critical steps are: (1) three unit complex numbers summing to zero must be the cube roots of unity up to a common factor; (2) coprimality and Bézout reduce every unit-circle zero to a primitive cube root; (3) the three pairwise differences of a normalized three-point spectrum force one frequency from each nonzero residue family; (4) any primitive integer tiling complement satisfies an invertible finite-state recurrence and is therefore periodic; (5) on a finite period, the tile mask has only the two primitive-cube-root zeros, forcing the complement indicator to be three-periodic; and (6) gcd residue fibers are independent.

The accompanying standard-library checker exhaustively verifies the spectral formula for bounded coprime primitive pairs and the tiling-complement count in finite quotients for \(1\le g\le 6\). Its output is included separately. These computations are finite sanity checks only and do not certify the infinite theorem.
