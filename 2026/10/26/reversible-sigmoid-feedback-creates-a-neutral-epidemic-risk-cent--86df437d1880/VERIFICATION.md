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

Direct checks: derive the cubic payoff at group size three and threshold two; differentiate the vector field and verify its off-diagonal elliptic Jacobian; substitute \(x\mapsto1-x\) and check the reversing involution; take the periodic time average of the cooperation log-odds derivative and pair time-reversed states. Run `python verify.py` for exact algebraic identities and numerical corroboration with the specified sample parameters. The proof of existence uses transverse symmetry crossings and the implicit-function theorem, not finite simulation. Independent audit and outside validation have not occurred.
