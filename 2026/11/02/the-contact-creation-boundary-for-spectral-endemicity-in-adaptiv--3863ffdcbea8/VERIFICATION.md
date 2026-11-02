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

From this package directory run `python3 check_adaptive_sis.py`; no third-party modules are required. The program checks exact rational matrices, the spectral test, the stationary partial-infection equilibrium, and numerical restoration branches. Its printed residual tolerances and bisection steps concern only the positive-creation illustration. The impossibility assertion uses nonnegative inequality chaining, and the positive-creation theorem uses a small-vector Perron inequality, Brouwer's theorem, compactness and graph connectivity; these are explicit analytical steps in `RESULT.md`, not inferences from numerical iteration.

The decisive spectral matrix is `[[4,1/2],[1/2,1/4]]` and the partial-endemic point is `[[3/4,0]]`. At the restoration boundary the prevalence Jacobian determinant is exactly `9/4`; the first derivatives with respect to the restored link fraction are `1/24` and `1`.

**Limits:** No exhaustive literature proof of uniqueness; no stability or global-attraction conclusion; no independent audit or independent validation has occurred.
