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

# Verification of the icosidodecahedral graph-metric filtration

Place `verify.py`, `collapse_certificate.json`, and `expected_output.txt` in one directory; run `python3 verify.py`. The program requires only Python 3.10 or newer and its standard library. The exact console transcript should equal the supplied `expected_output.txt` (including both success sentinels).

The program constructs the dodecahedral graph as \(GP(10,2)\), forms its line graph on thirty edge-vertices, checks the complete shortest-path distance spectrum, enumerates **all** simplices of the radius-one, radius-two, and radius-three clique complexes, and replays each of the \(20\), \(471\), and \(7964\) recorded elementary collapse pairs. At every pair the lower simplex has exactly one present immediate coface and that coface is maximal. It independently regenerates an acyclic greedy collapse sequence and verifies the remaining two-dimensional complexes have connected cyclic links, edge multiplicity two, a connected triangle dual graph, and Euler characteristic two.

The supplied oriented cycles are checked as integral cycles. The program computes their integer relationship under the simplicial inclusion followed by the certified radius-three collapse map, obtaining an invertible coefficient \(+1\). It also calculates signed antipodal degrees \(-1\) in both two-sphere stages and verifies that the radius-four forbidden-pair graph is a perfect matching of fifteen pairs. This certifies the integral homotopy classifications and all-field barcode.

Limitations: this is a complete computation for the specified thirty-vertex graph, not a general theorem about all Archimedean solids, arbitrary geometrically embedded polyhedra, or arbitrary metric perturbations. The computation has not undergone independent external mathematical audit.
