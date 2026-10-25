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

# Reproducibility and limits

The standalone program `verify.py` was executed against the formulas included here. It reports successful checks for the exact radial/angular constants, the threefold angular correlation for trigonometric sampling densities, the transverse Hessian, and near-maximum importance-sampling trials. With area-uniform points, the exact coefficient is \(32/(27\sqrt3\pi)\), approximately \(0.21780894633947345\). The numerical trials at area deficits \(0.02\) and \(0.005\) returned ratios to the predicted coefficient of approximately \(1.0230\) and \(0.9956\), with Monte Carlo uncertainties recorded by the script. For a radial-deficit boundary exponent \(b=2\) and angular perturbation \(p(\theta)=(1+0.35\cos(3\theta))/(2\pi)\), the conditional radial share means approach \(1/4\), while the angular-energy mean approaches \(1/8\). The normal-form derivation and Dirichlet integral in RESULT.md, rather than these finite checks, support the theorem.

Checks do not establish absence of stronger previously published theorems or furnish independent mathematical validation. The angular density must be strictly positive and continuous, and radial and angular coordinates must be independent. The theorem makes no finite-threshold error-rate claim.
