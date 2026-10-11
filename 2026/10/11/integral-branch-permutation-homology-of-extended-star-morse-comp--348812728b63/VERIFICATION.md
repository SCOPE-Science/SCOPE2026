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

# Verification record

The bundled `verify_morse_star.py` is standalone Python 3 standard-library code. It constructs matching simplices from oriented vertex–edge incidences on the specified two-edge-arm tree, independently of the join decomposition used in the mathematical proof. It verifies the predicted face count, exhaustively tests the signed reduced Lefschetz character against the sign-twisted augmentation character for all \(S_n\) elements at \(n=2,3,4,5\), and computes mod-two augmented boundary ranks and reduced Betti numbers for every degree at \(n=2,3,4\). On replay in the delivered package, the success output is `VERIFY_OK all_group_elements= 152 mod2_complete_for_n= [2, 3, 4]`.

Exact all-parameter integral correctness rests on the relative cone decomposition, join homology with integer coefficients, and the equivariant augmentation connecting map proved in `RESULT.md`. The finite checker does not establish untested parameter values, torsion-freeness in general, literature uniqueness, or independent assessment.
