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

The exact tilted-generator determinant, quadratic cumulant coefficient, discriminant, root formulas, and renewal-transform identity are checked by `python verify.py` using symbolic arithmetic. The code also checks the coefficient imposed by the passive-state occupation-time variance and performs 42 independent finite-time forward-semigroup moment checks at positive and zero passive diffusivity. They are computational corroboration; the analytic generator and discriminant arguments establish the theorem for all admissible rates and diffusivities.

The equal-rate finite-time comparisons are conducted at \(t=100\) and reproduce the predicted kurtosis-rate signs at \(D=0,0.02,0.2,0.5,1\). The old published long-time kurtosis display is not assumed as a verified formula; the direct equality of the model transform and the exact renewal formula is the primary cross-check.

No independent human or external mathematical audit has been performed. Publication priority beyond the cited sources and searched research records has not been established.
