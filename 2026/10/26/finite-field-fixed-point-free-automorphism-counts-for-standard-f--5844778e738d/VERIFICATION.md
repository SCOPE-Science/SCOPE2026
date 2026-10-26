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

## Checks and limits

- The defining bracket table, automorphism parametrization, triangular diagonal, fixed-point-free condition, divisor sum, and positivity criterion were checked symbolically in the proof.
- `verification/check_formula.py` was run from the package path. Output: `CHECK_OK: 243 divisor-sum/direct-count and existence-cutoff cases; n=4 simplification checked for 27 prime powers`.
- The checker compares the divisor sum with a separate enumeration of exponent pairs in a cyclic group of order \(q-1\); it is an arithmetic consistency check, not a proof of the universal Lie-algebra statement.
- The proof includes characteristic two and does not rely on the characteristic restriction in the cited grading paper.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
