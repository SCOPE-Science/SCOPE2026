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
Run `python verify.py` with Python 3, `sympy` and `numpy`. The file constructs all test Laplacians and observation operators from edge lists; no downloaded data or hidden files are required.

Checks passed: 18 exact full-observability comparisons for two three-core examples; 24 exact heterogeneous invisible-dimension comparisons; exact full-module ranks 5, 5 and 6 for gains 2, 1 and 1/2 respectively on the six-state pendant three-path; two numerical ranks on a doubled six-cycle. All exact comparisons use symbolic rational matrices. The two cycle checks use double-precision tolerance and have illustrative status only.

The all-graph theorem is verified analytically via the 2-by-2 spectral block factorization, disjoint monotone eigenvalue branches, nonzero-factor row reduction, and the symmetric Popov–Belevitch–Hautus eigenspace rank criterion. Symbolic experiments do not constitute an infinite proof. No independent audit has been performed.
