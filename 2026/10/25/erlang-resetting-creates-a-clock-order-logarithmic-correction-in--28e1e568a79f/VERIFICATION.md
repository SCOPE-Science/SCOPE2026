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

# Reproduction and scientific limits

Run `python verify_extreme.py` with NumPy, SciPy and mpmath. The program reconstructs exit probabilities using an independent killed-transition-kernel sine expansion at nine combinations of drift and Erlang order. It confirms that the derivation's exact Laplace boundary solutions match independent exit flux calculations at the stated spectral cutoff; this test controls numerical agreement, not an analytic spectral truncation bound. It separately evaluates both large-barrier tail constants and high-count Gumbel distribution values using 70-digit arithmetic and stable difference formulas.

Analytic verification consists of: solving the killed-diffusion backward equation with both endpoint data; finite differentiation of Laplace transforms against Erlang survival; renewal factorization of consecutive excursions; extraction of the dominant \(j=\ell-1\) derivative term; and substitution into the conditional maximum CDF for the size-biased count and Gumbel limit. Those steps establish the claimed infinite statements and identify the important distinction between finite spectral numerics and complete proof.

The program assumes Python with mpmath, NumPy, SciPy. Numerical checks do not cover every real drift, every positive parameter, or all clock orders and are not claimed as exhaustive. No independent external audit or formal proof validation is asserted.
