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

# Verification of divisor-and-root subalgebra classification

The proof in `RESULT.md` is a necessary-and-sufficient argument over any field and any dimension at least two. It uses the bilinear functional-tensor basis, rather than quadratic diagonal identities, so characteristic two presents no missing cross-term assumption. The weighted-block recurrence is checked at all block transitions, including the final wrap-around, and the order relation is proved in both directions.

Run `python checker.py` from the directory containing the extracted files. It enumerates all reduced-row-echelon subspaces and independently tests multiplication closure for twelve explicitly small field/dimension cases. It independently constructs every predicted weighted-block subspace, checks closure and root cardinality, and verifies the stated inclusion relation using finite-field matrix ranks for five further settings. The successful output ends with `VERIFY_OK`. These finite calculations are not presented as proofs of an infinite-field or infinite-rank assertion.

The result does not treat weighted cycles, disjoint cycle unions, or arbitrary regular evolution algebras. The published general disjoint-support-basis lemma and the rank-one idempotent coefficient are established prior art. The full text of a potentially relevant early permutation-evolution article could not be inspected; no claim of complete prior-art exclusion or independent scientific audit is made.
