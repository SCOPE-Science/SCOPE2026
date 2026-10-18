---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

PASS: From the exact printed nonlinear profile equation substitute v=1-phi, giving the upstream linearized Q(lambda)=tau*c*lambda^3-D*lambda^2-c*lambda+1. The cited minimal speed is the unique positive y=c²/D root of F_-(y)=4r y²+(1-18r-27r²)y-4, r=tau/D>1. Independently expanded cubic discriminants (sympy) to check disc(Q)=D³[F_-(y)+36r*y+8]>0 for y>=y*. Vieta and Q(-infinity)<0<Q(0) imply one negative/two positive distinct roots. F_-(1/r)=5/r-22-27r<0 implies c>D/sqrt(tau); Q(1/sqrt(tau))=1-D/tau>0 and Q'(1/sqrt(tau))=2(c-D/sqrt(tau))>0 place both positive roots below the Bessel Laplace radius. Each e^{lambda_j xi} solves both ODE and convolution using Φ(lambda)=1/(1-tau*lambda²) and meets the exact positivity, normalization, monotonicity, convexity and left decay imposed on the source limiting solution. The primary arXiv full text §6 lines 958-1006 explicitly states that no such limiting solution exists, so that specific proof step is falsified. This does not disprove existence of nonlinear oscillatory profiles by another route.

## originality

PASS

PASS, best of knowledge: Direct Section 6 of the *identical* Cao-Chen-Jin-Yin arXiv:2609.34368v1 concludes the opposite, hence cannot cover the correct two-exponent counterexample. Their Section 3 analyzes the downstream polynomial with constant -1 and minimal speed; upstream constant +1 is a different spatial problem. Wang-Bai-Cao 2014 works in small-viscosity stability and does not give these tau>D roots or source-specific logical correction. Resultary same-source self-hit is not a separate prior publication.

## value

PASS

PASS: A rigorously exhibited positive convex solution to the exact limiting system corrects a central analytical impossibility claim used to justify asymptotic traveling-wave oscillations; the complete admissible-speed root ordering is structurally useful in stability and tail analysis. Value does not rest on claiming to refute the full nonlinear theorem or explain finite overshoot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
