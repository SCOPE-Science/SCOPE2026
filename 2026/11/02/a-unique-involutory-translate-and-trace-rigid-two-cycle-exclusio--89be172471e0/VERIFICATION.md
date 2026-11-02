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

# Reproduction and limits

Run `python3 verify.py` using only the Python standard library. The code builds quotient fields over \(\mathbb F_2\), confirms their moduli are irreducible, and computes original polynomial maps and two successive iterations directly. It checks the predicted counts for all additive translates at field degrees 3, 5, 7, and 9, plus selected constants at degrees 11 and 13. Successful execution produces `VERIFY_OK degrees=6 translate_cases= 694 state_checks= 351296 exceptional_involution_points= 10920`.

The calculations do not certify the infinitely many fields. Universal correctness rests on the exponent-inverse conjugacy, characteristic-two trace argument, and exact period-two exclusion proved in RESULT.md. No external or independent audit has been performed.
