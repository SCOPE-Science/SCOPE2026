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

Run `python verify.py` from the extracted package. The checker uses only the Python standard library and exact rational arithmetic, reconstructs the SSPRK stability matrix via direct matrix powers, checks several rational rates and steps against the derived formulas, and prints `VERIFY_OK` if all assertions pass. This execution produced `VERIFY_OK`.

The mathematical proof itself derives the complete two-state projector formula and the three-state polynomial matrix for every allowed rate and step. The key universal impossibility follows from the contradiction between \(v\ge 4(z-1)/(3z^2)\) and \(v\le1/z\) when \(z>4\); finite checker samples are not substituted for this argument. At \(z=4\) both bounds force a unique tableau and direct substitution yields identity. The accuracy or positivity of intermediate stages is not certified; no external audit has been performed.
