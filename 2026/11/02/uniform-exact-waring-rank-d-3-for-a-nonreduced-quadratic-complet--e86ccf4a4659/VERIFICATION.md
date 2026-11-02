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
# Verification and boundaries
Run `python verify.py` with SymPy installed. It checks six integer cases d=5,6,7,8,9,12 by exact symbolic differentiation and polynomial arithmetic and prints `VERIFY_OK`. The actual execution produced that output. The finitely many examples do not prove the theorem for all d. The argument for all integers d>=5 is the explicit apolar Hilbert–Burch construction plus the degree-d separator/conic-pencil contradiction in RESULT.md. The finite-root checks use the fact that characteristic is zero. Independent mathematical validation was not performed.
