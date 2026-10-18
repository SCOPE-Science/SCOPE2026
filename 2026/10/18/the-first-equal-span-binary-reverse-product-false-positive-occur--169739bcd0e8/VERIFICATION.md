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

# Verification protocol

Run `python3 verify.py` in the extracted folder. The script enumerates every endpoint-anchored length-2-through-21 binary word modulo the reversal symmetry, computes exact bit-reversal products and all aperiodic autocorrelations, and rejects any outcome except the unique length-21 false-positive pair recorded in `RESULT.md`. It also checks the equality of the displayed products and the different support cardinalities.

The witness products have separately checkable exact integer factorizations in `RESULT.md`. The exhaustive assertion proves only the finite lower-bound and uniqueness claim in the stated domain; no infinite or unequal-length conclusion follows. The program uses standard Python only. No independent audit or external certification was performed.
