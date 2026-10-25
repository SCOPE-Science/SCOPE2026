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

`verify_incidence_rowmotion.py` uses Python 3.10+ standard-library operations only. It constructs the binary-coordinate cube and cycle-plus-opposite-chords Wagner graph without external datasets. Each is checked cubic and vertex-transitive by enumeration of vertex permutations (48 and 16 automorphisms, respectively). Every ideal is constructed as a pair of a vertex subset and an allowed subset of its induced edges.

The verifier computes rank coefficients in two different ways: from enumerated ideals and from the binomial contributions of vertex-induced edge counts. It verifies the entire two-variable induced-edge census difference and the claimed unique rank-eight discrepancy. Rowmotion is then evaluated twice at each of the 12643 and 12641 states: directly from complement-minimal elements and by twenty individual toggles of the incidence poset in reverse linear-extension order. Every image agrees.

The transition table is checked to be bijective. A full cycle traversal marks each ideal once and verifies that every cycle closes at its start. The exact orbit-length tables, the largest orbits, the number of orbits, the sum of their lengths, and the two rowmotion orders are compared to the claimed integers. A successful run finishes with `VERIFY_OK`.

These are exhaustive finite computations, not proofs of an infinite-family result. The polynomial identity additionally has the direct counting proof in `RESULT.md`. The computational source is supplied in full; no cached data or external package is required.
