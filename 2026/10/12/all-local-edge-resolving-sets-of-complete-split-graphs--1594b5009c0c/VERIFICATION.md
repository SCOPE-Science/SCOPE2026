---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For adjacent edges xy,yz, the local edge distinguishing landmarks in K_m join independent_n are exactly the nonshared endpoints {x,z}: all other vertices are either incident to the common vertex y or at equal distance 1 from both edge sets (check all clique/independent edge-type cases). With m>=2 any unordered vertex pair can be realized as the nonshared endpoints of such edges (including two clique vertices by using an independent common neighbor when m=2), hence R resolves iff |V-R|<=1. With m=1 only leaf pairs occur; R must choose >=n-1 leaves while center optional. For K2 there are no adjacent distinct edges; nonempty-generator convention gives 2z+z^2. Consequently polynomial for m>=2 is z^N+N z^(N-1), and for star n>=2 is z^(n-1)(n+z)(1+z). An independent BFS distance/adjacent edge test of every subset for all 1<=m,n<=4 confirms each branch. Universal claim follows from pair-realization lemma, not finite sampling.

## originality

PASS

Based on source-level and current-literature comparison, the complete surviving claim is not established by the named prior results. This is a best-of-knowledge priority judgment, not a guarantee of global novelty.

## value

PASS

The local edge metric generator family is computed completely, not just its cardinality optimum, on a natural split-graph join family; its transition when introducing a second clique vertex and exact basis counts reveal a sharp combinatorial constraint. The distinguished K2 convention is properly handled. This is an explicit structural classification beyond the known star scalar result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
