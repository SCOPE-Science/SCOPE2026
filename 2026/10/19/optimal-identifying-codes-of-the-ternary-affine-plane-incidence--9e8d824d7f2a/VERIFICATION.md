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

Pass for the corrected files in repairs/2. The frozen finding and proof explicitly depended on a false universal bound and wrongly treated the computed lower bound as redundant. Gravier et al. p. 4 does print 2|V|/(Delta+1), but subdividing each edge of K5 once gives 15 vertices of maximum degree 4 with an identifying code of size 5 (original vertices give singleton traces, subdivision vertices give distinct pairs), contradicting the claimed lower bound 6. Trace-incidence counting gives 2|V|/(Delta+2), only 7 here. The repair proves nine by upward closure, exhaustive rejection of every eight-set, and the all-point witness. I independently built lines as translates of 1-subspaces, enumerated the closed-trace hitting constraints, verified the claimed 1+36+72 families setwise, and built all exchange edges by common eight-subsets. Replay: python3 branches/independent_affine.py. It reproduced 37 vertices/126 edges with radius/diameter 1/2 and four 18-vertex, 27-edge components of radius/diameter 4/4. The cone follows from flag incidence. Fixing a parallel class, the omitted triples have sums 1 or 2 and only one-coordinate changes connect them. In the displayed Pappus incidence map, writing B-parameters as (u+d,v+e) reduces incidence to d+e=(e-d)^2 in F3; the solutions are (0,0),(1,0),(0,1), giving exactly the three specified edges. The maps are bijections since v-u and u+v are independent coordinates. Affine maps are transitive on flags and ordered noncollinear triples by carrying their corresponding bases to one another. Both point and line codes use closed neighborhoods throughout. The proof is exhaustive only for AG(2,3); it does not generalize to arbitrary orders.

## originality

PASS

The corrected record claims the complete optimum family, its three affine orbits and the exact exchange decomposition, not the minimum by itself. The closest indexed Pappus findings concern different input graphs and/or different trace predicates, even when they happen to include size-nine codes. The exact three-family classification and resulting five-state-component-type decomposition are not covered by the inspected materials. The apparent implication of a prior degree lower bound was removed after checking its actual validity.

## value

PASS

On the canonical nine-point affine plane, a minimum code's identity matters for one-swap mobility. The incidence cone and four classical 18-vertex configurations characterize exactly which minimum identification systems can be connected without spare budget. This is structural information beyond optimum size or recognizing a standard Pappus graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
