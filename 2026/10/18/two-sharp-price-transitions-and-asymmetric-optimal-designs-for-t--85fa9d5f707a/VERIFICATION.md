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

The reproducibility command is `python verify.py` from the folder containing this document and the standalone program. Python >=3.10 and NumPy >=1.24 are required. The code reconstructs complete weighted graph Laplacians directly from every conductance, compares their second eigenvalue with exact rational spectral-branch formulas, verifies all displayed price thresholds and budget equalities for a range of integer community sizes, and stress-tests arbitrary independent edge assignments against the universal Rayleigh upper bounds. It checks a rational, asymmetric high-price optimum separately. Local execution completed 3,055 checks successfully.

Verification is finite and numerical where full eigenvalues are computed; it does not replace the universal proof. In particular, near-multiple floating-point eigenvalues have tolerance of order \(10^{-9}\), whereas each formula for the three symmetric eigenvalue branches and the aggregate budget is checked in exact rational arithmetic. No exhaustive claim is made for arbitrary sizes or edge assignments. Independent audit and external validation have not been performed.
