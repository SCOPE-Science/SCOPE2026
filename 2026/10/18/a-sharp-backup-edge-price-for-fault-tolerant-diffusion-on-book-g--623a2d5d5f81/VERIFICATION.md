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
# Reproducibility

Run `python verify_bridge.py` in a Python environment with NumPy, SciPy and SymPy. The script was executed successfully against these exact source bytes. It checked the symbolic characteristic polynomial, its boundary evaluations and differentiation, the exact four-vertex price, direct full-Laplacian eigenvalues for multiple graph sizes and bridge ratios, worst outages, the derivative-defined optimum across price regimes, and independent asymmetric feasible assignments. The executed script reported `ALL CHECKS PASS 1295`, in addition to six symbolic assertions.

Every claim for unbounded graph size or continuous parameters is justified in the mathematical proof, not by the sample count. No external solver certificate or independent audit has been supplied. The paper records analytic uniqueness only for the symmetry-invariant allocation and for the hub-edge conductance across arbitrary global optimizers, not for all individual spoke weights.
