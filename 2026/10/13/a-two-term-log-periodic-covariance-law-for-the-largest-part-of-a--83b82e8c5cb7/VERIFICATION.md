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

Run `python artifacts/verify.py` with standard Python 3; there are no external package dependencies. It enumerates all \(2^n\) fair separator strings for each \(1\le n\le12\), computes exact rational covariances directly, and checks them against separately implemented exact rational derivatives of the generating-function recurrence. It also checks three larger \(n\) values (100, 1000, 10000), comparing numerically evaluated recurrence covariances with the explicit periodic asymptotic expansion. Expected output ends with `VERIFY_OK 15 tests plus 8190 enumerated bitstrings`.

The following proof steps—not the finite tests—establish the infinite theorem: exact product-measure derivative; avoidance rational generating function; isolation of its simple pole and differentiation uniformly for \(r=\log_2n+O(\log\log n)\); disjoint-block and pivotality tail estimates; and periodization/Fourier calculation. The numerical thresholds are corroborative and do not certify the asymptotic remainder. No independent scientific audit has been performed.
