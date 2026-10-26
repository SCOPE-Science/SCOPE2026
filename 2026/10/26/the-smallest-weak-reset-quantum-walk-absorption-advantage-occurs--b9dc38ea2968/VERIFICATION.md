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

# Verification instructions and limits

Run `python verify_variance.py` with SymPy installed. For each \(L=1,2,3,4\), the script builds the exact rational survivor superoperator in the reachable parity-supported real symmetric sector, solves two resolvent systems, and checks the defining residual identities with exact equality. It then asserts \((\mathbb ET_L,\mathbb ET_L^2,\operatorname{Var}(T_L),M_L'(0+))\) against the four claimed integer tuples. A distinct absorbing classical Markov matrix verifies the comparative moment formula and derivatives.

All four quantum and four classical matrix computations completed and passed with exact rational arithmetic. Independent direct state-vector propagation through several hundred steps reproduced the quantum moments to approximately 9–10 digits; this was corroborative only. The renewal identity and differentiability at the origin are proved analytically in RESULT.md, rather than inferred from a sampled reset grid. The certificate tests exactly the stated finite sizes and no others; it neither proves an all-size polynomial nor certifies bibliographic priority.
