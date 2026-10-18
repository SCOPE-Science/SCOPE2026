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

# Verification of exact geometric-level renewal law

The accompanying `verify.py` is self-contained and uses only Python's standard library. It represents numbers in \(\mathbb Q(\sqrt2)\) exactly as pairs of rational coefficients, not floating point.

Running `python verify.py` checks the explicit paired-digit increment masses against an independently composed one-digit distribution through level \(85\); calculates exact hit probabilities from their independent renewal recurrence; compares all \(86\) values (including level zero) against the four-phase formula; and checks exact total first-passage probability at \(25\) thresholds by adding the analytically known discarded tail. The limiting overshoot law is also normalized symbolically. Independently, 208 exact coefficients across eight rational overshoot generating functions are checked against the first-crossing convolution.

Observed output:

```
VERIFY_OK: 85 exact renewal levels; 84 exact paired-digit weights; 25 first-passage mass and k=0,1 checks; 208 exact rational overshoot coefficients
```

The checks are finite. The mathematical proof for arbitrary levels is the rational generating-function factorization and coefficient extraction in `RESULT.md`; the infinite overshoot limit follows by dominated convergence using an absolutely summable increment law. This package contains no separate independent audit, no formal proof certification, and no assertion about physical-time return statistics or initial phase-space ensembles.
