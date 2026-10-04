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

The proof is analytic. The checks below reproduce the algebraic constant and finite numerical sanity tests without substituting computation for the limiting argument.

- Recompute \(p_{\mathrm{sil}}=\log_2(1+\sqrt2)\).
- Verify \(2\rho^{-1}+\rho^{-2}=1\) for \(\rho=1+\sqrt2\).
- Differentiate the balanced quotient \(4(1-2^{1-p}-2^{-2p})\) and verify the derivative at the silver exponent equals \(8\log2(\rho^{-1}+\rho^{-2})\).
- Numerically minimize the quotient on a dense symmetric grid for several shrinking positive exponent offsets and confirm that the minimizer is at the balanced split to grid resolution and that the normalized slack approaches the analytic constant.

The numerical grid is not exhaustive evidence for the infinite statement. Correctness of the limit comes from the compactness, equality-classification, monotonicity, and mean-value argument in `RESULT.md`.
