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

# Reproduction notes

Run `python3 verify.py` from this directory. The script checks exact multinomial enumeration against the formula for two-, three-, and four-category finite profiles; verifies odd/even signs; and checks symbolic irrational three-category pair-independence with nonindependence of the triple. The expected successful output reports 320 checks. The unrestricted proof uses the character-moment identity and simple algebra; no finite set of tests is claimed to establish a universal law. Only the self-review was performed; independent audit remains not performed.
