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
Run `python3 verify.py` in the extracted package. The program creates adjacency operators directly from Hamming-distance differences rather than from the group-algebra proof, then performs exact binary elimination. Expected output: `VERIFY_OK all_eligible_hamming_shells_n_2_to_10= 45`. The run completed successfully using the included code. This verifies finite samples, not the all-dimension theorem. The analytical proof covers every claimed parameter. An independent mathematical audit has not been performed.
