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

# Reproducibility and checks

The accompanying `verify.py` independently builds finite-type adjacency matrices for five finite allowed-gap sets and checks each of four forbidden words (20 Perron-root comparisons), then checks three asymptotic regimes for each gap set (15 additional checks). Running `python verify.py` with NumPy installed yielded `VERIFY_OK 35 independent SFT spectral-radius and asymptotic tests`. The code evaluates the claimed root by bisection and independently evaluates the symbol-level SFT adjacency spectral radius. It also evaluates exact leading-term coefficients.

The finite experiments do not establish the formula for infinitely many gap lengths or arbitrarily large forbidden blocks. Those assertions are proved by the regeneration, word-count entropy comparison and analytic expansion given in `RESULT.md`. The source literature and historical-priority assessment are not independently audited.
