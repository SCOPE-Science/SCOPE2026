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

# Verification and scope

The theorem is proved in `RESULT.md` by a partition valuation argument; the proof does not rely on enumeration. `CHECK.py` is an independent rational-arithmetic coefficient check using Python's standard library. It generated `VERIFY_OK 206` from nine prime choices and genera up to thirty. The test compares prime-integrality, strict vanishing above the claimed index and the nonzero leading residue. Finite cases are not an exhaustive check of the quantified infinite family. The input Faber--Pandharipande generating identity is taken from the published literature, not independently reproved here. The original source's valuation framework is essential, and historical originality beyond the inspected literature is unconfirmed.
