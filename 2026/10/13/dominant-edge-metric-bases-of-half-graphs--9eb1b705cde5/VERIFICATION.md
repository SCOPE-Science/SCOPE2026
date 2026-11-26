---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The diagonal matching gives a lower bound n on vertex-cover and dominant-generator sizes. A size-n cover chooses exactly one endpoint of each diagonal edge. Choosing b_i and a_j at i<j would leave a_i b_j uncovered, so the choices must be an A-prefix and B-suffix. Conversely each such cut covers all edges. Independently, any vertex cover of a bipartite graph with pairwise distinct open neighborhoods within each part edge-resolves: equal signatures would have equal, nonempty zero-coordinate sets, so distinct edges would share exactly one selected endpoint and have unselected other endpoints x,y on the same side. A vertex in the symmetric difference of N(x),N(y) lies in the cover (as x,y are unselected) on the opposite side, differs from the shared endpoint, and has distance 1 to one edge but at least 2 to the other. In H_n the within-side neighborhoods are strictly nested, hence distinct. This proves resolution for all the cuts including the whole-side endpoints, with n+1 distinct optima. It agrees with the separate threshold decoding in the frozen proof.

## originality

PASS

The strongest same-object result classifies ordinary edge bases in the half graph; its statement is strictly different and does not imply the dominant basis classification by taking supersets. The general dominant lower bound yields n but no matching upper bound or all-optima statement for this family. Neither the other indexed half-graph record nor the inspected Ferrers work gives the same combined cover-and-resolution classification. The frozen reference to a published ordinary classification is best read as the public catalogue finding; an external journal identification for that exact classification was not verified.

## value

PASS

For a canonical infinite family of nested-neighborhood graphs, the result determines the effect of the cover requirement on both the optimum and the entire family of optima. In particular the interior cut bases cannot be constructed by simply augmenting the earlier ordinary minimum bases. The all-minimum-covers resolution property and exact optimum family are useful beyond merely exhibiting an n-vertex set or evaluating a lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
