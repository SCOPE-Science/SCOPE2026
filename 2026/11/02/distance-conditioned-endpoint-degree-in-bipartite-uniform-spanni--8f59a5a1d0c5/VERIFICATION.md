---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For K_{a,b} with marked opposite-part endpoints, the all-minors matrix-tree determinant of the Laplacian minor after forcing a path with s=t+1 vertices in each part is b^(a−s)a^(b−s)[1−(a−s)(b−s)/(ab)]. Counting paths gives P(T=t)=((a−1)_t(b−1)_t C_t)/(ab)^(t+1), which telescopes to P(T≥t)=∏_{j=1}^t(1−j/a)(1−j/b). Conditional marked-endpoint extra-degree factorial moments factor to Bin(b−s−1,1/a)+Bern(b/[s(a+b−s)]) for b−s≥1, terminal H=1. The decreasing Bern parameter, shrinking Bin parameter and Bernoulli-convolution log-concavity prove STRICT monotone likelihood-ratio decay, including terminal point-mass boundary. The exact mean deviation b/[s(a+b−s)]−s/a has unique sign switch since s²(a+b−s) strictly increases on [1,min(a,b)], and the tail product gives Rayleigh scaling r=√(ab/(a+b)) as a,b diverge proportionally. Independent enumerations of all spanning trees for K2,2 K2,3 K3,3 K3,4 reproduced the exact rational conditional distributions and ordering.

## originality

PASS

Ge–Dong (2019) and Dong–Ge (2021) already supply the fixed-tree/forest completion enumerations from which these distributions are computable; their theorems are credited as input. A published related Resultary finding proves conditional degree negative regression in complete-graph Cayley trees, but not the bipartite all-parameter STRICT likelihood-ratio ordering and crossing. No dominating same-host stochastic order theorem identified in inspected sources.

## value

PASS

Identifies a strong negative dependence in a canonical noncomplete host of uniform spanning trees: likelihood-ratio ordering at all distances is stronger than covariance or stochastic ordering. The exact crossover and Rayleigh localization determine where long-distance branches suppress endpoint branching, making a precise usable statistical law, not a renamed fixed-tree counting lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
