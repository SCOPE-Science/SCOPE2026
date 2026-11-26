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

The penultimate map collapses exactly one vertex. Translate that vertex to (0,0) by flipping coordinates. Collapsing it to its diagonal opposite gives worst ratio b/a (the two incident edges give b/a and a/b); collapsing it across the short edge gives 1+a/b (the incident long edge maps to a diagonal); collapsing across the long edge gives 1+b/a. The other pairs are fixed or give smaller ratios. Thus no ordering can beat min{b/a,1+a/b}. Order O,X,Y,Z as in the record: the second map fixes O and X and sends Y,Z to O. It is nonexpansive on all four cycle edges and hence on their shortest-path metric. The penultimate map can send Z to O or Y at the two desired costs, and both images are in the same second-map fiber as Z, proving commutativity. Constant and identity maps cause no restrictions. The branch switch at b/a=phi and the nonexpansive condition b=a follow exactly. This symbolic argument, not sampled weights, proves the real-parameter result.

## originality

PASS

Credit the common definition, linearization and exact unweighted value to the matched material. The distinct mathematical content is the optimal constant at unequal weights, including the switch between two minimizing collapses. Neither the unweighted exact results nor the available broader existence bounds determine it. This is a best-of-knowledge judgment, not priority certification.

## value

PASS

This is the basic two-coordinate test for sharp constants of commuting point retractions on weighted products. Unlike the unit-weight binary case, every positive unequal weighting forbids a nonexpansive filtration, even though the optimum tends back to 1 as the anisotropy grows. The exact bottleneck and the change of optimal collapse give a usable sharp obstruction for this class of metrics, not a claim about arbitrary Schauder bases. The golden-ratio value is a consequence of the invariant, not the reason for its value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
