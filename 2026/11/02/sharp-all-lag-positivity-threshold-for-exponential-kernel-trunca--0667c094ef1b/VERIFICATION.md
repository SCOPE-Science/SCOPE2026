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

The standalone `certificate.py` uses Python's standard-library `fractions.Fraction` and integer binomial coefficients. Running `python3 certificate.py` verifies 340 exact-rational assertions: the normalized coefficient recurrence and sixth-weight quartic, strict positivity of Bernstein coefficients for the remaining initial indices, negativity of the quartic derivative on its isolated interval, isolation of its first critical zero, and rational inequalities required for the Chebyshev tail estimates. It requires no input files or packages.

The proof in `RESULT.md` gives the exact rational generating function, pole decomposition, Chebyshev partial-sum identity, uniform positive-tail bounds and a Pringsheim argument for every larger step. Only finite polynomial/interval assertions are delegated to the program; it is not a numerical proof by sampling infinitely many weights. The proof assumes exact arithmetic and does not cover variable-step schemes, arbitrary kernels or finite precision.

Independent mathematical audit has not been performed.
