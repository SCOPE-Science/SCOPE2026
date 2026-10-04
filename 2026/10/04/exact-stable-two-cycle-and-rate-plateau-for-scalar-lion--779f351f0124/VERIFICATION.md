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
The proof reconstructs the exact scalar Lion ordering and exhausts nontrivial period-two orbits in the nondegenerate regime \(q\ne2\), then specializes to \(0<q<2\).

`verify.py` checks exact rational and floating-point instances, the sign margin, the Jacobian factor, the rate plateau, and the \(q=1\) nominal-bound crossing. Its bounded negative-case grid search is only a transcription guard; nonexistence is proved analytically in `RESULT.md`.
