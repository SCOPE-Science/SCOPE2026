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

Completing the square gives a positive radicand, and 4d(1+dx²+rx)−(2dx+r)²=4d−r² gives a global Lipschitz constant q=sqrt(d/(1+d))<1. Pullback gives the bounded shift-equivariant process and Bernoulli ergodicity. For uniqueness even without a finite moment assumption, any stationary solution satisfies |X_t|<=K+q^m|X_{t−m}|, K=1/[sqrt(1+d)(1−q)]; stationarity and the probability tail as m→∞ imply |X_t|<=K almost surely, and common-sign contraction then identifies it with the pullback. Fresh fair signs center every conditional odd power and give E[X_t²]=1 on averaging the defining equation. Writing a=d/(1+d), b=r/(1+d), the centered square obeys Z_t=aZ_{t−1}+bX_{t−1}. The cross term is zero in the variance and in its covariance with older squares, giving Var(Z)=b²/(1−a²) and the geometric square covariance. Its mixed covariance has initial term b then factors a at each lag; the reverse mixed covariance is zero by conditional centering. B_2/B_1=a for r≠0, yielding both claimed inverses. Reflection preserves the one-time marginal after changing r to −r, while r=0 gives the exact iid fair-sign solution and loss of identification. A multinomial expansion leaves d^k M_{2k} as the sole top-order term, verifying the triangular recurrence. The supporting verifier was inspected, not run; the finite diagnostics it records are not needed for the analytical check.

## originality

PASS

Pass is for the fair-Bernoulli stationary dependence, moment hierarchy, and signed identification, not for the quadratic correspondence, wedge, or symbolic coding themselves. Source-level comparison supports this distinction; absolute historical priority is not established.

## value

PASS

The Bernoulli measure is a natural specified law on the known branch coding. Under that law the usual linear autocovariances vanish at every nonzero lag and the marginal cannot distinguish opposite r. Explicit mixed lag values resolve this exact ambiguity and give both parameters, while identifying the singular r=0 regime where no time-series statistic identifies d. This yields a usable population identification criterion and exact benchmarks for nonlinear dependence, rather than a restatement of symbolic existence or an arbitrary moment evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
