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

For n>=2 iid continuous uniform U[a,b], condition on the sample extreme endpoints: interior observations are iid uniform between them as unordered symmetric statistics, hence S^2 scales as R^2 times the variance of 0,1 and n-2 independent U[0,1] values. Evaluating E sum Z_i^2=1+(n-2)/3 and E(sum Z_i)^2=(n-2)/12+n^2/4 gives c_n=(n+1)(n+2)/(12n(n-1)) in E[S^2|R]=c_n R^2. With R/(b-a)~Beta(n-1,2) exact moments yield unbiasedness, Var(c_nR^2), Cov(R,S^2) and Corr(R,S^2)^2. The standard fourth central moment formula gives Var(S^2)=(b-a)^4(2n+3)/(360n(n-1)); the relative variance is 10(2n^2+6n+1)/[(n+3)(n+4)(2n+3)], equals one at n=2 and <1 for all n>=3, with asymptotic 10/n. Independently reconstructed all rational calculations for n=2..150, rather than trusting CHECKER_OUTPUT.txt. The conditional endpoint derivation establishes all n, and no UMVU or other-distribution claim is made.

## originality

PASS

Best-of-knowledge originality comparison by actual statement and implication, with historical and unavailable-material risks recorded; no priority certification. Inspected closest prior statements use different scopes/estimands or do not directly entail this final exact claim.

## value

PASS

An exact conditional L2 projection and unbiased range-only estimator for an unknown-width uniform distribution is a natural finite-sample statistical invariant, and the strict n>=3 variance improvement together with O(1/n) relative efficiency quantify a meaningful inferential gain. While conditional extrema and Beta range moments are classical, their explicit estimator-to-sample-variance efficiency and mixed covariance/correlation comparison are substantive reusable facts rather than arbitrary arithmetic, without claiming general optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
