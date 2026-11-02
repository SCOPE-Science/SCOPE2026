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

# Reproducibility
The analytical argument is in `RESULT.md`. Run `python verify_star_restart.py` with Python 3, NumPy, and SciPy. The program checks the exact rational inequalities, validates the no-restart moment identity and first-order resetting slope, evaluates representative rates and asymptotics, and constructs an independent finite-state generator whose resolvent converges to the continuum exit transform. It prints `PASS: rational, moment, asymptotic, and independent resolvent tests` on success.

Finite-state checks at subdivisions of 8, 16, and 32 intervals per unit length returned the exact bare means \(17/4\) and \(13/2\) up to floating-point error for \(q=4,5\), with discounted-transform absolute errors decreasing quadratically from below \(2.4\times10^{-4}\) to below \(1.5\times10^{-5}\). They are not exhaustive and do not establish the theorem for all \(q\), nor do they constitute independent review.

Analytical sensitivity to model assumptions is explicit: other center boundary conditions, asymmetric edge diffusivities, nonabsorbing leaves, reset overhead, or fixed-total-length rescalings require new analysis. The proof does not establish the uniqueness or exact value of the globally minimizing reset rate.
