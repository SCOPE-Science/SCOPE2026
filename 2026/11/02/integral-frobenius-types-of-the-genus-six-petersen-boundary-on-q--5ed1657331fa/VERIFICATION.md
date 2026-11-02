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

# Reproducibility and scientific limits

The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py` from the directory holding the extracted files. It terminates with `INTEGRAL_TORUS_BLOCKS_OK` followed by `VERIFY_OK`. The complete captured output is in `verify_output.txt`.

The check creates all ten vertices and fifteen edges of the Petersen graph, its thirty node-branches, and all 120 permutations of five labels. Every representative type is checked against all permutations in its conjugacy class. It independently calculates the signed-edge/vertex quotient characteristic polynomial and the exact characteristic polynomial of an integer six-cycle matrix, and checks the exterior-square trace identity. The seven integral torus product decompositions receive explicit unimodular basis certificates, checked by fraction-free integer determinants; the resulting group-order identities are also evaluated at five sample prime-power arguments. Exhaustive combinatorial checks apply to every possible Frobenius class, while the finite evaluations only corroborate general polynomial identities already implied by the verified block decompositions.

Mathematical prerequisites not replaced by code include the standard configuration of ten exceptional curves on a smooth quintic del Pezzo surface, normalization of a nodal curve, the character-lattice equivalence for finite-field tori, and the geometric fact that a smooth genus-zero curve over a finite field is isomorphic to a projective line. No external mathematical audit has been performed.
