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

Run `python3 verify_list_profiles.py` (Python 3.10+, standard library only). The checker verifies the three codebook sizes and minimum distances, enumerates every near pair, triangle and four-clique, confirms uniqueness of qualifying four-clique centers and computes each spectrum from binomial moments. Expected output ends in `VERIFY_OK`. An auxiliary full-cube integer array enumeration of all radius-five and radius-six balls was run and independently matched each spectrum; it is not needed for the standalone proof. The exact computations are finite and establish no unenumerated larger-case claims.
