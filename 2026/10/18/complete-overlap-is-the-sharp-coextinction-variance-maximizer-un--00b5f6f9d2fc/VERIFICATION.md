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

Execute `python3 verify_variance.py` from a working directory containing the standalone artifact. The script requires only the Python standard library and exact integer arithmetic. It enumerates 90 degree-two 4-by-4 labeled incidence networks and 67,950 degree-two 6-by-6 networks, checks all removal counts, and independently verifies selected cases through direct enumeration of removed-pollinator subsets. The degree-three six-by-six check is intentionally limited to ten networks and is not presented as exhaustive. The code checks equality for block networks up to nine plants and the example values; the general proof relies on the symbolic discrete-convexity and double-counting identities in RESULT.md.

No independent scientific audit or external validation was performed. The model omits unequal failure risks, weighted interactions, rewiring, and demographic feedback.
