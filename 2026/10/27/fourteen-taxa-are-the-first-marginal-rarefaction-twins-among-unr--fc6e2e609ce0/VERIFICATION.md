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
# Verification record

The executable `verify.py` depends only on Python's standard library and the included `witness.json`. The run recorded in `verification_output.txt` passed: shape census for 3–14 leaves; injective moment-plus-two-tip-variance signatures for 3–13 leaves; identification of the three possible 14-tip collision pairs; exact 14-tip law comparison on 16,384 subsets per candidate; independent witness validation; and the unique matching pair of distinct canonical shapes.

The output records a 69-term exact integer coefficient array with SHA-256 `39dd8ac22976f34cecc7184c4196f401cf3de782053cfc939bb17ff8f397759d`. Finiteness of the census, absence of arbitrary weights, and lack of independent validation are material limitations. No claim of proof beyond fourteen tips is made.
