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

# Reproduction and limits

The result is an analytic theorem, not an experimental extrapolation. Its critical identities are the Fourier multipliers of the tent kernel, exact Fourier coefficients of the normalized half-periodic sine density, the cotangent partial-fraction identity, and a circular interval-overlap argument locating the minimum tent mass. The conditions \(n\ge2\) and \(\gamma>0\), normalization of \(K_\gamma\), and parity definition of \(d_n\) are essential.

Run the standalone `verify.py` with Python 3 and `mpmath` installed. It independently assembles the finite circulant Gram matrix via the Bernoulli-polynomial form of the kernel, calculates its kernel-mean vector from an analytic integral formula, solves the Gram system, and compares every weight with independently integrated tent masses plus the claimed common offset. It checks all sign regimes at 5 gamma choices for each of 11 grid sizes and tests large-grid asymptotics. The provided execution produced `PASS: 174 independent finite checks`. All tolerances are far above the working 65-digit rounding floor for the checked sizes; these numerical results are supplementary and do not prove the unlimited-size assertion.

Independent mathematical audit has not been performed. The theorem does not address multivariate lattices, alternative periodizing maps, density perturbations, positive-constrained weight optimization, or finite-precision computation. The inspection of related literature does not guarantee historical priority.
