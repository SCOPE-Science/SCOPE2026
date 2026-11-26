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

At s=1 the cited annual map reduces to the stated G. Its high branch forces p_-=(1-r)v with v=p_+; the other equation is F(v)=0. F decreases strictly on [p_c,1], with F(1)<=r-r(2-r)<0. Thus F(p_c)>=0 is necessary and sufficient, equality means v=p_c, and at a zero the positive outbreak size forces p_-<p_c. Substituting z=r(R-1) gives RF(p_c)=z^2[1/(R-1)-B(z)]. For Z(y)=y/(1-exp(-y))-1, direct differentiation gives Z''>0: the sign numerator reduces to (y-2)exp(y)+y+2, zero with zero first derivative at zero and second derivative y exp(y)>0. The sign of -Z''' reduces to y(cosh y+2)-3 sinh y, with vanishing first three Taylor coefficients and third derivative y sinh y>0. Hence Y''<0<Y''' for the inverse Y, and the integral Taylor remainder B(z)=integral_0^1(1-t)(-Y''(tz))dt is positive and strictly decreasing. The small-z inverse gives B(0+)=2/3; Z(y)=y-1+o(1) gives B(infinity)=0. Since Z(y)<y, B(R-1)<1/(R-1); these strict inequalities give the unique cost threshold when R>5/2 and strict crossings for all positive r when R<=5/2. On the outbreak branch, 1<1/Z'(y)<2; the product of branch slopes is strictly between -(1-r^2) and -r(1-r), so it proves local attraction at strict crossings only. Independent bisection of the original final-size equation, after removing its zero root, gave critical costs 0.256505291445, 0.662371550941, 0.872866377069 for R=3,5,10 and multiplier -0.426408399415 at the stated R=3, r=1/2 cycle. At R=3, r=1/4, F(p_c)<0, and at R=5/2, r=1/10, F(p_c)>0. Replay equivalent bounded checks with node /workspace/review-evidence/4/crossing-check.mjs; these checks do not prove the all-parameter result.

## originality

PASS

The behavioral map, outbreak branch, and numerical observation of alternating immunity are prior. The supported distinct result is the exact if-and-only-if positive-cost crossing criterion in the perfect-efficacy slice, with the universal R=5/2 divide, uniqueness, boundary case, and strict-crossing multiplier bound. Neither the inspected source for the same map nor the closest indexed matches establish that result.

## value

PASS

An observed positive-cost oscillation of a published behavioral map raises a natural exact existence question. The result replaces numerical regimes with a reproducible decision criterion, separates unconditional crossing from a positive cost threshold, distinguishes contact with the nonsmooth boundary from strict crossing, and proves local attraction for the latter. This is useful mathematical information about the model, not a parameter substitution or a single simulated orbit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
