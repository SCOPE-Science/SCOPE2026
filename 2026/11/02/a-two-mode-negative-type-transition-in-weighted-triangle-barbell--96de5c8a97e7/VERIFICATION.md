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

# Reproducibility and limits

Run `python verify_weighted_triangle_barbell.py` with an ordinary Python 3 interpreter and no third-party modules. The program independently reconstructs the weighted shortest-path distances using all simple paths and compares the resulting full quadratic form with the closed decomposition, using exact rational arithmetic on 640 coefficient/exponent/bridge profiles. It tests the strict inequalities at \((t,p)=(1,47/25)\) and \((10,48/25)\) with outward intervals for every integer-base rational power, justified by inequalities between integer powers. The executable also reports approximate root positions for orientation only; these numbers are not certified and play no role in the universal theorem.

The critical existence theorem uses analytic strict monotonicity, concavity, the negative-type interval theorem and continuity. The exact formulas and equality-space ranks are proved in `RESULT.md`. The verifier does not claim to exhaust continuum parameters, determine uniqueness of the crossing bridge length, or constitute independent review.
