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

# Verification information
The full proof is in `RESULT.md`. Run the bundled standalone script using `python verify_counts.py` (no nonstandard libraries). The script independently computes ordered unit triples by direct iteration in small cases, by quadratic-sum convolution for every tested case, and from the closed formulas, comparing all output fibers, total mass, and local sharp minimum values. The expected final line starts with `VERIFY_OK` and indicates 575 profiles. This is finite corroboration only: general correctness uses the character identities, inclusion–exclusion, the lifting bijection, and CRT proved in the result. Independent external validation was not performed.
