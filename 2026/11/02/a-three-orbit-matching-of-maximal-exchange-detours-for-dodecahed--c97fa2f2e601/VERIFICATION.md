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

For k<=5 the residual graph has at least 30-3k edges and a forest would have at most 19-k. Thus no smaller set works. In an independent bounded reconstruction I enumerated all six-subsets, used edge count 14 minus number of components as the exact residual forest test, bucketed accepted masks by their five-subsets to build exchanges, and ran BFS from every mask. The induced exchange graph has 2520 vertices, 23940 edges and eccentricity six at every vertex. All 12 table cells match, giving excess totals 3124960, 48800, 180; independently checked that the exceptional pairs occupy 360 distinct endpoints and that each original edge is the unique common edge in four overlap-two and two overlap-three pairs. Enumerating the full automorphism group by extending partial bijections preserving graph distances yielded 120 permutations: adjacency is exactly distance one, so those completed bijections are exactly the automorphisms. The three representatives yield disjoint orbits of 60 whose union is the exceptional set. This checks exhaustion and the full group rather than assuming the supplied generators are complete. The two frozen scripts were read, not executed.

## originality

PASS

The optimum size, base family size, and already reported coarse unrestricted exchange invariants are credited, not accepted as new. The distinct evidence-supported slice is the joint overlap/distance census and the 180-pair matching with its per-edge and orbit refinement. The closest inspected exact records give different statistics, different adjacency, or different feasible sets.

## value

PASS

The Johnson distance is the canonical unconstrained baseline for exchanges of minimum sets. Counting deviations from it asks how much the forest constraint actually obstructs shortest transformations, not just how far apart two states can be. The fact that maximal excess is a matching and always tied to a unique original edge is an exact structural benchmark for reconfiguration and for attempts to explain the detours. It is useful even without a general family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
