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

# Verification and limits

Run `python verify.py` with Python 3, SymPy, NumPy and SciPy available. No external data are required. The script reconstructs the exact invariant distribution, aggregate relaxation polynomial, two marked-jump kernel derivatives, and a separate two-counting-field tilted-generator calculation of mean currents, zero-frequency mixed noise and work variance.

Independent direct matrix-exponential two-time quadrature is compared with the scalar relaxation-ODE formula on 125 deterministic strictly admissible seven-rate and observation-time parameter sets. Positivity of the resulting time integral, strict negative mixed count covariance and exact rate reconstruction are checked in all cases. Some sets have an instantaneous correlation kernel with a sign change, demonstrating why the analytic integrated-kernel argument is needed.

The universal \(t>0\) inequality is proved by the real two-mode spectrum, a one-zero lemma, and a positive total integral in RESULT.md; finite computations do not constitute that proof. The tests do not establish external scientific priority, experimental feasibility, or finite-sample estimation errors. Independent mathematical audit has not been performed.
