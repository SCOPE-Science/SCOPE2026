---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The exact polynomial map F(x,y)=(r x(1-x+sy), r y(1-y-sx)) has an invariant ray (x,y)=(a z,b z), a=(1+s)/(1+s²), b=(1-s)/(1+s²), on which z follows the logistic map r z(1-z). For 0<s<1, z±=(r+1±sqrt((r-3)(r+1)))/(2r) are the prime-two points for r>3 near the onset. The full 2D return multipliers are nu_parallel=4+2r-r², nu_perp=r²−2r(r+1)/d+4(r+1)/d², d=1+s². Independent exact symbolic Jacobian and two-step determinant computations reproduce both multipliers. The first possible stability/contact thresholds are r_c=1+sqrt(6), r_perp(s)=[1+sqrt((d³+3d+2)/(2-d))]/d, r_clip(s)=(1+s)/(2d)[1+sqrt(1+4d/[s(1-s)])]. The symbolic resultant of transverse -1 and clip conditions factors as (s-1)^4 d^3(s³+s²+s-1)(s³+s²+3s-1); the unique positive roots s1~0.2955977425 and s2~0.5436890127 are transverse/clip exchanges. Comparing with r_c gives s3=sqrt((2sqrt(6)-3)/5)~0.6162758288. The first event on the specified smooth interior two-cycle has ordered intervals transverse (0,s1), contact (s1,s2), transverse (s2,s3), tangent (s3,1); at equality first events tie as stated. Independently evaluated full 2D return Jacobians and sample s=.25,.4,.6,.8 confirm the order, while exact monotonicity and resultant prove the continuum. No post-event attractor or global dynamics claim is made.

## originality

PASS

Best-of-knowledge PASS for exact analytic first-event division into four coupling ranges of the *clipped* antisymmetric equal-r two-site logistic map. Satoh–Aihara 1990 numerically studied exactly the underlying *unclipped* two-species polynomial and attractor phase diagrams, an unusually strong primary antecedent. The journal full text could not be obtained through arXiv/OA and authorized Oxford returned vpn_disconnected; only its abstract/published bibliographic page were read, so exact prior thresholds remain materially uncertain. Al-Kaff et al. 2024 treat related fixed-point bifurcations rather than the specified clipped period-two first-event chart. Best-of-knowledge judgment does not claim the unread Satoh article is definitively not covering.

## value

PASS

Determines a nonmonotone four-region ordering of two distinct instability mechanisms and clipping contact, with exact cubic transition boundaries. The distinction between physical clipped orbit and formal polynomial continuation is mathematically motivated, and the full 2D transverse eigenvalue is essential rather than scalar logistic analysis alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
