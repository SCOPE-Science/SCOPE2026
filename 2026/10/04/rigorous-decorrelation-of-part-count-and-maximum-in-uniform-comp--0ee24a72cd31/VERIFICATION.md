---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The fair-cut encoding gives exactly K_N=1+S and M_N=1+L. Conditional on S=s, the one-locations form a uniform s-subset; flipping a uniformly selected zero gives a uniform (s+1)-subset and cannot increase the longest zero run, yielding the stated strict stochastic regression. Conditioning on all coordinates except i gives -Cov(X_i,L)=E[Delta_i]/4, while the zero-to-one influence contribution is E[Delta_i]/2; summing proves the exact covariance identity. Only a unique longest zero run can contribute to the fixed-string decrement, and summing the split loss across a run of length ell gives at most floor((ell+1)^2/4). The elementary union bound P(L at least k) <= n 2^{-k} yields the displayed second-moment bound and hence the explicit covariance estimate. Together with Var(K_N)=n/4 and the classical positive lower bound for the longest-run variance, this proves the correlation rate to zero from below. A fresh independent exhaustive replay for bit lengths 1 through 10 reproduced the covariance/influence identity, strict negativity, and every adjacent conditional stochastic-order inequality; the package verifier separately checks through length 16.

## originality

PASS

Finch studies exactly the number of parts and maximum part of a uniform random composition, reduces them to the number of ones and longest zero run, reports negative numerical correlations, and explicitly calls for a rigorous proof that the correlation tends to zero. Philippou--Makri give an exact conditional longest-run distribution given the total number of successes, but the inspected source description does not state the monotone subset coupling, influence identity, or quantitative covariance bound. The submitted result therefore resolves a stated rigorous-decorrelation gap and strengthens it to stochastic negative regression and an exact influence formula. Targeted Resultary search located no stronger published equivalent theorem.

## value

PASS

The theorem resolves the rigorous asymptotic-decorrelation question explicitly raised for uniform compositions and gives substantially more structure than the limit alone: all monotone transforms are negatively associated in the stated two-variable sense, with an exact coordinate-influence identity and an explicit quantitative rate. This is a motivated probability result on a natural composition model, not a finite numerical observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
