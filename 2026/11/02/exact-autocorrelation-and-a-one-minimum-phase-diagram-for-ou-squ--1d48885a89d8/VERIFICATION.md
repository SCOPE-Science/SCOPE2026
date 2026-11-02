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

# Mathematical and computational verification

The critical analytic steps are the covariance of two integrated OU intervals, conditioning on the independent position Brownian noise, the strict covariance/variance derivatives of a positive tilted Laplace integral, and the sign of the envelope derivative. These steps are stated and proved in `RESULT.md` with the exact condition \(\kappa>2D_k/\mu^2\). The stationary covariance formula is valid for every \(t\ge0\); the strict response inequality holds for \(t>0\). Boundary thresholds are included; no inapplicable equality case has been silently omitted.

The attached `VERIFY.py` is standalone source code (requires NumPy and SciPy). It directly contrasts the defining integral and its first weighted moment against confluent hypergeometric evaluations at **81** parameter/lag combinations; tests the unique two-threshold order and all three envelope monotonicity classes for four positive noise levels; independently compares numerical covariance ratios against the averaged response; checks the weak-noise and long-lag expansions; and samples stationary OU stiffness paths to check a covariance without using the Gaussian moment-generating function from the analytic derivation. All checks executed successfully. The path check used 30,000 sampled paths, with analytical covariance approximately \(0.44011379\), observed estimate approximately \(0.43685757\), and a Monte Carlo standard error approximately \(0.00233857\). Finite sampling and quadrature do not establish a global theorem; the analytic derivation supplies the proof.

This verification establishes no independent audit and no independent external confirmation. It does not establish uniqueness against inaccessible literature. Claim-to-evidence scope is the overdamped scalar harmonic trap with an independent stationary OU stiffness and finite stationary variance.
