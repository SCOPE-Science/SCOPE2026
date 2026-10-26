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

# Reproducibility and limits

The standalone `verify_gp_rook.py` requires only the Python standard library. Run `python3 verify_gp_rook.py` in the directory containing the script. The expected deterministic standard output is supplied in `verification_output.txt`.

For the nine boards \((2,2),(2,3),(2,4),(2,5),(2,7),(3,3),(3,4),(3,5),(4,4)\), the code enumerates each of the \(2^{pq}\) vertex subsets. It tests the original geodesic rule, a separately implemented bipartite-component criterion, inclusion-maximality under every possible single-vertex addition, and the exact two polynomial recurrences. These runs exhaustively cover 120,656 masks. Direct counts include the \(3\)-by-\(5\) polynomial coefficients \((1,15,105,335,495,303,15)\) and maximal-set coefficients \((0,0,0,5,0,213,15)\).

For \(2\le p\le8\) and \(p\le q\le12\), additional exact-integer computations test polynomial low coefficients, the thin-graph identities, all claimed maximal-cardinality supports, and the maximum-set multiplicity for rectangular boards with both sides at least three. The recurrence treats the component containing the smallest left vertex as isolated, a single edge, a larger left-centered star, or a larger right-centered star, and counts these disjoint cases directly.

These tests are finite. The proofs of the infinite results are the structural and component-counting arguments in `RESULT.md`, not extrapolations from computations. No outside proof assistant or independent expert audit was used.
