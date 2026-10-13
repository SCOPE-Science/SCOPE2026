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

# Reproducibility and verification limits

Run `python3 verify_order_gini.py` beside this file. The code uses Python's standard library and reports its exact-rational and seeded numerical checks.

The independent calculation forms the covariance matrix \(\operatorname{Cov}(X_{(i)},X_{(j)})=\lambda^{-2}\sum_{r=n-\min(i,j)+1}^{n}r^{-2}\). A second linear representation \(G_n=\frac{2}{n(n-1)}\sum_i(2i-n-1)X_{(i)}\) then gives the mixed covariances and Gini variance. These exact identities are tested for every rank through sample size 45 (1,034 rank cells) against the formula stated in the result. Independently generated samples are used for four simulation comparisons, alongside direct pairwise differences and gap reconstruction. Five numerical maximizer searches and bisection check the numerical constant.

The tests establish only their specified finite numerical/exact instances. Independence of exponential spacings, the finite-sample formulas for all \(n\), monotonicity of the limiting profile, and control of boundary rank sequences are justified analytically in `RESULT.md`. No independent audit has been performed.
