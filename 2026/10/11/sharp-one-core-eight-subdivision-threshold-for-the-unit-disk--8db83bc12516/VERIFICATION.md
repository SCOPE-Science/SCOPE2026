---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The claimed domain is the unit disk and eight connected subdivision regions with pairwise disjoint interiors, with at least one region disjoint from the outer circle. No equal-area hypothesis is used.

The critical lower-bound check is exact: a unit-circle chord of circular separation \(\delta\) has length \(2\sin(\delta/2)\). Therefore a boundary subset of diameter at most \(2\sin(\pi/7)\) lies in an arc of angle at most \(2\pi/7\). If one region misses the outer circle, at most seven such traces cover that circle, forcing one trace to reach the threshold.

The upper-bound construction uses \(s=\sin(\pi/7)\). The core diameter is \(2s\). In an outer sector, squared distance is \(r^2+t^2-2rt\cos\delta\), with \(r,t\in[s,1]\) and \(0\le\delta\le2\pi/7\). Monotonicity in \(\delta\) and convexity in each radial variable reduce the maximum to the corner cases. The outer-outer corner equals \(4s^2\); the inner-inner corner equals \(4s^4\); and the mixed corner differs from \(4s^2\) by
\[
(s-1)(4s^2+s-1)<0.
\]
The sign is certified without decimal approximation because \(s>2/5\), giving \(4s^2+s-1>1/25\).

The numerical value \(2\sin(\pi/7)\approx0.8677674782\) is included only as a consistency check. The unrestricted eight-subdivision optimum and a classification of interior equality interfaces are unproved and are not part of the claim.
