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

Exact verification runs `python CHECK.py` using only the standard library. The checker independently derives covariances by overlap probabilities for all 4≤n≤19 and all edge counts, directly enumerates all labeled graphs with 4, 5, and 6 vertices under fixed-m sampling, and enumerates the corresponding G(n,p) expectations for n=4,5 and several rational probabilities. The general proof does not rely on finite enumeration. Separate symbolic polynomial factorization compared the two rational identities without assuming their truth. Independent external review has not been performed.
