---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS: The free positive occupation fraction is a ratio of two independent positive mu-stable variables, yielding E[(a(1-V)+bV)^(-1)]=(a^(mu-1)+b^(mu-1))/(a^mu+b^mu). Conditioning on the first independent Poisson reset gives M_k(t)=e^(-rt)g_k(t)+r(e^(-r.)g_k)*M_k and Laplace denominator 1-rG_k(r+s). The unique real pole has r+psi>max(0,k) because the Stieltjes function strictly decreases from infinity at the endpoint to zero. Exponential tilting of its finite-mean, nonlattice renewal kernel gives the growth exponent psi(k), analytic strictly convex by the positive tilted-excursion variance. Gärtner–Ellis plus compact support gives the full LDP with boundary limits by continuity from interior. The q=(r+psi-k)/(r+psi) substitution gives the displayed parametric formulas; expansion q->0 proves I(eps)=r-[r/mu](mu/(1-mu))^(1-mu)eps^mu+o(eps^mu). The mu=1/2 boundary recovers the known Brownian rate. Independent high-precision Stieltjes/pole/quadratic-core calculations checked mu=.25,.4,.5. These numerical checks do not replace the infinite-time renewal proof.

## originality

PASS

PASS best-of-knowledge: Frimpong–Bresque–Roldán (2026) provide the free sluggish Lamperti distribution, reset occupation transforms and long-time Gaussian core but not this full nonquadratic LDP/edge exponent in inspected Section 6.1 and conclusion. Den Hollander et al. (2018) prove a Brownian mu=1/2 occupation LDP and general resetting methods. The audit claims only the alpha>0 explicit rate and exact sluggish edge coefficient, not generic resetting theory. General positive-stable functional LDPs may imply a specialization, a material residual priority risk.

## value

PASS

PASS: The exact non-Gaussian rate and fractional endpoint exponent quantify exponentially rare occupation imbalance in the recently studied sluggish reset model. They sharpen a Gaussian central-limit core to an entire constrained large-deviation law and precisely isolate a physically meaningful dynamical parameter mu; this is a motivated missing statistic, not a general theorem restated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
