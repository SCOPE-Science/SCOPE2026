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

Reproduction: run `python3 verify_crown.py` in this directory. The script is standalone Python 3 and should print `VERIFY_OK`, followed by exact minor, face, orbit, and intersection statistics. Its full exact-arithmetic checks certify the stated finite lattice and fan counts. The circuit-to-Segre identification and standard toric smoothness/normal-fan correspondence are supported by the written integral proof in `RESULT.md` and are not replaced by finite testing. There is no separate independent audit.
