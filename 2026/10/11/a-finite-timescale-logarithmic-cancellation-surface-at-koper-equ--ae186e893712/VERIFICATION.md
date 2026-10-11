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
# Verification record

The model is the Koper polynomial ODE with finite positive \(k,\varepsilon,\delta\) on the ordinary equilibrium fold \(\lambda=2(k+3)r/3\), \(r=\pm\sqrt{(k+3)/3}\). The claim is local and excludes trajectories in the strong-stable manifold.

Run `python check_koper.py` with SymPy installed. It checks the fast equation's quadratic and cubic center coefficients, the \(y\)- and \(z\)-graph invariance residuals through cubic order, and the displayed logarithmic ratio. Every listed residual is exactly zero in symbolic arithmetic. The analytic proof, rather than code, establishes the center/stable splitting, reciprocal asymptotic and unique positive logarithmic-cancellation threshold.

Optional: run `python numerical_koper.py` with SciPy and NumPy installed. For \(k=\delta=1\), the critical value is approximately \(8.9544511501\). At \(\varepsilon=2\), the logarithmic coefficient is about \(-1.8763883749\); at the critical value it is zero; at \(\varepsilon=18\) it is about \(0.2020725942\). The compensated reciprocal is numerically near-constant at large finite times, but this finite-time experiment is not an infinite-time certificate.

The original Koper model and its equilibrium folds are traceable to Koper (1995), DOI 10.1016/0167-2789(95)90061-6; later analytic and numerical comparisons include arXiv:1406.1813 and DOI 10.1063/5.0073353. No independent scientific audit or validation has taken place.
