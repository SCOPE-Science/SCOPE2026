---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Under record-bias weight theta^R with theta=lambda*n for fixed lambda>0, the independent rank insertion U_i law yields record indicators B_i=1{U_i=i} and descent indicators X_i=1{U_{i+1}<=U_i}, a bounded 1-dependent triangular array. The proof computes exact r_i,p_i,j_i=Pr(X_i=X_{i+1}=1), derives the finite covariance -theta*n*(n-1)/[2(theta+n-1)^2] by exponential-family differentiation of known ED, and integrates Riemann-limit variances: Sigma11=lambda log(1+1/lambda)-lambda/(1+lambda), Sigma12=-lambda/[2(1+lambda)^2], Sigma22=(6lambda^2+4lambda+1)/[12(1+lambda)^3]. Its conditional three-rank argument gives strict positive definiteness; gap-separated blocks of n^(1/4) produce the Lindeberg–Cramer–Wold joint Gaussian limit. Independent weighted permutation enumeration for n=2..7 and theta=1/2,2,3 verified exact means/covariances; symbolic integration checked the descent variance integrand; these finite tests are not an n->infinity proof.

## originality

PASS

Best-of-knowledge PASS for the explicit bivariate n^(1/2) CLT and strictly negative correlation at theta=lambda*n. Bouvel–Nicaud–Pivoteau give independent rank representation and exact record/descent means, fixed-theta marginal Gaussian results, and theta=lambda*n permuton/first-order statistics. The exact mixed covariance alone is a short derivative of an earlier mean and is NOT claimed new. No inspected primary theorem provides the joint covariance and fluctuation law in the linear record-bias regime.

## value

PASS

Linear record bias creates order-n records and a nontrivial permuton. The order-sqrt(n) joint record–descent Gaussian covariance and strict negative correlation provide a natural second-order law for a canonical permutation model; explicit covariance cannot be inferred from separate first moments or marginal CLTs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
