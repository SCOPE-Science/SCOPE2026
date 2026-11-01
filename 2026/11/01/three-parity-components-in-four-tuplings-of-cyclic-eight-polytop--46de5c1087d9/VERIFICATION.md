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

# Reproducibility

Run `python3 verify.py` with Python 3; no third-party packages or remote data are required. Expected final line: `ALL_VERIFY_OK`.

The checker completely rebuilds the 210-vertex, 525-edge base graph for the path on ten vertices and proves, by deterministic breadth-first search, that it has exactly three connected components containing the three parity classes separately. It independently verifies Gale's evenness facets for cycle lengths 9 through 14 and exact graph component/edge formulas through length 17. It also checks every marked subset of at most three vertices in paths of lengths 9 through 16 against the matching-cover lemma.

The **universal** result does not rest on testing finitely many values. The proof in `RESULT.md` establishes a general path matching-cover lemma, induction from the verified ten-vertex base, and explicit wrap-edge bridges. The graph Betti numbers then follow exactly from counted vertices, uniquely determined facet edges, and component connectivity. Only the stated ordinary integral homotopy classification is concluded.

Self-review: passed. Independent audit: not yet performed.
