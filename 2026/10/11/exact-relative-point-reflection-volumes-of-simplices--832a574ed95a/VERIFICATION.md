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

For the standard simplex
\[
\Delta_n=\operatorname{conv}\{0,e_1,\ldots,e_n\},
\]
the relative unit ball is
\[
M=\frac12(\Delta_n-\Delta_n).
\]
Rogers--Shephard equality gives
\[
\lambda_n(M)
=
\frac{\binom{2n}{n}}{2^n n!}.
\]

The polar satisfies
\[
M^\circ
=
\left\{
y:
\max(0,y_1,\ldots,y_n)
-
\min(0,y_1,\ldots,y_n)
\le2
\right\}
\]
and has vertices
\[
\pm2\,\mathbf1_S
\]
for nonempty \(S\subseteq\{1,\ldots,n\}\). Partitioning by the number of positive coordinates shows that each of the \(n+1\) sign-count layers has volume \(2^n\), hence
\[
\lambda_n(M^\circ)=(n+1)2^n.
\]

The largest determinant of \(n\) generators from \(M\) is \(2^{-n}\): after doubling, the columns are reduced incidence vectors \(e_i-e_j\), and total unimodularity bounds every maximal minor by \(1\). Therefore the largest inscribed cross-polytope has volume \(1/n!\).

For the polar, separate convexity of the absolute determinant reduces the maximum to the vertices. Factoring \(2\) from each column leaves a zero-one matrix, so the determinant maximum is
\[
2^nD_n.
\]
The largest polar cross-polytope therefore has volume
\[
\frac{4^nD_n}{n!}.
\]
The parallelotope--cross-polytope polar volume product
\[
\frac{4^n}{n!}
\]
then gives the minimum circumscribed parallelotope volume \(1/D_n\).

`verify.py` checks the polytope volumes, determinant maxima, and all four resulting normalization formulas in dimensions \(2,3,4\). Those finite checks are diagnostic only; the proof in arbitrary dimension is the exact argument above.
