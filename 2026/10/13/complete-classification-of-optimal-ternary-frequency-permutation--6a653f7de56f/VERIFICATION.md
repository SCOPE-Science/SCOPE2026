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

`verify.py` constructs all 90 ternary composition-\((2,2,2)\) words and the complete compatibility graph for Hamming distance at least \(4\). It exhaustively enumerates all maximal cliques with a pivoted Bron–Kerbosch recursion, checks every maximum code directly, and exhausts all \(4320\) coordinate/symbol transformations of one maximum.

The completed package was replayed successfully. Expected invariants are: 2745 compatibility edges; 90627 maximal cliques; maximal-clique size distribution 6:38895, 7:20160, 8:20520, 9:10320, 11:720, 15:12; maximum 15; 12 maximum codes; one natural orbit of size 12; stabilizer 360; representative pair-distance distribution 90 at distance \(4\) and 15 at distance \(6\); census SHA-256 `65b3cfc15c29027b96d96a9b3fb72f83d7374b00b975eb9f7b33c574234b8da7`.

The computation is exhaustive for this finite domain. It proves nothing about other compositions, lengths, distances, or submaximum equivalence classes.
