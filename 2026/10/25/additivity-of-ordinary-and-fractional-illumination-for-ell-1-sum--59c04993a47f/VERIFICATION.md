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

# Verification of the free-sum illumination formulas

The claim is an all-dimensional deductive theorem; no standalone numerical certificate is needed. Independent scientific audit has not been performed.

## Critical proof checks

1. For every boundary pure-block point \(\iota_jy\), write the sum norm along any direction as \(\|y+tv_j\|_j+t\sum_{k\ne j}\|v_k\|_k\). Since the norm is convex and \(\|y+tv_j\|_j\ge1-t\|v_j\|_j\), actual illumination implies the strict dominance inequality \(\|v_j\|_j>\sum_{k\ne j}\|v_k\|_k\). Equality cannot illuminate because the right derivative is not negative.
2. Distinct dominant cones cannot intersect, since both would demand a distinct block norm larger than half of the same nonnegative total. Projection of every direction illuminating an embedded boundary point illuminates the corresponding factor, preserving weighted constraints. Thus ordinary direction counts and fractional total masses each sum.
3. For any boundary point with a nonzero coordinate \(x_j\), a factorwise inward direction for the normalized block point \(x_j/\|x_j\|_j\) decreases the original \(\ell_1\) norm without changing other blocks. Union (respectively, summed weighted union) of block coverings gives the matching upper bounds.
4. For Euclidean factors, every fixed direction illuminates half the spherical boundary. Uniform spherical measure of mass two gives equality; the finite-measure definition is matched by discretizing a strict cap with a positive gap and rescaling, so no unproved limiting interchange is needed.

## Boundary cases and normalization

The proof includes \(r=1\), one-dimensional real factors, and any finite mixture of factor dimensions. Positive direction rescaling does not change illumination. For \(r=2\) with one-dimensional real factors, the free sum is the planar diamond with ordinary and fractional values four; for two real two-dimensional Euclidean factors, values are six and four. The complex \(\ell_1\)-ball identification is as a real \(2r\)-dimensional convex body, with ordinary and fractional illumination based on all real directions; no holomorphic restriction is inserted.

## Limits and reproducibility

Nothing in the proof claims an analogous statement for non-centrally-symmetric gauges or \(\ell_p\)-sums with \(p>1\). Historical priority, especially versus the inaccessible 2025 direct-sum covering article, remains uncertain. Every displayed identity can be reconstructed from the five proof steps without external computations or numerical heuristics.
