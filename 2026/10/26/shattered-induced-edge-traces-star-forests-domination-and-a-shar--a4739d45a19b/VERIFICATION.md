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

For the trace F minus one edge e, one endpoint of e must be omitted while retaining the endpoints of all other selected edges. Hence every e of a shattered F has an endpoint private to e. Conversely, the union of the endpoints of any T⊆F realizes just T if all edges have a private endpoint. This property is exactly being a star forest: a triangle or a noninduced three-edge path violates it, whereas an acyclic nonstar component has diameter at least three. Centers of a spanning star forest dominate the host, including isolates; assigning every vertex outside a minimum dominating set one edge to that set gives the reverse inequality. This establishes the exact VC parameter and the threshold reduction, with a star forest as a polynomial certificate. The labeled component counts 1,1,r for sizes 1,2,r>=3 give exp(ze^(zt)-z²t/2); the k-edge coefficient uses n-k components. A separate distinguished-vertex recurrence reproduced the recorded small profiles. In the uniform m-subset of N edges, the probability of a specified e-edge set is (m)_e/(N)_e. The (n)_4/2 paths give mean tending to 4c³, and disjoint path tuples give the powers of this mean. At the first overlap with earlier disjoint copies, the intersection with the new path is a nonempty proper subgraph, so its 3v-4e is positive; even when later intersections are entire copies, their 3v-4e is nonnegative. This makes the union's 3v-4e strictly negative and the overlap contribution negligible. Triangles vanish in expectation. First moments give the c=0 case, and monotone coupling handles diverging m/n^(2/3). The frozen script was inspected, not executed.

## originality

PASS

The supported distinct core is the exact identification of the shattered sets of the specified edge-ground-set incidence model with star forests. The star-forest/domination correspondence and hardness are established prior facts; the EGF uses the standard labeled exponential formula and the window specializes the classical strictly balanced subgraph mechanism. They are not credited as independently novel tools or results about star forests in isolation. No inspected earlier source identifies the shattered sets in this same model, or implies that identification under the same assumptions.

## value

PASS

The edge range family is the natural vertex-induced range system, or principal Boolean ideals on rank-two elements in a complete host. Identifying its actual shattered subsets for every host is more informative than a dimension bound: it gives a local structural test and connects the dimension exactly to a standard optimization invariant. The labeled size profile and random sampling window then answer natural questions about the same shattering system. The contribution is the structural connection and exact profile, not a new general enumeration or probability technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
