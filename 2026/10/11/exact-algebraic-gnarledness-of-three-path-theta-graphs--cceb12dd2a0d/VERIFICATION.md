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

The proof was checked symbolically at each reduction:

1. A degree-one chain extension on a theta graph is determined by three path sums whose pairwise differences are the two integral cycle generators.
2. For a fixed cointegral basis, the optimum equals a weighted \(\ell^1_2\) one-center radius. The map \((r,s)\mapsto(r+s,r-s)\) converts this exactly to intersection of axis-aligned \(\ell^\infty\) boxes, so pairwise distance bounds are sufficient as well as necessary.
3. Cointegral bases correspond to independent integer coordinate columns for the integral homology generators. Each of \(u\), \(v\), and \(u-v\) is nonzero, and they cannot all have \(\ell^1\)-norm one.
4. The three possible locations of the necessary norm-two vector are realized by explicit unimodular coordinate pairs. Sorted path lengths make the placement on the denominator \(b+c\) optimal.

The standalone script `verify_theta.py` uses exact rational arithmetic. It checks every sorted triple \(1\le a\le b\le c\le12\), every independent integer coordinate pair in \([-2,2]^2\), the box-feasibility form of the weighted center problem, all three witness placements, and representative points on both sides of the phase transition. Its finite range is a reproducibility check, not a proof of the universal statement.

Scientific limits: no claim is made for arbitrary rank-two graphs, higher-degree gnarledness, or algorithmic complexity. Independent audit has not been performed.
