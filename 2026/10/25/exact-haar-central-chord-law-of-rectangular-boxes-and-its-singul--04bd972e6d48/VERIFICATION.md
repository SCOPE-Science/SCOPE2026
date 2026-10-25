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

# Reproducibility checks

Run `python3 verify.py` from the folder containing the standalone script. It requires only Python 3's standard library. The deterministic computation checks the closed two-cap overlap against an independent one-dimensional integral, tests the exact law against Gaussian-normalized uniformly random directions for several positive box aspect ratios, and compares threshold and endpoint coefficients at decreasing distances. The terminal marker is `VERIFY_OK`.

The mathematical proof requires none of these finite checks: its infinite-parameter content is established by exact spherical integration, finite inclusion–exclusion, a local quadratic-form rescaling and the Dirichlet endpoint density. Numerical estimates are not exhaustive, and their tolerances are explicitly encoded in the script. Scientific historical-priority limitations are recorded in RESULT.md and REVIEW.md; an independent audit has not been performed.
