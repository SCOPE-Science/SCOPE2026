---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

A direct edge-distance table for horizontal X/Y edges and matching edges yields the three collision criteria in RESULT.md, covering each unordered pair of edge types. Two omitted matched columns create indistinguishable matching edges, forcing |S|>=n-1; with at most one omitted column, every edge is vertex-edge dominated, so dominant and ordinary edge-metric minima agree. At size n-1, exactly one omitted column, no doubled columns, and each layer has >=3 selected vertices are necessary and sufficient. This requires n>=7. For n<=6, the only size-n support profiles are a full transversal or one empty and one doubled column; the collision criteria give the stated layer restrictions. Combinatorial counting then yields M_n. Independently built graph adjacencies and BFS edge distances, exhaustive minimum-size subsets n=2..8, including n=2 square and n=7 first drop, produced basis counts 4,14,50,182,532,140,560, all matching the claimed classifications. The all-n conclusion rests on explicit collision exhaustion, not just these tests.

## originality

PASS

A 2024 Cartesian-product inequality gives n-1 <= edim(K_n square K_2) <= n but not the sharp transition or all minimum bases. The close Resultary theorem gives MIXED metric bases of complete prisms, which impose additional vertex/edge distinction constraints; its n-value does not imply the edge-only n-1 regime. The original dominant edge-metric work treats other graph families. The exact full classification is best-of-knowledge new.

## value

PASS

The 7-column sharp threshold and exact bases/enumerator explain a natural transition in a standard two-layer graph family, and distinguish edge resolution from stronger mixed resolution; researchers working in metric location parameters can use the complete extremizer structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
