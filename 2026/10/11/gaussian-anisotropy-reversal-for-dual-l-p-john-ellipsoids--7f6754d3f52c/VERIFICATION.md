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

The argument is analytic. The following checks were completed.

1. The exact characterization equation was read from Theorem 1.3 of arXiv:2608.21958v1, and the Gaussian specialization was checked against Remark 3.7.
2. For a radial density, the first variation of the dual conical measure was recomputed directly:
\[
\delta\log\!\left(\rho^n\phi(\rho)\right)
=
\left(n+\frac{R\phi'(R)}{\phi(R)}\right)\delta\log\rho.
\]
3. The spherical tensor identity
\[
\frac n{|S^{n-1}|}\int (x\cdot u)^2u^{\mathsf T}Cu\,d\sigma(u)
=
\frac{\operatorname{tr}C+2x^{\mathsf T}Cx}{n+2}
\]
was used exactly, not numerically.
4. Scalar and traceless matrix modes were separated. The derivative in the ellipsoid variable has nonzero factors \(p\) and \(2(n+p)/(n+2)\), so no hidden neutral mode obstructs the implicit-function theorem.
5. A deterministic two-dimensional Gaussian stress test at \(p=3\) reproduced the predicted multipliers below, at, and above \(R=\sqrt5\). This check is supplementary and is not used to prove the theorem.

The claim is limited to first order. In particular, no computation here establishes the leading higher-order term at the critical radius.
