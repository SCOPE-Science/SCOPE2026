---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For finite level-regular rooted tree of height h>=1 and b_i>=1, a frontier is a maximal antichain meeting every root-to-leaf path once, with whole-vertex binary queries. Last-level parents P (size product_{i<h} b_i) are VC-shattered by independently keeping parent or all its leaf children. A shattered set cannot include comparable vertices or two sibling leaves (identical membership across frontiers), permitting a disjoint injection into leaf-parent blocks and VC upper |P|. For any positive response at depth d, the remainder is the Cartesian product of independent maximal frontiers in path sibling subtrees, whose online ranks add; their rank sum telescopes to |P|-1, so Ldim<=|P|, and VC<=Ldim yields equality. Unary branching and h=1 are included. For binary trees, N_h=1+N_{h-1}^2 gives N_4=677 vs dimension8 and a growing entropy gap. Independent enumeration confirmed profiles (1,2,2): 6 frontiers / rank2, (2,2,2):26/rank4, (2,1,3):10/rank2.

## originality

PASS

Best-of-knowledge PASS for exact VC and Littlestone formula for the *maximal-antichain vertex-membership* concept class of level-regular finite rooted trees. Maximal frontiers themselves are classical (Darnstädt–Ries–Simon 2018), and general thicket and product-Ldim machinery is prior. Full primary PDF of the hierarchical minimum-disagreement paper, inspected with page screenshot, uses antichains for partition optimization and mentions VC in different learning arrangements; it does not provide the sharp membership-class online formula. Walker examines leaf subsets of decision trees rather than frontier hypotheses; Ghazi et al give general closure bounds, not this evaluation.

## value

PASS

The exact number of penultimate-level parents as both shattering dimensions for every (including unary) level-regular profile is a natural complete classification of a basic hierarchical coding object. It exposes a meaningful exponential gap between the hypothesis-count entropy ceiling and optimal online mistakes without creating a VC/Ldim gap, and separates membership-based learning from partition-fitting; not a mere reparametrization of frontier enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
