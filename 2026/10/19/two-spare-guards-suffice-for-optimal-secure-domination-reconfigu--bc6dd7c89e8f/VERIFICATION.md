---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

I wrote and ran an exact independent enumeration in complement-pair labels: join opposite 2-subsets when disjoint, which is the stated incidence graph after complementing the right side. For each mask I tracked vertices covered once or more than once. A chosen neighbor can defend an unoccupied vertex u exactly when each vertex uniquely covered by that neighbor belongs to N[u]. This checks ordinary domination after defense, not security after defense. Exhausting all masks of sizes at most 10 gave counts zero through 7, then 155, 5700, 37746. All 155 minimum masks have four per side and, after relabeling, match the frozen minimum-mask list exactly. Pair enumeration gave zero one-exchange edges and 750 two-exchange edges. The permutation/side-swap action gave orbit size:degree pairs 5:24, 30:6, 120:10. Independent breadth-first searches gave eccentricity 4 for every optimum in X. Direct TAR searches from one representative of each orbit reached only its starting optimum at capacity 9 and all 155 at capacity 10, with maximum optimum-pair distance 16. The theoretical bounds also hold: upward closure permits four moves per X edge at capacity 10, capacity 9 can only connect optima by a chain of forbidden one-exchanges, and disjoint optimum masks 983055 and 31440 in incidence order require at least 16 moves. The frozen programs and output excerpts were read, not executed. Replay the new check from /workspace with python3 branches/reproduce_desargues.py followed by the assigned source path to checks/certificate.json.

## originality

PASS

The verified distinct claim is the exact secure-state optimum geometry and the sharp TAR threshold and optimum distance on the Desargues graph, together with the minimum classification. Same-graph catalogue results use different predicates; a general secure-domination algorithm and ordinary domination TAR methods do not give the configuration and distance data without an additional computation or theorem. A bounded search did not establish priority for the scalar invariant in isolation; possible older coverage is recorded, not treated as disproved.

## value

PASS

For a canonical symmetric graph with a natural secure defense predicate, the calculation exposes a qualitative obstruction not captured by the optimum number: every optimum is isolated under a single exchange and remains isolated from other optima with one extra guard, yet two spare guards give full optimum connectivity with a sharp distance bound. The complete orbit and exchange data explain and make reusable this finite example; the work is more than checking a minimum number on an arbitrary graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
