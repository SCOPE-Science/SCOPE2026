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

The exact covariance is proved by conditioning on four specified paired half-edges. The conditional residual matching remains uniform, so forced-plus-residual and residual-plus-residual parallel-edge counts can be evaluated by factorial moments. Algebraic expansion gives the stated polynomial, and a complete positivity argument follows after substituting the nonnegative excess degrees. The exceptional \(L=4\) case follows from the exact two-state distribution. The fixed-degree asymptotics follow from the mean-square count and the leading polynomial coefficient.

The standalone `verify_cycles.py` uses only Python's standard library. It exhaustively enumerates all labelled half-edge matchings in the seven models with \(L\le8\), computes exact rational \(\mathbb E X\), \(\mathbb E Y\) and \(\operatorname{Cov}(X,Y)\), and asserts agreement with the formulas. This verifies those models, not an infinite parameter space. No independent audit or external validation is claimed.
