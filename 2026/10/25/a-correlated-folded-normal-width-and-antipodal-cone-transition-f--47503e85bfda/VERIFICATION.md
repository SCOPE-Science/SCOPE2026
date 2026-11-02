---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

From actual RESULT.md and code: the polytope is the convex hull of within-part indicator sets. Maximizing over each part gives exactly W(U)=(sum|G_i|+|D_+|+|D_-|)/(2||G||), including p,q>=1. The mean of D_± is μ(p−q), variance n(1/2−1/(2π)), covariance −n/(2π). A multivariate CLT including sum|G_i| and sum G_i², with cross-covariance order (p−q)/n→0, followed by the delta method, proves joint convergence and independence of Y of variance (1−3/π)/4. Portmanteau and Gaussian quadrant geometry imply F(t) and balanced arcsine value; derivative >0 at t>0 and Chebyshev handles divergent imbalance only for same-level probability. Cramér decomposition establishes genuinely non-Gaussian width at every finite t. Independently reconstructed 120 sample support enumerations, exact width identity and balanced arcsine constant; these finite checks do not prove asymptotic quantifiers. The exceptional all-one-sign directions have probability 2^(1−n).

## originality

PASS

Best-of-knowledge, not absolute priority: For canonical Euclidean two-level chain/stable-set polytopes of K_{p,q}, the centered spherical width and both antipodal exposed-level labels converge jointly at (p−q)/sqrt(n)→t to an independent Gaussian plus two negatively correlated folded normals; balanced same-level probability equals 1/2−arcsin(1/(π−1))/π and the imbalance transition is at sqrt(n). The inspected primary sources contribute prerequisite constructions or related weaker/different statements, without identifying a prior theorem that logically entails the distinctive final statement. Inaccessible/unindexed historical overlap remains an explicit risk.

## value

PASS

The standard chain polytope of a two-level poset is a canonical non-smooth full-dimensional object. Its opposite exposed-vertex classes are a natural normal-fan intersection statistic: the balanced antipodal class coincidence is strictly below one half, and the full directional width has a non-Gaussian square-root imbalance transition, despite the ordinary cube Gaussian CLT. The joint law, covariance and strict phase behavior are not recovered from the previously known mean width; mathematical scope stays tied to the standard Euclidean embedding and isotropic directions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
