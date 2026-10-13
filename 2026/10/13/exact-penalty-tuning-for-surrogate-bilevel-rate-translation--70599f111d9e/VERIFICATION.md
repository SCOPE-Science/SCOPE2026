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

The theorem is analytic. For \(b_0>0\), differentiating the translated bound gives an explicit positive second derivative, so the stationary point is the unique global minimizer whenever \(a_1>0\). Clearing the stationary equation gives the monotone quartic in `RESULT.md`.

`artifacts/verify_penalty_tuning.py` checks exact test instances with \(\rho_\star=1\), derivative signs on each side of the optimizer, the minimum-value identity, the cube-root special case, and the three degenerate regimes.

The finite replay is supporting evidence only. It does not replace the quantified derivative proof, and it does not test cases where the Lipschitz certificate depends on \(\rho\).
