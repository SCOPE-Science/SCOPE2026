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

## Actual reproducibility checks

Run `python3 verify_deformations.py` with the Python standard library. The program checks every ordered basis triple for the polynomial sandwich products at each scalar parameter of F2 and F3, in ranks 2 and 3. It checks the full family of annihilator-pair probes that distinguish the displayed cocycle classes. Expected final line: `RECTANGULAR_BAND_DEFORMATIONS_OK`.

The uniform proof of associativity, injectivity into HH², generic determinant, and radical cube zero is given in RESULT.md. Finite checks cannot prove statements for arbitrary ranks and fields. No independent validation has been performed.
