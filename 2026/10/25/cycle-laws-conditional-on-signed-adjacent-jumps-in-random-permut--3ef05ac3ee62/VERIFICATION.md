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

# Reproducibility and limits

Execute `python signed_jump_cycle_verify.py` with a standard Python 3 interpreter. The program checks all \(n!\) permutations for each \(2\le n\le8\), every signed jump \(0<|d|<n\), and every eligible site, using exact integer and rational arithmetic. It independently checks pooled conditional cycle-count laws and all derived covariances. Reported local-case counts: \(2,8,18,32,50,72,98\) for \(n=2,\ldots,8\). The infinite-range statement follows from the contraction argument in `RESULT.md`, not from finite enumeration. Literature-priority uncertainties are described in `REVIEW.md`; no independent validation is claimed.
