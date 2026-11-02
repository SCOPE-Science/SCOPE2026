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

# Verification of the coordinate-correlation claim

The analytic proof holds for every integer dimension \(M\ge2\) and every nonnegative lag. The supporting standard-library script `CHECK.py` was run from its actual included content and printed `PASSED 346 independent exact partition/coboundary/adjoint identities`. It independently enumerates the forward map's rational itinerary rectangles for \(2\le M\le5\), integrates the coordinate product for \(0\le n\le9\), and verifies exact agreement with transfer-matrix powers. It additionally checks the branchwise coboundary and the conditional two-preimage cancellation for dimensions through nineteen. The script prints the exact lag-zero through lag-eight covariance values for four dimensions.

Proof-only steps that the finite checker does **not** establish include the symbolic cofactor formula for unbounded dimension, exclusion of nonzero real poles, Pringsheim's sign-change implication, and the stationary reverse-martingale central limit theorem. Those steps are explicitly justified in RESULT.md, using the published ergodicity of the map. The rational tests are a reproducibility check rather than an external mathematical audit. In particular, no independent validation is claimed.
