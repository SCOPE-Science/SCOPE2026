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

# Reproducibility

Run `python3 check_phi.py` with Python 3 and its standard library. The checked source is bundled alongside this report. The output `VERIFY_OK` records 700 exact modular prime/semiprime witnesses, 25 exact prime/prime-square witnesses, and 118 computed values divisible by six. A separate brute-force enumeration of every nonempty subset for indices one through fourteen agreed with the Möbius formula. These are bounded checks only; the unrestricted theorem is established by the proof and Dirichlet's theorem. No independent audit or formal proof-assistant certification has been performed.
