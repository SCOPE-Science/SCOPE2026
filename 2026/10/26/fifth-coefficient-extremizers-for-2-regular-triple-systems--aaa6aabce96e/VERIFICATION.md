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

The all-order proof uses exact incidence counting and inclusion-exclusion. The supplementary checker `artifacts/verify_small.py` was run from its saved package path with the Python standard library. It enumerated 640 labeled loopless cubic multigraphs on six vertices with edge multiplicity at most two; all cases satisfied the exact identity and bound, with maximum 54 independent five-sets and 120 equality cases. Alternating-cycle examples at orders 9, 12, and 15 attained 54, 540, and 2403, respectively.

The enumeration is finite corroboration only; the general theorem is proved in `RESULT.md`. Independent audit and independent validation remain unperformed.
