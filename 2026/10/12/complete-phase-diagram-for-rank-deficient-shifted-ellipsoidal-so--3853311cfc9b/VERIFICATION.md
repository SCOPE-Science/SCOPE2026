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

The proof is based on an exact orthogonal decomposition into \(\operatorname{Range}(H)\) and \(\ker H\). The singular case is reduced to the positive-definite theorem only after the nullspace compatibility condition has been proved.

`artifacts/verify_rank_deficient_socp.py` checks diagonal rank-deficient instances with exact rational arithmetic. It confirms strict-case feasibility and value, invariance under arbitrary kernel shifts, the pseudoinverse formula, and explicit unbounded rays when \(b\) has a kernel component.

The finite replay does not prove the general theorem. The quantified result follows from the range--kernel decomposition and the positive-definite quotient argument.
