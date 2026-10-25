---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

For the coordinate octahedron, the six vertices of each relevant central section are \((e_i-e_j)/2\) for distinct \(i,j\). Their cyclic edge differences are vertices of the same section; this proves a self-perimeter of six without a floating-point calculation. Cross-product and polygon-area identities give squared facet area \(3/4\) and squared section area \(27/16\). The recursive facet sum therefore equals \(16/3\). The product identity is proved by the boundary decomposition in RESULT.md.

The supplied `CHECK.py` was executed from its actual package directory using Python 3; its exact-rational assertions passed. It also checks the resulting ratio in 25 odd dimensions. Those finite checks are supplemental, not an exhaustive proof of the all-dimensional claim.

The conjecture being contradicted appears in Wolansky's arXiv:2604.01950 (2026), Section 4.4. A residual originality risk is the possible existence of previously unindexed calculations of the same regular-octahedral self-volume. Independent review has not been performed.
