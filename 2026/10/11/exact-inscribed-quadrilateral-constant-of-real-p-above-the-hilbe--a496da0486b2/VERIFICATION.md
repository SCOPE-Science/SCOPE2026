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
Let
\[
D(a_1,a_2,a_3,a_4)
=
(a_i-a_j)_{i<j}.
\]
The exact endpoint checks are
\[
D^{*}D=4I-J,
\]
so
\[
\|D\|_{2\to2}=2,
\]
and
\[
\|D\|_{\infty\to\infty}=2.
\]
Riesz--Thorin interpolation therefore gives
\[
\|D\|_{p\to p}\le2
\]
for every \(2\le p\le\infty\), while \((1,1,-1,-1)\) attains ratio \(2\) for every \(p\). Hence
\[
\sum_{i<j}|a_i-a_j|^p
\le
2^p\sum_i|a_i|^p.
\]

Applying this coordinatewise to four unit vectors in \(\ell_p(I)\) gives
\[
\sum_{i<j}\|x_i-x_j\|_p^p
\le
4\cdot2^p.
\]
Power mean on the six pairwise distances yields
\[
\sum_{i<j}\|x_i-x_j\|_p^2
\le
24\left(\frac23\right)^{2/p}.
\]
The centered sign tetrahedron supported on three coordinates has all six distances equal to
\[
2\left(\frac23\right)^{1/p},
\]
so equality holds.

The bundled `verify.py` checks the matrix identity, endpoint norms, equality vector, tetrahedral objective at representative exponents, and numerical samples of the scalar inequality. These samples are supplementary; the all-\(p\) proof is analytic.

No independent audit or independent validation has been performed.
