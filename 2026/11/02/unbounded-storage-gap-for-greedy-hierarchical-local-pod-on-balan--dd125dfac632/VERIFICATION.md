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

For any block the positive eigenvalues of its Gram matrix are twice the multiplicities of its pairwise orthogonal row types. This gives 4b at the root, 2b for every represented type below it at group-aligned nodes, and 2h for h identical rows. The corresponding squared tolerances are b/4, gb/(8r) and h/(8r), strictly below those eigenvalues; exact local ranks and zero reconstruction error follow. The root split adds r(n+1) storage, since both children contain all r types, so the specified one-step procedure stops. Within each child, splitting a g-group node into equal halves saves g²b/2, while cuts inside one homogeneous group only add overhead. Thus each child is optimally cut into single groups. The root can either be kept or replaced by the two independently optimal child cuts, and the latter saves r(2r³−2r²−2r−1)>0 for every r≥2. The exact costs are r(2r³+2r+1) and 2r(r+1)², the ratio is asymptotic to r, and even the larger cost is strictly below the raw 4r⁴ entries. These conclusions concern the prescribed hierarchy and factor-entry measure, not arbitrary partitions or a particular graph-partitioner run. The supplied finite verifier was inspected, not run; the uniform claim follows from the calculation above.

## originality

PASS

The no-lookahead pitfall is recognized in the motivating POD paper and appears qualitatively in earlier hierarchical tensor compression. The supported distinct claim is an explicit admissible binary path-mesh family with a proved unbounded quantitative ratio between the greedy and optimal cuts, both reconstructing exactly under the stated positive tolerance rule and both compressing the data.

## value

PASS

This supplies a worst-case obstruction to any dimension-independent factor-storage guarantee for the specified greedy rule, even on connected balanced path partitions and without any reconstruction tradeoff. It gives a concrete reason to compare against deeper lookahead or whole-hierarchy optimization. The approximation claim is useful within that scope without implying practical failure of a particular partitioner.

The dated certificate retains the supplied scientific assessment, sources and limitations.
