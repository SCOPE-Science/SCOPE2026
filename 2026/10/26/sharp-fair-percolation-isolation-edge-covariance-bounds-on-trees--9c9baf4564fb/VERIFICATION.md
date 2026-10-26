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

# Reproducibility

Run `python verify.py` with Python 3.9 or later. The script uses only the standard library and exact rational arithmetic. A successful run terminates with `VERIFY_OK`.

The program enumerates integer partitions of \(n-2\), corresponding bijectively to nondecreasing feasible tree degree multisets. For every multiset with \(2\le n\le10\), a Prüfer word constructs one realizing tree; all \(2^{n-1}\) retention outcomes are explicitly enumerated, and their exact covariance is compared with \(-\tfrac12\sum_v d_v2^{-d_v}\). For every degree multiset with \(2\le n\le16\), exact profile covariances are compared with both sharp extremal values and, when \(n\ge5\), the complete predicted equality classes. A separate dynamic program independently optimizes hub profit for every order through \(120\) and compares it with the closed four-residue formula.

These tests are finite; the all-orders validity and uniqueness statements rely on the explicit exchange proof in `RESULT.md`. The code does not inspect any outside database and does not constitute an independent audit.
