---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction

Run `python3 artifacts/verify.py` with Python 3 and its standard library. The checker compares literal Boolean products to the rectangular commutation rule at dimensions 2 through 4. At dimensions 2 through 5 it constructs the graph, compares its degree frequency table to the predicted table, checks its isolated vertex count, and computes distances in the nonisolated component. The predicted diameters in those dimensions are 1, 3, 3, and 3. The checker retains additional clique and facet count tests; its existing success marker is `VERIFY_OK_BOOLEAN_RANK_ONE_IDEMPOTENT_CLIQUES`.

The degree theorem and diameter classification for general dimensions are proved in `RESULT.md`, rather than inferred from the finite checks.
