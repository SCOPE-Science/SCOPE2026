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

# Verification of the exact finite-sample Gaussian null mean

The attached `verify.py` evaluates the explicit confluent-hypergeometric formula, checks its defining beta moments by numerical quadrature, and separately constructs the original Fourier–Stein statistic from standardized Gaussian samples.

Executed from the package with `python verify.py`. The check reported `PASS 101 independent beta-integral, exact-simplex and Monte Carlo comparisons` and the reference value `1.4582618412279` for \(n=5\), \(d=2\), \(a=1\). In detail, 36 independent beta-integral comparisons, 60 exact regular-simplex comparisons, and five Gaussian simulation-mean comparisons passed. Monte Carlo comparisons use a six-standard-error-plus-tolerance criterion and do not prove equality for infinitely many parameters.

Analytical dependencies to recheck: (i) the original source's exact finite-data representation, including the theoretical Gaussian characteristic function; (ii) the Haar projection law for a centered Gaussian data matrix; (iii) beta projection marginals, including the \(n=d+1\) point-mass case; (iv) the conditional rotational trace identity \(\mathbb E[Q\mid Z]=(d-Z)/(n-2)\); and (v) the resulting combinatorial counts of diagonal and distinct-index contributions. These are all derived in `RESULT.md`.

No exact critical value, infinite-dimensional numerical certification, external validation, or proof by finite numerical enumeration is claimed. Special-function evaluation at extreme parameters may require increased precision.
