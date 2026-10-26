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

Run `python3 verify.py` from the extracted package directory. The actual execution reported:

`VERIFY_OK rational_parameter_cases=42 crossover_cases=15`

The checker confirms the characteristic identity \(p(1+w)=w^2-s^2\) by exact rational arithmetic for 42 parameter pairs, including exact factorization at the equality locus. It numerically brackets all three distinct real eigenvalues, tests the sign of the dominant nonstationary eigenvalue, and reconstructs the stationary law for these cases. Fifteen additional finite instances check consistency of the critical-window phase weight and scaled spectral gap with the stated asymptotic expressions.

Finite computations do not certify the theorem for all real parameters or all inverse temperatures. That universal conclusion follows from the sign-changing polynomial identity, Vieta's formulas, and the explicit asymptotic root expansion in RESULT.md. Independent audit is not performed.
