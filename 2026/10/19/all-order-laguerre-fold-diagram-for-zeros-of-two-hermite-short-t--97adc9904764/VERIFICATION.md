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

Completing the square in the defining integral and introducing physicists' Hermite generating variables u,v yields the normalized Gaussian/phase prefactor times exp(sqrt(2) z u-sqrt(2) conjugate(z) v+2uv). With the stated normalization, the coefficients for (n,0) and (n,n) are z^n/sqrt(n!) and L_n(s). Since P(0)=t and the imaginary part off zero is r^n sin(n theta)/sqrt(n!), the listed rays are exhaustive. With R=s^(-n/2)L_n(s), its derivative numerator H=2sL_n'-nL_n has degree n, is negative at zero, and is positive at negative infinity. Rolle gives n-1 distinct gap roots; the negative root exhausts the degree, making every gap root simple, with none in the two outer intervals. This includes n=1. The outer limits are +infinity at zero and signed infinity at infinity. Each nonzero horizontal level has the required n rays of the opposite parity to the sign of R, and each inner gap can only meet its level twice, touch, or miss it. Disjoint radii make coincidences additive. At a zero, angular differentiation of the imaginary part is nonzero, while the real radial derivative has the sign of R'; the oriented determinant has the stated additional ray sign. The outer populations are opposite and an inner pair has opposite indices. At a stationary zero the second radial derivative and the parameter derivative L_n(beta) are nonzero, giving a rank-one fold with zero local degree. For n=2, H=s^2-2 and direct substitution gives the exact threshold and 4/6/8 counts.

## originality

PASS

Credit the known complex-Hermite transform, ordinary Laguerre roots and general local fold mechanism. The distinct supported contribution is the complete deterministic Laguerre-gap count and thresholds, with indices and simultaneous folds, for this prescribed input/window family. The strongest available comparisons differ on the actual radial function, assumptions, or invariant; no dominating statement was identified in the bounded check.

## value

PASS

At fixed Hermite order the positive mixing amplitude changes the number of isolated Gabor zeros from 2n to 2n². Exact cutoffs and the degeneracy and orientation at each transition provide substantially more than generic finiteness or a numerical example, and determine when a reader studying this standard window perturbation gains or loses phase singularities. Coincident thresholds are covered without a distinctness conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
