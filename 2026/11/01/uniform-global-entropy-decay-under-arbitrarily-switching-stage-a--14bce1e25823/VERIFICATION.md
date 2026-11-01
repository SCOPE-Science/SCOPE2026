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

Run `python checker.py` in an environment with Python 3, NumPy, and SciPy. The exact arithmetic part checks the entropy derivative for 48 rational states and balanced skew cycles of sizes \(3,4,5,7\). The numerical part integrates a five-species example with switching coefficients and a variable maturation rate, and checks the prescribed entropy bound at 41 sample times. It reports the initial entropy, scalar endpoint bounds, and certified exponent.

The critical analytic facts are the cancellation \(a^\mathsf TAa=b^\mathsf TAb=0\), the migration identity \(-m(u-v)^2/(uv)\), and scalar convexity of \(z-1-\log z\). The proof in RESULT.md establishes the infinite-time convergence and rate. Finite computations are not a substitute for that proof, and no external or independent validation has been performed.
