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

PASS: In the stated four-orientation quarter-turn harmonic model, the published stationary rotated coordinates U,V are independent with density (1-z²)^{β-1}/B(1/2,β) on (-1,1). Then S=ρ²=U²+V² is the sum of independent Beta(1/2,β) variables; p(ρ)=2ρ g(ρ²), so the radial Jacobian is correct. Direct beta convolution for 1<s<2 with t=2-s gives p(sqrt(2-t))=4 B(β,β)t^{2β-1} Hβ(t/(2-t))/[B(1/2,β)^2 sqrt(2-t)], Hβ(w)=2F1(1/2,1/2;β+1/2;w²). Its positive-power-series tilted mean Q=wH'/H has dQ/dlog w=Var(2n)>0. Thus eta=t dlog p/dt=2β-1+t/[2(2-t)]+2Q/(2-t) strictly increases; it starts negative iff β<1/2 and diverges at t->1 for β<1/2, giving one outer valley and two integrable shell peaks. For β>=1/2 eta>0, hence monotone radial decrease for 1<ρ<sqrt2; for β<=1 inner radial density is strictly increasing. Independent scipy evaluations at β=.25,.4,.49,.5,.75,1.3 confirm monotone eta and β=.25 valley t=0.6353250926701738; they are corroboration of the analytic argument. At β=.5 logarithmic singularity at ρ=1 and outer limit 2sqrt2/pi; near threshold tβ=4(1-2β)+O((1-2β)^2). Precise β>1 inner mode classification is not claimed.

## originality

PASS

Smith et al (2022) already derive the exact two-dimensional stationary product-beta law and its angular/planar features; those are not new. The independently audited additional statement is a sharp radial *two-shell* phase classification with uniqueness of the separating minimum. The 2026 isotropic-redraw paper has a different orientation law and circular rather than square support. Best-of-knowledge PASS on the radial classification, with possible broader analytic-hypergeometric prior coverage.

## value

PASS

PASS: Two distinct integrable radial concentration shells separated by exactly one minimum mark a sharp morphology change in an established physically motivated square-supported stationary model. The analytic critical beta=1/2 boundary and rigorous uniqueness, not merely computing an already-known marginal, give a natural useful structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
