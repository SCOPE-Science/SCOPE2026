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

# Verification and reproducibility

The mathematical proof uses a stationary velocity-resolved telegraph resolvent, Poisson-thinning of anchors, and an independent-reset renewal decomposition. Symbolic algebra of the rational square-root transform establishes its zero-lag and stationary-lag limits. The inverse Laplace branch expansion establishes the exact long-lag coefficient. The included `check_cov.py` independently estimates the covariance directly from regenerative telegraph trajectories, and compares these estimates to high-precision inverse Laplace values with explicitly reported sampling uncertainty. The numerical experiment is finite and cannot certify general positive parameters or infinite time. Model parameters and random seed appear in the checker itself.
