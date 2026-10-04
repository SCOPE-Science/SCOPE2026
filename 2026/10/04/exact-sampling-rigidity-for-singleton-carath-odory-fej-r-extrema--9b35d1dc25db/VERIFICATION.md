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

The theorem is proved analytically in `RESULT.md`. The key checks are:

1. With \(\alpha=\pi/(2n)\), the explicit polynomial \(\phi_n\) is nonnegative on the full circle. Its transformed Chebyshev expression is the gap between \(T_n\) and its tangent at \(\cos\alpha\), and the proof establishes that this tangent is globally supporting.
2. The zero set is exactly \(\pi\pm\alpha\). At either zero, the auxiliary harmonic vanishes, so a sampled contact gives the sharp upper bound on the first-harmonic coefficient.
3. The two contact fractions have reduced denominator \(4n\), so a finite grid contains them exactly when \(4n\mid m\).
4. If the grid misses them, strict positivity on the finite grid gives a positive perturbation margin for the first-harmonic coefficient.

The bundled script `artifacts/verify.py` checks these identities and the perturbation construction for all \(3\le n\le40\) and \(3\le m\le300\). Its finite scan is corroborative only and is not treated as proof for unbounded parameters.
