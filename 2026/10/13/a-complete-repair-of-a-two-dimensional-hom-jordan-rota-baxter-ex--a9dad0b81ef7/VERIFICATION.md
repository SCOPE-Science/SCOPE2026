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
The packaged checker `artifacts/verify.py` reconstructs the Hom-Jordan and Rota–Baxter equations from the multiplication table rather than hard-coding the final classification.

For
\[
R=
\begin{pmatrix}
x&y\\
z&w
\end{pmatrix},
\]
it verifies symbolically that
\[
R\alpha-\alpha R
\]
is controlled by
\[
(\lambda-1)y,\qquad(1-\lambda)z.
\]

It computes the Rota–Baxter defect on the three unordered basis pairs and recovers the five equations used in `RESULT.md`.

For the printed Example 2.2 map
\[
R(e_1)=b e_2,\qquad R(e_2)=0,
\]
the product defect is verified to vanish identically, while the twist defect equals
\[
(1-\lambda)b e_2.
\]

The checker also verifies the Hom-Jordan identity symbolically for the displayed multiplication.

Finally, it exhaustively enumerates all parameters and all \(2\times2\) maps over
\[
\mathbf F_3,\quad\mathbf F_5,\quad\mathbf F_7.
\]
At each odd field it finds \(q\) operators for \(\lambda=0\), \(q\) for \(\lambda=1\), and one for every other parameter, hence
\[
3q-2
\]
parameter-operator pairs.

The checker returns `VERIFY_OK`.

Finite enumeration is a replay check. The arbitrary-field theorem for \(\operatorname{char}K\ne2\) is proved by the symbolic case split in `RESULT.md`.
