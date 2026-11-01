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

## Reproduction
Run `python verify_symbolic.py --write-tables` and `python verify_direct.py` using Python 3.9 or later, with no third-party packages. `verify_symbolic.py` produces the exact class and representative tables and checks the class counts 4, 14, 40, 108, 340 at ranks 0 through 4 and the sharp bounds 4, 7, 11, 19, 35. Its successful terminal marker is `EXACT_FINITE_CLASSIFICATION_OK`.

The second program builds the atomic diagrams directly on `range(n)`, enumerates every possible vertex witness, and compares exact recursive types with the gap-based computation. It checks rank 0 through 3 on cycles of sizes up to 20 and rank 4 up to 12. Its successful terminal marker is `INDEPENDENT_DIRECT_CHECKS_OK`. These are distinct finite implementations; the second one cross-checks rather than replacing the first exhaustive finite calculation.

The inductive gap lemma in RESULT.md, not a finite sample, justifies truncating all rank-four inputs to 32 vertices per gap. The 1024 rows in `class_table.csv` and 340 rows in `class_representatives.csv` are the complete finite certificate. Their counts and minimal representatives are mathematically exact modulo correct execution of the transparent algorithms. Independent expert review has not occurred.
