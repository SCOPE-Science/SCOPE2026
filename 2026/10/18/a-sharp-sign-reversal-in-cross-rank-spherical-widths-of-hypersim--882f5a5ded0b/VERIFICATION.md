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

Reconstructed the proof for fixed positive rank fractions (not fixed ranks) and one common spherical direction. Optimizing the indicator dot products gives differences of top and bottom k sums; centering Gaussian coordinates cancels from their difference. The empirical-CDF bound at tolerance n^(-1/3) puts each empirical quantile within O(n^(-1/3)) of its fixed threshold, and the convex positive-part objective has slope O(n^(2/3)) there, so the replacement costs O(n^(1/3)). A polynomial fourth-moment bound for n times one plus the Gaussian maximum controls the exceptional event in L2. Floors cost O(1), including at half rank. Expanding the residual chi radius gives influence variable X_alpha−EX_alpha−phi(t_alpha)(Z^2−1); integration by parts gives E[X_alpha(Z)(Z^2−1)]=2phi(t_alpha), and the mixed positive-part integral yields the stated formula. The exact covariance identity from independence of the common radius and all widths, with Var(chi_(n−1))→1/2 and E[T]/E[R] the mean width, establishes actual covariance convergence separately from weak convergence. In the half-rank comparison, G(0)=1−3/pi>0, Mills' ratio gives a negative tail tending to zero, and B=G'/2 decreases, increases, then decreases according to the quadratic sign of B'/phi. Because B(0)=0 and B is positive eventually, it crosses once on its increasing interval; G therefore has exactly one positive zero. Independent scalar bisection gives t*=0.813387056891897 and alpha*=0.207998088885385 and the stated sample signs. The frozen verification note and numerical checker were read, not executed; no simulation is needed for the limit.

## originality

PASS

Best-of-knowledge pass for the explicit same-direction off-diagonal kernel, actual covariance convergence and analytic unique sign transition. The Gaussian order-statistic methods, cube endpoint, and diagonal dense-rank formula have real overlap; they do not supply the full claim in the inspected sources.

## value

PASS

The same direction is the natural coupling across uniform-matroid ranks. The explicit kernel identifies how angular normalization creates strictly negative dependence where the Gaussian trimmed-sum contribution is nonnegative, and provides a sharp, nontrivial dividing rank rather than isolated sign examples. It is usable for comparisons across dense ranks and separate from a scalar variance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
