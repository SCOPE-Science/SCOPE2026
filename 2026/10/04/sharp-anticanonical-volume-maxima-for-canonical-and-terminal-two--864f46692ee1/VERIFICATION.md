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

The universal inequalities and equality cases are established by symbolic analysis of the Reid--Tai feasible region and exact derivatives of the anticanonical-volume function.

`verify_volume_two_heavy.py` is an independent exact-rational regression check. It enumerates the canonical and terminal regions for every \(2\le r\le100\), computes the rational volume exactly, and verifies the claimed maxima and complete equality sets. Its executed output is:

`VERIFY_OK r=2..100`

The finite sweep is not used to infer the infinite theorem. Independent audit has not been performed.
