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

The claim follows from exact triangular-difference moments and algebraically invertible Gram invariants, as detailed in `RESULT.md`. No external independent audit has been performed.

Reproduce deterministic and stochastic diagnostic checks with `python3 verify.py` from this extracted directory. Only Python standard-library modules are required. The checker recomputes the first three distance moments using multinomial coefficient enumeration with exact fractions; verifies exact inverse formulas, the three sharp moment-image vertices, and a pair of distinct parallelograms sharing two moments; checks the explicit square-root Gram bound for rational square perturbations; and separately samples Euclidean coordinates with fixed random seed. On the verified package the output was:

```
EXACT_MOMENT_EXPANSION_INVERSION_AND_TRIANGLE_PASSED 100
OPTIMAL_SQUARE_ROOT_GRAM_BOUND_CHECKED
INDEPENDENT_EUCLIDEAN_POINT_PAIR_SAMPLING_PASSED
ALL_CHECKS_PASSED
```

The 100 finite rational samples and the random simulation do not prove an infinite-domain theorem; the proof in `RESULT.md` supplies all quantifiers and boundary cases. The geometric stability estimate concerns normalized, exact populations, not statistical guarantees from finitely many noisy samples.
