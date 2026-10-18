---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Identify a regular side-ℓ n-simplex with ℓ/√2 times standard coordinate simplex Δ_{d−1}, d=n+1; averaged vertices give all integer compositions m of k scaled by 1/k. For q=kp, nonnegative floors b_i and fractions f_i, r=Σf_i is an integer 0≤r≤min(k,d−1). Exchange argument shows nearest integer composition rounds up exactly the r largest fractions, so squared error is min_{|S|=r}||f−1_S||². The hypersimplex {f in [0,1]^d:Σf_i=r} is convex hull of r-subset indicators: averaging over its indicator vertices gives bound r−Σf_i²≤r(d−r)/d. Equality forces all f_i=r/d and is attained there; each r class feasible via b composition of k−r. Maximize concave integer r(d−r) to obtain r*=min(k,floor(d/2)); tied r when odd d at large k. Undo scaling gives ℓ/k sqrt(r*(d−r*)/(2d)); all deep holes p_i=(b_i+r/d)/k with b summing k−r and count Σ_r binom(k−r+d−1,d−1). Edge d=2,k=1 and d odd ties included. Independent exact Fraction re-enumeration of every predicted deep hole and its nearest grid squared distance for 30 (d,k) pairs 2≤d≤7,1≤k≤5 passed; infinite result rests on hypersimplex argument.

## originality

PASS

The full-space root-lattice A_n covering radius and its high-k numerical expression are known and expressly NOT original. The exact finite-domain low-k radius profile, threshold, and all farthest-site count for a regular simplex vertex Minkowski average constitute the narrow remainder. Meyer and van Hintum address more general convexification bounds/thresholds but do not supply this fully classified constrained grid in material inspected.

## value

PASS

A regular simplex is the natural highly symmetric test case for Hausdorff convexification under repeated Minkowski averaging. Exact radius for every dimension and averaging count, the sharp threshold between finite-boundary and saturated lattice behavior, and all worst-case barycentric configurations/counts give a complete motivated exact model. This value is not claimed to be a general contraction theorem or a new large-k lattice radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
