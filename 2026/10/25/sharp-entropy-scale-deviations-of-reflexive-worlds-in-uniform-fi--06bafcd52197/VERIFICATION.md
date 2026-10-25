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

# Verification and scope

Run `python3 verify_kd45_core_ldp.py` from a directory containing the accompanying standalone script. The standard-library checker independently enumerates all serial relations on one through four labelled worlds, requiring every edge to have equal successor rows (equivalent to transitivity plus right-Euclideanness), and compares the distribution of reflexive vertices with the exact Stirling formula. The checks return profiles \((1)\), \((2,2)\), \((3,9,5)\), \((4,30,40,15)\). The checker compares theoretical totals at sizes five through ten with an independent block-decomposition recurrence. Successful execution ends with `KD45_REFLEXIVE_CORE_FORMULAS_OK`.

The infinite large-deviation law is established analytically by the full proof in RESULT.md; finite enumeration cannot verify convergence or absence of prior equivalent statements. No external independent audit has been performed.
