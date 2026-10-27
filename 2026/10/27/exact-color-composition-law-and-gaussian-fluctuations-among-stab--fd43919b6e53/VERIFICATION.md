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
The included `verify.py` runs a direct synchronous-majority fixed-point test for each of the \(2^n\) profiles on cycles \(3\le n\le16\), independently evaluates the run-composition binomial sum, and independently builds and traces the four-state weighted transition matrix. All computed coefficients agreed. The finite checks support, but do not establish, the central limit theorem; its proof uses analytic spectral perturbation and the Perron gap. Eigenvalue first and second derivatives were independently evaluated symbolically.
