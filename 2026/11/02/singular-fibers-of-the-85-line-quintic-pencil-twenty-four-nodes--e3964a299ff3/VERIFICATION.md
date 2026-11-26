---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Reconstructed the projective gradient exhaustion. If x=y=0, the two last derivatives exclude zw≠0 and z=0, leaving only P at t=0. With exactly one of x,y zero, the other derivative forces z=w≠0 and then t=1 and one of the two quartic equations at w/z=1. With xy≠0, z=w=0 is excluded by F_z+F_w=−12x²y². The first two derivatives then require h=(z−w)/(z+w) with h²=−3 and x²=−hy², ruling out zw=0. The mixed quartic terms cancel in F, forcing t=1 at w/z=ρ a primitive cube root. In z=1, F_w gives y⁴=−(1+ρ)/4=ρ²/4, and F_z vanishes with these substitutions. This gives 4+4+8+8 points. Independently evaluated the Hessian: at the two axial families it has determinant 3456. Off-axis, write B=1+ρ; H_xx=24By², H_xy/H_xx=−x/y, and the leading 2×2 block has determinant zero. The full determinant is −H_xx(H_yw+(x/y)H_xw)² with the squared term’s argument 24(1+h)y³. This simplifies to 3456ρ², so all points are nodes. At P the homogeneous leading quartic has no projective gradient zero; blowing up gives smooth strict transform along the exceptional genus-three quartic, with E²=−4 and discrepancy 2−4=−2. The smooth tangent cone gives the ordinary multiplicity-four Milnor number 3³=27. A smooth quintic has Euler number 55, and smoothing increases it by the sum of local Milnor numbers on a complex surface; the claimed values 28 and 31 follow. Homogenizing in the base gives the stated nonreduced fiber at infinity.

## originality

PASS

The contribution is the exact singularity basket and its invariants for the displayed pencil, not the known exceptional affine parameter set, the standard ordinary-point invariant formulas, or the formal compactification of the defining equation. Yu–Zhu leave the singular endpoints out of their derivative argument. The closest distinct indexed result concerns the same ordinary-quadruple-point type on a different surface, not this basket.

## value

PASS

The 85-line quintic pencil is already a motivated family. Classifying its two finite degenerations distinguishes markedly different local and topological behavior (one nonrational exceptional curve versus 24 nodes), giving precise input for degeneration and vanishing-cycle calculations. This value rests on establishing the complete fiber baskets, not on reapplying standard formulas in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
