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

# Verification details

The standalone `checker.py` performs finite exact-integer and high-precision calculations for the Fourier reduction of the folded-cube metric. It enumerates even characters of small quotients, verifies their Krawtchouk eigenvalue formula by direct vertex sums, checks the negative-type zero-exponent normalization, checks the derivative's approach to the predicted Gaussian constant, and confirms positivity of the weight-four obstruction beyond the stated asymptotic scale in selected dimensions.

Analytical verification is in `RESULT.md`: the critical proof steps are the quotient Fourier diagonalization, the universal distance-matrix perturbation bound, the explicit fourth Krawtchouk polynomial, uniform integrability at the binomial central-limit step, and a globally bounded second-order Taylor remainder. The finite computations do not certify the asymptotic claims, priority, or global optimality of a particular Fourier witness for each finite dimension. Only the stated asymptotic upper bound, rather than an exact formula or limiting equality for the global threshold, is proved.

The computational script requires Python 3 and `mpmath` for high-precision arithmetic. It does not read external data files and is not an independent mathematical audit.
