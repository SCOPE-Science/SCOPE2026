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

The population OU covariance is \(A e^{-a|t|}/(2a)\), the nuisance covariance is \((B/2)q(|t|)\), and independence fixes the covariance sum. Differentiating \(C_a(t)=[r e^{-at}+a q(t)]/(r+a)\) gives \(r e^{-at}[q(t)e^{at}-1-(r+a)t]/(r+a)^2\); direct symbolic simplification returned zero for the difference. Strict convexity and the first derivative at the origin establish an **infinite-domain** sign classification; the finite numerical examples below are supplemental only.

For the independent three-rate example \(r=0.4\), with rate/mass pairs \((0.7,0.2)\), \((1.5,0.3)\), \((5,0.5)\), solving \(\sum_j p_j e^{(a-\beta_j)t}-1-(a+r)t=0\) yields unique positive lags approximately \(15.8422975046\) for \(a=1\), \(2.6440311110\) for \(a=2\), and \(0.7138126494\) for \(a=4\). Independent evaluations on either side give the expected opposite signs. These calculations can be reproduced with bisection and standard exponential evaluations.

To verify the edge coefficient, translate the nuisance rate distribution by its spectral infimum, integrate its Laplace transform by parts, and use the exact assumed edge-mass asymptotic to obtain \(K\Gamma(\kappa+1)t^{-\kappa}\). The fixed-lag root identity then gives both the leading \((\kappa+1)\log t/t\) term and its constant. The proof does not claim quantitative finite-sample detection or effective error estimates beyond its asymptotic \(o(1/t)\) remainder.

An independent audit has not been performed.
