---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For m>=2 uniform iid coupons, conditioning on first repeat B=t<=m leaves m-t+1 unseen types, and future coupon discoveries have independent geometric waiting times with parameters j/m. The endpoint B=m+1 implies C=m. Adjacent conditional laws couple with difference G_{m-t+1,m}-1>=0 (last endpoint separately), establishing strictly decreasing stochastic regression and negative quadrant dependence for all increasing tails. The exact birthday probability and harmonic conditional mean give covariance as a finite sum. With B/sqrt(m) Rayleigh and uniform exponential tails, the conditional mean difference D_m(B)=sum_{j=1}^{B-2} j/(m-j) is asymptotic B^2/(2m), and uniform integrability controls rare large B. Rayleigh moments E[R],E[R^2],E[R^3] yield Cov(B,C)/sqrt(m)->-sqrt(pi/8). Using Var(B)/m->(4-pi)/2 and Var(C)/m^2->pi^2/6 gives m Corr(B,C)->-sqrt(3/(2pi(4-pi))). All claimed exceptional and normalization cases are handled.

## originality

PASS

Marginal birthday Rayleigh and coupon-collector geometric waiting-time laws are classical. Conditional strict stochastic regression between first duplicate and complete collection on the same iid sequence, their exact mixed covariance and sharp sqrt(m) and 1/m correlation constants are the assessed additions. Known two-independent-collector studies and marginal limit theorems do not by themselves imply these mixed facts. Best-of-knowledge PASS qualified by older joint-occupancy literature not fully read.

## value

PASS

The first repeat and final coverage times are canonical linked stopping times, yet their joint negative regression is not determined by their well-known marginals. A sharp mixed covariance and correlation law characterizes a natural stochastic dependence scale and is meaningful independently of an overarching theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
