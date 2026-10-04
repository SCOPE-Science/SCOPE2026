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

The symbolic proof in `RESULT.md` is the evidence for the infinite theorem. The executable check is deliberately finite and serves as a regression test of the definition, formula, and construction.

`verify.py` enumerates every nondecreasing complete-multipartite profile with at least three parts and total order from \(3\) through \(10\). For each profile it enumerates every allowed label vector whose total weight is at most \(\lceil(N+m)/2\rceil\), evaluates the strong Roman condition directly, confirms that the least feasible weight equals the theorem, and independently checks the explicit construction supported on a smallest part.

The finite census does not establish the theorem for larger orders and is not used as a substitute for the lower-bound proof. It does, however, exercise all parity patterns and many unequal part profiles in the stated domain.
