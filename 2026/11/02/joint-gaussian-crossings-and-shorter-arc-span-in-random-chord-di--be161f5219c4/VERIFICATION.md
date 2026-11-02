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

The exact finite-sample checker is `verify.py` and uses Python 3 standard-library `fractions.Fraction`. In the packaged run it passed 13,895 exact assertions, including exhaustive independent enumeration of all matchings for \(2\le n\le7\) and symbolic-formula comparisons at additional finite sizes. Run `python verify.py` from the extracted directory.

Analytic checks: the independent-endpoint coupling gives the uniform matching law; the crossing kernel has first Hoeffding projection \(2s(1-s)-1/3\) with variance \(1/45\); the shorter-arc rank-correction kernel has conditional mean zero in both coordinates, because \(f(1-x)=f(x)\). Its off-diagonal sum therefore has variance of order at most \(n^2\). The remaining cusp-error term is \(O_p(n^{4/3})\); each is negligible after \(n^{3/2}\) scaling. The bivariate iid CLT then proves the claimed nondegenerate Gaussian limit.

The enumerations are finite checks and are not treated as a proof of convergence for all sizes. Historical originality of the joint limit is assessed against the specifically inspected sources; an undiscovered equivalent result remains possible. Independent audit is not performed.
