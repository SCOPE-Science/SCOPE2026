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
# Verification

The symbolic proof is the primary verification of the universal claim. It uses only the published face formula and the canonical parameter inequalities.

The embedded `verify.py` is an independent finite stress test. It reconstructs all faces and edges, enumerates all graph triangles, removes actual faces, checks the exact formula, constructs every predicted arithmetic family separately, checks disjointness, and verifies the first flag parameter. Running it on every admissible pair with \(7\le n\le180\) gives:

`VERIFY_OK parameters=7656 range=n7..180 first_flag=13,3 exact_formula=yes relation_families=yes`

The computation does not certify parameters beyond the tested range; those are covered by the symbolic proof, not by extrapolation from finite data.
