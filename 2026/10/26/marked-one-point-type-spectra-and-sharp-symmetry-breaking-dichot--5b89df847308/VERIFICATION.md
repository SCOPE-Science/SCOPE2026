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

# Finite verification

Run `python3 artifacts/verify.py` with the Python standard library; the recorded output is in `artifacts/verification-output.txt`.

The checker enumerates all labeled finite posets with one through five vertices, all admissible one-point extensions over each, and the canonical labeled three-point rotation-class signatures. It also computes the two-level-complete subset spectrum directly, checks the mixed/reversal quotient rules, both extremal equality conditions, and explicit antichain fiber counts through ten parameters. These are finite corroborations, not proofs of the unrestricted theorem.

The full theorem uses the published finite-rotation and extension results cited in the mathematical proof. No independent mathematical audit has been performed.
