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

The proof is reduced to a finite rational polyhedral certificate.

Write
\[
K
=
\{x:|x_j|\le1,\ \|x\|_1\le2\}
\]
and
\[
K_{1/13}
=
\{x:|x_j|\le12/13,\ \|x\|_1\le25/13\}.
\]
The verifier represents these by their fourteen linear inequalities.

The six centers are
\[
(1,-1/4,-1/4),\quad
(-1,1/4,1/4),\quad
(1/4,1,-1/4),
\]
\[
(-1/4,-1,1/4),\quad
(1/4,1/4,1),\quad
(-1/4,-1/4,-1).
\]
Exact checks confirm that each is on
\[
\partial K
\]
and that each pairwise difference is outside
\[
\operatorname{int}K.
\]

The boundary of \(K\) is decomposed into six square facets and eight triangular facets. Each facet has an explicit two-dimensional rational parametrization. On a fixed facet, nonmembership in one translated inset
\[
z_i+K_{1/13}
\]
is a disjunction of fourteen half-plane violations. The verifier recursively branches through those disjunctions for all six centers and clips the facet polygon by exact rational line intersections.

If an uncovered boundary point existed, it would survive in at least one branch after all six centers. The final branch set is empty on each of the fourteen facets. Hence
\[
\partial K
\subset
\bigcup_{i=1}^6(z_i+K_{1/13}).
\]

Since
\[
K_{1/13}\subset\operatorname{int}K,
\]
this gives the strict boundary cover required by the blocking criterion.

Running the packaged script prints `VERIFY_OK`, the six exact centers, the clearance \(1/13\), and fourteen facet reports whose final surviving-branch count is zero.

The checker establishes only the finite coverage and separation certificates. The implication from those certificates to a blocking configuration is the cited geometric boundary-cover lemma. No lower bound \(b(K)\ge6\) is claimed.
