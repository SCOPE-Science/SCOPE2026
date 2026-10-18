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
# Verification and reproducibility

The finite checker is `checker.py` and requires only the Python standard library. Execute `python3 checker.py` in the directory containing `RESULT.md` and `checker.py`. The checker evaluates the closed circular-cap identity against independent quadrature, the endpoint norm against direct polar midpoint integration, sample interior evaluation norms, monotonicity along a finite mesh, two limiting expressions, and the local \(5/2\) coefficient.

The analytical basis is separate: covariance gives the reproducing kernel; absolute-kernel convexity gives the outer-boundary maximum; integration yields the exact cap function; a single-crossing weighted derivative proves strict monotonicity; and a tangency integral gives the nonanalytic term with its exact coefficient. Numerical assertions do not certify all radii or rule out previously published equivalent statements.

No independent audit or validation has been performed.
