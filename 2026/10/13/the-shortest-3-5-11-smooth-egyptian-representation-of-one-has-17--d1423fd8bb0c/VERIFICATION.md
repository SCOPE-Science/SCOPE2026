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

# Verification scope

The proof is wholly exact and elementary. The companion Python script performs rational arithmetic for the 14- and 15-term bounds, lists the three possible penultimate denominators, verifies their forced partners are nonintegral, and checks the 17 reciprocal sum with no floating-point arithmetic.

Run `python3 verify_egyptian.py` with Python 3 standard library. Its expected terminal result is `EXACT_EGYPTIAN_3_5_11_MINIMUM_17_OK`. The script checks finite facts only, and does not establish anything about every possible larger denominator by brute-force enumeration: that assertion follows from the maximal-reciprocal inequality in the written proof.

Independent validation has not been performed.
