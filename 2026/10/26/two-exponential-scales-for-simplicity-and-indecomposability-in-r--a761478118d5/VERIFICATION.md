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

The standalone `check.py` script was run directly with Python 3 and returned `VERIFY_OK` for exhaustive prime-field cases \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,2),(3,3)\). It calculates field determinants by row elimination, builds support digraph reachability directly from each enumerated matrix, verifies the exact labelled connectivity recurrence, and verifies the exact one-way zero-cut incidence and isolated-vertex formulas. Its largest full enumeration contains all \(20160\) invertible \(4\times4\) binary matrices.

The proof for all dimensions and all prime-power fields is the block-matrix and union-bound argument in `RESULT.md`. The checker treats prime fields only; it does not independently implement extension-field arithmetic. The algebraic proof uses only finite-field cardinality identities and is valid for any prime power. No infinite statement is inferred solely from the finite tests.
