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

# Reproducibility of the covariance classification

Run `python3 verify_general.py` and `python3 verify.py` with Python 3.9 or newer. Both scripts use only standard-library code and have been executed on the exact files included here. The general certificate reported `PASS: exact coefficient-by-coefficient identity in Q[p,q,t]`, with 21 monomial coefficients checked. The independent specialized verifier reported `PASS: 103 exact tests`.

The general script implements sparse multivariate polynomial arithmetic over rational coefficients. It derives the stationary second moments with common denominator, clears the strictly positive common denominator, and checks the entire algebraic covariance formula as an identity in three independent indeterminates \(p,q,t\); this is not interpolation, finite sampling or floating-point testing. The specialized script separately checks all nine entries of the complete \(p=4,q=2\) covariance matrix, generator moment identities, symmetry, conservation, exact sample fractions and sign behavior at the rational witness parameters.

The mathematical proof in `RESULT.md` independently establishes stationarity and uniqueness by synchronous coupling, rational closure from the actual Markov generator, denominator positivity, the all-real-parameter sign classification, and a unique positive root for the bias threshold. The code is supporting algebraic evidence, not an independent audit or an automatic theorem prover for all probabilistic hypotheses.

Limits: publication priority, higher-site effects, arbitrary independent bond concentrations and a formula for the entire stationary law have not been independently validated or established here.
