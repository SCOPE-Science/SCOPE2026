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
# Verification notes

The analytical generator proof, the time-dependent forced covariance equation, and the discrete convexity equality cases were checked against the definitions. The standard-library program `verify.py` independently enumerates uniform subsets for tested finite parameters, verifies fixed-batch limiting formulas, and checks temporal order on finite test grids. It does not exhaust arbitrary distributions, times, or particle counts; the proof handles those quantifiers. Check the exact decoded file with `python verify.py`.

The accepted result is specific to squared-position pair correlations for independent Brownian particles, with i.i.d. batch size draws and initially zero coordinates. The pre-existing fixed-size formula is treated as prior work, not a new contribution.
