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
# Verification
The analytic proof reduces every statement to an exact distribution formula before applying a standard asymptotic expansion. No finite enumeration is used to infer an infinite limit.

`verify_endpoint_rates.py` evaluates the exact formulas for \(y\in\{0.3,1,2.5\}\). It checks Gamma and Beta at parameter \(10^{-6}\), Pareto at \(\varepsilon=10^{-8}\), log-normal at \(\sigma=12\), and Weibull at shape \(0.005\). The acceptance tolerances are intentionally loose enough to test the predicted limiting scale rather than accidental decimal agreement.

Limitations: the script depends on `mpmath`; it is a consistency check, not a certificate. The theorem is pointwise for fixed \(y>0\), and the Beta statement is restricted to the \(\operatorname{Beta}(1,q)\) witness path.
