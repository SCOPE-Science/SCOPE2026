---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: for every m,n>=2 the product of two simplices has rook-graph one-skeleton K_m square K_n. An affine functional takes additive values a_i+b_j; reordering each axis gives exactly Ferrers positive-sign diagrams D with descending row lengths, and every Ferrers diagram can be realized by explicit strict additive values. Generic section vertices are precisely crossed graph edges. For lengths lambda_i and column heights k_j, the count V=Σ lambda_i(n−lambda_i)+Σ k_j(m−k_j) telescopes using square increments to Σ_(i,j) in D(m+n+2−2i−2j). Thus every positive-weight antidiagonal cell is compulsory for equality and every negative-weight cell excluded; zero-weight cells are mutually incomparable, giving 1 generic maximizing Ferrers pattern if m+n odd and 2^min(m,n) if even. Summing positive row weights yields Σ_{i=1}^{min(m,n)}(floor((m+n+1)/2)−i)(ceil((m+n+1)/2)−i). Nongeneric or supporting sections admit generic perturbations with at least as many section vertices; the all-affine maximum follows. For square q, count q(q²−1)/3 vs unrestricted rook cut 2q floor(q²/4), ratio→2/3. Independently enumerated Ferrers lengths and maxima in small m,n and checked combinatorial identities; finite experiments are not used to infer the all-parameter theorem.

## originality

PASS

PASS best-of-knowledge: published simpotope triangulations, separating hyperplanes avoiding new cut vertices, polygonal section host problems and arbitrary-polytope section bounds are logically different. The exact all-(m,n) Ferrers-weight maximum, equality antidiagonal and 2/3 realizability gap were not contained in inspected primary text; prior extremal Ferrers/rook threshold cut identity could overlap and remains an explicit priority risk.

## value

PASS

PASS: hyperplane section complexity of Δ_(m−1)×Δ_(n−1), a natural polytope family, is completely solved for two positive-dimensional factors including all generic maximizers. The exact finite formula and 2/3 gap distinguish geometric realizability from abstract graph max-cut; this is a meaningful all-parameter polyhedral classification, not a tiny special instance or old-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
