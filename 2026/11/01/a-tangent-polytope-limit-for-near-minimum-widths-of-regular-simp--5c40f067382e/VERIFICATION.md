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

Run `python verify.py` from the extracted package with Python 3, NumPy and SciPy installed. The checker evaluates exact formula identities, uses an independent exact CDF for the equilateral triangle, integrates the nonlinear spherical area for a tetrahedron (instead of relying on a first-order volume approximation), and checks the exact local chart and angular slope bounds for representative finite dimensions. Successful execution prints `ALL_CHECKS_PASSED`.

The proof is analytical and valid for every fixed integer \(n\ge3\). Finite numerical checks neither certify all dimensions nor establish historical originality. The independent audit has not been performed.
