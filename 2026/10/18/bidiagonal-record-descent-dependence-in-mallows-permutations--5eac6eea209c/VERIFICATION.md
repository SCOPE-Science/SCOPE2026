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

# Reproducibility and scope
Run `python3 verify.py` in a directory containing this file and the standalone checker. The checker has no third-party dependencies. For each \(2\le n\le7\) and \(q\in\{1/2,1,2\}\), it enumerates every permutation with exact rational weight, calculates all upper-record and descent indicator expectations, compares every cross-covariance matrix entry to the asserted closed form, and checks both the aggregate covariance and its negative sign. It also checks the \(q=1\) telescoped value. The expected final line is `ALL_RECORD_DESCENT_CHECKS_PASS`.

This is a finite consistency check only. The unrestricted statement follows from the independent prefix insertion-rank representation and the analytic covariance calculation in `RESULT.md`; no numerical tolerance, Monte Carlo estimate, or unproved exhaustive extension is used. No independent external audit or proof certification is asserted.
