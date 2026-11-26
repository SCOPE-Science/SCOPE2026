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

The coexistence equilibrium in original time has Hopf Jacobian [[0,−d_H],[h,0]] and frequency ω=√(h d_H); differentiation along the equilibrium gives d(tr J)/dd=−(1−h)(1+h)/(2h). I independently checked the period coefficient using a polar expansion instead of the complex normal-form computation. In coordinates u=x−x_H, v=d_H(y−y_H)/ω, write the quadratic terms as (A u²+Buv, C u²+Euv) and cubic terms as (F u³+Gu²v, H u³+Iu²v). With L=1+h and d=d_H, direct Taylor expansion gives (A,B,C,E)=(−d,−4hω/(L²d),−2ω/L,4h/L²) and (F,G,H,I)=(−4h/L²,8hω/(L³d),4ω/L²,−8h/L³). For c=cos θ,s=sin θ, the first angular correction is Cc³+(E−A)c²s−Bcs²; the second-order radius correction is the antiderivative of [Ac³+(B+C)c²s+Ecs²]/ω. Averaging reciprocal angular speed with this radius correction gives the coefficient [10C²+(E−A)²+B²−BC−3A(E−A)]/(24ω²)−(3H−G)/(8ω), which simplifies to the stated rational C(h). The radial cubic averaged in the absence of time rescaling is (3F+I)/8−(2AC−AB+EC)/(8ω)=−1/(2L), confirming transversality leads to the local stable branch for d<d_H. In a smooth off-Hopf eigenbasis the trace shift is O(r²) on the branch and affects the radial equation first at cubic order, while the constant angular term is exactly ω_lin(d,h); the leading polar radius agrees with the prey harmonic to first order. Thus this computes a least-period correction relative to the same-d focus rather than the frozen Hopf frequency. The numerator of C(h) is positive by the indicated grouping and its endpoint limits diverge. Direct differentiation gives the displayed P and negative sign of its denominator on (0,1); the positive-half-line substitution has coefficients with one sign change and P(0)=1, P(1)=−32, so there is exactly one global minimizer. Independent bisection gave h=0.37246273719082396 and C=1.2232816447053083. CHECK.py and NUMERIC_CHECK.py were inspected, not executed; their recorded finite checks are not the proof.

## originality

PASS

Credit the normalized physical-time coefficient relative to the same-d linear frequency and its unique sharp model-specific minimum, not the known predator–prey model, existence of a supercritical Hopf cycle, or normal-form method. The decisive prior accessible normal-form calculation uses a different clock and reports stability, not this frequency observable. The original period equation's scope remains unresolved and is not treated as negative evidence.

## value

PASS

Using the physical-time prey harmonic and the equilibrium's changing linear frequency separates nonlinear slowing from the parameter-driven frequency shift. These are observables a researcher can directly estimate near a supercritical Hopf cycle. The exact positive rational coefficient and its unique least-sensitive parameter value provide a quantitative benchmark for this canonical model, rather than merely repeating Hopf stability or claiming global period monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
