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

# Analytical and finite verification

Run `python check.py` using Python 3 with only the standard library. The program was executed successfully, producing:

```
m= 2 N= 16 blocks= 30 exact checks passed
m= 3 N= 64 blocks= 126 exact checks passed
m= 4 N= 256 blocks= 510 exact checks passed
ALL EXACT CHECKS PASSED
```

For every listed dimension, it exhausts all Walsh coefficients, all nontrivial affine hyperplanes, and all standardized affine-hyperplane sample totals, using integer arithmetic. It verifies finite-population variance exactly with fractions. For \(N=16\), it also enumerates all subsets of one, two, and three distinct population units, comparing their incidence frequencies to exact SRSWOR ratios. Reproducibility has no external dependencies or random seed.

The independent algebraic argument in RESULT.md proves the identities for all \(m\ge2\). The standard hypergeometric/finite-population CLT provides the asymptotic normal limit; Portmanteau gives vanishing SRSWOR point masses at the two hyperplane totals. No finite program proves this infinite limit. The numerical checks are supporting error-detection only. Verification of scientific priority remains limited by searchable accessible literature; independent audit has not been performed.
