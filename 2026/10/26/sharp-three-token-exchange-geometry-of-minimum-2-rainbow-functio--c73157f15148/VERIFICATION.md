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

# Reproduction of the finite classification

The claimed graph is \(Q_4\), with vertices \(0,\ldots,15\), edges by XOR with one of \(1,2,4,8\), and two labeled color slots at each vertex.

Run `python3 code/verify_colortokens.py` using a Python 3 standard-library installation. The script enumerates exactly \(4{,}514{,}873\) subsets of the \(32\) named color slots of cardinality at most \(7\), checks all empty vertices against both color neighborhoods, checks the two orbits under coordinate permutations, translations and color swap, and builds all pair distances and the exact distance-three exchange graph. Its completed output is `logs/colortokens.out`.

Run `c++ -std=c++17 -O2 code/verify_color_masks.cpp -o verify_color_masks && ./verify_color_masks`. This code independently enumerates pairs of color masks at weights at most \(7\), checks feasibility and pair distances, then conducts a breadth-first search from every minimum function. Its completed output is `logs/color_masks.out`.

The completed runs agree: no feasible weight below seven; exactly \(320\) minima; orbit sizes \(192\) and \(128\); pairwise token distances \(3,4,5,6,7\) appearing \(4320,1440,22080,11520,11680\) times; and a connected \(27\)-regular, diameter-three three-token exchange graph. The two-orbit equitable row degrees \((15,12)\) and \((18,9)\) are also explicitly asserted in the Python checker.

These are finite exhaustive checks, not extrapolations to larger hypercubes. The 2019 primary literature full text was not available for a definitive publication-priority comparison. No external independent audit has been performed.
