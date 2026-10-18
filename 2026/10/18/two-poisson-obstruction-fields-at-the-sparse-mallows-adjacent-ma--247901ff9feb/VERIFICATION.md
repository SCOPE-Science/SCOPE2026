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

The included `verify.py` uses the Python standard library only. Its exact checks enumerate permutations up to size eight and verify the inversion-code encoding, the absence-of-defects characterization, the weighted path-matching identity, and normalization at three rational values of the parameter. Additional numerical checks compare an independent logarithmic expression with exact partition-function values and test critical-scale asymptotic errors.

Run `python3 verify.py` in the same directory. No stochastic seed or external data are used. The finite checks cannot establish the all-size theorem, the uniform remainder, the weak convergence of point measures, or historical priority; those depend on the accompanying analytic arguments and source comparison.
