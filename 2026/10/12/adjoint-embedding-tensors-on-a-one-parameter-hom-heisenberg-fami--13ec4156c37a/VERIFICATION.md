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
The packaged checker `artifacts/verify.py` starts with the ordinary Heisenberg bracket
\[
[e,f]=c
\]
and the twist
\[
\alpha_\lambda=\operatorname{diag}(1,\lambda,\lambda).
\]

It verifies directly that \(\alpha_\lambda\) is a Lie endomorphism and constructs the Yau-twisted bracket
\[
[e,f]_\lambda=\lambda c.
\]

For a general \(3\times3\) matrix \(T\), it reconstructs both equations
\[
T\alpha_\lambda=\alpha_\lambda T
\]
and
\[
[T(x),T(y)]_\lambda=T([T(x),y]_\lambda)
\]
on all ordered basis pairs.

It exhaustively tests every matrix for every parameter over
\[
\mathbf F_2
\]
and
\[
\mathbf F_3.
\]

The fiber counts are
\[
32,\quad48
\]
over \(\mathbf F_2\), and
\[
243,\quad333,\quad27
\]
over \(\mathbf F_3\).

The exact rank profiles are also matched in every fiber.

Finally, the checker verifies the closed rank formulas for
\[
q=2,3,5,7.
\]

It returns `VERIFY_OK`.

Finite enumeration is a replay check. The arbitrary-field theorem follows from the symbolic case analysis in `RESULT.md`.
