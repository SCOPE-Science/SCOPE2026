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

Put
\[
c_\beta=\frac{1-\beta}{\beta},
\qquad
M_2=\sqrt{1+c_\beta^2}.
\]
The unit ball is an octagon with vertices
\[
(\pm1,\pm c_\beta),\qquad(\pm c_\beta,\pm1).
\]
Because Euclidean squared norm is strictly convex along each edge,
\[
E(z)\le M_2N_\beta(z)
\]
with equality for nonzero \(z\) exactly on vertex rays.

For
\[
\frac12<\beta<\frac1{\sqrt2},
\]
\[
N_\beta(z)\le E(z)
\]
with equality exactly on coordinate-axis rays. Hence an extremizing unit pair must consist of vertices and must have both sum and difference on coordinate axes. After a signed-coordinate symmetry, this is exactly
\[
((1,c_\beta),(1,-c_\beta))
\]
up to order and signs.

For
\[
\frac1{\sqrt2}<\beta<1,
\]
writing \(t=\min\{|u|,|v|\}/\max\{|u|,|v|\}\) gives
\[
\frac{N_\beta(u,v)}{E(u,v)}
=
\frac{\max\{1,\beta(1+t)\}}{\sqrt{1+t^2}}
\le\sqrt2\,\beta,
\]
with equality exactly at \(t=1\), namely on diagonal rays. Thus an extremizer must consist of vertices whose sum and difference are both diagonal. After symmetry, this is exactly
\[
((1,c_\beta),(c_\beta,1)).
\]

At \(\beta=1/\sqrt2\), equality in \(N_\beta\le E\) occurs on axes and diagonals, giving the union of the two classes.

The numerical values coincide with the classical Example 4.4 formulas. No numerical sampling, nonexhaustive enumeration, or external certificate is used as proof.
