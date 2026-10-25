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
# Verification and limits

Run `python3 verify_cactus_standalone.py` with Python 3.10+ from the unpacked files. No nonstandard packages are required. `verification_output.txt` is a record of the local deterministic execution against exactly this included program. It reports 1,211 complete-subset comparisons for cacti of orders at most 13, plus explicit seven-vertex examples. These finite cases do not prove the all-orders theorem. The proof is an induction using the three vertex messages and the constant-width cycle closing transfer. No independent audit has been conducted.
