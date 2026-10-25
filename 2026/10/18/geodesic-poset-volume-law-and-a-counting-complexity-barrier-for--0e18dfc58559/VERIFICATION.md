---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Every edge on a shortest terminal u–v path has forward distance potential φ(b)−φ(a)=ell_ab and the oriented graph is a terminal DAG. In the positive cap s=L−f(v)∈[0,eps], z_x=φ(x)−f(x), each edge becomes 0≤z_b−z_a≤2ell_ab. Every vertex lies on a directed u–v path, so 0≤z_x≤s; eps≤2ell_* makes all upper bounds automatic. At fixed s the internal coordinate set is exactly s times the reachability order polytope, with anchored Jacobian one; Stanley’s volume=e(P)/(N−2)! integrates to each cap e(P)eps^(N−1)/(N−1)!, doubled by central symmetry. For an isolate-free height-two poset, H_P edges u–A–B–v realize every relation and have terminal distance and graph diameter exactly 3; no-isolates ensures all edges lie on length-three terminal geodesics. eps=1 recovers 2e(P)/(n+1)! and polynomial time counting reduction from Dittmer–Pak #H2LE. Finite rational tests corroborate rather than prove the exact all-graph identity.

## originality

PASS

Best-of-knowledge PASS, accounting for Stanley and Sanyal–Stump as prior. Classical order-polytope volume=e(P)/n! alone does not state the symmetric graph-metric shortcut cap law, nor the strong unweighted bipartite diameter-three realization of arbitrary height-two posets and its consequent #P-hard exact volume difference. Sanyal–Stump Corollary 5.2 is a different poset-hypersimplex order-polytope slice; Dittmer–Pak Theorem 1.1 provides #P-hardness of height-two linear extensions, used explicitly. A previous specialized one-stretched-edge complete-bipartite cap formula is a covered special case and not claimed as separately novel.

## value

PASS

A natural metric response under shortening one redundant terminal distance is exactly quantified by the geodesic reachability poset linear-extension invariant. Its order-d flatness and an explicit #P-hard exact evaluation already on diameter-three unweighted bipartite graphs give structural geometry and a genuine complexity barrier, not a trivial restatement of Stanley without geometric reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
