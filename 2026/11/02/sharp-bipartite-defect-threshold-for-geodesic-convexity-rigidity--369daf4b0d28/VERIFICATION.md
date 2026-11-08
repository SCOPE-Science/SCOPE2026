---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For p,q≥2t+3, same-part pairs have at least three common opposite neighbors, hence those are forced into every geodesic hull. If a proper convex set contains a≥2 left vertices, it subsequently contains b≥3 right and a≥3 left. Outside vertices have at most one neighbor inside each opposite side; this gives (q-b)(a-1)≤at and (p-a)(b-1)≤bt, together with a,b≤t+1, leading to incompatible lower/upper bounds on q-b. Thus proper convex sets are ∅, singletons, or edge pairs. The VC=2 and Littlestone=3 claims follow by direct combinatorial version-space shattering and upper bound. At p=q=2t+2 the explicit partitioned missing-edge pattern leaves a proper convex K2,2, establishing sharpness. Independently calculated 32 convex sets on the 5×5 crown graph, confirming edge+singleton+two count; finite check is corroborative only.

## originality

PASS

Earlier g-minimal graph characterization already names and recognizes the class; the precise universal max-missing-degree cutoff 2t+3 and all-t counterfamily appear additional in checked claims. The learning dimensions are straightforward but meaningful conditional descriptions, not separately marketed as new theory.

## value

PASS

Sharp high-density structural threshold with a matching extremal witness for every defect t, and complete learning-dimension description. This is a natural robust rigidity classification and finite sharp boundary rather than an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
