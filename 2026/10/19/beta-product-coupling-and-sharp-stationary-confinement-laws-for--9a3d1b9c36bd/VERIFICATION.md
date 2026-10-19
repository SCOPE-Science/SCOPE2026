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
# Verification record

The scientific proof in `RESULT.md` is self-contained. Its critical steps are the independent three-state stationary-generator recurrence, compact-support moment determinacy, positive gamma-increment coupling, and beta-convolution endpoint analysis. The beta representation is a stationary-marginal identity, not a pathwise decomposition.

The included standalone `check.py` runs with Python's standard library. Executing `python check.py` on the supplied bytes completed successfully with **37,096 exact-rational and analytic-coefficient assertions**. The tests cover 576 distinct pairs of positive rational transition rates, sixteen generator-moment levels, the resulting beta-product moment recurrence, a closed elementary density family, and the beta-function limiting amplitudes in that family. All tests completed without an exception.

The exact-rational tests are finite corroboration and do not certify every real parameter, asymptotic limit, or originality. The paper's known fixed-rate stationary characteristic function and hypergeometric density are not attributed as new here. The strict two-rate stochastic-order theorem is proved analytically. No external independent audit has been performed.
