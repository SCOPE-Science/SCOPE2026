---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For n=rm+1 the orthogonal Laplacian eigenspaces have eigenvalues 0 (constants), 1 (r−1 blade-balanced modes), m+1 (r(m−1) blade-internal modes), and n (one hub-against-blades mode). The stated projectors therefore give the exact G=L^+ and G². Writing s=e_a+e_b and d=e_a−e_b, the two diagonal leader penalties equal κ(ssᵀ+ddᵀ)/2. Eliminating the constant mode by the Schur complement leaves L restricted to 1-perp plus κddᵀ/2; applying Sherman–Morrison gives exactly J=n/(2κ)+tr G+(n/4)sᵀGs−κ[dᵀG²d+(n/4)(sᵀGd)²]/(2+κdᵀGd). All possible two-vertex sets belong to exactly A (hub/peripheral), B (same blade), C (distinct blades). Projector substitution yields all three rational formulas in RESULT.md, independently cross-checked by direct rational inverse for six r,m,κ triples. Symbolic simplification independently reproduced JB−JA=m(r−1)(3κ+2m+2)/[2(m+1)(κ+m+1)]>0 and JC−JA=P/[2(m+1)(κ+m+1)(2κ+m+1)], P=(r−2)m(2κ+m+1)²−4κ²−(m²+8m+7)κ−(m+1)². For r=2, P<0. For r≥3, P strictly grows with r and at r=3 equals 4(m−1)κ²+(m+1)(3m−7)κ+(m−1)(m+1)²; for m≥3 all coefficients positive and at m=2 it is 4κ²−3κ+9>0 (discriminant −135). Hence C uniquely minimizes when r=2 and A uniquely minimizes when r≥3, modulo graph automorphisms, for EVERY integer r,m≥2 and finite real κ>0, without gain-dependent ties.

## originality

PASS

Best-of-knowledge originality of the explicit strict gain-uniform transition, with substantial qualification. Lin–Fardad–Jovanović already formulate precisely the finite-gain trace objective; Fitch–Leonard already provide general two-leader joint-centrality evaluation. Their inspected full texts do not present the all-parameters clique-windmill minimizer phase classification. Independently proving strict orbit inequalities for every r,m,κ is additional graph-specific information, not merely a new notation for the prior general formula. The directly relevant Sun–Li–Liu 2020 windmill coherence work was inaccessible beyond abstract; it MAY already cover the theorem and therefore remains a material residual priority risk. Unavailable full text alone is not used as scientific FAIL or as evidence of noncoverage.

## value

PASS

The two-leader placement problem with finite pinning gains is a motivated stochastic-control graph-design problem; choosing where to place leaders affects total steady-state variance. The theorem completely solves the optimal pair and exact objective over the natural two-parameter clique-windmill family. It establishes a non-obvious structural phase discontinuity at three blades: with two blades the central maximum-degree hub is strictly suboptimal, while with three or more it is indispensable in every optimal pair; this holds for all finite positive gain strengths and clique sizes, with no ties up to automorphism. These strict gain-uniform inequalities give reusable exact benchmarks for placement heuristics and show why degree-only placement can fail, without inventing a downstream theorem. This is more than a routine isolated numerical example or a mere coefficient calculation; the result concerns an infinite graph family and a sharp parameter boundary. It does not address heterogeneous gains, nonuniform noise/edge conductance, singular zero gain or three-plus leaders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
