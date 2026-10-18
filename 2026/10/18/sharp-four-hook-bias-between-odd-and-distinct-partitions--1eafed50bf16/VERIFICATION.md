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

The symbolic rational identity was checked with exact polynomial arithmetic in SymPy. A standalone independent Young-diagram enumeration at every integer from 0 through 26 checks the boundary table directly. The verifier also computes integer series through degree 160 to corroborate coefficient monotonicity, while the all-degree result is established by the coefficient pairing in RESULT.md. Run `python3 artifacts/verify.py` with SymPy installed. The verifier does not constitute an independent mathematical audit.
