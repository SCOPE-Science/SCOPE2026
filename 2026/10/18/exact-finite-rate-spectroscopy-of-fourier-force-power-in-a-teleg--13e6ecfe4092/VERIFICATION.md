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

The mathematical derivation is in `RESULT.md` and the independent numerical/symbolic checker is `verification/verify.py`. Run `python verification/verify.py` using Python 3 with `numpy`, `sympy` and `scipy`.

The checker verifies the two-orientation generator resolvent, the derivative and high-rate deficit identities symbolically, 16 matrix-exponential time-kernel quadratures, four randomized finite-rate reconstructions for band limits one through four, and an exact rational six-harmonic reconstruction. These finite tests support, but do not prove, the infinite-spectrum assertions. The infinite claims rely on the displayed analytic proof, uniform convergence of the mode series away from poles, and Cauchy-matrix invertibility.

The observed finite-rate data are assumed exact, and the inverse problem is not numerically well-conditioned for arbitrarily many harmonics. Independent audit has not been performed.
