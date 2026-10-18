---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For n≥3 rooted star with m=n-1 leaves, Sack tube definition and ατ cover differences imply full equation ∑y_i=M=n^(2n) with y_i=p_i-p0 and p0=-M/n constant on the affine span, so the affine map y preserves inherited Euclidean distances. Proper tubes are {0}∪S, ∅≠S⊊[m], and the complete halfspaces are ∑_{i∈S}y_i≥n^(2(|S|+1)). Projected singleton facet normal has length sqrt((m-1)/m); summing all radius-r constraints y_i≥n^4 gives r≤(M/m-n^4)sqrt(m/(m-1)), with equality forcing all center y_i=M/m and hence p0=-n^(2n-1), p_i=n^(2n-1)/(n-1). For k-subset face, normal norm sqrt(k(m-k)/m) and distance Dk=(kM/m-n^(2k+2))/sqrt(k(m-k)/m). qk=m/n^(2(m-k))<1/4; for k≥2, Dk/A>(7/8)sqrt(mk/(m-k))>sqrt(m/(m-1))>D1/A, so exactly m singleton facets touch; closed r=(n^(2n)-(n-1)n^4)/sqrt((n-1)(n-2)). The n=3 one-dimensional boundary is valid. Independent exact rational distance comparison checked all cardinalities for n=3..60 (1711 checks) and the squared closed formula.

## originality

PASS

The source Sack 2023/2025 constructs the poset associahedron by a general H-description and verifies tubings, but does not in the reviewed primary 12-page realization article compute Euclidean Chebyshev radii or incenter. Combinatorial permutohedron equality does not fix this exotic cardinality-weighted metric. Follow-up 2024 f-vector and stack-sorting work is combinatorial rather than metric. No stronger covered metric formula was established; an alternative generic symmetric generalized-permutahedron Chebyshev observation remains a residual risk. Resultary failed and is not a negative search.

## value

PASS

The rooted star is the elementary maximally symmetric branching poset; Sack’s high-exponent realization is a natural exact family. Computing its Euclidean Chebyshev center, all-rank closed inradius, and establishing only n−1 active singleton facets among 2^(n−1)−2 makes meaningful geometric data not obtainable from combinatorial permutohedral type. The all-n inequality separating constraints is substantive but elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
