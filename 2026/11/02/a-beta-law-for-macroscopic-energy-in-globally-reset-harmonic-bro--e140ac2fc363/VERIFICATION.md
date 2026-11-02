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

# Reproducibility checks and limitations

`python verify.py` with NumPy installed reproduces stationary quadratic and quartic moment identities by two pathways: direct exponential-age Gaussian integration and generator balance for normal-mode polynomials. Its exact checks include three independent normal-mode fourth-order balance laws; its independent simulations use 100,000 stationary observations per regime at four configurations, including unconfined center drift \(\kappa=0\). It checks the explicit global/local squared-coefficient gap at twelve rate/size configurations and beta first and second moments for three parameter ratios. The extracted program was executed successfully and ended with `PASS`.

A finite numerical sample is not a proof of the stationary process representation, infinite-population limit, correlation formula, or time-average central limit theorem. Those follow from the orthogonal stochastic convolution, strong law, generator eigenfunction and bounded-jump martingale argument in `RESULT.md`. The finite-\(N\) formulas permit independent symbolic checks without simulation. No external audit or independent validation is claimed.
