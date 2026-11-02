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

## Exact finite checks

Run `python3 verify.py` in a directory containing that script. Only the Python 3 standard library is required. It constructs each graph from the adjacency definition; computes shortest-path distances by breadth-first search; extracts the two-edge maximal geodesics from those distances; enumerates every unordered packing by a dynamic program over path choices; separately scans every vertex subset to determine the geodesic-free sets and their inclusion-maximal members.

All cases \(2\le n\le8\) were checked exhaustively. The observed packing polynomials, maximum packing counts, transversal polynomials and inclusion-minimal transversal counts agreed with the theorem. The numbers of maximal geodesics in these graphs were, respectively, \(4,12,24,40,60,84,112\). The script also checks the closed formulas and strict log-concavity inequalities with exact integer arithmetic for \(2\le n\le150\). A successful execution ends with `VERIFY_OK`.

## Proof versus computation

The independent finite checks do not prove the all-parameter theorem. The proof depends on the unique-full-column description of each maximal geodesic, its reversible packing bijection, the complete classification of geodesic-free sets, and the explicit decreasing-ratio argument. The claims concern vertex-disjoint path collections, not edge-disjoint collections, and distinguish an individual geodesic from a packing of geodesics. The reverse orientation of a shortest path is identified.

## Scientific limitations

No independent audit or proof-assistant certification has been performed. The theorem does not assert real-rootedness of the polynomial, extensions to more than two clique layers, or definitive publication priority.
