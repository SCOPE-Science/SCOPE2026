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

For connected triangle/C4-free G and distinct centers, closed balls B(u) are distinct and pair intersections have at most two elements. Consequently after root positive x, any second query has its positive branch of size <=2, prohibiting complete online depth 4. The root positive child can shatter depth2 exactly when degree(x)>=3 (use neighbor y, yielding two positive and at least two negative centers); root negative child depth2 iff some y satisfies 2 <= |B(y)\B(x)| <= |V\B(x)|-2, since different centers distinguishable. This gives iff Ldim=3 else 2 for n>=5. VCdim<=2 via common-neighbor obstruction to three shattered query vertices, and >=2 by neighbor witnesses for branching, paths and cycles. Eight-leaf capacity forces n>=8, explicit eight-vertex tree has depth3. Independently enumerated the 35 connected triangle/C4-free graph atlas examples through seven vertices and verified exact Ldim equals criterion; also independently checked eight-tree. Finite checks do not prove universal theorem.

## originality

PASS

General published graph-ball VC/2VC results already imply portions of the static tree VC bound; the exact local online/Littlestone classification for all girth>=5 connected graphs and minimal eight-vertex witness is an additional assertion not contained in inspected full original papers. Best-of-knowledge PASS with unindexed-tree-learning risk.

## value

PASS

Natural complete all-graph local criterion that replaces exponential online decision-tree search with neighborhood cardinalities and pinpoints a sharp minimum-order separation between VCdim2 and Ldim3. Covers all finite trees of size >=5, rather than a randomly selected graph instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
