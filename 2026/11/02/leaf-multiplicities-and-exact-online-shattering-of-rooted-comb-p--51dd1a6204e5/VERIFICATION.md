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

The exact classification is proved for every positive integer leaf-multiplicity profile in `RESULT.md`. The bundled `verify_comb.py` independently constructs the original tree paths and checks dimensions via exhaustive finite version-space recursion, rather than reusing the packing proof. Running `python3 verify_comb.py` successfully checked all 1,023 ordered positive compositions with at most ten leaves, including the single-hypothesis boundary. It also checked six informative fixed examples symbolically.

Finite checks are supporting tests only. The all-size correctness rests on the ordered-interval argument and its matching balanced search construction. The present package is not independently audited; no priority claim beyond the inspected comparisons is certified.
