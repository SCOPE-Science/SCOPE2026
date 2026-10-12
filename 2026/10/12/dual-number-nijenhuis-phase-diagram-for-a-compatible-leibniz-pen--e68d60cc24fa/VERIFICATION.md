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
The packaged checker `artifacts/verify.py` reconstructs the compatible pencil
\[
\mu_{u,v}(e_2,e_1)=ue_1,
\qquad
\mu_{u,v}(e_2,e_2)=ve_1.
\]

It verifies the left Leibniz identity symbolically for arbitrary \(u,v\).

For a symbolic matrix
\[
N=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\]
it reconstructs all Nijenhuis torsion components and verifies that, for every nonzero \((u,v)\), the field-valued solution criterion is
\[
c=0,
\qquad
(a-d)\bigl(v(a-d)-ub\bigr)=0.
\]

It exhaustively checks every \(2\times2\) matrix for every projective parameter over
\[
\mathbf F_2,\quad\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7.
\]

The total projective-incidence counts are
\[
16,\quad54,\quad250,\quad686,
\]
matching \(2q^3\).

The exceptional-fiber rank profiles are
\[
(1,1,2),\quad(1,2,6),\quad(1,4,20),\quad(1,6,42),
\]
and every generic fiber has respectively
\[
(1,3,2),\quad(1,6,8),\quad(1,12,32),\quad(1,18,72).
\]

The checker verifies that any two distinct projective fibers intersect exactly in
\[
\{aI+bE_{12}\},
\]
and symbolically verifies
\[
(\mu_{u,v})_{aI+bE_{12}}=\mu_{au,\,bu+av}.
\]

It returns `VERIFY_OK`.

Finite enumeration is replay evidence. The arbitrary-field phase diagram and dual-number action follow from the symbolic proof in `RESULT.md`.
