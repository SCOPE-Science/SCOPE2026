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

The included checker `verify_rank3_binary_n8.py` was executed from the package directory using the Python standard library. It reported seven projective lines, 3003 nonzero-direction multiplicity profiles, 2702 full-rank profiles, minimum expected coverage time `422/105`, exactly seven minimizing profiles with multiplicity pattern `[1, 1, 1, 1, 1, 1, 2]`, next distinct value `88/21` with 21 profiles, simplex benchmark `47/12`, and increment `43/420`.

The mathematical verification uses the Fano-plane line criterion for rank three and an inclusion-exclusion tail identity. The enumeration is finite and exhaustive over all profiles; it does not assert an all-length theorem. Zero columns are handled by the monotonic replacement argument in the result. No independent audit or independent validation is claimed.
