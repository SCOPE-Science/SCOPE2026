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
# Reproduction and limits

Run `python3 verify.py` using Python 3.9 or later and no external packages. The script reconstitutes the complete ternary length-five universe from `itertools.product`, rejects the 99 self-overlapping words, and checks every edge between the remaining 144 vertices through two equivalent but separately coded definitions. It proves four canonical maximum nine-cliques with both maximal-clique and all-clique traversals and a five-clique cap for singleton first/last supports; it also directly performs the unrestricted 144-vertex exhaustive maximal-clique census with 24 optima, transports the canonical optima through all 12 allowed symmetries, and compares the two distance signatures. The expected last line is:

`VERIFY_OK viable=144 edges=3324 maximum=9 labeled_optima=24 orbits=2 orbit_sizes=12,12 canonical_candidates=48 canonical_maxima=4 singleton_pair_cap=5`

The complete code is included. Finite exhaustion certifies only alphabet \(\{0,1,2\}\), blocklength five, and minimum distance two. Literature comparison does not establish universal publication novelty, and independent external validation has not been performed.
