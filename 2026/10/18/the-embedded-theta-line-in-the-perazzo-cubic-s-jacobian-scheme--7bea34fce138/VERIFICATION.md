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

## Reproducibility
The supplied `verify.py` uses only the Python standard library. Run `python3 verify.py` from the extracted package; its expected success marker is `VERIFY_OK`.

## Computations performed
The polynomial identities \(f=uL_1+vL_2\), \(\Delta u=x_2L_1-x_1L_2\), \(\Delta v=x_0L_2-x_1L_1\), and all five gradient formulas are checked over the integers. The checker enumerates every homogeneous multiple of the five quadratic generators through degree seven (characteristic \(101\)), and through degree five (characteristics \(3\) and \(5\)), and performs exact finite-field row elimination. Every resulting graded quotient dimension matches the theorem.

## Proof limits
Finite modular computations do not prove the formula for all degrees or all fields. The written proof establishes those claims by an injective graded free presentation over \(k[x_0,x_1,x_2]\), identifies the presented module as an ideal of the conic ring, proves the primary decomposition and saturation, and computes the Hilbert series formally. Neither the checker nor this note constitutes independent review.
