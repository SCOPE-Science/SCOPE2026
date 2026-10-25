---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the exact Cardinal–Pilaud realization SR(n)⊂1^perp with n≥3, Theorem 3(ii)/Lemma 19 provides f_n(X) as the sum of two consecutive-interval-pair indicators and proves the subset inequalities are irredundant. An exact inclusion–exclusion by maximal constant-color runs gives f_n(X)=2T_n−Σ Phi_n(ell_j)+Σ ell_j ell_{j+1} with T_n=n(n²−1)/6 and Phi_n(t)=t(t+1)(3n−t−2)/6. The merge identity Phi_n(u+v)−Phi_n(u)−Phi_n(v)=uv(2n−2−u−v)/2 bounds the splitting penalties; if one color has two runs the other one run, the positive split penalty gives strictness; if both have at least two, the split terms beat k(n−k)−A. This proves f_n(X)≥n k(n−k)/2 with equality exactly for proper prefixes/suffixes. The centered permutahedral facets are n*k(n−k)/2, hence sharp containment. Facet normals in 1^perp have norm sqrt(k(n−k)/n), giving centered ball radius n/2 sqrt(n(n−1)) with exactly four endpoint contacts; two opposite facet pairs bound all possible balls and force c_1=c_n=0, and all other facet constraints are slack at the origin. Thus the set of inball centers has affine dimension n−3 (unique n=3, nonunique n≥4).

## originality

PASS

Best-of-knowledge originality credited to the all-rank sharp comparison of the strong rectangulotope facet height with the scaled permutahedral cardinality function, the equality classification, and incenter affine dimension. Exact-object primary source gives complete facet data but does not state the metric/containment theorem; later same-object literature is combinatorial. Searches across synonyms and Resultary found no distinct prior record of a dominating metric statement. The matching Resultary index result is the very record under review, not independent prior art. This is a qualified best-of-knowledge assessment, not a global priority certificate.

## value

PASS

Strong rectangulotopes are a natural infinite family encoding strong rectangulation flip graphs. The precise Euclidean inradius and n-fold permutahedral containment solve a canonical metric problem for the explicit realization, and the equality facet classification provides structural explanation. The n−3-dimensional center locus is a nontrivial complete affine-dimension classification distinguishing n=3 from every n≥4; it is not a low-rank experimental table nor an unmotivated numerical slice. The method yields a useful sharp submodular facet-function inequality not mechanically obtained by substituting parameters into the standard permutahedron.

The dated certificate retains the supplied scientific assessment, sources and limitations.
