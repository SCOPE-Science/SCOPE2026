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

# Verification of the stated scientific claim

Execute `python VERIFY.py` with dependencies in `requirements.txt`. The script checks the direct matrix expression for the squared Frobenius residual against its closed form, 31 numerical error thresholds across the entire correlation parameter range, the rank-one Cauchy CDF, the isotropic beta CDF, and the exact rank-one mean against numerical integration. It independently checks positivity of the analytical second derivative for hundreds of positive arguments, and checks strict boundary CDF inequalities at several dimensions. The replay of the embedded file reports `PASS: 1264 independent deterministic numerical/algebraic checks.`

The finite checks do not constitute an infinite certificate. The analytical proof uses exact projector identities, the standard chi-square ratio laws, strict convexity of the chi-square-one survival function, and the strict symmetric-convex characterization of majorization. The numerical quadrature checks have ordinary floating-point precision and finite tolerance. No independent audit was performed.
