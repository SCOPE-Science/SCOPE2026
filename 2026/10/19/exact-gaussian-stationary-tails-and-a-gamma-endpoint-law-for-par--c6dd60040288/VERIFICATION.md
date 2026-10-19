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

The proof supplies: contractive stationary construction; conditional Gaussian variance; Poisson backward-age factorization; an exact deficit CDF on \(0<z<1-a^2\); stationary moment recurrence; absolutely convergent exact prefactor series; dominated-convergence endpoint Laplace calculation; and conditional Gamma localization. The domain excludes the no-reset endpoint \(a=1\).

The included `verify.py` is a reproducible independent finite-parameter check requiring Python, NumPy, and SciPy. Executed checks: variance moments of orders one through six (180,000 recursion draws), convergent exact coefficient series against independent Monte Carlo, and conditional-age direct integrals at four increasingly extreme positions, approaching the derived asymptotic constant. The code prints the observed ratios and fails if thresholds are not met. These checks do not prove a statement for infinitely large positions or all parameter values. They are supportive, not a claim of external certification.

The analytical original-versus-approximation comparison uses the stationary Fokker–Planck equation of the second-order Kramers–Moyal SDE; no limit interchange with \(s\downarrow0\) is asserted.
