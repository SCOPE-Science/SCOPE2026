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

Run `python3 verify_hasse.py` and `python3 verify_quotient.py` from this directory with Python 3 (standard library only). The first constructs the full characteristic-seven residue-form Hasse matrix by explicit multinomial expansion and checks exact polynomial determinants, support blocks and specialized ranks. The second checks the algebraic group-action and quotient identities, the genus-three Hasse diagonal, and all prime-field projective points for the two singular parameter values.

Checks executed successfully with outputs `HASSE_OCTIC_21x21_BLOCK_DETERMINANT_AND_RANKS_OK` and `PGL2_7_QUOTIENT_GROUP_ACTION_SMOOTHNESS_AND_HASSE_OK`. Finite rational-point tests alone do not establish claims over the algebraic closure; the mathematical proof uses polynomial identities, the gradient criterion and Deuring–Shafarevich. No independent mathematical validation or historical uniqueness certification was performed.
