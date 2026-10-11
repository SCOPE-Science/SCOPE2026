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
The proof was replayed symbolically for an arbitrary integer \(m\ge2\).

For the positive unit ball of
\[
N_m(r)=\max_q\sum_{j\ne q}|r_j|,
\]
every vertex with a zero coordinate lies on a simplex coordinate face, so its only nonzero possibilities are the standard basis vectors. A full-support vertex must activate all \(m+1\) facet inequalities; their normal matrix is invertible, forcing the unique point \((1/m,\ldots,1/m)\). This establishes the complete relevant vertex list.

Among at most \(m\) chosen nonzero vertices, one standard-basis index is missing. The corresponding facet contains all of them, including the full-support vertex. Maximizing each slice functional at one such vertex and using coordinate slices of \(c_0\) reduces the convex-combination problem to the known \(\mathrm{P3}\) property of \(c_0\). Reassembly gives a point whose coordinate norms are exactly the convex average of the maximizing vertices, hence a norm-one point on the common facet.

For the obstruction, an element of the \(i\)-th coordinate slice has \(i\)-th coordinate norm greater than \(1-\alpha\). Every different coordinate is smaller than \(\alpha\), because an \(N_m\)-constraint can be chosen that contains both coordinates. Averaging all \(m+1\) such slices gives the uniform bound
\[
\|z\|\le\frac{m(1+m\alpha)}{m+1}<1
\]
for \(0<\alpha<m^{-2}\). Thus the bad convex combination misses the sphere.

No finite computation is used to infer the arbitrary-\(m\) result. The result does not verify the analogous \(\mathrm{P2}^{(m)}\) hierarchy, classification of all separating spaces, or optimality of the quantitative radius.
