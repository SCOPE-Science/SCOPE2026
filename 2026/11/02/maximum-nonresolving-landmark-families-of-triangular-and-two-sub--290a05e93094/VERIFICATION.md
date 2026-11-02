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

# Reproducibility and proof checks

The package contains `verify_threshold.py`. Run `python3 verify_threshold.py` with Python 3 (standard library only). It creates \(J(n,2)\) and \(KG(n,2)\) from adjacency definitions, computes shortest-path distances using breadth-first search, enumerates every bisector, selects inclusion-maximal bisectors by set containment, and compares them with the two asserted root-edge constructions.

The verifier covers triangular graphs for \(4\le n\le10\) and Kneser graphs for \(5\le n\le10\). On the two smallest triangular graphs and the Petersen graph it also enumerates every vertex subset and checks resolving directly, without using the bisector criterion for the actual resolving decision. A successful execution ends with `VERIFY_OK`.

The structural proof for arbitrary \(n\) is located in `RESULT.md`, including the exhaustive two-pair-type reduction, cardinality comparison, connected-component containment test and distance-complement transfer. Computation cannot replace those unbounded proofs.

The result does not claim a formula for arbitrary \(k\)-subset Johnson graphs, or an independent external mathematical audit. The literature-priority comparison is bounded to inspected accessible sources.
