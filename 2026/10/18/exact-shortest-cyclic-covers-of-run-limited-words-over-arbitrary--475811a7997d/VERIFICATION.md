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

Execute `python3 CHECK.py` using Python 3 standard library only. `CHECK_OUTPUT.txt` records the exact reproducible output. The checker verifies legal directed edges, the integer potential bound, a bijection between imbalance vertices, balanced Eulerian augmentation, cyclic exact coverage, formal generating-function coefficients, and exhaustive exclusion of shorter covers in six small parameter instances.

The checker tests 47 parameter combinations with \(q=2,3,4\) and \(r=2,3,4\), verifying full cyclic factors and edge multiplicities. It cannot establish the theorem beyond its finite ranges; the general proof in `RESULT.md` supplies the mathematical justification. This record has undergone self-review only. Independent audit has not been performed.
