---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The claim is correct for rho,g>0, 0<k1<k2, h,D>0, massless unstressed homogeneous elastic plate. From U=(1+b)tanh(t), fixed U gives b=U*coth(t)-1 with exact domain (0,arctanh U) if U<1 and (0,infinity) if U>=1. The reduced V map G_U(t)=(1+q^4 b(t))*tanh(qt) has the exact derivative 2q^4*tanh(qt)*[(1+q^4*b)/(q^3*sinh(2*q*t))-(1+b)/sinh(2*t)]<0 using sinh(2qt)>q*sinh(2t) and 1+q^4*b<q^4*(1+b), for every q>1 and b>0. As t down to zero G->q^5 U; at the other end G->tanh(q*atanh U) for U<1 or 1+q^4*(U-1) for U>=1; endpoints excluded. IVT and strict decrease give necessity, sufficiency and unique recovered (h,D). The forward Jacobian is positive via -tanh(t)*G′(t). All quantifiers and strict boundaries including U=1 have been checked. An independent high-precision test of 120 sample triples corroborated the algebra and numerical reconstruction; it is not used as an infinite proof.

## originality

PASS

Best-of-knowledge originality is accepted for the exact noise-free global bijection and sharp two-frequency realizability interval, not for the classical flexural-gravity forward dispersion law. Direct comparisons with accessible original manuscripts show that previously established forward laws, pressure-sensor inversions, field-wave inversions, and bottom-pressure reconstructions use different observables or do not establish this necessary-and-sufficient two-mode data image. The scalar derivative calculation is elementary once formulated, so unlocated specialized inverse literature remains a priority risk; negative search results do not certify novelty.

## value

PASS

Depth h and plate rigidity D are distinct natural unknown physical coefficients in an established flexural-gravity dispersion relation; two independent wavenumber-frequency observations are the minimal nontrivial joint identification design. Beyond the known forward formula, the theorem provides the entire attainable measurement region for every q>1, a sharp if-and-only-if feasibility test, a globally unique scalar reconstruction and the correct weak-conditioning caveats. This exact invariant of the two-observation inverse map can be used to rule out inconsistent ideal-model data or ambiguity without arbitrary fitting. The result is modest in scope (elementary hyperbolic inequalities, no noisy inverse theory) but a meaningful complete natural classification, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
