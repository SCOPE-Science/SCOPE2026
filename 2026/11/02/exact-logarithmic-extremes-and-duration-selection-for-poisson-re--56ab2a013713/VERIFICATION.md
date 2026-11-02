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

The analytic proof establishes, under fully renewed scaled Brownian paths and independent exponential waiting times, an exact Gaussian supremum tail rate, the uniquely minimizing exponential-clock/Gaussian-amplitude saddle, and a constrained saddle that identifies the selected duration of the maximal area. It also proves the longest-duration mismatch by exponential order statistics and independent Brownian marks.

The accompanying \(`check_extremes.py`\) uses only the Python standard library and runs 276 deterministic checks of the covariance double integral, the saddle-point first derivative, tail normalization, positive strict cost gaps, and the ordinary Brownian coefficients. The included checker was executed successfully and reported 276 passing checks.

Finite coefficient tests are **not** proofs of the large-\(n\) limits. The concentration and renewal/extreme-value arguments are supplied in \(`RESULT.md`\). The proof does not establish a centered extreme-value distribution, convergence rates or an exact tail prefactor. Independent audit remains unperformed.
