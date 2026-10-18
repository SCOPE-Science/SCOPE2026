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

# Exact verification

Run `python verify_gp93.py` with `networkx` and `sympy` installed as in `requirements.txt`.

The standalone code reconstructs the 18-vertex GP(9,3) graph and enumerates its 2,316 nonempty independent faces. It performs the deterministic 1,148-pair face-poset matching, constructs every Hasse arrow, checks acyclicity globally, computes the signed 4-by-15 Morse differential by matched-gradient expansion, and checks its rank four and determinant-one minor. A separate mod-two simplicial calculation obtains boundary ranks 17, 109, 326, 448, 216, 36. These finite certificates, together with standard discrete Morse/CW attaching-map arguments, prove the integral homotopy conclusion for this graph.

The code independently enumerates the full 18-element graph automorphism group, computes signed simplicial traces of the nine rotations and nine reflections, and checks the character decomposition. For the shortest carriers, it enumerates five-edge induced matchings from all 27 edges, finds exactly nine, verifies each 32-simplex integral sphere cycle has zero simplicial boundary, and finds a rank rise from 216 to 225 when these nine cycles are adjoined to the mod-two fifth-boundary columns. It also verifies the single reflection-fixed matching has positive orientation and that the nine matchings form one rotation orbit.

The flag-complex lower-bound lemma and the inference from the Morse CW complex to the wedge of spheres are mathematical proofs in `RESULT.md`, not brute-force experiments. A modular rank alone is not claimed to establish a characteristic-zero equality. The exact group character and homotopy conclusions require the integer Morse certificate. No integral saturation statement for the nine shortest generators and no independence or external certification claim is made.
