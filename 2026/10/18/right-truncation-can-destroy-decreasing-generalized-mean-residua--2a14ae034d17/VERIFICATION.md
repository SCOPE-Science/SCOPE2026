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

# Verification and limitations

Run `python3 verify.py` with a standard Python 3 interpreter. The executable script verifies the strict rational certificate derived from the first three terms of the alternating logarithm series:
\[
\log(5/4)<43/192,\qquad 11-48\log(5/4)>1/4.
\]
It also recomputes \(T\), the truncated mean residual life at age \(1\), and the left- and right-hand derivatives to 70 decimal digits, and checks a short increasing sequence of truncated generalized mean residual life values approaching the age switch from below.

The proof of decrease on all ages for the original lifetime and the exact local failure for its right truncation appears in `RESULT.md`. Finite diagnostics are not treated as a substitute for the analytic all-ages argument. The counterexample covers conditional right truncation, not right censoring; no claim of independent proof audit or exhaustive literature priority validation is made.
