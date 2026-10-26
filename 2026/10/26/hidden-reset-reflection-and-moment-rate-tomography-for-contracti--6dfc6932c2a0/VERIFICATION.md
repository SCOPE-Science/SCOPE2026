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

The exact proof uses a two-sided marked-Poisson stochastic integral, contraction coupling, reflected-Brownian modulus dynamics, Poisson-product conditional moment coefficients, compact moment determinacy, a finite-atom Vandermonde argument, and stationary generator covariance formulas. These cover every regime \(D,r>0\) with multiplier law supported in \([-c,c]\), \(c<1\), rather than only sampled parameters.

`check.py` was run with SymPy and produced `PASS 211 exact symbolic/rational assertions` as recorded in `check_output.txt`; checks include a signed example at \(q=\pm2/3\). The checker supports algebra and normalization but does not establish stochastic convergence, moment determinacy, or novelty by itself. The limits of identifiability are exact-population conditions: high-order conditional moments may be difficult to estimate, and no sample-size or observation-noise result is claimed.
