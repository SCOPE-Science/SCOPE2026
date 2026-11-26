---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Under the specified continuous simple null, the probability-integral transforms are iid uniform. The maximum's density is n t^(n-1); conditional on its value t, the other unordered observations are iid uniform on (0,t). Below t, the conditional squared empirical error is the binomial variance divided by n² plus the squared bias; above t the empirical CDF is 1. Integration against 1/[u(1-u)] gives exactly the three terms in the frozen formula. For the continuous conditional version, scale all order statistics by t: their normalized law is t-independent and the last normalized value is 1. The ordered-log formula then has a -n log(t) term and a positive weighted sum of expectations of -log(1-tV). The former is strictly convex and diverges at zero; the term for V=1 diverges at one. This proves existence and uniqueness of the interior minimum. For covariance, each log U_(j) contributes Cov(log M,M)=1/(n+1)² by independence after scaling. Given U_(j)=u, E[M|u]=1-(1-u)/(n-j+1), also valid at j=n. Differentiating the beta first moment in its first shape parameter gives Cov(Y,log Y)=b/(a+b)²; with Y=1-U_(j), this gives the negative upper-log contribution -j/[(n-j+1)(n+1)²]. Reindexing in the log statistic and summing gives the exact harmonic formula. It is zero at n=1, -1/36 at n=2, and H_n-2n/(n+1) is increasing. Harmonic asymptotics yield the stated order and constant. The proof covers n=1, including g_1=-1-log[t(1-t)].

## originality

PASS

Credit the classical ordered-log statistic and uniform-order-statistic tools. The supported distinct contribution is the joint simple-null calculation with the upper order statistic: exact regression, global shape and exact mixed moment. Neither the strongest same-day catalog neighbor nor the relevant conditional or component work inspected establishes or subsumes this combination. This is a bounded comparison, not a priority or literature-exhaustion claim.

## value

PASS

The statistic and upper order statistic are natural tail diagnostics under a common null. The exact regression shows that larger maxima do not affect conditional AD severity monotonically, despite a strictly negative mixed moment for n≥2. That distinction, with a finite-sample calibration and quantitative covariance decay, is substantively more informative than a marginal AD calculation or a numerical sign check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
