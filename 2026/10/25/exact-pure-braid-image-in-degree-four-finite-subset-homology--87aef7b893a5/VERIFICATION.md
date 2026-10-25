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

The exact checker `verify_h4.py` computes the operator matrix on the two cycle generators associated to every triple and uses rational Gaussian elimination. Its ranks for n=2 through n=8 are 0, 0, 5, 9, 14, 20, and 27, respectively, matching the stated formula. It also verifies that the all-ones combination of correction operators vanishes. The remaining cycle classes are killed directly by the exterior-algebra calculation.

These finite computations are supplementary. The all-parameter proof is the symbolic classification of degree-four cycles and the coefficient-equality argument in RESULT.md. No exact image formula is asserted outside degree four. Independent audit and independent validation have not been performed.
