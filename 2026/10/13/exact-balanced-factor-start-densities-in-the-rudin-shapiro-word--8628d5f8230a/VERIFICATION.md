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

Run `python3 verify.py` with Python 3 standard library. It checks the base-four residue classification for every start in a prefix of length 131072 and for k=1 through 6, with independent binary-digit Rudin–Shapiro generation; it verifies the crucial prefix inequalities and level-set formulas at m=0 through 6. The formal proof for all indices and all k is the induction and substitution-frequency argument in RESULT.md. Neither the finite output nor an external solver supplies an infinite certificate.
