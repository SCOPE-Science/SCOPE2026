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

# Exact finite verification

Execute `python3 verify.py` with Python 3 standard library. The companion `verification_output.txt` records the exact expected stdout. The checker starts from the graph's cyclic adjacency and re-enumerates all \(\binom{21}{5}\) candidate facets, constructs every subface, checks 3220 matched pairs and topologically sorts the 29106 oriented Hasse incidences.

The checker recursively computes all 650 columns of the exact signed integer Morse boundary, checks that exactly 13 are nonzero and each is a primitive two-entry column \(e_i-e_{13}\), checks the eight-term integral cycle, the integral cocycle on every four-face, and evaluates every element of \(D_{21}\) on that primitive cycle and on all oriented fixed faces. As an independent check, mod-two elimination directly on the original chain groups gives boundary ranks 1140 and 1883.

These are exhaustive finite calculations for the labeled 21-vertex graph. The homotopy equivalence uses the acyclic-matching theorem and the cancellation of primitive attaching degrees between cells of dimensions three and four; numeric field homology alone would not suffice. The quotient statement is rational only; no integral quotient computation or independent external validation is claimed.
