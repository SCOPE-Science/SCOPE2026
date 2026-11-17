---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For independent cells f_i(t)=X_i+sqrt(v)(Z_i cos(2πt)+W_i sin(2πt)), covariance 1+v cos2π(t-s) is positive semidefinite; I_i=X_i and y_i=X_i-sqrt(v)Z_i. Exact Gaussian leaf posterior is mean y_i/(1+v), variance v/(1+v). At height j with m equal-size independent children, pseudo-observation merge with exact prior child-integral C=m I_2 multiplies child means by (1+jv)/(1+(j+1)v) and yields variance 2m v/(1+(j+1)v). Induction gives root mean Y/[1+(h+1)v] and reported variance n v/[1+(h+1)v]. Conditioning independent leaves once instead yields Y/(1+v), nv/(1+v). From S-Y/D=((D-1)ΣX_i+sqrt(v)ΣZ_i)/D, D=1+(h+1)v, true variance n[(D-1)^2+v]/D², so the reported-error variance ratio is [1+(h+1)^2v]/[1+(h+1)v]→∞ and Gaussian z-interval coverage tends 0, asymptotic sqrt(2/π)z/sqrt(h+1). Independent rational recombination checks h<=5 and three v; these are checks, analytic induction proves all depths.

## originality

PASS

Weiland–Karvonen–Hennig 2026 primary full text explicitly gives the Gaussian hierarchical pseudo-observation equations (Section 3.2), but its convergence theorem analyzes quadrature under regularity and does not state the present depth calibration failure or exact coverage law. Distributed Gaussian-product expert overconfidence and nested Kriging theory concern different aggregation/cross-covariance assumptions, not the defined repeated posterior-mean pseudo-noise rule. No matching example or bound emerged from targeted indexed searches. Best-of-knowledge PASS with artificial-model limitations.

## value

PASS

A quantitative prior-predictive coverage collapse to zero despite correct finite-rank leaf GPs and oracle child prior covariance is a motivated and potentially diagnostic negative counterexample to a specified Bayesian quadrature fusion rule; it separates numerical accuracy/convergence from uncertainty calibration rather than merely renaming a Gaussian identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
