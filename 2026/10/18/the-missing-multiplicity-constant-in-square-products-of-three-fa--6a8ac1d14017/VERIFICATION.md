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

Erdős–Selfridge rules out equal factorial kernels across a gap of at least two. A gap of one gives equality precisely at a square, yielding disjoint pairs of indices {t²−1,t²}; their kernels exceed one (handle 2! directly). For b=n−1 the square condition is exactly s(n)=s(c!), and both indices of a repeated pair are allowed precisely when n=b_t u²≥t²+2. The exponential kernel bound leaves only finitely many lower-cutoff corrections and O(sqrt(log(2X))) significant summands, proving the error for M(X) after rounding. It also ensures convergence of both series. The distinct-endpoint count plus M(X) counts all consecutive-largest triples. Yudin's exceptional-endpoint bound alone does not bound triples with multiplicity, but his uniform estimate (3.2) bounds the two free parameters by X^η; applying the endpoint bound with exponent slack ε/2 and 2η<ε/2 gives the claimed triple error. The exceptional endpoints also account for all possible changes to the consecutive multiplicity distribution on nonsquares, whose positive leading endpoint constant is C₀−1. The first eight kernels and partial sum 0.55554194167094… were independently recomputed using Legendre exponents; the direct M counts at X=6,70,180,250 were 1,4,6,7. These checks do not prove the analytic estimates.

## originality

PASS

Credit the repeated-kernel observation, the exceptional-interval analysis, and the distinct-endpoint asymptotic to prior work. The supported distinct claim is the weighted triple count with the positive leading correction K and the resulting multiplicity asymptotics. Neither the endpoint result nor the prior total-count bound states this correction.

## value

PASS

The distinction between endpoints and triples changes the leading coefficient of an explicit published conjecture, not merely its error term. The result also quantifies the positive-density two-representation stratum among the nonsquare endpoints of minimum length three, separating the systematic duplicate family from the exceptional shorter-interval configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
