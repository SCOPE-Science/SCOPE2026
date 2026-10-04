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

The proof was checked in four independent ways within the package:

1. **State recursion.** For a finite spending vector, the checker compares the product formula with a direct dynamic recursion using the state rejection probability \(\alpha\gamma_j/(1+\alpha\gamma_j)\) and advancement probability \(1/(1+\alpha\gamma_j)\).
2. **Sharp envelope.** Deterministic one-mass and equal-on-\(N\) schedules are evaluated to confirm the lower endpoint \(\alpha/(1+\alpha)\) and convergence toward the upper supremum \(1-e^{-\alpha}\).
3. **Inverse-square schedule.** Truncated products for \(\gamma_j=6/(\pi^2j^2)\) converge numerically to \(1-\sqrt{6\alpha}/\sinh(\sqrt{6\alpha})\).
4. **Quoted numerical value.** At \(\alpha=0.2\), the checker reproduces \(0.17515476014878684\).

The numerical checks do not prove the infinite theorem; the analytic state-exit argument and infinite-product limit in `RESULT.md` do. The theorem has not been checked outside independent exact-uniform complete-null p-values, fixed \(\lambda,\tau\), and rejection levels contained in \([0,\lambda]\).
