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
The bundled checker `artifacts/verify.py` reconstructs the multiplication table
\[
e_1^2=(1-\varepsilon)e_1+\varepsilon e_2,\qquad
e_1e_2=\frac12(e_1+e_2),\qquad
e_2^2=e_2.
\]

It symbolically verifies, for
\[
u=e_1-e_2,\qquad
v=e_1+(2\varepsilon-1)e_2,
\]
that
\[
u^2=-\varepsilon u,\qquad
uv=0,\qquad
v^2=\varepsilon(-u+2v).
\]

It verifies the baric rescaling to
\[
x^2=-x,\qquad xy=0,\qquad y^2=-x+2y,
\]
and checks the complete automorphism and natural-basis equations.

As replay evidence it exhaustively enumerates the relevant maps and ordered bases over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,\quad\mathbf F_{11}.
\]
For every tested field, the zero parameter has no ordered natural basis, each nonzero parameter has exactly \(2(q-1)^2\) ordered natural bases, and the fixed algebra has exactly one automorphism.

The checker returns `VERIFY_OK`.

Finite enumeration is replay evidence only. The arbitrary-field theorem follows from the symbolic identities and the multiplication-kernel proof in `RESULT.md`.
