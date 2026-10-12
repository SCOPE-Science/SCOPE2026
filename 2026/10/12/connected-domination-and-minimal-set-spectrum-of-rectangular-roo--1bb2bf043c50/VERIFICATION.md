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

# Reproducibility and scientific limits

Run `python3 verify_rook_connected.py` in the same directory. The supplied source uses only Python's standard library, no external datasets, and no platform-specific paths. It computes \(\mathrm{CD}_{m,n}(z)\) using an independent root-component decomposition recurrence for connected bipartite graphs and the formula based on binomially chosen supports. It computes \(\mathrm{MCD}_{m,n}(z)\) using Stirling recurrences, then independently enumerates every subset of board squares and tests connected domination by rook-neighborhood coverage and breadth-first search. Minimality is determined by checking all single-vertex deletions, and independently checked against the tree and nonleaf structural condition.

All assertions passed for the eleven boards \((2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(3,3),(3,4),(3,5),(4,4)\). The verifier reports `VERIFY_OK boards=11 subset_checks=190277 connected_sets=158351 minimal_sets=1548`. For \((3,3)\), it yields coefficients \(6,72,117,84,36,9,1\) in degrees \(3,\ldots,9\) for the complete polynomial and coefficients \(6,36\) in degrees \(3,4\) for the inclusion-minimal polynomial.

The program does not prove the result for unbounded \(m,n\); the general proof uses a direct support criterion, graph connectivity, the absence of cycles in minimal supports, a weighted matrix-tree calculation, and the exponential formula. No independent validation or audit has been performed.
