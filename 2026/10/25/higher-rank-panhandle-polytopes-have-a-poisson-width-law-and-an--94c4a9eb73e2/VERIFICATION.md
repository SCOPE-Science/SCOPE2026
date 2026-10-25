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
# Reproducibility and verification limits

The embedded `verify_width.py` is a stand-alone NumPy/SciPy program. Run `python verify_width.py` with Python 3, NumPy and SciPy installed. No external files, network access, or private inputs are required.

The checker enumerates all permitted rank-\(r\) bases in 120 small random-score problems and compares the optimum to the greedy closed form. It computes the exact finite-size mean Gaussian support difference as a one-dimensional integral of binomial tails and compares it with 160,000 independent samples at \((p,q,r)=(4,3,3)\). The empirical value is 0.23674741512508113 and exact integral 0.23920176634808954 (standard error 0.0011243664257310866). It also prints the asymptotic coefficient and finite-size ratios at selected larger dimensions, followed by `VERIFY_OK`.

Numerical checks provide finite corroboration only. The law and limiting expectation require the analytic greedy, Poisson-process, uniform-integrability and gamma-integral proofs supplied in `RESULT.md`. No independent audit or theorem certification has been performed.
