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

# Reproducibility and bounds

Run `python verify.py` in Python 3 (no external packages). The program independently builds all edges of each deleted-matching biclique, enumerates all subsets, tests the induced-degree-one condition on the actual adjacency matrix, and separately checks inclusion-maximality by all one-vertex extensions. It checks all 130 parameter triples with \(3\le m,n\le7\) and \(0\le t\le\min(m,n)\). The observed final output is `VERIFY_OK 130 graph parameter triples; all subsets checked`.

This finite computation is not a proof for unbounded parameters. The all-parameter proof appears in `RESULT.md`, derived from the selected degree formula and exact mixed-shore case analysis. The relative well-dissociated classification and the crown-family gap follow algebraically from the proven maximal-set polynomial. No independent audit has been conducted.
