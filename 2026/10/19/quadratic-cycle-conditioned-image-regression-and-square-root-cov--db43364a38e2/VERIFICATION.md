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

Extract `verify_mapping.py` from this package and execute `python3 verify_mapping.py` with Python 3.10 or later (no third-party dependencies). The checker enumerates all maps on two through six labeled vertices, measures cyclic vertices and missing images directly, and compares the observed conditional distribution to inclusion-exclusion. It also checks factorial moments, the conditional-mean increment and exact covariance using rational arithmetic through size 70, and estimates the asymptotic covariance coefficient at larger sizes. The mathematical proof relies instead on directed matrix-tree enumeration, inclusion-exclusion, conditioning on an absent target, and moment convergence.

The reference calculations are finite checks; they do not establish the infinite assertions independently. The oldest cited primary sources contain classical ingredients that could imply weaker or overlapping special cases. The findings have not been independently audited.
