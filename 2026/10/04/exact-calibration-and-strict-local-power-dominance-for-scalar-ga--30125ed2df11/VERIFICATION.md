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

The analytic proof establishes the exact finite-sample null representation and the all-\(h\ne0\) asymptotic dominance theorem. The accompanying `verify.py` performs independent numerical and algebraic checks without replacing those proofs.

Checks performed by `verify.py`:

1. It evaluates the published scalar cross-fit formula on deterministic nondegenerate half-samples and verifies equality with \(\sqrt{m/(m-1)}\{\operatorname{sgn}(t_2)t_1+\operatorname{sgn}(t_1)t_2\}\).
2. For \(\alpha=0.05\), it recomputes \(u_\alpha\) and \(c_\alpha\), then verifies the closed null-tail identity \(\tfrac12[1-\{2\Phi(u_\alpha)-1\}^2]=\alpha\).
3. It checks on a dense deterministic grid that the conditional cross-fit minus single-split rejection probability is negative below \(u_\alpha\) where nonzero and positive above it.
4. It numerically evaluates the limiting cross-fit and single-split power formulas for several positive local signals and confirms the displayed strict inequalities, including the reported \(h=1\) values.

Limits: the numerical grid does not prove the continuum sign statement, and numerical quadrature does not prove the all-signal power theorem. Those statements are proved analytically in `RESULT.md`. The code does not attempt finite-sample power comparison or dimensions above one.
