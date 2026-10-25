---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For any involution with t≥1 transposition pairs, f≥0 fixed symbols, q=2t+f, exactly f² ordered two-windows are fixed and forbidden; remaining windows split into (q²−f²)/2 two-element coordinatewise involution orbits, at most one used. If f=0, crossing from the a-half to the b-half comprises t² paired orbits with one direction each. For t odd a directed cycle has balanced cross-edge flow, impossible with an odd number t² of +1/−1 choices, so lose ≥1 orbit. An explicit directed graph selects one representative per orbit (except omitted one internal orbit when f=0,t odd) via matching pairs of transposition blocks, a special odd-index connector, and circuits through fixed symbols. Each block balances indegree/outdegree; the active directed graph is strongly connected, hence admits Euler tour reading a cyclic word with distinct unpaired two-windows of maximal length (q²−f²)/2−1_{f=0,t odd}. Independently reimplemented the graph and checked 48 cases 1≤t≤8,0≤f≤5: no paired opposite, exact count, vertex balance, connectivity; includes t=1 edge cases. Constructive generic proof (not finite checks) covers all parameters.

## originality

PASS

Best-of-knowledge PASS for the orbit-type classification over arbitrary alphabet involutions, particularly fixedpointfree cases t≥2 and arbitrary f≥3; source modular-negation constructions already cover f=1,2 and the exceptional t=1,f=0 is known. The partial overlap is disclosed, not counted as new.

## value

PASS

The fixed-point count f and transposition count t are intrinsic conjugacy invariants for finite involutions. The exact orbit count is not always attainable: the parity obstruction when f=0,t odd is a genuine sharp combinatorial boundary. An explicit uniform Eulerian construction classifies every nontrivial involution and can be reused for constrained de Bruijn sequence design; not just checking the binary exception.

The dated certificate retains the supplied scientific assessment, sources and limitations.
