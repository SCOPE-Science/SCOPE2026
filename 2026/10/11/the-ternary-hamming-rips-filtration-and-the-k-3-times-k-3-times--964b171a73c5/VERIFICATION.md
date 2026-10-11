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

Run `python3 ternary_hamming_verifier.py` using Python 3.10 or later with only the standard library. It derives all finite objects directly from the 27 lexicographically ordered triples; no accompanying data file is required.

The verifier confirms exact Hamming distances, the radius-two face vector including the empty face \((1,27,243,945,1728,1620,945,351,81,9)\), 5949 nonempty faces, 2951 matched pairs and exactly one unmatched vertex and 46 unmatched tetrahedra (three-dimensional simplices). It constructs and orients all 27189 nonempty-face covering incidences and checks that topological sorting consumes all 5949 nodes. This certifies the acyclic discrete-Morse matching used in the proof. A separately implemented reduction of the mod-two simplicial boundary matrices gives reduced Betti rank 46 exactly in degree three. The radius-one checks count 81 edges and 27 triangles and prove every edge lies in exactly one triangle.

On success the program prints one line starting `VERIFY_OK`. A failure of any required assertion produces a nonzero exit and no success marker. The Morse theorem gives the integral homotopy type, whereas the mod-two computation alone would not. No claims are made for larger alphabets, more coordinates, or the general conjecture. Independent external verification has not been performed.
