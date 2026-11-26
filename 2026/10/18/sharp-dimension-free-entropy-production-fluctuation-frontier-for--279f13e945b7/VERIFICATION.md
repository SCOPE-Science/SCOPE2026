---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For finite-dimensional positive-definite Gaussian pairs, whitening P and diagonalizing the relative precision gives log(p/q) as a constant plus the sum of (u_i−1)Z_i^2/2−u_i m_i Z_i under P. The normal quadratic and linear terms have zero cross covariance, yielding k_i=[h(u_i)+u_i m_i^2]/2 and v_i=(u_i−1)^2/2+u_i^2 m_i^2. At fixed k_i>0 the feasible u are exactly the two-root closed interval, with m_i^2=(2k_i−h(u))/u. The derivative of the resulting v with respect to u is 2k_i−h(u), strictly positive in the interior; endpoints have m_i=0. The endpoint functions have derivative 2u_±(k) and strict concavity/convexity on k>0. By continuity at zero and strict subadditivity of the lower endpoint function (superadditivity of the upper), equality at K>0 requires a single nonzero k_i. All other modes have u_i=1,m_i=0, so the means coincide. Varying the one nontrivial mode across its interval constructs every V in every dimension; K=0 forces P=Q. Direct bisection of h(u)=2K reproduced the displayed numerical V intervals at K=1 and 8. Inspected RESULT.md, VERIFICATION.md, verify.py and requirements.txt; the frozen checker and its sampling assertions were not rerun. The entropy-production rescaling is conditional: Ding–Quan–Tu §3.3 eqs. (35)–(40) require exact score and infinite forward time, and use X sampled from P at the endpoint.

## originality

PASS

In the compared work, the endpoint entropy-production identity and unconstrained Gaussian moments are prior ingredients, and the scalar allocation strategy and one-exceptional-eigenvalue pattern closely resemble reverse-KL results. The supported distinction is the fixed-forward-KL attainable interval for forward log-likelihood-ratio variance, including equality and no gaps, not the general methodology or the physical identity.

## value

PASS

A fixed mean log-likelihood ratio does not constrain the variance to one value even within full-rank Gaussians. The result gives sharp, dimension-free extremes, exact extremizers and realizability of all intermediate variances; these let researchers benchmark Gaussian fluctuation comparisons without arbitrary dimensional or conditioning cutoffs. The physical application is limited to the cited endpoint assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
