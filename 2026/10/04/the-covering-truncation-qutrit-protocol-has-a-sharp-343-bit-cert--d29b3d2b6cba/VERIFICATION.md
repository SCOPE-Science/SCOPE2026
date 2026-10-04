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

The scientific checks for this result are reproducible with `verify.py`. The script performs exact rational and integer comparisons for the chosen parameters and for every finite inequality used in the family-wide 342-bit exclusion. It also checks the sign condition used to prove monotonicity of the optimized fallback product on the threshold range.

The proof uses the source construction only under the stated admissibility conditions. It does not verify or claim optimality over unrelated qutrit simulation protocols, improved projective-space coverings, or variable-length communication schemes.
