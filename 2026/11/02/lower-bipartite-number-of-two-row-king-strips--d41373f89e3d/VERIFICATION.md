---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Two adjacent columns form K4, so any adjacent occupancies summing to at least three are impossible. Conversely, with adjacent sums at most two, double columns induce isolated edges and runs of singleton columns induce paths, for any choices of rows. An empty column is blocked exactly by an adjacent double, and a singleton exactly by an adjacent singleton; unavailable end neighbors do not count. For p double, q singleton and r empty columns, r≤2p, q≠1, and n≤s+p for s=2p+q. If s≤2k then n≤3k; at s=2k+1 one has odd q≥3, so p≤k−1 and still n≤3k. This implies s≥2ceil(n/3). The three residue constructions separate all double columns by zeros and cover all zeros by adjacent doubles, with exactly ceil(n/3) doubles. They include n=1 and 2. Independent replay: python3 /workspace/branches/e7df607f-23db-41ef-8993-0e09fdb3b774/audit_lb.py --direct 8 --occupancy 12. The direct graph check compared actual maximal masks with the expanded occupancy rule for all 87,380 masks through n=8; the finite occupancy check went through n=12. Output AUDIT_OK direct_orders=8 subsets=87380 occupancy_orders=12 (audit_lb.log). The proof, not enumeration, controls all n.

## originality

PASS

The strongest same-graph hit gives the same scalar for two-fair domination, not for maximal induced bipartite sets; the set classes fail to contain each other. The nearest inspected same-invariant work concerns other graph families or general enumeration. This supports the strip formula and occupancy test as a distinct result to the best of the available evidence, not as a certification of publication priority.

## value

PASS

This determines the lower bipartite number for the smallest nontrivial king-strip width, including boundaries, and gives a local test for all inclusion-maximal sets. The lower bound accounts for singleton columns rather than assuming an optimal solution is an ordinary dominating construction. Both the precise minimum and the occupancy test are useful for comparing nearby strip invariants and for higher-width work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
