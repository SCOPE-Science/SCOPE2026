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
The proof was checked symbolically from the quotient stabilizer condition and the Reid--Tai specialization. `verify_isolated_totient.py` exhaustively enumerates the relevant integer triangles for every \(2\le r\le150\), checks coprimality directly, confirms the three exact counting formulas, and checks the explicit canonical-boundary parametrization. The script prints `VERIFY_OK`. The finite computation is a regression check only; the infinite result rests on the written proof.
