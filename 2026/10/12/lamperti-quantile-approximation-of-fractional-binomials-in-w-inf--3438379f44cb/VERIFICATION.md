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

All mathematical steps are contained in `RESULT.md`; this file records reproducible checks and their limitations.

The constructive Bernoulli law is given by the exact quantile formula
\[
p_\alpha(v)=\left[1+\exp\left(-\frac2\alpha\operatorname{artanh}\frac{\tan(\pi\alpha(v-1/2))}{\tan(\pi\alpha/2)}\right)\right]^{-1}.
\]
Its fractional log-cumulant identity is
\[
\alpha\int_0^1\log(1-p_\alpha(v)+p_\alpha(v)e^t)\,dv
=\log\frac{1+e^{\alpha t}}2.
\]
The bundled standard-library verifier checks this numerically over three distinct values of \(\alpha\) and five tilt parameters, using midpoint quadrature, and tests quantile symmetry and monotonicity.

The script also constructs the exact finite Bernoulli-convolution probability mass function recursively for the \(\alpha=2/3\) instance with \(N=3n\), and evaluates the one-dimensional quantile-coupling distance for \(n\in\{1,2,3,5,8,12\}\). A successful run prints a line beginning `VERIFY_OK alpha=0.666666666667`.

These checks are neither an exhaustive quantifier test nor an infinite proof. The exact mathematical certificate consists of the stable Laplace integral identity, Stieltjes inversion and explicit CDF differentiation, the Chernoff-and-tilt proof of the common rate function, and the full-level quantile comparison argument in `RESULT.md`. The stronger bounded-discrepancy question remains unproved.
