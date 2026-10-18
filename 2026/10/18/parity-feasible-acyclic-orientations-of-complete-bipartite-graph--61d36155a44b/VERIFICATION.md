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

Run `python verify.py` with Python 3. The program constructs literal edge matrices and separately tests indegree parities and acyclicity by Kahn topological sort on the literal directed graph. The exhaustive parameter range is \(1\le a\le4\), \(a\le b\le8\), \(ab\le20\); it covers 21 graph orders and 2,390 feasible signature checks and reports `VERIFY_OK`. The proof of the unbounded theorem is the induction and column classification in `RESULT.md`; no finite census is interpreted as proving it. Independent audit has not been performed.
