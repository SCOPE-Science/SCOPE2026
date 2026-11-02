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

# Independent reproducibility and limits

Execute `python3 verification/verify_polar.py` from the package root. The check uses only Python's standard library. It reconstructs the integral cubic identity and all five gradient quadrics, checks an integral generator of the six-coordinate symmetry, enumerates the complete projective gradient base loci over three sample finite fields, and verifies each point's cubic membership and Hessian rank. The Hessian determinant witness equals \(-128\), valid in every odd characteristic.

The mathematical proof, not the sample-field enumerations, establishes the all-characteristic sign classification and the polar-map degree by separability and Bézout. There is no claim for characteristic two. There is no independent scientific audit or external certification.
