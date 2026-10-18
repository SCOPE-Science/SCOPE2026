---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For the exactly specified parent density f_T(t;a)=a^2(a+t)e^(-at)/(a^2+1), independent of the unit transform X=T/(1+T), differentiate log f twice. Expected minus second derivative equals 2(3a^2+1)/(a^2(a^2+1)^2)+a^2/(a^2+1)e^(a^2)E1(a^2). The last term follows from integral of e^(-at)/(a+t). E1 asymptotics give lim(a sqrt I)=sqrt 2 as a->0 and =1 at infinity, proving Jeffreys sqrt I cannot be proportional to 1/a. For sample t_i=x_i/(1-x_i)>0, the log-uniform posterior is O(a^(2n-1)) near 0 and O(a^(n-1)e^(-a sum t_i)) at infinity, hence proper for all interior nonempty samples. Independent mpmath quadrature at a=.03,.2,1,4,30 agrees with the expectation and limiting behavior.

## originality

PASS

The target 2026 unit-Shanker source presents the inverse-scale improper gamma-kernel choice as Jeffreys, but defining Jeffreys by expected Fisher information produces a distinct exact exponential-integral formula. The 2019 parent-Shanker Bayesian treatment makes the same gamma-to-log-uniform limiting choice but its inspected prior discussion does not derive the Jeffreys-rule prior. Parameter-independent unit transform makes parent and unit model equivalent here; searches for prior, exponential integral and correction yielded no matching prior formula. Some publisher full-section content could not be re-inspected, retained as access/priority risk.

## value

PASS

The correction concerns an actual named inferential procedure in a current distribution article: posterior summaries reported as Jeffreys analyses depend on a prior different from the genuine Jeffreys-rule prior. The exact formula allows recalculation and the propriety proof prevents overstating the error as invalid Bayesian inference. This is substantively motivated, not merely renaming a parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
