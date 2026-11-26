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

For each set W of omitted originals, all edge-vertices internal to W are forced. These dominate every nonisolated vertex of G[W]; each remaining vertex v in W needs a nonempty selection from its incident star. Such stars are mutually disjoint and disjoint from internal edges. All other edge-vertices have a selected old endpoint and are free. The fixed-W generating product follows, including zero terms for omitted degree-zero originals. Its least feasible degree is n-|W|+e_W+|I_W|. The savings from n are the sum of |V|-|E| over nontrivial components, at most one per component. Edges taken one per component give an induced matching in G, and omitting the endpoints of a maximum induced matching attains the bound. Equality forces a tree in every nontrivial component and exactly the specified boundary choice at each isolate, with no selections in the free class; W is recovered from its dominating set, so the multiplicity formula does not overcount. The complete/biclique specializations follow by listing their eligible induced trees; the biclique star count subtracts its twice-counted single edges. The edgeless case forces all originals, including the empty set of a null graph. Independent replay on 79 graphs (all labeled roots through four vertices and additional complete, biclique and disconnected cases) checked 47,735 candidate subsets, full coefficients and the complete list of minimum sets against direct adjacency enumeration. Replay: python3 /workspace/branches/audit_finite_reproduction.py.

## originality

PASS

The distinct result is the ordinary set enumerator and all-minima classification with its boundary-star factors. No separate novelty is credited to the scalar minimum: it follows from the earlier indexed independent-domination theorem once ordinary and independent domination are identified on these incidence graphs, and multiple scalar specializations already appear in the subdivision literature. Neither the independent polynomial nor the inspected scalar results give the extra ordinary choices. The exact biclique minimum count also appears as a value described as originating in earlier ordinary-domination analysis; its priority is not credited or resolved here.

## value

PASS

The product formula expresses a standard graph invariant directly in root-graph data and explains precisely which boundary choices create nonindependent minima. It reduces the enumerative description from subsets of original and subdividing vertices to subsets of the originals and produces the entire minimum family, not just an optimum value recoverable from known work. That structural enumeration applies uniformly to all finite simple roots, including isolates and disconnected graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
