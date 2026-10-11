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

The displayed vector field has diagonal Jacobian entries \(-\sigma\), \(-1\), \(-b\), \(-d\), and \(-4b\), so its trace is exactly \(-\sigma-1-5b-d\). Jacobi's determinant identity then gives the tangent-volume law used in the proof. This analytic step is independent of trajectory, numerical integrator, and the value of \(r\).

`verify.py` uses exact `Fraction` arithmetic to check the source specialization \(-92/3\), the two printed spectrum sums, the exact discrepancies, and the corresponding determinant exponents at \(T=500\). It has no third-party dependencies and the packaged checker returns `VERIFY_OK`.

The checker does not reconstruct the source's Lyapunov algorithm and does not compute replacement exponents. The finding therefore stops at the exact incompatibility of the displayed full-spectrum vectors with the printed ODE.
