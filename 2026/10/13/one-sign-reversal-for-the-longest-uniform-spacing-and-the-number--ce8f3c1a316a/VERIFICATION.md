---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Conditional on D_1>t, the simplex section is t+(1-t)B_1,(1-t)B_2,..., so the covariance is mt(1-t)^(m-1)(R_m(delta)-H_m/m), delta=t/(1-t). Strict growth of the shifted-coordinate win probability p_m implies strict growth of its running average and one crossing. Endpoint signs follow from the beta/simplex section law and max-indicator at t=1/2. The exponential representation B_i=E_i/sum E_j and Gamma concentration give p_m(s/m)~e^s/m uniformly for s<=3 log log m, leading to the double-logarithmic location. Rational finite checks corroborate rather than prove the all-m result.

## originality

PASS

The distinctive global one-crossing mixed covariance and additive double-logarithmic crossover were not implied by the inspected primary spacing results. Known maximum-spacing and independent-exceedance techniques provide the basic tools but not the stated same-sample sign theorem; classical full-text historical coverage remains qualified.

## value

PASS

A naturally defined pair of statistics of uniform spacings shows an unexpected single sign reversal and an unusually early crossover on the log-log rather than log extreme-spacing scale. The exact all-m classification and location law offer a nontrivial answer relevant to dependence between extremes and exceedance counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
