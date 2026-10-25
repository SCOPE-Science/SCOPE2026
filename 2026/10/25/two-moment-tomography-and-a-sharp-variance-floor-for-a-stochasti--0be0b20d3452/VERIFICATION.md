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
# Verification of the gated-absorber inverse theorem

The analytical proof is in `RESULT.md`. To reproduce computational checks from these files, use Python with NumPy and SciPy and run `python verification/check_gated_moments.py` in the package root. The checker solves the two-state Brownian backward boundary problem by exponentiating a four-dimensional first-order coefficient matrix; it separately evaluates the closed transform, obtains moments, reconstructs both positive switching rates and checks the sharp inequality for five parameter pairs. Fifteen transform comparisons and five inverse checks passed at development time. These are finite numerical checks; strict global monotonicity and the full realizable moment region are proved analytically, not inferred from numerical samples.

There has been no independent audit. Literature-priority risk remains for an equivalent unlocated inverse derivation, particularly within broader stochastic-gating analyses.
