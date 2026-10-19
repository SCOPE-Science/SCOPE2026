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

# Computational and analytic verification

Execute `python3 verify.py` with Python 3 (standard library only) in the directory containing this file. The checker tests the exact identities \(c=-\alpha(1-\alpha\beta)/r\), \(\eta=(1-\alpha\beta)^2/2+\alpha\beta(1-\alpha\beta)/r\), and \(\eta\)'s induced reciprocal coefficient at four rational parameter triples. It then iterates the full, untruncated planar recurrence to times \(120{,}000\) and \(240{,}000\) to compare its two-scale reciprocal logarithmic slope with the predicted parameter expression.

The four parameter sets include both possible signs of the logarithmic coefficient and its exact cancellation case. All assertions passed when run on the packaged code. These finite tests do **not** certify the infinite-time limit or novelty; those depend on the symbolic proof and the published global convergence theorem identified in RESULT.md. In particular, the approximate two-scale slope has finite-time error, and numerical tests are not used to establish the existence of the limiting offset.
