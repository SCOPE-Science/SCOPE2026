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

# Verification methods and limits

Run `python3 verify.py` with the standard Python 3 library. The checker has no external file dependencies.

The checker forms each crown graph directly from the rule \(a_i b_j\in E\) if and only if \(i\ne j\). It forms each original edge's closed edge neighborhood, tests domination by union of those neighborhoods, and tests inclusion-minimality by deletion of every chosen edge. Across \(n=2,3,4,5\), this exhausts 1,052,740 edge subsets. The exact size distributions are:

- \(n=2\): \(z^2\).
- \(n=3\): \(3z^2+2z^3\).
- \(n=4\): \(8z^3+117z^4\).
- \(n=5\): \(45z^4+1824z^5+20z^6\).

A separate exact-arithmetic evaluator implements the formal coefficient expression by truncated bivariate formal power series, and independently enumerates spanning star forests for \(t\le4\). Coefficient endpoints are additionally checked for \(3\le t\le8\). A successful run prints `VERIFY_OK`.

The finite tests corroborate the classification, the unusual one-hole boundary, and the coefficient extraction, but they do not prove the infinite-parameter theorem. The mathematical proof is provided in `RESULT.md`. Publication priority and independent mathematical validation remain unperformed.
