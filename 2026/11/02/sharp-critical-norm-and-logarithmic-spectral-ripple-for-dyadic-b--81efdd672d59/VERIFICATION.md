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

# Reproducible supplementary verification

Run `python verify_dyadic.py` with Python 3 and `mpmath` 1.3 or newer, from this directory. In the packaged check, 55 finite assertions passed. These compare the direct one-sided multiplier with its bilateral Gamma-periodized expression, the omitted positive tail, periodicity, and numerical phase optimization. The checker prints the critical phase, sharp constant estimate and an analytic derivative-tail bound evaluated numerically.

## Proof versus finite checks
The checker cannot validate every real exponent, every frequency, surjectivity of the Bergman--Laplace representation, uniqueness of extrema on the continuum or absence of eigenfunctions. Those are established in RESULT.md by exact Plancherel, Mellin transform, and quantified first-harmonic domination. Reported decimals are numerical approximations, not rigorous interval bounds. No external audit or independent validation has been performed.
