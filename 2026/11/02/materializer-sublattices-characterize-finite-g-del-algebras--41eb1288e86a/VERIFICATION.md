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

The principal theorem is established by the finite-poset/downset proof in RESULT.md. To repeat the finite checks, run `python verify_materializers.py` and `python verify_example.py` with Python 3 and no third-party dependencies.

The first program enumerates all naturally labeled posets of orders one through six and independently computes Heyting implication, materializer fixed points and ambient union closure. It verifies the local principal-downset criterion and its global equivalence with prelinearity and the forest property. Poset counts by size are 1, 2, 7, 40, 357, 4824 (5231 total). The second program uses frozenset ideals and verifies the nine-element example, the seven-element materializer, and failure of distributivity of its internal lattice.

Finite exhaustive tests provide cross-checks, not proofs beyond the tested sizes. The general statements follow from the written mathematical argument. An independent scientific audit has not been performed.
