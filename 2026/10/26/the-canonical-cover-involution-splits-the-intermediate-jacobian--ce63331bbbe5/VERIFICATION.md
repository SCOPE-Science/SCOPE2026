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

`verify.py` checks the Chern-class coefficient, Euler characteristic, Betti number, Lefschetz trace, and eigenspace dimension equations using exact integer arithmetic. It prints `VERIFY_OK` on success.

The script does not certify the geometric inputs: smoothness, weak Lefschetz, the local fixed-point index, and the topological Lefschetz theorem are used in their standard forms. The eight-fixed-point hypothesis comes from the cited construction. Independent audit and independent validation have not been performed.
