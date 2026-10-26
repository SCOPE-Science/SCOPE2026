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
# Reproducibility

Run `python3 checker.py` with Python 3 using only the standard library. It prints `ALL_CHECKS_OK` after exhaustive runs across \(1\leq n\leq6\), \(0\leq k\leq2\), and `ALL_PARTITION_CHECKS_OK` after checking every labelled set partition through \(n=7\) for direct diamond stability. The code derives its partitions, forward closure and histograms independently rather than loading theorem tables.

The complete theorem is proved algebraically in `RESULT.md`; these bounded finite tests only corroborate it. No stochastic simulation is used as a substitute for the binomial law or the Poisson limit. The historical priority assessment has incomplete full-text coverage of Blok's 1977 article; an independent audit is not performed.
