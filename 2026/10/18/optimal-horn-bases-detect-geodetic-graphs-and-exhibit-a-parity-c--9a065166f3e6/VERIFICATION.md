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

# Direct verification

Execute `python3 verify.py` with Python 3 standard library. The program computes shortest-path intervals by independent breadth-first searches, then checks the geodesic closure and the consequence-rule closure of every vertex subset for each tested basis. It enumerates all optimum-choice systems for cycles with at most seven vertices and samples further cases through ten vertices. It also enumerates every connected labelled simple graph with two through five vertices and tests the geodetic/nongeodetic characterization algorithmically. Result of the packaged program:

`VERIFY_OK cycles_bases=231 cycle_subsets=42040 all_connected_labelled_graphs=771 geodetic=357 nongeodetic=414 graph_subsets=21672`

For cycle vertex counts from three through ten, verified optimum literal costs are `0, 8, 15, 30, 42, 64, 81, 110`. Counts of optimum bases are `1, 1, 1, 64, 128, 1679616, 10077696, 63403380965376` respectively; the largest counts are calculated from the theorem's finite product, not exhaustively enumerated. The computations are bounded consistency checks, not a proof for arbitrary input size. The general arguments are given in `RESULT.md`. No independent audit or external validation has been performed.
