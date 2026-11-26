---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a maximal matching, no edge can join two unmatched vertices. Since the absent cross-edges form a matching, an unsaturated vertex facing two unmatched opposite vertices would contradict maximality. This forces size m for m<n and size at least n-1 for m=n. With equal shores, any maximal matching of size n-1 must leave a deleted pair unmatched. At t=0 this is impossible; at t=1,2 the present edge a_1 b_2 meets every candidate pair and forces local size n, including the disconnected n=t=2 boundary. At t≥3, an arbitrary present edge a_p b_q meets at most two deleted pairs: reserve one disjoint from it as unmatched. After removing its two vertices and the endpoints of the prescribed edge, the remaining graph is K_{n-2,n-2} with a matching missing. For order at least two on each shore, Hall follows from nonempty singleton neighborhoods and full collective neighborhoods of subsets of size at least two. For n=3=t, the two remaining vertices have swapped distinct indices q,p and their edge is present. Adding the prescribed edge to the residual perfect matching gives the required maximal matching. This proves the local assertions and the global value. The reviewed source checker was not executed. Independent cardinality-organized enumeration, `python3 -I /workspace/checks/5.py`, covered all 65 triples with 2≤m≤n≤6 and 0≤t≤m, 1098 prescribed-edge values and 10722 maximal matchings; see /workspace/checks/5.log. This corroborates the boundary cases, not the general proof.

## originality

PASS

The distinct content is the sharp third-deletion threshold, including intermediate deletions, contrasted against the no-drop result on unbalanced shores. Existing verified coverage includes t=0 and the crown endpoint by ordinary edge domination plus symmetry; neither determines the intermediate prescribed-edge maxima. This is a bounded best-of-knowledge assessment.

## value

PASS

This natural test family for a new prescribed-edge invariant separates a drop in the smallest maximal matching size from a drop valid through every edge. The strict-imbalance obstruction and the sharp threshold of three deleted pairs distinguish those phenomena uniformly over the full deletion range; the proof explains why the threshold counts pairs touched by the specified edge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
