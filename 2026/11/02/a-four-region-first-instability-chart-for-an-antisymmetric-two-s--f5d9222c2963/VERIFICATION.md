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

# Verification of exact first-event formulas

The standalone `CHECK.py` runs with Python 3 and SymPy. Executing `python CHECK.py` checked the invariant ray, the exact tangent/quotient and two-step multiplier identities, the explicit resultant for coincident clipping and transverse-flip thresholds, the tangential coincidence factor, the three parameter-root locations, and four representative first-event cases. It additionally tests physical interior orbit coordinates and one-step transitions in each case. Exact symbolic equalities verify algebra; strict analytic inequalities and continuity given in RESULT.md prove all-parameter ordering. Numerical spot checks cannot show uniqueness on a continuum.

The exact theorem requires fixed antisymmetric coupling \(0<s<1\) and the period-two branch born at the scalar flip; it stops at the first clipping or multiplier event. Clipped boundary contact is **not** a smooth flip of the clipped map, and a Floquet multiplier reaching \(-1\) is not in itself a proof of any nonlinear child cycle. Priority assessment is limited by inaccessible complete historical texts of the matching polynomial model. No independent audit is asserted.
