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

The proof has two exact algebraic stages and one inequality stage.

For a norm-one cubic unit with polynomial \(X^3-DX^2+CX-1\), the square has coefficients
\[
(C,D)\longmapsto (A,B)=(C^2-2D,D^2-2C).
\]
Applying this map twice gives the published \(\eta_b\) polynomial coefficients at \(b=5\) and \(b=96\).

The field discriminants are recomputed from the source's prime-by-prime index formulas:
\[
D_{K_5}=-135,\qquad D_{K_{96}}=-2104.
\]
The fourth roots satisfy \(3<\gamma_5<4\) and \(12<\gamma_{96}<13\). If either were a proper prime power, Artin's inequality would give a field-discriminant upper bound below the corresponding exact discriminant, so both fourth roots are fundamental.

Replay with:

`python3 verify.py`

Expected output:

`VERIFY_OK cases=2 exact_fourth_powers=2 fundamental_units=2`

The script uses only exact integer arithmetic. It does not attempt a classification outside the two stated parameters.
