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

## Reproducibility

Run `python verify_bipartite.py` under Python 3. The script uses Python standard-library `fractions` only, constructs the full orbit-lumped Markov generator over all pairs of plus-spin counts, solves the stationary linear systems by exact rational Gaussian elimination, checks every stationary equation, and recomputes both the pair correlations and the magnetization variance. Expected result: `PASS 54 full exact rational lumped CTMC stationary checks`, followed by nine optional large-size asymptotic samples.

The 54 exact tests are finite examples; the all-size result rests on the generator identities and rational asymptotic arguments in RESULT.md. No independent external audit, formal proof system, or certification was performed.
