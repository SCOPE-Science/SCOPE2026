---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The half-gap Dirichlet simplex of 3 independent arclength-uniform circle points is uniform at density 2/pi^2, or 12/pi^2 in the ordered sixth. Caliper width equals the minimum altitude, 2 sin(beta) sin(gamma) for the two smaller ordered half-gaps; slice integration yields the stated exact CDF. Direct integration gives E W=5/pi^2 and E W^2=1-47/(8 pi^2). The small-t boundary-layer integral yields 3t[log(8/t)+1]/pi^2+o(t), whereas the unique equilateral maximum and its ordered tangent wedge give P(W>3/2-epsilon)~12 epsilon^2/pi^2. Independent checks: Independently rederived the half-gap chamber and implemented 2D numerical quadrature of k=0,1,2 moment integrals, yielding 1.0, 0.5066059182116889, and 0.40473804610126557; 200000 independently generated Cartesian Euclidean triangles gave first moment 0.5064642067220751 and second moment 0.404172202145847. Checked the stated verifier source verify_inscribed_triangle_width.py (Git blob 66a39f310269ba95110ff7e43ca7459ea92b0fb2) by reading it, not treating its claimed success as proof. Endpoint laws rest on the local analytical rescaling, not simulation.

## originality

PASS

Koroleva–Nikitin arXiv:1301.1360v1 studies the identical circle-point sampling model, but the inspected full-paper theorem statements and sections 2.1–2.2 give U-maximum perimeter and area extreme-value laws over large samples, not the fixed-three-point minimum-caliper-width distribution, moments, or tails. Residual limits explicitly listed in originality.residual_risks.

## value

PASS

A full probability distribution and two endpoint regimes for a canonical intrinsic size statistic of a random inscribed triangle; the logarithmic thin limit and quadratic near-equilateral limit quantify distinct degeneracies that are not reducible to area or perimeter moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
