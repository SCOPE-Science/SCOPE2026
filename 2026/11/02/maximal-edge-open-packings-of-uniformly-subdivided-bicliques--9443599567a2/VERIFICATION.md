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

Same-type incidences never conflict; opposite types conflict exactly when they share just one of row or column. Hence a maximal set must take on either side every position compatible with all selected positions on the other. The resulting mutual closures are the two pure sets, b(b−1) identical transverse pairs, 4b oriented singleton/full-neighborhood pairs, and the complementary single-row blocks. In the last case each block has at least two positions; otherwise double closure adds an opposite-row position or fills the full pure side. If both rows are used and one has at least two positions, the other side is forced to a singleton or empty, so there are no additional cases. For b=1 the conflicts form a matching and for b=2 two disjoint K_{2,2}, giving the stated four counts in each small case. The binomial sum for the blocks, overlapping exponents and total follow; for b≥3 all mixed cases have size at most b+1, while each pure set has size 2b. The subdivisions have degeneracy at most two by deleting the subdivision vertices first. An independent run enumerated directly from third-edge witnesses for each b=1,…,5, matching the full distributions, including the collisions at b=3 and b=4.

## originality

PASS

The prior general S(G) decomposition of all packings and maximum-cut formula materially cover the feasible packings and imply the maximum size and its two attaining sets here for b≥3. The supported distinct part is the explicit classification and cardinality distribution of all inclusion-maximal sets, including the gap, not that prior decomposition or its extremal consequences. This requires analyzing extensions that can change the matching or center sets; the inspected prior result does not give a maximality filter or the mixed-type contributions.

## value

PASS

The polynomial enumerates the possible sizes of saturated packings, not just which packings can attain the maximum. The four-type description explains how exponentially many smaller maximal choices coexist with only two largest ones. Unbounded missing sizes on connected bipartite graphs of degeneracy two provide a natural structural contrast with the familiar scalar extremum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
