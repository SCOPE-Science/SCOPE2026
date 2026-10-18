---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

All distances checked: dist(a_i,b_i)=3 unique farthest; dist(a_i,b_j)=1 for j!=i, dist(a_i,a_j)=2. For same-part A-pair distance 2, a resolving other part has distances 1 and 3 (zero impossible), hence must be singleton {b_i} or {b_j}. Within A-occupancy r every pair forces one of its matched b singleton, so at least r-1 distinct B singletons; summing over q A-meeting parts yields n-q additional parts and lower n. Explicit n classes U0={a1,..,a_(n-1),b_n}, U1={a_n,b1}, singleton b2..b_(n-1) resolve each same-class pair; direct distance verification includes n=3. Independent exhaustive set-partition search finds minima n=3 and 4 with 122 and 2795 tested partitions. Thus all n are covered by combinatorial proof, not small enumeration.

## originality

PASS

Foundational González Yero 2014 paper gives bounds from strong-resolving graph and observes 2-antipodal graph associated matching; for crown these yield 2<=pd_s<=n+1, not exact n. No inspected source or Resultary crown-graph item reports exact strong partition dimension under this graph alias. Other crown graph invariants (edge-metric, odd coloring) are not implication equivalents.

## value

PASS

The crown family is a standard 2-antipodal symmetric connected bipartite graph; exact strong partition dimension is a natural metric-location invariant. The n-valued classification closes the generic [2,n+1] gap and supplies an inductively reusable singleton-antipode charging obstruction, rather than a finite table, renaming or arbitrary instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
