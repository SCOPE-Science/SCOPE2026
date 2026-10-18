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

The proof is analytic and self-contained. Reproduce the crucial boundary coefficient by setting \(h=1-r\) and \(u=(1-t)/h\) in the positive derivative kernel, then evaluate \(\int_0^\infty u^{1-\alpha}(1+u)^{-2}du\) as \(\operatorname B(2-\alpha,\alpha)\). Check compactness of \(D_\rho\mathcal H\), the nonnegative Taylor coefficients of the difference kernel, and the weakly-null little-Bloch embedding step.

For the lower bound, compute \(h_n^{\alpha-1}f_n(1-h_nu)\) using the defining derivative and \(h_n=n^{-2}\), \(w_n=1-n^{-4}\). The scaled integral is dominated by a constant times \(u^{1-\alpha}/(1+u/2)^2\), which is integrable precisely on \(1<\alpha<2\). The result makes no claim based on a finite sample.

The optional `CHECK_NUMERICS.py` evaluates \(A_\alpha(r)\) for selected exponents and radii and prints the ratio to the predicted Beta value. These values approach one with parameter-dependent rates; the code is not an exhaustive test or a mathematical certificate. No independent audit has been performed.
