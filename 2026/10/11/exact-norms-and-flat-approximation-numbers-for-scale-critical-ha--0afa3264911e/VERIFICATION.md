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
# Analytic verification and limitations

The scalar change of variables \(t=e^{u+v}\) and the Lebesgue Jacobian \(dx=e^u du\) give the exact input/output norm identities shown in the proof. The test functions \(L^{-1/p_i}t^{-1/p_i}\mathbf1_{[1,e^L]}(t)\) have exact unit input norms; their common constant-output region of logarithmic length \(L-R\) forces the sharp limit \(A_1A_2\). This is a direct infinite-dimensional proof, not an extrapolation from finite tests.

For nonattainment, equality in the strictly convex \(L^{p_i}(\mathbb R)\) norm of a positive average of translations would imply two distinct translates of a nonzero integrable function coincide, forcing nonzero periodicity and contradicting finite \(L^{p_i}\) norm.

For the compact-distance assertion, the full image of the product unit ball under a compact bilinear map is totally bounded. Each target function has vanishing \(L^q\) mass on shrinking intervals; a finite net transfers this to the full image. The exact norm-preserving input dilation transforms output by \(r^{1/q}y(rx)\), concentrating its mass at zero. This supplies the reverse distance bound. If \(q<1\), every triangle step is applied after raising quasi-norms to \(q\), which is a metric power.

Arithmetic check at \(p_1=p_2=2\), \(\lambda_1=\lambda_2=2\): each kernel mass is \(2(\sqrt2-1)\), so their product is exactly \(12-8\sqrt2\). The old \(\log2\) estimate is an upper bound, not equality. At unequal widths \((2,4)\) the exact product is \(4(\sqrt2-1)\).

The proof covers only fixed multiplicative windows, exact critical scaling and finite input exponents above one. It does not assert extension to noncritical exponents, variable endpoint functions or general weights. No external independent audit has been performed.
