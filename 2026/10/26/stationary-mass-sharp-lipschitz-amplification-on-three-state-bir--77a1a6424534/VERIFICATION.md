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

# Computational verification and limits

The standalone `verify.py` evaluates the formula using a direct two-by-two gradient matrix exponential. Independently, it constructs the three-state Markov transition matrix, uses cumulative signed masses to compute exact Wasserstein-one distances between adjacent transition rows on the unit-edge path, and compares their maximum with the proposed norm. Randomized parameter suites also check the strict fixed-stationary-law bounds, the strictly monotone row behavior under individual conductance changes, and the contractivity condition. Separate singular-perturbation checks approximate both unattained envelope branches.

The standalone script uses NumPy and SciPy, a fixed random seed, and no external files. Execute with `python verify.py`. These numerical comparisons do not establish the universal theorem and cannot exclude historical precedence; the analytical proofs and documented literature comparisons address those issues separately.
