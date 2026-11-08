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

The legal de Bruijn overlap digraph is strongly connected (append a nonzero character then construct any target). At k>h, indegree/outdegree defects arise precisely at vertices beginning/ending with 0^(h-1), with the overlap correction at k=2h. Source set S and sink set T each have M vertices. For d=k-h, every S-to-T directed path must have length >=d because a shorter arrival in 0^(h-1) would force forbidden 0^h from overlapping marked zero runs; appending the final d symbols of each T yields a unique legal bridge. Any additional balanced edge flow in a covering cycle decomposes into >=M S→T paths and nonnegative circuits, giving lower bound d*M; adding chosen M shortest bridges yields an Eulerian multigraph. Independent legal graph assembly, BFS every defect source→sink and extra cost matched in 8 cases q=2,3 h=2,3; binary q=2,h=3 gives 14,28,53 and ternary q=3,h=3,k=6 gives 696.

## originality

PASS

Directed Chinese-postman theory explains computing repeat-allowed shortest covers, while Chee et al. maximize run-restricted no-repeat de Bruijn sequences; Moreno thesis focuses constrained language cycles and lexicographic Euler tours. The inspected material does not establish the stated first-overlap closed cost and all-optimal bridge classification. A hidden exact restricted-language postman specialization remains a material originality risk.

## value

PASS

Explicit all-parameter first-window-regime optimal cyclic cover length and complete minimal augmentation structure for a natural run-length-limited language; separates unavoidable duplicate windows from prescribed distinct factors and resolves dependence on alphabet and forbidden run length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
