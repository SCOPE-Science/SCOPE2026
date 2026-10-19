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

The proof derives stationarity from the Poisson-kernel transformation of a Cauchy variable, not from numerical evidence. The finite binomial expansion and the exact half-Cauchy representation then establish the claimed parameter scaling, moment transition, and locally uniform crossover.

`python check.py` returned `VERIFY_OK` using SymPy and mpmath. The calculation checked degree-indexed binomial coefficients for degrees 2 through 12, an exact moment identity, representative moment regimes, the critical crossover, and numerical stationarity tests for degrees 2, 3 and 5. Finite checks do not certify the statements for all degrees or all parameters. No independent mathematical audit has been performed.
