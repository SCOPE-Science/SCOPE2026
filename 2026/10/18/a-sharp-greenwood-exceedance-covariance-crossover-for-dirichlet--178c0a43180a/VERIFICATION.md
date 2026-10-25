---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For X_i~Beta(a,b) under positive Dirichlet parameters, conditional Dirichlet decomposition gives E[G|X_i=x]=x²+c(1-x)² with c=Σ_{j!=i} α_j(α_j+1)/[b(b+1)]. Integrating the identities [x(1-x)f]′=(a-(a+b)x)f and [x²(1-x)f]′=((a+1)x-(a+b+1)x²)f yields Cov(1{X_i>t},G)=((1+c)/(s+1))t(1-t)f_{a,b}(t)(t-τ), τ=[2c(s+1)-(1+c)(a+1)]/[s(1+c)]. Since 0<c<=1 and s(1+c)(τ-1)=c(b+1)-(s+a+1)<0, τ<1 and the law has at most one interior sign switch (possibly none if τ<=0). For symmetric Dirichlet the root simplifies to (α+1)/(mα+2), and for α=1 it is 2/(m+2), with the stated Greenwood factor. For joint CLT represent X_j=Y_j/ΣY for iid Gamma(α,rate α), expand the moving threshold y*mean Y by empirical-CDF equicontinuity; iid influence functions A=1{Y>y}-p-yf(Y-1), B=Y²-μ2-2μ2(Y-1). Their covariance yields Σ11=p(1-p)-y²f²/α, Σ22=2(α+1)/α³ and Σ12=(y f/α)(y-(α+1)/α). Positive marginal variances follow nondegenerate gamma support and nonlinearity. Thus only limiting Gaussian independence is claimed at y=(α+1)/α. Independent rational beta-integral tests for 36 choices m∈{2,3,4}, α∈{1,2,3}, t∈{1/5,2/5,3/5,4/5} passed; CLT rests on analytic influence-function argument.

## originality

PASS

Royen 2010 explicitly studies the marginal distribution and quantiles of quadratic Dirichlet Greenwood statistics, and Ghosh–Jammalamadaka 1998 treats marginal spacing statistics; they do not in the material read give exact covariance of an exceedance indicator/count with G. The classical Pyke spacings survey and empirical-process CLTs can give background or parts of the asymptotic analysis; originality is assigned to the exact all-parameter labeled mixed-covariance identity and complete finite-m sign classification, not mere existence of a Gaussian limit. Resultary comparisons found no equivalent exact sign formula, with material risk of older spacing identities.

## value

PASS

Both Greenwood quadratic concentration and threshold exceedance counts are natural classic statistics of random spacings and Dirichlet compositional concentration. Knowing that their covariance changes from negative to positive at exactly twice the mean spacing for uniform gaps is a meaningful sharp dependence feature; the nonexchangeable coordinate criterion and joint fluctuation covariance expand it beyond a toy instance without claiming testing optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
