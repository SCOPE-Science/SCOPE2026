---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For graph K1 joined to m disjoint r-cliques, r>=2 fixed, hub-t fiber of fractional edge relaxation factorizes over blocks. Below t=1/2, partition leaf cube into all-small and exactly-one-large coordinate regions: b_r(t)=2^(1-r)-t^r; above t=1/2, b_r(t)=(1-t)^r. Fractional volume is ∫0^(1/2)(c-t^r)^m dt+2^(-rm-1)/(rm+1). Integral stable-set fiber is m r-simplexes (1-t)^r/r!, total 1/(r!^m(rm+1)). Dominated convergence after u=m^(1/r)t gives fractional volume ~c^m c^(1/r)Gamma(1+1/r)m^(-1/r), normalized hub law exp(-u^r/c), and ratio ~ (r!c)^m*r*c^(1/r)Gamma(1+1/r)*m^(1-1/r). Integral hub scaled by (rm+1) tends exponential. r=2 gives sqrt(pi m/2) and half-normal. Independently checked several finite quadratures, exact r2 and small m formulas and limiting constants; no finite check substituted for dominated convergence.

## originality

PASS

Stanley chain polytope gives integral S_mr exactly and Steingrímsson general 2-weak-vertex packing volume recurrences subsume finite volume computability, so isolated one-block volume is NOT novel. Hamano/Hibi/Ohsugi concern Ehrhart/Gorenstein structure, not the fixed r hub coordinate law; prior symmetric edge windmill inballs and graph general-position polynomials concern different polytopes/invariants. Specific sharp familywise ratio and distinct hub probability limits not found, with residual unindexed probabilistic polytope literature risk.

## value

PASS

Graph-packing relaxation has a natural fractional vs integral comparison. Even r=2, where each leaf edge block itself is integral, sharing a hub forces unbounded sqrt(m) volume discrepancy and different power-law versus exponential hub scales. For each fixed r, rigorous condensation exponent 1/r and sharp constants explain a genuine high-dimensional phenomenon rather than arbitrary finite integration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
