---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

All-true labeling forces an acyclic query digraph with weak components of size <=b. A redundant directed arc cannot be independently false when an alternate directed path is true. Conversely, the transitive closure of the positive query arcs realizes any assignment because any falsely queried arc would need precisely such an alternate path. A transitively reduced DAG has triangle-free underlying graph, so Mantel and the discrete convex increments of floor(t^2/4) establish the max for components <=b; bipartite orientations attain it. An always-false-until-seen online learner makes at most the number of true ordered pairs, bounded by sum binom(component_size,2). Actual depth-three and depth-six certificate JSONs were independently traversed: n=3 has seven valid internal nodes and eight distinct valid poset leaves; n=4 has 63 and 64, all paths consistent and transitively closed. Blockwise concatenation attains the upper bound for b<=4. Independent Boolean-relation enumeration counted 19 and 219 orders on 3 and 4 vertices and VC=2,4. The finite certificates establish only local bases; the unrestricted formulas require the preceding arguments.

## originality

PASS

Best-of-knowledge original relative to the materially inspected exact claims and implications; source-access and alternative-formulation limitations are not concealed. Exact transitive-reduction criterion plus VCdim for arbitrary b, alongside matching Littlestone dimensions through b=4, identifies the smallest comparability-component bound where adaptive query complexity exceeds static complexity. Unbounded gap alr

## value

PASS

Exact transitive-reduction criterion plus VCdim for arbitrary b, alongside matching Littlestone dimensions through b=4, identifies the smallest comparability-component bound where adaptive query complexity exceeds static complexity. Unbounded gap already with three-point components gives a natural locality-vs-online-learning phenomenon, substantially beyond a small poset table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
