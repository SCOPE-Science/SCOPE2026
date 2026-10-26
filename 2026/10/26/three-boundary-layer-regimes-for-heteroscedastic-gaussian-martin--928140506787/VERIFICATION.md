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

Run `python verify.py` with Python 3, SciPy and a standard math library. This verifies finite exact rational martingale rows (255 cases), numerical Gaussian Wasserstein comparisons (93 alternatives against optimized costs), stationarity, monotonicity and symmetry, plus numerical critical-scaling trends. Execution returned success on 2026-10-19 UTC.

## What was proved analytically

The support-to-interval reduction, Gaussian quantile covariance identity, strict concavity of the scalar objective, the unique interior optimum, and the three asymptotic boundary scales are derived in `RESULT.md`. The proof uses Gaussian normal-tail asymptotics and deterministic Taylor expansion. The counts above are not a substitute for proof of universal quantifiers or infinite limits.

## Boundaries and unresolved checks

The theorem excludes degenerate terminal parameters and zero Gaussian variance. The small conditional mass in the first regime has only a logarithmically equivalent leading decay rate. Two relevant antecedent papers were compared through accessible bibliographic abstracts rather than their full text; a possible implicit equivalent example has not been decisively excluded. No independent mathematical audit has been performed.
