---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the positive L_p-spherical copula at fixed d>=2 and p>d−1, the radial-angular representation has Y=R^p~Beta(a=d/p,b=1−(d−1)/p) independent of W=(U_i^p)~Dirichlet(1/p,...,1/p). The boundary statistic is the maximum across samples of single-observation threshold roots Q(X). Conditional endpoint threshold satisfies r_t^p=(sum W_i^(1−t/p))^(−p/(p−t)), with 0<=z_t/t<=(log d)/(p−t) and z_t/t→H(W)/p. The beta upper tail is z^b/[bB(a,b)]+o(z^b), so bounded convergence yields P(Q>p−t)=κ t^b+o(t^b), κ=E[(H(W)/p)^b]/[b B(d/p,b)]. iid maxima then prove a.s. consistency and survival exp(−κ x^b) for M^(1/b)(p−p_hat). Independent high-precision quadrature gives κ_(2,2)=0.40611684413775677, agreeing with the claimed value. The numerical constant is not proof of the limit.

## originality

PASS

Best-of-knowledge distinct mathematical statement relative to the compared accessible primary results, with explicit access and broad-priority risks.

## value

PASS

The direct copula source proposes the moving-support p-star statistic as a natural estimator, but this determines its nonregular convergence rate M^(−p/(p−d+1)), complete Weibull limiting distribution and angular-entropy scale for every fixed admissible parameter. This gives useful inferential calibration and a nontrivial geometric coefficient, rather than a generic textbook extreme-value theorem with an uncomputed model tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
