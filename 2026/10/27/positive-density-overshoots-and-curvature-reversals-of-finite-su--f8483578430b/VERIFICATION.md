---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The proof of the block guarantee is analytic. It uses the convex recurrence on positive successive ratios and its equality case, together with the dominant-pole argument excluding a one-signed error tail. The truncated geometric example has an exact coefficient formula establishing sharpness for every maximum step.

Run `python3 verify_sharp_blocks.py` to check the sharpness example in exact rational arithmetic for maximum steps 2 through 9 and three rational geometric parameters. The program uses the renewal recurrence independently of the asserted explicit formula to compute the masses, then compares the values and signs. These finite checks do not prove the block theorem or establish priority. The earlier `verify_renewal.py` and recorded output remain evidence of finite sign checks for the earlier positive-density formulation only.
