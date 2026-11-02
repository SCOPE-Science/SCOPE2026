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

# Reproducibility

Execute `python verify.py` using standard-library Python 3. The checker enumerates every admissible ordered triple and every target pair for each of the 23 explicitly listed moduli. It compares all 86,504 target fibers to the independently implemented prime character formula and checks total triple counts. Its successful final line is `VERIFY_OK full_moduli= 23 target_fibers= 86504`.

The enumerations include the exceptional field cases and higher-power and mixed-prime moduli. They are finite corroboration, not an exhaustive verification of all integers. The universal claims follow from the explicit conic count, rank-two lifting argument, and Chinese remainder theorem in RESULT.md. No external formal or independent validation was performed.
