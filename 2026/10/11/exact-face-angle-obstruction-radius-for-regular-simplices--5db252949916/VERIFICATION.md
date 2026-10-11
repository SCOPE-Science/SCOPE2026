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

Represent a regular simplex by the \(n+1\) standard coordinate points in their affine hyperplane. Face-direction spaces are spanned by coordinate differences.

For two positive-dimensional faces \(I,J\), exact rank calculations give
\[
L_I\cap L_J=\{0\}
\quad\Longleftrightarrow\quad
|I\cap J|\le1.
\]

If \(I\cap J=\varnothing\), the two direction spaces are orthogonal. If \(I\cap J=\{p\}\) and the face dimensions are \(r,s\), bases anchored at \(p\) have Gram blocks
\[
I_r+J_r,\qquad I_s+J_s
\]
and cross block
\[
J_{r\times s}.
\]
Since
\[
(I_r+J_r)^{-1}=I_r-\frac1{r+1}J_r,
\]
the largest squared normalized inner product is
\[
\frac{rs}{(r+1)(s+1)}.
\]

The exact checker exhaustively enumerates every positive-dimensional face pair for
\[
2\le n\le6,
\]
using integer matrix rank to verify the intersection criterion. It then compares every admissible dimension pair \((r,s)\) with the closed formula by exact rational arithmetic for
\[
2\le n\le100.
\] It confirms that the maximum is attained exactly at
\[
r+s=n,
\qquad
|r-s|\le1.
\]
It also checks
\[
1-c_n^2
=
\frac{n+1}{(r+1)(s+1)}
\]
and the resulting formula for \(M_n\).

The finite enumeration is not the proof of the all-dimensional claim; it is a replayable check of the analytic argument.

The verification does not test whether the sufficient radius inherited from Proposition 4.3 is globally minimal, because no such minimality claim is made.
