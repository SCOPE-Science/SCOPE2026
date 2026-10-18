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

# Reproducibility and verification

Run `python3 verify_convex.py` with Python 3 and no third-party packages. The program enumerates intermediate subsets in both neighborhood families to test convexity; enumerates the 19 nonempty downward-closed predicates over three propositional world types (where nonempty means the collection contains the empty profile); checks 38 unary-modal tests, 5,776 statewise implication tests, and directly verifies the binary conditional's different values. Its success token is `VERIFY_OK`. An independent evaluator, `direct_semantic_test.py`, checks 2,500 deterministically generated formulas of mixed nesting depth under the direct state-level semantics, comparing all 16 states in the two models (40,000 paired comparisons); its success token is `DIRECT_SEMANTICS_OK`.

A proof, not program enumeration, establishes invariance for all unary formulas at arbitrary nesting depth: the support-profile structural induction appears in `RESULT.md`. The checker verifies the finite model assumptions needed in the induction and the separating instance; it does not claim an exhaustive search of all formulas or a minimal-world theorem.

Literature comparisons establish best-knowledge originality against inspected sources, not independent priority certification. Independent audit: not performed.
