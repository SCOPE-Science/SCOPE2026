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

# Reproduction and boundaries

Execute `python verify.py` with SymPy and mpmath. The code independently recomputes the four dimensionless small-angle Taylor coefficients, the inverse-area second coefficient, and high-precision endpoint ratios at \(\(r/R\in\{1/5,1/2,9/10\}\)\). It checks the sign-transition algebra. The analytic proof in `RESULT.md`, rather than finite experiments, establishes the assertions for all \(\(0<r<R\)\) and every feasible illumination parameter.

The radius-\(R\) hull formula can be checked independently by intersecting its admissible disks: \(\mathcal C_s=B_{R-r}(0)\cap B_R((s,0))\). Polygonal approximations to this disk intersection at five parameter points agreed in area within \(10^{-5}\) at unit scale; this is only a numerical stress test. The exact boundary follows from two-point spindle arcs and supporting disks.

The terminal \(\(r=R\)\) case, exterior infeasibility beyond \(s=2R-r\), and any higher-dimensional or weighted version are outside the claim. The external independent-audit channel has not been performed.
