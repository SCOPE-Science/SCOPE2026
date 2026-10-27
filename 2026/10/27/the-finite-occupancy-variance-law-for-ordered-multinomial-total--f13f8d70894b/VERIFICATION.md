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

The standalone Python 3 standard-library checker `check_sparse_variance.py` was executed directly. Its output `check_sparse_variance_output.txt` reports 90 successful assertions, covering exact small finite multinomial enumeration, local moment identities, the score/Bessel formula, several proportional-occupancy covariance approximations, and both coefficient boundary checks. The computation uses finite sums and floating-point approximations; it does not establish infinite limits or the uniform error term. Those are justified by the weighted fixed-dimensional Poisson expansion in the mathematical proof. Re-run with `python check_sparse_variance.py` from a directory containing this document and the checker. No independent mathematical audit has been performed.
