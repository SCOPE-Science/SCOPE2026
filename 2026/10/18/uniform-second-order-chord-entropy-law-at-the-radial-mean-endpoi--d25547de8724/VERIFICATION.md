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

`checks/verify.py` uses Python 3 standard-library `math` functions and executes four groups of checks: exact beta/gamma cone envelopes over 18 dimensions; second-order cone coefficients; the disk chord formula and its nonextremal behavior; and the prism and diagonal-square equality models for multiple parameters. It checks numerical identities but does not certify an infinite theorem. The general proof is given in `RESULT.md`, including quantitative sublevel and Taylor bounds.

The linearized volume coefficient is a direction-integral, not a sampled approximation. The remainder constant is existential and uniform for fixed dimension, not optimized. No independent scientific audit has been performed.
