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

The analytical argument is given in RESULT.md. The spectral inversion uses the Stieltjes/Pick property of the renewal Laplace transform, a uniquely located simple pole, its explicitly computed residue, and the continuous spectral measure recovered from upper-half-plane boundary values. These steps establish the infinite-parameter and infinite-distance statements, not the finite tests.

Run `python check.py` with NumPy and SciPy installed. At preparation time this checker completed 53 assertions. Tests include transform equality for several \(q\)-values, exact mass normalization by integration, the stationary variance identity, Gauss--Laguerre matrix eigenvalues, the exponential small-refresh scaling, and the dominance of the slowest exponential for large spatial displacement. The quadrature and eigenvalue computations have finite precision and do not constitute rigorous numerical bounds on arbitrary parameters.

As a numerical illustration, for \((L,\mu,D)=(1,1/2,1)\), the pole data are \(s_*\approx0.10185321148\), \(\delta\approx0.39814678852\), and \(A\approx0.51163648391\); the moment-defined effective rate is \(r_{\mathrm{mom}}\approx0.58352852899\). For \((L,\mu,D)=(1,0.05,1)\), the pole weight is approximately \(4.6290172\times10^{-7}\), explaining the small amplitude of the true asymptotic at slow refresh.

Limits: no exact computer-assisted enclosure for \(\mu\to0\) or \(|x|\to\infty\) is claimed; those limits follow from the written analytic estimates. This is a self-review only, not independent validation.
