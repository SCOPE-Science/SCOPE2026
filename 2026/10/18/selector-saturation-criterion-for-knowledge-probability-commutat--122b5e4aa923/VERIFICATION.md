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

# Verification and limits

The packaged standalone checker runs with Python 3 standard library. Execute `python3 verify_commutation.py` in the package directory. The enumeration consists of 1,099 exact partition/half-integer probability-kernel configurations on one, two and three worlds; each is checked against all subsets of worlds and all evaluation worlds, and its truth result is compared with the proposed selector-saturation criterion. It also validates the eight-world sharp example with four independent choice tuples.

Expected markers: `FINITE_EXHAUSTIVE_OK 1099 matching_cases 249` and `SHARP_MULTI_BLOCK_OK 4 4`. The symbolic proof, rather than finite enumeration, establishes the theorem for all finite sizes and arbitrary real probability weights. No independent audit is claimed.
