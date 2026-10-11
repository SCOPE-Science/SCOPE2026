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

For a \(2\)-inner-product space, the defining nondegeneracy condition is
\[
\langle x,x\mid z\rangle=0
\quad\Longleftrightarrow\quad
x,z\text{ are linearly dependent}.
\]

Let \(a\ne0\) and \(b\ne0\), and define
\[
u=a\oplus2b,\qquad v=a\oplus b.
\]
If \(u=\lambda v\), the first component gives \(\lambda=1\), while the second gives \(\lambda=2\). Hence \(u,v\) are linearly independent.

The source's formula gives
\[
\langle u,u\mid v\rangle
=
\langle a,a\mid a\rangle_H
+
\langle2b,2b\mid b\rangle_K.
\]
Both terms are zero by the defining axiom in the component spaces because the relevant component pairs are linearly dependent. Thus the proposed direct-sum square is zero on an independent pair.

For ordinary real Hilbert spaces, the canonical comparison is
\[
\langle x,y\mid z\rangle_{\oplus}
=
\langle x,y\rangle_{\oplus}\|z\|_{\oplus}^{2}
-
\langle x,z\rangle_{\oplus}\langle z,y\rangle_{\oplus}.
\]
Its square is the Gram determinant
\[
\|x\|_{\oplus}^{2}\|z\|_{\oplus}^{2}
-
|\langle x,z\rangle_{\oplus}|^{2},
\]
which is strictly positive for linearly independent \(x,z\). Expansion yields cross terms that the componentwise source formula omits.

The earliest public source and the published source were checked at the defining axiom, formula (10), and the direct-sum theorem/proof. The proof is symbolic and uses no finite experiment, numerical approximation, or computational certificate.
