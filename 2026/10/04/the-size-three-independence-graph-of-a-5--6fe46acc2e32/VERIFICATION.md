---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Independent construction of A5 as the 60 even permutations reproduces the class sizes 15, 20 and 24 at orders two, three and five. Exhaustive closure of all pairs and triples gives 1140 generating pairs and exactly 1240 minimal generating three-subsets. Building adjacency from those triples yields 35 nonisolated vertices, 405 edges, the degree multiset 26 repeated 15 times and 21 repeated 20 times, and exact diameter two. The structural proof also explains the census: an order-five subgroup lies in its unique maximal dihedral normalizer, while the remaining proper pair-generated subgroup types yield the stated involution and fixed-point criteria.

## originality

PASS

Lucchini introduces the fixed-size independence graphs and proves fixed-size connectivity for soluble groups, but does not work out the smallest nonsoluble group A5. The exact vertex classes, pair criteria, edge count, degrees and diameter require the A5 subgroup analysis or exhaustive calculation. No independent exact predecessor was located.

## value

PASS

This is the smallest nonsoluble test case for the fixed-size connectivity theory and gives the complete graph structure rather than only a yes/no connectivity answer. The pair criteria, degrees and diameter make it a reusable benchmark for larger nonsoluble groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
