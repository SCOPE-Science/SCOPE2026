---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For n>=2 the n uniform gaps have Dirichlet(1^n) law. For any set of j coordinates all exceeding t, its probability is (1-jt)^(n-1), and conditional remaining mass 1-jt is another uniformly distributed Dirichlet simplex. Expanding Q conditional on this event yields jt^2+2jt(1-jt)/n+2(1-jt)^2/(n+1). Inclusion-exclusion in E[M Q]=integral E[Q 1_{M>t}]dt reduces to the exact beta-integral contributions 2/(n(n+2)j)+2/(n(n+1)(n+2)j^2). Binomial sums for j^-1 and j^-2 give H_n and (H_n²+H_n^(2))/2, proving E[M Q] and covariance (H_n²+H_n^(2)-2H_n)/(n(n+1)(n+2)). Marginal Dirichlet fourth moments and maximum-gap tail formula give the displayed varQ and varM, with strict positivity because (H-1)^2+(H2-1)>0 for n>=2. Harmonic asymptotics prove covariance ~(log n)^2/n^3 and correlation ~(sqrt6/(2pi))(log n)^2/sqrt n. Independently calculated alternating binomial-beta formula and exact fractions for n=2..10 (n=2 covariance 1/48). Rotationally symmetric circular spacings have the same Dirichlet vector. This is not an independence theorem.

## originality

PASS

Independently compared actual mathematical implications and the natural invariant against ranked published results and the primary material actually read. The specific evaluated final claim was not found as a stated theorem or direct special case; all relevant earlier general techniques are credited and priority limitations retained.

## value

PASS

The largest gap and Greenwood squared-spacing sum are classical yet distinct goodness-of-fit diagnostics; their exact finite-n mixed covariance and slow vanishing correlation quantify the dependence between two natural statistics, rather than a trivial normalization or margin calculation. The joint moment is not determined by the two marginal moment lists.

The dated certificate retains the supplied scientific assessment, sources and limitations.
