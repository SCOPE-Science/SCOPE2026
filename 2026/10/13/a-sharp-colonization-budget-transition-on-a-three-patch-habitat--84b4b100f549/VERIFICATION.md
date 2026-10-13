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
# Verification and scope

The standalone `verify_corridor.py` computes both required bivariate polynomial determinant identities over exact integers, directly from the seven-state transient generator. It also solves 64 rate-pair Markov linear systems in exact rational arithmetic and compares 707 candidate budgets against the theorem's optimum. Successful output: `VERIFY_OK polynomial_determinants=2 exact_CTMC_instances=64 exact_budget_grid=707`.

The determinant computations provide algebraic identities for all real rates, and the human-readable rational inequalities in RESULT.md establish the global optimizer and all equality cases. The rational grids corroborate rather than replace the infinite-dimensional parameter proof. There was no external independent audit. The model has no empirical calibration, and the full text of two relevant older optimization papers was unavailable for a decisive novelty exclusion.
