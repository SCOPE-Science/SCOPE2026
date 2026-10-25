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
# Reproducibility and boundaries

Run `python verify_brinkmann.py` with the versions in `requirements.txt`. The verifier independently generates the specified 21-vertex 42-edge graph, all faces and Hasse arrows, the deterministic acyclic matching, the integral Morse boundary, the complete induced-five-matching census and its cycles, and the full graph automorphism group. It verifies that the boundary of each sphere cycle is literally zero, the integer homology class is primitive, and the two seven-orbit coefficient determinants are units. It checks the signed actions of reflection and rotation on the actual integral classes.

Expected exact output includes `MORSE_PAIRS 2176`, `SIGNED_MORSE_D5 [1, -2, 1, 1, -1, -1, 1, -1]`, `TEN_VERTEX_CROSSPOLYTOPE_SPHERES 21`, `THREE_ORBITS [(0, 6, 0), (3, 7, 1), (4, 7, -1)]`, followed by `VERIFY_OK_BRINKMANN_INTEGRAL_SHORTEST_SPHERE_ORBITS` (the success line may precede the numerical lines). The method is an exhaustive finite calculation for this graph plus the mathematical flag-link lemma; it does not establish a classification for arbitrary graphs. Independent scientific assessment has not been performed.
