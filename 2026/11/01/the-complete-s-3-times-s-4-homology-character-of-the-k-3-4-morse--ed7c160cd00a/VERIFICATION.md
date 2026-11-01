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

Run `python3 verify.py` using Python 3 and its standard library. The program enumerates every rooted forest face, checks all five exact mod-two boundary ranks, determines all 144 signed Lefschetz traces, and computes exact Specht inner products. The saved `VERIFICATION_OUTPUT.txt` is the actual output of that program and ends in `VERIFY_OK`. No infinite-parameter claim is made. Rational boundary rank is inferred from exact mod-two lower bounds together with the chain-condition dimension upper bounds; this argument is explained in RESULT.md. Independent audit remains not performed.
