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
The packaged checker `artifacts/verify.py` reconstructs the algebra and representation from first principles.

For the Leibniz bracket
\[
[x,y]=x_2(y_1+y_2)e_1,
\]
it builds
\[
L_x^\ast
\]
and
\[
-L_x^\ast-R_x^\ast
\]
and expands both relative Rota–Baxter identities on all four ordered basis pairs.

It separately encodes the fourteen scalar equations printed in Example 2.3 of arXiv:2101.04831v1.

For
\[
R=\begin{pmatrix}-2&0\\2&0\end{pmatrix},
\qquad
S=\begin{pmatrix}-1&0\\2&0\end{pmatrix},
\]
all fourteen printed equations vanish, while the true \(S\)-defect at
\[
(e_1^\ast,e_1^\ast)
\]
is
\[
2e_1.
\]

For
\[
R=\begin{pmatrix}-2&-2\\2&0\end{pmatrix},
\qquad
S=\begin{pmatrix}-2&2\\2&0\end{pmatrix},
\]
all defining defects vanish, while the source's third printed equation has residual
\[
-8.
\]

The checker also verifies symbolically the repaired branch
\[
R=S=t\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
\]
and exhaustively checks the branch over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7,
\]
finding exactly
\[
q-1
\]
solutions in each case.

It returns `VERIFY_OK`.

The finite-field enumeration is a replay check. The branch theorem for arbitrary characteristic different from \(2\) is proved symbolically in `RESULT.md`.
