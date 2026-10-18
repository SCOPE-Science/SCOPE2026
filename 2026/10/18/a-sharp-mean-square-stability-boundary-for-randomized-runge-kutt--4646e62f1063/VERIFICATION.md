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

The standalone `verify.py` was run from its own directory under Python 3 with SymPy 1.14 and mpmath. It completed 24 exact symbolic assertions and printed the unique isolated root numerically; see `verification_output.txt`. Its checked objects are the full six-coordinate covariance recurrence, factorization of \(\det(I-M(s))\), complete Sturm sign-variation counts, exact rational instability witness, deterministic central-stage Routh inequality, and the positive covariance increment from stage variance. The high-precision root is supplementary: exact crossing uniqueness follows from the Sturm counts and the analytic cone argument in `RESULT.md`.

The verification does not furnish independent mathematical peer review, a machine-checked proof of the positive-map Perron theorem, or an exhaustive search of historical literature. Those mathematical steps and scientific limitations are explicitly given in `RESULT.md`.
