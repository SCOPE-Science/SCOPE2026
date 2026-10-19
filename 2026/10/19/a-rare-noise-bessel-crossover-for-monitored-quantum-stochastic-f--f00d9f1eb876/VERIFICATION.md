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

The theorem's mathematical proof appears in `RESULT.md`; none of the finite tests substitutes for the singularity analysis, compact-uniform coefficient limit, or Laplace-transform uniqueness. The supplied `rare_noise_return_check.py` uses Python 3, the standard library (`fractions`, `collections`, `math`) and `mpmath>=1.3`. Install the dependency from `requirements.txt` and run `python rare_noise_return_check.py`.

The checker confirms 215 individual assertions, including exact rational propagation of the position/coin Markov chain after each origin projection for several mixing probabilities, independent Fourier resolvent evaluation against the closed two-state return Green matrix, numerical Bessel-coefficient convergence at several shrinking mixing probabilities and fixed-noise first-return tail constants. Exact rational finite-horizon assertions are not claims of exhaustive enumeration across horizons or probabilities. The termwise uniformity follows analytically from the displayed factorial majorant, not from numerical fitting. Independent audit and external certification have not been performed.
