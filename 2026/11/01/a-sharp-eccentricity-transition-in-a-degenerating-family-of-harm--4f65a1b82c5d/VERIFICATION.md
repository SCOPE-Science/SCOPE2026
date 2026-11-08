---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The boundary argument derivative equals 1+P_a-P_b, with cleared numerator 4ab x^2-4b(ab+1)x+a^2 b^2-a^2+3b^2+1, strictly concave on [-1,1]. Its endpoint factorizations give positive orientation for a=-1+epsilon,b=k epsilon (0<k<1/4) and small epsilon; degree one and Radó-Kneser-Choquet give the harmonic disk diffeomorphism. The real-affine normalization has Delta=c_1^2-c_{-1}^2>0, yields h'(0)=1 and g'(0)=0 and an ellipse of asymptotic axis ratio (1-k)^(-1). Geometric Fourier tails converge locally with derivatives to F_d=z+(1+d)^2z^2/(1-z)+overline(d^2z^2/(1-z)), d=k/[2(1-k)]. Independently expanded the boundary limiting Jacobian as a polynomial in y^2 with strictly positive nonconstant coefficients; its constant (6d-1)(6d^2+6d-1)/16 stays nonnegative through d_c=(sqrt(15)-3)/6. The analytic derivative stays zero-free for d<=d_c; maximum modulus of g'/h' yields strict interior J>0, including the boundary critical case. For d>d_c the real-axis J=[1-Ct][1-(1+2d)t] has a negative interval. Exact Fraction substitution independently gives the finite k=23/100,epsilon=1/100,x=-99/100 witness p'=0.015438327897...,q'=-0.016697718785..., axis ratio 6030299371723/4647100628277. Finite arithmetic corroborates, but does not prove, the continuum argument.

## originality

PASS

The inspected original Wang-Zhong abstract states a fixed bounded-ellipse self-convolution counterexample, not a degeneration-wide precise Jacobian threshold. Read the complete directly relevant published fixed-a Resultary/SCOPE finding e20d7884e72b: it keeps a=-10/11 and classifies Jacobian at the fixed point x=-99/100 as b varies; it does not imply the simultaneous singular ray a->-1,b/(1+a)->k. Distinct complex-linear disk normalizations do not preserve g'(0)=0. The new parameter-dependent limiting Jacobian phase boundary and bounded ellipses approaching sqrt(5/3) survive best-of-knowledge comparisons. The 12-page Wang-Zhong PDF was inaccessible despite arXiv and lawful OA attempts; authorized institutional download returned VPN disconnected, a material priority risk rather than a scientific failure.

## value

PASS

A natural two-scale degeneration of the known convex-ellipse counterexample family yields a genuine sharp geometric transition and bounded counterexamples with axis ratio below 1.3. The classification connects the image eccentricity with exact Jacobian sign and a critical boundary-contact mode; it does not falsely claim a universal optimum among all harmonic maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
