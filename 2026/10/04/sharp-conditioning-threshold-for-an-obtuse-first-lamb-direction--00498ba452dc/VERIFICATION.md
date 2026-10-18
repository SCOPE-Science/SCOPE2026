---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

At first bias-corrected step from zero moments, mhat=g and vhat=g^2 for any beta1,beta2 in (0,1), so r_i=g_i/(|g_i|+epsilon). LAMB scales -r by a positive factor; x^+ norm squared difference is -2a x.r+a^2||r||^2. The SPD turn-angle bound cos(angle(x,Hx))>=2 sqrt(kappa)/(kappa+1) follows by endpoint chord lambda^2<=(kappa+1)lambda-kappa and optimization of mean. In 2D, if x.g>0 but x.Teps(g)<=0 then angle(x,g)>pi/4: reflect x to quadrant I and examine the compression of a mixed-sign g's coordinate ratio toward one. Therefore kappa<=3+2sqrt2 ensures x.r>0 for every epsilon>0. For larger kappa the rotated two-eigenvalue maximizer makes x1>x2>0 and g1<0<g2 so x.sign(g)<0; scaling Hessian with fixed kappa makes r tend to sign(g). Independently checked rotated numerical witnesses above threshold and positivity of x.g, plus the explicit rational H,x example. This controls Euclidean distance, NOT objective descent; g.r always positive.

## originality

PASS

You et al. Algorithm 2 provides precisely the first-step Adam normalization and layerwise trust ratio but proves general stationary-point performance, not the sharp two-dimensional SPD turning threshold. Fong et al. clip magnitude to address extreme trust ratios, which cannot fix the sign of x.r. An older Polyak threshold numerically shares 3+2sqrt2 but derives an unrelated step-size objective bound, not an implication of this coordinatewise LAMB angle result.

## value

PASS

Identifies a motivated limitation of positive trust-ratio rescaling: no step magnitude can repair an obtuse first-step direction as measured by Euclidean distance. The exact spectral conditioning threshold separates safe and unsafe orientations, making it a structural optimizer-boundary result; caveat objective descent remains possible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
