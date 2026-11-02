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

# Verification and reproducibility

The accompanying `verify.py` is standalone and requires Python 3 standard library only. Execute `python3 verify.py` in a directory containing the extracted file. The executed checker completed 142 assertions, including hyperbolic-function reduction for \(\alpha=0\), interval-exit calculations against independent killed-generator finite-volume discretizations for \(\alpha\in\{0,0.5,1,2\}\), \({}_0F_1\) ODE residuals, exact positive/negative excursion-overlap inequalities across several parameters, and rare-excursion intensity convergence. The checker's printed mesh errors decreased upon refinement and the finest errors were below the documented \(10^{-3}\) tolerance.

The mathematical proof in `RESULT.md` establishes the claims for all allowed parameters. The finite-volume and asymptotic tests are finite checks only: they do not establish infinite-time convergence or an exhaustive search of prior publications. No independent audit has been performed.
