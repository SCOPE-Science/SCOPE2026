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

# Verification of the sharp concordance penalty

Run `python verify_tau.py` using Python 3.10+ and SymPy 1.12+. It builds the exact nine-term mixture for Kendall tau from normalized rates \((a,a+b,a+b+c)/(3a+2b+c)\), subtracts it from the claimed upper envelope, multiplies by the explicit positive factor in RESULT.md, and confirms the resulting exact polynomial has 40 positive integer coefficients of total degree 8. It verifies the coefficient sum \(1743120\), the zero case of homogeneous hazards, and the sharpness limit as one rate approaches zero. These are exact symbolic assertions, not numerical evidence alone.

The probabilistic reduction is independently justified by exponential racing and direct integration of the independent exponential spacing differences in RESULT.md. The proof covers every strictly positive rate triple and all common continuous strictly increasing proportional-hazards baselines. The singular limit is used solely to establish optimality and is not an admissible equality configuration. No external independent validation has taken place.
