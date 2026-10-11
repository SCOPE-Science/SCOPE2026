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

Let
\[
F=(e_1,e_1,e_2),
\qquad
G=(e_1,e_1+e_2,2e_1+e_2).
\]
For every partition of the three indices, the mixed frame operator is one of
\[
\begin{pmatrix}6&3\\3&2\end{pmatrix},
\quad
\begin{pmatrix}6&2\\2&1\end{pmatrix},
\quad
\begin{pmatrix}2&1\\1&2\end{pmatrix},
\quad
\begin{pmatrix}2&0\\0&1\end{pmatrix}.
\]
Their spectra are, respectively,
\[
\{4-\sqrt{13},4+\sqrt{13}\},
\]
\[
\left\{\frac{7-\sqrt{41}}2,\frac{7+\sqrt{41}}2\right\},
\]
\[
\{1,3\},
\qquad
\{1,2\}.
\]
Thus every original weave is a frame.

The individual frame operators are
\[
S_F=
\begin{pmatrix}2&0\\0&1\end{pmatrix},
\qquad
S_G=
\begin{pmatrix}6&3\\3&2\end{pmatrix}.
\]
Exact inversion yields
\[
\widetilde F=
\left(\frac12e_1,\frac12e_1,e_2\right)
\]
and
\[
\widetilde G=
\left(
\frac23e_1-e_2,
-\frac13e_1+e_2,
\frac13e_1
\right).
\]
The mixed dual family for
\[
\sigma=\{1,2\}
\]
is
\[
\left(\frac12e_1,\frac12e_1,\frac13e_1\right),
\]
whose frame operator is
\[
\begin{pmatrix}11/18&0\\0&0\end{pmatrix}.
\]
It therefore has no positive lower frame bound.

For the common-frame-operator repair, if every constituent has the same frame operator \(S\), the canonical-dual weaving energy is the original weaving energy evaluated at \(S^{-1}x\). The bounds
\[
\frac{A}{\|S\|^2}
\quad\text{and}\quad
B\|S^{-1}\|^2
\]
follow immediately.

The verified public source arXiv:1709.05154v1 contains the claimed unconditional canonical-dual statement in Corollary 2.5, and v3 contains the same statement. All computations above are exact; no finite numerical experiment is used as evidence for an infinite claim.
