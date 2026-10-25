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

# Reproducibility and verification

The accompanying `check.py` is self-contained scientific verification code. Install Python 3 with `sympy`, `numpy`, `scipy`, and `mpmath`, then run `python check.py` from the directory containing the script. Its verified execution returned `PASS 75 checks`.

The checker independently generates all stationary polynomial moment balances through degree four, forms the cubic Markov-generator matrix, derives the exact rational Laplace transform, checks zero derivatives through second order and the stated third/fourth derivatives, verifies the critical parameter and the sign of its fourth derivative, computes the double- and simple-pole leading coefficients and the degenerate case at \(\rho=1\), and cross-compares 35 exact-semigroup evaluations with independent high-precision numerical Laplace inversion. As a separate numerical check it samples the last-reset Gaussian-mixture representation to compare two stationary moments at three reset rates.

These finite checks do not prove a theorem by themselves. The all-parameter claims rest on the generator, rational identities, analytic pole comparisons, and continuity argument in `RESULT.md`. No assertion of independent verification or third-party certification is made.
