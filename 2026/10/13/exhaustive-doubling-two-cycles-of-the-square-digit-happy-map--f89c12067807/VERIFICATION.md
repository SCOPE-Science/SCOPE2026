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

The proof in `RESULT.md` is exact and infinite. The checker is a finite corroboration.

It exhaustively enumerates every base
\[
2\le b\le400
\]
and every two-digit integer \(X\) for which \(2X\) is also two-digit. It computes the digit-square map directly and retains exactly those pairs satisfying
\[
S_b(X)=2X,\qquad S_b(2X)=X.
\]
The observed set is compared with the predicted set
\[
b=5t+3,\qquad X=t b+(3t+2).
\]

The checker separately validates the explicit family through
\[
1\le t\le10000
\]
and checks the two algebraic branch substitutions and the carry obstruction numerically over a large integer grid.

Finite enumeration is not used to infer the universal statement. The universal statement follows from the carry dichotomy, the two exact cycle equations, and the factored elimination displayed in the proof.
