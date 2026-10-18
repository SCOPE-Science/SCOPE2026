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

The standalone `verify_nonagon.py` uses Python 3 standard-library rational arithmetic, not floating-point decisions. It verifies the unique cubic-root isolating interval, Chebyshev identities, all 3060 four-normal combinations, boundedness, exact support-half-plane feasibility, exact signed-area comparisons, nine and only nine minimizers, and the strict improvement over the best fully edge-tangent candidate. Successful execution prints `EXACT_NONAGON_CHORD_QUADRILATERAL_CERTIFICATE_OK`.

The analytic reduction from unrestricted chord quadrilaterals to the enumerated support-normal configurations is proved in RESULT.md. The script checks an exhaustive finite algebraic problem; it does not test arbitrary nonregular polygons or prove the unrestricted continuous-direction quadrilateral minimum. A displayed decimal is for orientation only and does not enter any comparison. Independent audit has not been performed.
