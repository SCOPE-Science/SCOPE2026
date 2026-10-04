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

The proof reduces constant-reflection generalized FRB on \(F(x)=ax\) to a real second-order recurrence. The stability statement uses the necessary-and-sufficient Jury conditions, while the rate statement follows from exact differentiation of the two dominant-root branches.

`artifacts/verify_generalized_frb_scalar.py` checks the Jury identities and finite boundary in rational arithmetic and evaluates characteristic roots for representative parameter values around both the stability boundary and the predicted rate optimum.

The finite replay does not prove the all-parameter result; the algebraic argument in `RESULT.md` does. General nonlinear, nonnormal, constrained, composite, adaptive, and stochastic settings are outside the claim.
