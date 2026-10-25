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

# Verification

The `verify.py` script uses analytic endpoint integrals for the zero-order-hold transfer columns, not numerical quadrature. For oscillator counts 1 through 8 it checks arbitrary unequal-length partitions at the rank-obstruction budget, the exact uniform Gramian at three budgets for each oscillator count, direct full-row rank, and sampled-energy worst-mode ratios. The formula for arbitrary oscillator count, the partition-independent lower bound, and the sharp limiting constant are proved symbolically in `RESULT.md`; finite tests alone cannot prove these quantified statements.

Independent audit: not performed.
