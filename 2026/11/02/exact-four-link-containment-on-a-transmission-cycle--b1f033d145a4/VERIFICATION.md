---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For n>=4 and q in (0,1), collapse deterministic edges into four positive integer arc masses l_i. Pair connection between adjacent arcs is c1=q+q^3-q^4; opposite c2=2q^2-q^4. Exact uniform-seed outbreak expectation is l^T C l/n. Orthogonal decomposition into total, two opposite contrasts and alternating contrast gives n*lambda0/4+[lambda1(u^2+v^2)/2+lambda2(a-b)^2/4]/n. Since lambda1,lambda2>0 and lambda1-lambda2=2q(1-q)^2>0, minimizers are uniquely the balanced four-arc patterns up to dihedral symmetry; for n mod4=2 the two larger arcs must be opposite, with strict adjacent penalty 2q(1-q)^2/n. Fresh exact rational enumeration of all 4-part compositions n=4..17 at three q values confirms the algebraic classification.

## originality

PASS

Existing cycle-percolation and barrier-placement sources have other graph classes or objectives; the explicit uniform-seed finite four-link placement theorem and all-n mod-four parity penalty are not established by the inspected material. This is a bounded priority assessment with limited full-text access for closest epidemic papers.

## value

PASS

Provides a clean exact optimal-intervention benchmark for a single-seed spreading model and a non-obvious strict placement rule at remainder two. The phenomenon is motivated by minimizing average outbreak susceptibility, not by an arbitrary chosen numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
