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
# Mathematical verification

The exact update, stationarity equation, fold polynomial, Jacobian and unit-disk inequalities are established in the accompanying analytic proof. Execute `python3 verify.py` with SymPy to independently recompute the derivative identities and the symbolic witness; a successful execution prints `VERIFY_OK`. The exact proof controls all \(a>0\), \(\rho>0\), \(b\in\mathbb R\), \(\ell>a\), and \(\beta\in[0,1)\). The checker uses finitely many symbolic operations, not an exhaustive numerical enumeration, and it does not certify nonlinear behavior at degenerate fold points.

No independent external audit or external validation is claimed.
