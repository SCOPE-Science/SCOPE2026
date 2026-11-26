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

At radius one, write the half-edges as (A,At) and (−Bt,B) with t=tan θ. A rotation by 2π/5 modulo the quarter-turn direction convention generates shifts of π/10. For 0≤t≤r/s the four selected facet projections have the signs used in the frozen proof. The strictly positive weights (1,ρ,ρ,1)/2 eliminate the center and give (p+qt)A+(s−rt)B≤2k. AM–GM fixes both half-edge sizes uniquely at equality, and the tight facet normals span the plane, so equality also fixes the center. An independent symbolic check with z=t/s, S=s²=(5+√5)/8 and K=sB verified the weighted coefficients, four contact identities, and exact omitted-facet slack (5−√5)z(1−Sz/r)/(8(p+qsz)(1−rz)), which is nonnegative over the entire closed interval. Therefore the bound is attained, not just an upper envelope; degenerate projection signs at the endpoints do not remove uniqueness. The product-to-sum denominator is minimized only at the two equivalent endpoints and maximized at π/20, giving the claimed area extremes. The θ=0 rectangle has left endpoints (−p,±q), and the other two corners meet the sides incident to the east vertex. The orbit consists of five distinct rectangles, and all other orientations are strictly suboptimal globally. General radius follows by scaling.

## originality

PASS

Pass is for the saturated area-versus-orientation formula, including a feasible optimizer and rigidity at every angle. A later catalogue record has the same analytic bound and the same unrestricted value and equality cases; these are material overlaps and are not separate grounds for this pass. The closest accessible earlier general algorithm establishes computability but not the closed profile or uniqueness. Informal candidate overlap is not a verified unrestricted equality classification.

## value

PASS

The continuous angular dependence measures the loss imposed by an orientation constraint and identifies the least favorable orientation as well as the best ones. The primal and positive dual certificates resolve rigidity rather than assuming a favored symmetry or contact pattern. This is more informative than recomputing the unrestricted extremal area or running a general polygon algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
