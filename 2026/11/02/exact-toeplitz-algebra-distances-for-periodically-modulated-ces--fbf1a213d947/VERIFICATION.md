---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For periodic zero-mean b, (C*D_b C)_{jk}=Σ_{n≥max(j,k)} b_n/(n+1)²=O((1+max(j,k))^-2) by bounded partial sums; its Hilbert–Schmidt norm is finite. This yields C*D_|a-µ|² C=v C*C modulo compacts. Weakly-null Hardy extremizing vectors prove ||π(C)||=2, so ||π(D_(a-µ)C)||=2√v. Conjugation by the Calkin shift is a *-automorphism and cyclic averaging annihilates the periodic centered row modulation. Averaging (y+z)*(y+z) for fixed-point z eliminates both mixed terms, giving lower bound 4v for squared distance to the essential commutant. Since C and finite-ranks lie in the Toeplitz algebra, µC+P_ND_(a-µ)C achieves the limiting upper bound. One shift conjugation gives essential commutator 2√δ. Finite averaged variance/tail tests corroborate, not replace, Calkin proof. Full Hardy/Calkin and Sang inclusion explicitly needed.

## originality

PASS

Sang’s 2026 primary theorem proves C belongs to the Toeplitz algebra and provides a broader Rhaly operator membership criterion; hence qualitative nonmembership for nonconstant periodic Rhaly sequences is NOT new. The exact quantitative two-algebra distance 2√v and essential commutator 2√δ, with sharp approximants, were not found in the inspected source.

## value

PASS

A complete exact norm-distance profile of a natural periodic family to two important operator algebras is a substantive quantitative operator-algebra invariant, in contrast with binary membership and generic compactness bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
