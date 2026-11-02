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

The standalone standard-library verifier `verification/verify.py` completed with `PASS 40497 exact assertions`. It checks exact rational endpoint and beyond-endpoint values for sizes 2 through 30, algebraic root brackets for sizes 2 and 3, rational positivity certificates at the exceptional endpoints for sizes 4 and 5, and the distance-three degree-sum identity through size 30.

The proof is symbolic and handles all integer sizes \(n\ge2\). Finite checks are supplemental, not an exhaustive proof for unbounded size. Independent scientific validation has not been performed. No floating-point implementation guarantee is asserted.
