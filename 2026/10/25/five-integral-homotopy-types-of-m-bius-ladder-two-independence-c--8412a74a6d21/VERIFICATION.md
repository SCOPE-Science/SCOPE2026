---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For the graph on 2n vertices with edges i↔i±1 and i↔i+n, an Ind_2 face is exactly a vertex subset inducing max degree≤1 (equivalently every component size≤2). Independently enumerated every nonempty bitmask and checked the supplied pivot orders, matched face pairs and topological acyclicity across all nonempty Hasse covers for n=4,5,6,7,8. Found respectively 78,232,685,2046,6078 faces; 38,111,339,1022,3023 Morse pairs; 192,720,2556,8946,30384 Hasse edges; one critical 0-cell plus k d-cells at (d,k)=(2,1),(3,9),(3,6),(4,1),(5,31). Entire Hasse digraph acyclic in all five. These finite exhaustive matchings and the CW theorem establish the *integral homotopy* wedges, not merely mod-p Betti ranks.

## originality

PASS

Best-of-knowledge PASS: the graph family is known but its *induced-component-size≤2* complex Ind_2 is distinct from ordinary independence, perfect matching, and bounded-independence BI_3/total-cut duals. Exact first five integral types were independently certified, not mere homology ranks.

## value

PASS

The five smallest nondegenerate cases immediately after M6=K3,3 show nontrivial changes of sphere dimension and multiplicity upon permitting induced isolated edges. The integral types form a motivated baseline for higher-independence topology on a natural symmetric cyclic graph family; no infinite-family classification is claimed or needed for this exact useful finite invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
