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

The exact theorem is proved without computer assistance in `RESULT.md`. The packaged source `verify_ldc_multipartite.py` uses an independent exhaustive method for finite corroboration: adjacency construction, direct open-neighbourhood signature tests for every vertex subset, and unrestricted enumeration of all set partitions. Its computation checks each complete multipartite part-size profile on three through nine vertices and compares the brute-force maximum with the proposed formula. The raw output `verification_output.txt` records `VERIFY_OK` for all 86 profiles, broken down by order. No finite search has been used to infer the unbounded assertion, and no independent mathematical audit or external verification is asserted.
