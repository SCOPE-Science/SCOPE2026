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

# Reproducibility and limits

Run the included standard-library Python script with `python verify_boolean.py`. This directly checks deterministic-grain closed forms, two independent expressions for the covariance density for finite-atomic length laws, higher-order coefficient inequalities, numerical sign bracketing, and ordered grain-law examples. The run recorded 322 successful comparisons and gives the four mean-one critical intensities reported in the result.

The script performs finite numerical checks only. The proof of existence of the limiting covariance density uses the marked Poisson Mecke identity and integrability of the conditional occupancy kernel. The proof of a unique intensity zero uses a sign-definite entire power series. Convex-order monotonicity is established by the stop-loss characterization of convex order; it is not inferred from numerical sampling. No independent audit or external proof certification has been performed.
