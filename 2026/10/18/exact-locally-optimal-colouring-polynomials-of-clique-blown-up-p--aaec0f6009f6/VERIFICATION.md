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

# Verification

Run `python3 verify.py` with a standard Python installation. The script independently builds the adjacency lists of the vertex-labelled lexicographic products for each tested path and cycle, enumerates every named palette assignment, and checks that the vertex's own colour is uniquely most frequent among open neighbours. It compares this result with separately implemented path- and cycle-binomial formulas. It does not use the proof's fibre-monochromatic assumption in its brute-force acceptance test.

The executed verifier reported `SUCCESS cases=34 assignments=1969502`: 20 path cases and 14 cycle cases, including clique sizes \(s=2\) and \(s=3\), named palettes \(q=2\) and \(q=3\), and the path singleton case. All comparisons passed. This is exhaustive only within the listed finite parameter cases, not a proof for all \(n,s,q\).

The general proof requires no software: adjacent true twins cannot take different colours under unique plurality, strict fibre-neighbour comparisons reduce to weak plurality on the base, and the valid path/cycle colour sequences are counted by non-singleton-run compositions and cyclic boundary markings. Independent review has not been performed.
