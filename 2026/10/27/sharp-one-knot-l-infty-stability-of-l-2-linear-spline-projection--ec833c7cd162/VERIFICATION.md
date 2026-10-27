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

Reproducibility: use Python 3 with SymPy installed and run `python CHECKER.py`. The program returns `PASS: general symbolic identities and 1485 exact-rational row comparisons` on success.

It independently forms and inverts the three-by-three nodal Gram matrix, verifies the endpoint and interior-knot formulas symbolically for general \(a\), checks their exact absolute-integral identities, and compares rational row norms at 135 parametrized knots and additional output locations. The checker does not establish novelty, infinite-domain claims, or mathematical independence. The universal continuous-parameter claims follow from the written proof.
