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

# Reproducible numerical checks

Run `python verify.py` with Python 3 and the SciPy library. This script compares (i) the Lamperti Stieltjes formula with independent, endpoint-regularized numerical integration, (ii) the unique renewal root with the explicit parametric formulas, (iii) the symmetry identity \(\psi(k)=k+\psi(-k)\), (iv) the known exact Brownian occupation rate \(I(x)=r[1-2\sqrt{x(1-x)}]\), and (v) the normalized non-Brownian edge-cusp constant for \(\mu=1/5,1/3,1/2\). All scripted finite checks completed successfully during preparation, reporting `PASS 96` parameter-group cases with multiple assertions per case.

The analytic proof does not depend on the numerical root solver or quadrature. In particular, finite samples cannot establish the full large-deviation principle, exact root uniqueness, all-parameter convexity or a limiting asymptotic. The checks independently support the constants and formulas used in the proof under the stated finite parameter selections.
