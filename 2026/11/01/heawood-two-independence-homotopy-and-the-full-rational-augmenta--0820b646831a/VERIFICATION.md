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

Run `python3 verify_heawood_ind2.py` (Python standard library only) to regenerate all 16,383 nonempty subset tests, the 2,256 admissible faces, 1,121 matching pairs, 10,150 face-poset incidences, and the complete directed acyclicity test. The resulting critical-cell multiset is one vertex and thirteen five-cells. Full mod-two boundary ranks are `(0,13,78,244,407,321,58)`.

The checker enumerates all 5,040 permutations of Fano points, finding 168 collineations, adjoins the explicit incidence polarity, validates 336 graph automorphisms, and computes oriented fixed-simplex Lefschetz numbers on all 2,256 faces for each group element. Every trace equals its vertex fixed-point count minus one. The character sums give full-group invariants of rank zero, and the point/line-preserving subgroup invariants of rank one.

These finite checks, together with standard discrete-Morse and rational character arguments spelled out in the proof, establish the claim. Tests alone do not establish worldwide novelty, an integral equivariant isomorphism, or integral quotient-space acyclicity. An independent mathematical audit has not been performed.
