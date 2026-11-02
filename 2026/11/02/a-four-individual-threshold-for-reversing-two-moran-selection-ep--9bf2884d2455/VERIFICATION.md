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

# Reproducible mathematical verification

The archive includes `moran_epoch_checker.py` and `requirements.txt`. Install the recorded dependency, then run `python moran_epoch_checker.py`.

The checker symbolically reconstructs the one-update drift and each two-step expectation commutator for \(N=2,3,4\); it verifies all six simplified identities and the two positivity substitutions, then compares a separate exact-rational implementation of the full transition matrices across 486 model and fitness combinations. It also checks the exact witnesses and the quadratic threshold identities. On the inspected environment, it produced `PASS: 498 exact symbolic identities and independent rational two-step checks`.

The analytic classification does not depend on the number of test cases: the separate proof establishes all parameter inequalities for \(a>b>0\) and the unique crossover by exact polynomial reasoning. No external mathematical audit, automated theorem prover, or empirical validation is claimed.
