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

# Reproducible scientific verification

Use the included `verify_minimal_separation.py` with Python 3.8 or later; it uses no external dependencies. Its terminal `VERIFY_OK` is reached only after every asserted condition succeeds. The script enumerates every preorder and every accessibility relation for one and two worlds, checks the four relational inclusion conditions, and compares the entire four-operator truth-set tables over every upset. The one/two-world table-signature census proves the finite universal lower bound; it is not a sampling exercise.

For each three-world pair, the checker verifies all required confluences, exactly one added edge, complete equality of the other three operator tables, and discrepancy at the input \(\{2\}\). Expected 2-world relation counts for every omission, by four preorder shapes, are \(16,6,6,8\). The symbolic structural-induction step for arbitrary-depth formulas appears in `RESULT.md`; a finite executable cannot independently certify an unbounded induction. No independent audit has been carried out.
