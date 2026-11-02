---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

A two-sided stationary Poisson clock has Exp(r) age; conditioning on no reset in (0,t] yields the exact covariance, and the positive same-monotonicity paired-difference identity gives strict positivity. Independent exponential cycles produce centered renewal rewards F(L)-mL, finite moments, the reward CLT, and exactly the Green–Kubo rate. For 0<alpha<1, scale U=rL and prove the relevant L² limit of the primitive, giving B_alpha>0; alpha=1 gives a log² border, alpha>1 an integrable primitive. Stationary variance has separate alpha<1/2, =1/2 and >1/2 regimes; division of half integrated variance by C(0) proves the five stated correlation-time equivalents. Domain alpha,r,T_*,tau>0 and order of limits were checked. Fresh independent numerical integration of regenerative rewards and an independently conditioned covariance agreed in six parameter cases to relative error under 1e-6; these finite tests do not prove asymptotics.

## originality

PASS

Qualified best-of-knowledge originality is limited to the evaluated two-time temperature covariance and the sharp divergent integrated-noise/vanishing static-noise regimes and five correlation-time equivalents; general resetting, stationary one-time moments and regenerative CLTs are established prior results.

## value

PASS

The known Poisson-reset granular cooling model has a physically motivated long-time integrated-temperature observable. Its exact positive covariance, sharp variance-rate divergence for alpha<1/2 despite vanishing stationary fluctuation, and five nontrivial correlation-time regimes isolate two genuinely different critical exponents and supply useful fluctuation thresholds. This is more than a routine named-parameter substitution; the distinct L² asymptotic regimes and logarithmic boundaries have mathematical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
