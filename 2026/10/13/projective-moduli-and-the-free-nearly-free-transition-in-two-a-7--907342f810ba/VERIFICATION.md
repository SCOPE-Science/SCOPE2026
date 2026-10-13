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

# Verification

Run the accompanying `verify.py` with Python 3 and SymPy 1.14 or compatible to check exact polynomial identities and rank certificates. The program verifies the universal cubic Jacobian relation, the specialized quadratic Jacobian relation, the degree-two coefficient determinant \(3538944\kappa^{11}(\kappa-1)\), the nonzero rank-seventeen subminor \(-884736\) at \(\kappa=1\), smooth conic matrices, the collision resultant \(\kappa(\kappa-1)\), and stabilizer substitutions. The rank arguments therefore apply to **every** allowed complex parameter rather than just sampled rational parameters.

The geometric steps additionally require the conic restriction exact sequence, projective automorphisms of a smooth conic preserving two marked points, local classification of two smooth branches of contact order four or two, and pairwise Bézout. Those arguments appear in RESULT.md and are not automatically decided by the program. The conclusion about freeness uses established necessary-and-sufficient numerical criteria for reduced curves; it is not an independently certified theorem.
