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

The independently recomputed rational long-gap-mask probabilities yield exactly the covariance formula for every tested stratum: 20 combinations of \(n=4,\ldots,8\) and \(r\in\{1/12,1/5,1/3,2/5\}\), totaling 1,984 binary masks. All mass functions are nonnegative and normalize to one. Four fixed-density sparse-limit numerical diagnostics passed. Run `python3 verify.py` with Python 3 and its standard library.

The universal proof is the included simplex translation argument, overlap classification, and explicit asymptotic expansion; verification of a finite list of cases is not a substitute. Independent mathematical auditing was not performed.
