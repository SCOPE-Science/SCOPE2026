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

For an original leaf u adjacent through midpoint w to v, name four arcs a:u->w,b:w->u,c:w->v,d:v->w. Every face containing c can add a; remove dominated vertex c by elementary collapse. In the remaining complex every face containing d can add b; delete d. The residual a,b form an S0 join with the once-subdivided bidirected forest after deleting uv. Induction applies for arbitrary branching, components and isolated vertices. Since reversal has no invariant nonempty face it acts fixed-point-freely geometrically; the Lefschetz trace on the sphere gives (-1)^m (m=1 treated separately). Independent complete arc-mask checks for six small branched/disconnected forests tested 2,450 faces and 2,240 domination incidences.

## originality

PASS

Best-of-knowledge comparison of actual final mathematical implications with primary sources and relevant published semantic records. Relevant predecessor results were credited; no inspected full-theorem statement covers the final claim, with explicit residual priority risks.

## value

PASS

An exact simple-homotopy collapse for an infinite, arbitrarily branching and disconnected graph family gives integral homotopy and reversal symmetry, not only a numerical Betti count. The contrast with mixed-dimensional homology on unsubdivided bidirected double stars makes once-subdivision a mathematically structural operation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
