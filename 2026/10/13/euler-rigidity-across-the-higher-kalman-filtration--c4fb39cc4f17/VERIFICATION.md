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
The checker uses the coordinate model
\[
L=\langle e_1,\ldots,e_d\rangle.
\]
For every
\[
2\le n\le30,\qquad 1\le d<n,\qquad 1\le s\le d,
\]
it enumerates all ordered off-diagonal matrix units
\[
E_{ij},\qquad i\ne j,
\]
and applies the invariant-subspace criterion directly.

For \(s<d\), every matrix unit is accepted. For \(s=d\), it rejects exactly those with source index in \(L\) and target index outside \(L\), confirming that the rejected count is
\[
d(n-d).
\]

Adding the Euler characteristic \(n\) of the diagonal projective fixed component gives the claimed formulas.

The checker also uses weights
\[
1,2,4,\ldots
\]
and verifies on \(2\le n\le20\) that all ordered off-diagonal differences are distinct, so the off-diagonal projective fixed loci are isolated coordinate points.

Finite checks do not prove the all-parameter theorem. The proof is the symbolic fixed-point classification and Euler-localization argument in `RESULT.md`.
