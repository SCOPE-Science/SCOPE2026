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

The executable `check.py` performs small exact stationary-window enumerations; high-precision checks of the immigration–death Laplace transform and hitting-time recurrences; and simulations of 900 uniform plus 650 logarithmically tilted two-group coupon collectors at alphabet size 350. The tilted model uses half the types with \(\theta=1\) and half with \(\theta=-1\), so its limiting effective intensity is \(\cosh(1)e^{-c}\). Its empirical CDF is compared with the predicted absorbing-generator matrix exponential at three time points. The actual output is recorded in `check_output.txt`; all 60 assertions passed.

The finite tests do not establish the functional limit or the original contribution. Those are argued in `RESULT.md`. NumPy, SciPy, and mpmath are required. Independent audit: not performed.
