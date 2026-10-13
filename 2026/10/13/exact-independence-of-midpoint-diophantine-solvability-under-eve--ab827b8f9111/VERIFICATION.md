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

# Verification record

A reproducible exact-arithmetic checker is included as `verify.py` (stdlib only). Run it alongside the included `verify-output.txt` for a comparison. Actual checks: direct nonnegative Diophantine enumeration versus inverse-parity condition for 1,387 coprime pairs, independent direct checks for 81 squared pairs, complete reduced residue classes for 30 odd moduli from 3 to 61, and several complete higher even-power moduli (including whole joint vectors).

The exact claim for every odd modulus and arbitrary finite sets of even exponents is proved mathematically in `RESULT.md`: inverse parity; fixed-point-free reflection; uniform square-lift counts. Finite checks and output logs do not prove universality. Full text of the motivating 26-page paper was inaccessible; overlap beyond the accessible abstract and indexed excerpt cannot be excluded. No independent audit or validation has been performed.
