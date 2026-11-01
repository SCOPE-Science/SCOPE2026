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

For complete bipartite K_{a,b}, uniform choice of exactly m distinct edges, a,b>=2, all joint falling factorial moments of isolated side counts equal (a)_r (b)_s * binom((a-r)(b-s),m)/binom(ab,m) for allowable integer ranges. The conditional pair-event ratio factors into product of 1-rsj/((ab-rb-j)(ab-as-j)), giving strict negative cross-part factorial dependence at m>=2 when both margins are positive. The exact covariance sign interval follows at r=s=1. In the balanced sparse m/n->c>0 the product log expansion gives covariance -> -(c²/2)e^(-2c). With-replacement independent row/column index sequences give independence; Bernoulli edges give covariance ab*p*(1-p)^(a+b-1)>0.

## originality

PASS

Best-of-knowledge new exact all-parameter factorial-moment comparison and three-ensemble covariance sign contrast; prior replacement-model independence and disjoint-group negative association are important ingredients but do not imply the overlapping row-column fixed-m calculation.

## value

PASS

The negative/zero/positive covariance contrast between natural three ways of sampling the same bipartite potential-edge set is a concrete structural probabilistic distinction, with exact all-size factorial moment inequality and nontrivial balanced sparse limit. It informs which random-graph ensemble can legitimately support isolated-vertex independence approximations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
