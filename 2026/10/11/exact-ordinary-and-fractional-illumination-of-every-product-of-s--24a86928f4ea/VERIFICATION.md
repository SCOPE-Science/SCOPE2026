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
\Sigma_d=\{x_j\ge0,\ \sum_jx_j\le1\},
\]
the vertex tangent-cone interiors are
\[
T_0^\circ=\{u:u_j>0\ \forall j\}
\]
and
\[
T_i^\circ=\left\{u:u_j>0\ (j\ne i),\ \sum_ju_j<0\right\}.
\]
These are pairwise disjoint by direct sign comparison.

For a product, the tangent cone at a product vertex is the Cartesian product of the factor tangent cones. Hence a single direction cannot belong to the interior tangent cones of two distinct product vertices. This proves the exact vertex lower bound for ordinary illumination. The same pairwise-disjoint illuminating-direction sets at the vertices give the fractional lower bound by summing the mandatory unit weights.

One interior tangent direction at each vertex illuminates every boundary face because every facet active at a face point is also active at any chosen vertex of that face. Therefore the lower bound is attained.

The fixed-dimension gap uses
\[
d+1\le2^d
\]
for every \(d\ge1\), and
\[
d+1\le3\cdot2^{d-2}
\]
for every \(d\ge2\), the latter with equality only at \(d=2\).

`verify.py` checks deterministic cone memberships in dimensions through eight and exhaustively verifies the partition maximization through dimension twelve. These are regression checks only; the theorem itself is proved symbolically above.
