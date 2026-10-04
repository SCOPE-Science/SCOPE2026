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

The packaged checker `verify_example67_nonnormal.py` uses exact rational Gröbner-basis arithmetic. It reconstructs the elimination kernel of the graph parametrization, dehomogenizes the complete kernel on \(X=D=1\), and verifies equality with
\[
(Y-CZ,\;W-BZ^2,\;C^2-ABZ^2).
\]
It then checks the obstruction \(C\notin ZR\), the normalization substitution \(C=ZT\) with \(T^2=AB\), and the Jacobian equations defining the two singular strata.

The exact conductor equality \((R:S)=(Z,C)\) is completed by the algebraic quotient argument written in `RESULT.md`: modulo \(Z\), the image of \(R\) is \(k[A,B]\), while the normalization contains the independent class \(T\) satisfying \(T^2=AB\). Thus an element whose product with \(T\) returns to \(R\) must vanish modulo \((Z,C)\).

A successful replay prints `VERIFY_OK`. The checker establishes the stated chart-level algebra; it does not certify any unclaimed global normalization or characteristic-two statement.
