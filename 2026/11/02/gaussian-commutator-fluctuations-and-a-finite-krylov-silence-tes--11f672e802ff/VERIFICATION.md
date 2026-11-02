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

# Verification record

`verify.py` was executed with the stated dependencies and reported:

```
COV n=40 h=0.0125 scaled_var=0.0069838388 target=0.0073137278 error=3.299e-04
COV n=80 h=0.00625 scaled_var=0.0071462762 target=0.0073137278 error=1.675e-04
COV n=160 h=0.003125 scaled_var=0.0072293631 target=0.0073137278 error=8.436e-05
COV n=320 h=0.0015625 scaled_var=0.0072713842 target=0.0073137278 error=4.234e-05
COV n=640 h=0.00078125 scaled_var=0.0072925155 target=0.0073137278 error=2.121e-05
VERIFY_OK exact resolvent products; Gaussian covariance limit; commuting and Krylov-null boundaries
```

The exact finite-step recursion computes \(\operatorname{Cov}(X_j)\) without Monte Carlo sampling. The independent analytic covariance in the two-state witness is \(e^{-2}(1-e^{-2})/16\) for \(L=1\). Rational symbolic identities test the sign and factor of the leading commutator. The covariance test covers finitely many step sizes and does not replace the Lindeberg argument, uniform matrix-product approximation, or analytic Krylov necessity in the proof. The package includes no independent expert validation.
