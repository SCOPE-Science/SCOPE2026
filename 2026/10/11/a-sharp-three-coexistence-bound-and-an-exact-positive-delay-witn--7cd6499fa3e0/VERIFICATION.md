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

# Verification record

The claim concerns equilibrium *existence and counting*, not nonlinear delay-equation stability. Let \(z=\lambda V/r\) and use the reconstruction and scalar polynomial in RESULT.md. The polynomial-equivalence check is symbolic. The bound uses polynomial degree plus signs at the two physical endpoints; those universal inequalities must not be interpreted as finite enumeration. The sharpness uses rational sign changes at four separate intervals and the implicit-function theorem for simple roots; the checker independently evaluates all exact signs with rational arithmetic.

For reproducibility run `python check_equilibria.py` with Python 3 and SymPy as specified in `requirements.txt`; the expected terminal marker is `CHECK_OK`. The program also verifies the source model's four steady-state residuals after reconstruction (three identically vanish and the fourth is equivalent to the scalar condition). A passing computation checks these nonstandard identities and the exact instance, not the general mathematical reasoning in isolation.

No stability, basin or epidemiological calibration claim is tested. No independent external mathematical audit has been performed. The literature comparison draws on the cited 2016, 2020 and 2023 primary texts and is limited by the completeness of accessible literature.
