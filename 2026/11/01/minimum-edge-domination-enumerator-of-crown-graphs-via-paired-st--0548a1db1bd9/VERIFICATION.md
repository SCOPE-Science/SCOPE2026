---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The uncovered vertices U_A,U_B characterize domination: no cross-edge may join uncovered endpoints, so one side is fully covered or both uncovered sides are the same singleton. Removing an essential edge proves the perfect matching, one-sided restricted surjection, and matched-hole star-forest cases; the one-hole map must give f(j) a unique preimage, otherwise that edge is inessential. The EGF exp(W) labels components of complete-bipartite star forests; inclusion-exclusion over forbidden diagonal edges works because disjoint forced matching edges belong to distinct stars, each contributing z(exp(zx)+exp(zy)-1). Component-count bounds yield n-1 and 2n-4 extrema with stated parameter qualifications. Independent full subset enumeration n=2,3,4 reproduced all size distributions; original verify.py was inspected, not used as proof.

## originality

PASS

Bonamy et al enumerate minimal dominating sets algorithmically in broad classes, and Anderson–Kuenzel–Rall characterize well-edge-dominated graph families including undeleted balanced K_{n,n}; neither inspected theorem gives all coefficients of minimal edge-dominating sets after deletion of the full matching. Crown-graph Resultary records concern restrained, Roman, edge-metric, and other domination variants. A published alternative via line-graph dominating sets or forbidden-matching star forests remains possible.

## value

PASS

Crown graphs are a natural complete-bipartite family missing a perfect matching. Full distribution of inclusion-minimal edge-dominating sets, including unusual one-hole essentiality and paired star forests, determines more than a single minimum bound and quantifies loss of the well-edge-dominated property. Exact extrema and complete enumerator are useful for graph domination benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
