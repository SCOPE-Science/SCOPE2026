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

The definition requires an open-neighborhood hit at every vertex and excludes any cut that isolates a vertex. For a fixed cut, row i is dominated exactly by the surviving same-row neighbors of its selected mask together with surviving vertical neighbors selected in rows i−1 and i+1. The two-mask transfer, with zero boundary masks, covers every possible selected set and minimizes its cost once each row condition is enforced. I inspected both frozen implementations and the fresh checker's decisive loops. The fresh checker enumerates all intact optima by branching over every optimal row choice, then records for each vertex and pattern of removed incident edges the bitset of optima still supplying a neighbor. For each k=1,2,3 the code visits each k-combination once, excludes zero residual degree, and intersects the bitsets over all vertices. An empty intersection is necessary and sufficient for damage by monotonicity under deletion. In the order n=5,7,8 we reproduced (edge count, γ_t, optimum set count)=(31,8,256),(45,10,121),(52,12,2916). By cut sizes 1,2,3 the admissible/damaging pairs are (31/0,461/0,4369/40), (45/0,986/0,14004/727), and (52/0,1322/0,21884/0). A separate transfer in the fresh script checks that the displayed witnesses are isolate-free and give γ_t=9,11,13 with cut sizes 3,3,4. Hence the exact minima are 3,3,4. No four-edge census or all-length claim is supported or needed.

## originality

PASS

The exact three values and small-cut census close named gaps in the inspected grid theorem. The intact total-domination numbers are known, the three-edge G_7 witness is from the prior construction, and a four-edge upper bound for G_8 was already known. The inspected preprint says G_8 has that upper bound by direct check but does not exhibit its specific cut; it does not confirm the frozen prose attributing this choice of witness to an earlier displayed construction. That attribution caveat is separate from the verified witness and the novelty of the exact lower bound.

## value

PASS

These n were selected before enumeration as the first lengths in the three residue classes left at upper bounds by the published theorem. Their exact values give one strict improvement and two concrete sharpness benchmarks; the latter bear directly on the stated tightness conjecture without claiming it for larger grids. The complete small-cut checks also address precisely why small admissible cuts cannot improve those bounds. This is a motivated finite invariant, not an arbitrary small slice or a recomputation of the intact baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
