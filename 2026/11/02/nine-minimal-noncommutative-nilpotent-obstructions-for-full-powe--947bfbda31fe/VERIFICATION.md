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

# Verification record

The accompanying self-contained `verify.py` was run with the local Python 3 interpreter and returned `VERIFY_OK`, including `TOTAL_MINIMAL_NONCOMMUTATIVE_NFB_CLASSES: 9`.

The program enumerates all 63 nonempty labeled loopless digraphs on three vertices, canonicalizes them to 15 digraph isomorphism types, computes induced retract cores, and searches all off-diagonal dominated-vertex removal sequences for the categorical-square finite-duality criterion. Its twelve noncommutative digraph classes split into four finitely based and eight nonfinitely based classes. It also examines all 1,296 layer-compatible index-four multiplication tables (filtered by associativity and the strict power filtration), verifies that every noncommutative survivor has a nonzero pure cube, and tests the two-generator/two-product-value template.

The proof in `RESULT.md` explains why these restricted searches cover every relevant semigroup, and relies on the published equivalence of finite duality and finite equational basability. In particular, computer checking finite tables by itself does not prove an infinite nonfinite-basis assertion. The outcome is not independently audited; originality remains vulnerable to older unpublished or unexamined exact small-order classifications.
