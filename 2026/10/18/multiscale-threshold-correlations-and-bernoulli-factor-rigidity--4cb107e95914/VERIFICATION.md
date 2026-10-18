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

# Verification and limits

The analytical proof derives each orbit covariance by counting all complete inverse branches plus the unique partial branch. The all-order IID conclusion follows from repeated transfer of branch-union indicators, not merely pairwise covariance checks.

An exact-rational checker (`verify.py`) reconstructed the two-time overlap separately from the closed expression for degrees 2–8 at lags 1–3, checked rational threshold boundaries and the exponential bound, and enumerated every binary word of lengths 2–4 at each nontrivial q-grid threshold. It printed `VERIFY_OK`. This finite verification is not an exhaustive argument for arbitrary degree, lag, or word length.

The contribution is restricted to the invariant arcsine law and ordinary Chebyshev maps. Direct reading of the accessible 2013 coarse-graining preprint PDF was not possible, so further bibliographic comparison may be warranted. Independent audit has not been performed.
