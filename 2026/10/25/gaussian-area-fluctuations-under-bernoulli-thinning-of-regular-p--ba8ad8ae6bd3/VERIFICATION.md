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
# Reproducible checks and limits

Run the standalone Python 3 script `verify.py` without additional packages. The checker enumerates all vertex subsets for \(3\le n\le12\), compares direct planar polygon areas to the cyclic gap deficit, and tests the finite-sample expectation for \(p\in\{1/4,1/2,3/4\}\). It also tests the two-term asymptotic expected deficit and independently simulated variance for three retention probabilities at \(n=700\).

Observed output:

```text
EXHAUSTIVE_POLYGON_AREA_AND_CYCLIC_GAP_CHECKS_OK n=3..12 p=1/4,1/2,3/4
EXACT_MEAN_TWO_TERM_ASYMPTOTIC_CHECK_OK
MONTE_CARLO_ASYMPTOTIC_VARIANCE_OK 0.35 0.9449
MONTE_CARLO_ASYMPTOTIC_VARIANCE_OK 0.5 1.02551
MONTE_CARLO_ASYMPTOTIC_VARIANCE_OK 0.75 1.01126
ALL_BERNOULLI_CYCLIC_AREA_CHECKS_OK
```

The exact symbolic geometric-moment and regenerative central limit arguments in `RESULT.md` are the universal proof. Finite enumeration is exhaustive only through \(n=12\); stochastic simulations and their tolerance windows do not prove convergence, independence of untested cases, or historical novelty. No external validation has been performed.
