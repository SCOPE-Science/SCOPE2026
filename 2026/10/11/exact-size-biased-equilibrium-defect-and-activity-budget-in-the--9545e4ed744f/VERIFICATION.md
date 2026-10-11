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

The statement was checked from the defining delay equation under a compact time-translation-invariant law on bounded complete strictly positive solutions.

1. Stationarity check: for every \(C^1\) function \(G\) on the compact current-state range, differentiation of the constant quantity \(\mathbb E[G(x(t))]\) gives \(\mathbb E[G'(X)\dot x(0)]=0\). This implies \(\mathbb E[\dot x(0)\mid X]=0\) and hence the displayed conditional production law.
2. Size-bias check: the stationary mean balance is converted to \(\mathbb E_Q[(1+X^n)^{-1}]=\gamma/\beta\). The exact nonnegative remainder follows from a pointwise rational decomposition; `checker.py` replays that algebra.
3. Activity check: the conditional law fixes \(\operatorname{Cov}(X,f(B))\); stationarity identifies the marginal laws of \(B\) and \(X\); expansion of \(\dot x(0)^2\) gives the variance identity. `checker.py` replays the algebraic reduction.
4. Equality check: either zero rational defect or zero mean-square activity forces the positive equilibrium trajectory.

Limits: no numerical orbit computation is used as proof. The result is conditional on a compact positive stationary law and does not prove that a chaotic invariant measure exists for any parameter set. Literature searches reduce but cannot eliminate the risk of an unlocated equivalent statement; in particular, the full text of arXiv:2605.14134 was not retrievable through the accessible source path and is recorded as an access-limited residual risk.
