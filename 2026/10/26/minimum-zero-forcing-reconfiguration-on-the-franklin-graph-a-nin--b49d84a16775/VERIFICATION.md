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

On the specified labels, the bipartite edges A_rB_s for s=r,r−1,r+2 are exactly the two cycle edges at each even vertex and the added even-to-i+5 chord. If a legal force's target stays white as the blue set grows, its source still has only that white neighbor. This justifies parallel closure and monotonicity, so testing all four-sets excludes every smaller size. An independent exhaustive check, not a rerun of the frozen scripts, found zero forcing sets among 495 four-sets and 324 among 792 five-sets. It enumerated all 48 adjacency-preserving permutations and recovered the nine stated orbits with sizes 12,24,24,24,48,48,48,48,48 and the stated representative degrees and eccentricities. The one-replacement graphs and all-source shortest paths gave connected J/T with (edges,radius,diameter)=(2910,5,5)/(534,9,13), slide degree counts 3:276,4:24,6:24, and eccentricity counts 9:24,10:144,11:60,12:48,13:48. Comparing every jump edge against the slide distance matrix gave maximum 9, attained by the stated {0,2,5,6,11} to {0,5,6,9,11} pair; shortest paths rule out any smaller distance for that witness. The excess over the single jump is eight moves. Replay: /workspace/branches/f916f99d-38ec-42cb-a181-5e8c7bd1d5f8/independent_check.py and independent_output.json. The check is exhaustive for this ordinary-forcing graph only.

## originality

PASS

The supported distinct claim is the complete Franklin ordinary minimum-set census and exact jump/slide geometry, particularly the sharp local sliding detour. Established definitions and graph aliases were credited. The inspected closest catalogue and literature treatments do not supply this combination of graph, feasibility condition, and distance statistic.

## value

PASS

The Franklin graph is a canonical small cubic vertex-transitive host, rather than an arbitrary sampled case. Its complete minimum-set geometry is a useful exact benchmark: both move graphs stay connected, yet a single jump can require nine optimal slides and the slide eccentricities vary despite host symmetry. The census and shortest-path witness distinguish unrestricted and local movement in a way neither the scalar Z nor generic graph connectivity can.

The dated certificate retains the supplied scientific assessment, sources and limitations.
