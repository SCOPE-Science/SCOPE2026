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
The packaged checker `artifacts/verify.py` constructs the alternating bracket
\[
[e_1,e_2,e_3]=e_1
\]
over prime fields.

It first verifies the \(3\)-Lie Fundamental Identity on every ordered basis quintuple.

For a general \(3\times3\) matrix \(T\), it tests the adjoint embedding-tensor identity
\[
[Tx,Ty,Tz]=T([Tx,Ty,z])
\]
on every ordered basis triple.

It exhaustively checks every matrix over
\[
\mathbf F_2
\qquad\text{and}\qquad
\mathbf F_3
\]
against the rank-theoretic criterion from `RESULT.md`.

The totals are
\[
93
\qquad\text{and}\qquad
965,
\]
with rank profiles
\[
(1,49,42,1)
\]
and
\[
(1,338,624,2).
\]

The checker also verifies the closed counting and rank formulas for
\[
q=2,3,5,7.
\]

It returns `VERIFY_OK`.

Finite exhaustive checks are replay evidence. The arbitrary-field result follows from the volume-form proof in `RESULT.md`.
