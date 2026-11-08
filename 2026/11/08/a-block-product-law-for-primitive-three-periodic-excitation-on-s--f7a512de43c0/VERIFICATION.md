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

# Reproducible checks

Run `python3 verify_global.py` and `python3 verify_local.py` using Python 3, without external dependencies. The first program directly evaluates three GHM updates for every three-color configuration of ten explicitly constructed cacti and verifies equality with the local successor condition and with the closed count, including a zero-resonance control. The second program uses an independently implemented transfer over mod-three edge increments for every rooted cycle length 3 to 200 and separately enumerates vertex-color assignments for cycle lengths 3 through 10. Actual saved outputs are `global_output.txt` and `local_output.txt`.

The exact infinity-family argument is in `RESULT.md`. Finite enumerations validate examples and the dynamic program but do not establish the general theorem by themselves. No independent audit has been performed.
