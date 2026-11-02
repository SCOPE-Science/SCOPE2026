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

The exact proof derives the Gram-kernel numerator by applying the mixed differential operators to the unweighted half-plane Bergman kernel. The equivalent Fourier–Laplace integral yields the spectral density \(t[(1-bt^2)^2+a^2t^2]\), independently confirming positive definiteness and all normalizations for real parameters. The polynomial reduction and discriminant are elementary algebraic identities valid for all real coefficients, and its roots have been classified including the boundary and degenerate cases.

Run `python3 check.py` with Python's standard library. The checker reconstructs the numerator coefficients using integer factorials, verifies the discriminant at rational inputs, checks the two boundary constants, and exercises sample root counts and polynomial substitutions. Its success message is `THREE_JET_CERTIFICATE_OK`. Separate high-precision numerical quadrature of the Fourier–Laplace representation at three interior configurations agreed with the mixed derivative formula to relative discrepancy below \(4\times10^{-46}\). These are corroborative finite checks, not an infinite proof or independent mathematical audit.

Primary source material was inspected for the canonical Gram construction and the scope of its zero-free examples. Two closely related published research claims were read in full and compared at the level of their quantifiers and functional support. Their two-term settings do not imply the present three-consecutive-order coefficient cone. No exhaustive originality certification is claimed; possible unindexed work is a residual risk.
