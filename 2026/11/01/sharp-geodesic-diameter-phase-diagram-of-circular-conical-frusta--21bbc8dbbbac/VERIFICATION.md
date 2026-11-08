---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: The lateral frustum intrinsic metric dr²+(r sin gamma)² dtheta² develops to an annular Euclidean polar strip with angle period 2phi=2pi sin gamma, where half-period phi<pi. The shortest between radii r,s and shorter developed separation delta<=phi is a straight chord when delta<=acos(b/r)+acos(b/s), otherwise the sum of two tangents and the inner-circle arc. Shorter winding is optimal by contracting angular speed while fixing the radial path. Distance strictly increases with delta>0, and for fixed other endpoint it is a globally convex function of each radius: chord branch has second derivative s² sin²(delta)/distance³, tangent branch has positive b²/(r²sqrt(r²-b²)), with matching first derivatives at contact. Therefore diametral radii lie at corners (B,b) or (B,B); (b,b) is smaller. Comparing their exact values gives mixed-rim chord only if phi<pi/3 and q<2cos phi-1; outer-to-outer chord if otherwise q<=cos(phi/2); and outer rim tangents+inner arc for q>cos(phi/2). The two transition regularities follow by differentiating these branches. Independent 18,225 radial-grid pairs at several rational-angle numerical samples did not violate the derived corner bound. Finite checks corroborate the analytic convexity argument.

## originality

PASS

PASS, qualified: Local cone developability and shortest geodesics are classical and explicitly credited. Chen 2017 primary six-page cone geodesic paper treats rectifying curves and untruncated cones, not the intrinsic diameter of the lateral frustum with forbidden inner disk. No inspected matching prior formula or dominating exact two-parameter diameter classification was found, but older elementary annulus-obstacle geometry may imply it and searches are not proof of priority.

## value

PASS

PASS: The intrinsic diameter of a naturally parametrized compact surface with boundary is a meaningful exact geometric invariant. The formula classifies diametral boundary-pair geometry and distinguishes a strict endpoint-switch corner from a twice-derivative failure at the geodesic tangency threshold. Though derivable with classical planar tools, the global optimization and sharp phase boundaries are substantive, not just renaming a known local geodesic formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
