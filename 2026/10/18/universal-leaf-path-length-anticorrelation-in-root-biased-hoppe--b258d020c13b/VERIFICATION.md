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

Writing J for a leaf-parent indicator and d for parent depth gives leaf/path increments 1−J and 1+d and leaf-depth increment 1+(1−J)d. The conditional mixed covariance is L_n P_n/W_n²−Q_n/W_n; the covariance of the conditional means has coefficient 1−1/W_n², so combining gives C_(n+1)=C_n−delta_n/W_n as stated. The mean leaf-depth recurrence gives delta_(n+1)=(1−1/W_n)delta_n+1/2−h/[2W_n(W_n+1)], h=theta(1−theta); the forcing and the base theta/(theta+1) are positive. With D_n=(W_n−1)(delta_n−W_n/4), one obtains D_(n+1)−D_n=−h/[2(W_n+1)] and D_2=−theta(theta−1)^2/[4(theta+1)]. Summing this recurrence and then C_(n+1)−C_n gives the displayed exact harmonic term by partial fractions; C_2=0 and C_3=−theta/(theta+1)^2. The fixed-theta error and the correlation normalization follow. For x=theta+1>1, trigamma(x)<x^−2+x^−1<2/x, proving positivity of the variance constant. An independent exact enumeration of 29,565 weighted tree instances agreed in all 35 cases (sizes 2–8, root weights 1/3, 1/2, 1, 2, 5).

## originality

PASS

Credit the exact mixed formula, its strict sign and asymptotic consequences across fixed positive root weights, not the exact uniform-tree covariance or either marginal variance. The inspected uniform-tree records have exact overlap at theta=1; the strongest same-day result additionally proves asymptotic independence there, but its growth law fixes theta=1 and its theorem does not subsume the root-biased formula.

## value

PASS

An exact finite-size dependence law distinguishes one model bias from universal behavior: every positive fixed root weight gives strict negative dependence, the linear covariance coefficient is bias-independent, and its correlation coefficient depends on theta through a known fluctuation scale. This is a useful benchmark for joint limits and not merely the established uniform parameter case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
