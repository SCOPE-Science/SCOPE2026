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

# Verification and reproducibility

Run `python3 verify.py` from the extracted bundle; it uses only Python 3's standard library. A successful run reports:

```
ROOT_GRAM_COUNTS_AND_TRIPLE_THRESHOLD_PASSED
INDEPENDENT_SPHERICAL_LENS_AND_ONSET_COEFFICIENT_PASSED
ALL_CHECKS_PASSED
```

The checker enumerates the \(d(d+1)\) directed roots and their pairwise inner products for dimensions \(3\) through \(10\), counting \(d(d+1)(d-1)\) neighboring unordered pairs. It checks all triple sets with pairwise inner product \(1/2\) and their exact squared sum norms. For dimensions \(3\), \(4\), and \(5\), it numerically integrates the directly conditioned one-dimensional spherical-lens probability using closed beta-coordinate primitives and compares to the analytically derived contact coefficient at two independent offsets below \(\sqrt3/2\).

The infinite-dimensional quantifier over every integer \(d\ge3\), exact pair-count formula, no-positive-mass-triple-overlap interval, exact lens integral, and fixed-dimensional asymptotic are proved analytically in RESULT.md, not inferred from finite enumeration. Finite quadrature cannot prove the limit or exact equality; its sole purpose is to test normalization and detect algebraic or implementation mistakes. No independent mathematical audit has been performed.
