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

Run `python3 verify_cyclic_subsequence_multiplicity.py` from the same directory as this document. The script needs Python 3 and no external packages. For each of 16 small hosts it builds embedding counts by processing all host positions with dynamic programming, independently of the block-index proof. It compares literal counts, predicted weak-descent frequencies, and the total \(\binom{qk}{m}\). It also performs 52,318 exact arithmetic coefficient checks for larger parameter ranges.

Observed result from actual execution:

```
VERIFY_OK literal_hosts= 16 distinct_targets= 9287 histogram_bins= 380 absent_degree_checks= 272 formal_positive_coefficients= 52318
PROFILE 2 3 m=2 {3: 3, 6: 1}
PROFILE 3 3 m=2 {3: 6, 6: 3}
PROFILE 4 2 m=2 {1: 10, 3: 6}
```

All computations use exact integers. These experiments do not certify the unrestricted theorem; its infinite validity follows from the bijective proof in RESULT.md. No external audit or independent formal verification is asserted.
