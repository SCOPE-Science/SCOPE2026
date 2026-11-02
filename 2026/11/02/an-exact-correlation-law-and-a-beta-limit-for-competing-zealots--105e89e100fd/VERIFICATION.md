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

The attached `verify.py` was executed using Python's built-in `fractions.Fraction` (no floating-point tolerance). It passed 196 independently enumerated copying-event rate checks, 16 complete exact-rational invariant-distribution calculations for all \(2\le a,b\le5\), and 361 symbolic-fraction stationary-moment equation checks for \(2\le a,b\le20\). Each invariant distribution was checked against exact expectations, factorial second moments, and cross moments.

The probabilistic limit is an analytic theorem: the exact moment formulas first show the two empirical group shares synchronize in stationary mean square, while the rescaled degree-weighted share has a Jacobi diffusion limit identified by the stationary polynomial moment recurrence. Finite checking does not establish infinitely many parameters or convergence in distribution.

Reproduce with `python verify.py` after extracting this finding's files together; it reports the case counts, failing with an assertion on a discrepancy. There is no independent external audit or certification.
