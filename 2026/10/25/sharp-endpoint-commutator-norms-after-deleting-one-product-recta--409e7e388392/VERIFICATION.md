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

Run `python3 conditional_commutator_checker.py` with Python 3 standard library only. A complete run passed **14,358 exact-rational assertions**, covering 81 weighted finite product models with deletion of proper nonempty rectangles and the exact conditional-weight matrices. Tested properties are: weighted skew-adjointness of the commutator; every kernel entry; exact endpoint row/column norms; degree-three annihilating identity and trace of the squared matrix; and sign-valued sharpness witnesses. No floating point arithmetic or externally downloaded data is required.

The proof is analytic on arbitrary probability spaces and uses the three positive-measure block reduction, its skew kernel, row-sum equality and the exact three-dimensional skew spectrum. Finite tests are regression evidence only; they do not certify an infinite-dimensional assertion. All source comparisons are finite and historical priority outside inspected material cannot be guaranteed. Independent audit has not been performed.
