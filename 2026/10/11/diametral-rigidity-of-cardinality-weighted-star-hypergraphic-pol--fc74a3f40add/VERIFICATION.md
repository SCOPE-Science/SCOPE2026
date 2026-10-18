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

For each strict coefficient order, every positive hyperedge simplex contributes to its largest-coordinate vertex. Thus every exposed vertex is a prefix v_(s,pi)=(T-sum_{j<=s}a_j)e0+sum_{j<=s} a_j e_pi(j), and sum a_j=T by hockey-stick identity. For vertices u,v with leaf coordinate sums x>=y, all leaf weights nonnegative, ||U||²<=H=sum a_j², ||V||²<=y² and U·V>=0; hence ||u-v||²<=(T-y)²+H+y²=T²+H-2y(T-y)<=T²+H. If 0<y<T the inequality is strict; if y=T both endpoints have >=2 positive leaf entries so ||V||²<y², strict. Equality only y=0, x=T; the full-support permutations give equality. Pascal difference a_j-a_(j+1) is positive whenever w2>0, so precisely r! distinct pairs in that case. Independent exact vertex- and distance-enumeration for 9 parameter cases r=2,3,4 corroborates. A general algebraic proof, not finite enumeration, establishes the theorem.

## originality

PASS

The published partial-permutohedron diameter and graphical-zonotope cone law were read in full as particularly relevant potential covering results. Both are mathematically adjacent yet fail to imply the positive-higher-order cardinality-weighted star’s complete ambient diametral-pair classification. The m=2 projected leaf model omits the hub-coordinate squared-sum correction, which changes distances; the graphical-zonotope cone law treats only size-two edge summands rather than all star hyperedges. The original m-graph and partial-permutohedron papers concern face/Ehrhart properties, not this metric classification.

## value

PASS

Computes a natural complete ambient Euclidean invariant of a substantial class of star hypergraphic generalized permutohedra, with all extremizers and a sharp multiplicity transition from one to r! at m=2. Its embedding sensitivity distinguishes meaningful metric geometry from the familiar face and projection invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
