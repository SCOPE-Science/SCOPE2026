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

At time n the urn contains n+1 balls; while X_n=x>0 the white/right probability equals (n+2-x)/[2(n+1)] <= 1/2 and conditional mean equals (n x+1)/(n+1). With s_n=P(T>n), a_n=E[X_n 1_(T>n)], the exact killed identity (n+1)a_(n+1)=n a_n+s_n telescopes to n a_n=1+sum_(k<n)s_k, with s_1=a_1=1. A common-uniform path coupling bounds subsequent survival by a simple symmetric walk absorbed at zero. Reflection gives Q_m(x)=P(-x<S_m<=x)<=min(1,2x/sqrt(m)). Hence s_(2n)<=2 n^(-3/2)(1+sum_(k<n)s_k). Starting from s_n=O(n^-1/2), applying the inequality yields O(n^-1), then O(log(n)n^-3/2), a summable tail, then O(n^-3/2). Summation yields E T<infinity and E T^theta<infinity for 0<theta<3/2, not a matching lower bound or endpoint result. The accompanying source exact-fraction checker is finite corroboration.

## originality

PASS

Best-of-knowledge PASS: Balaji and Mahmoud introduce the same one-dimensional opposite-reinforcement Friedman urn and explicitly conjecture finite expected first return, which the submitted stopped-moment/comparison proof establishes with a stronger n^-3/2 upper tail. Classical reflection bounds and existing Eulerian one-time laws alone do not imply stopped-path return moments.

## value

PASS

This directly settles a named finite expected first-return conjecture for a natural one-dimensional Friedman urn model. The quantitative n^-3/2 upper survival law and entire subcritical moment range are much stronger than mere recurrence and matter for renewal quantities; no sharpness or endpoint claim is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
