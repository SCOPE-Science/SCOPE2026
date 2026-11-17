---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Generator on n and n(n-1) yields (d+r)m1=a and (2d+r)m2=2(ell+a)m1, so multiplying by v and sending v→infty at fixed ζ gives Pζ=∫2ell bζ/[(d+r)(2d+r)] d ell and Vζ=ρζ+Pζ. The self-consistency denominator stays bounded away from zero, q(1-x)=O(x^alpha) ensures bζ→1 at endpoint, and r(1-x)~Cx^nu. Singular integrand behaves like 2/[(ζ+Cx^nu)(2ζ+Cx^nu)], integrable iff 2nu<1, at nu=1/2 log coefficient 4/C², and at nu>1/2 scale x=(ζ/C)^(1/nu)y gives 2C^(-1/nu)Jnu ζ^(1/nu-2). Sympy checks moment identities, numerical quadratures Jnu at .6,.7,.8 agree within 3e-9 relative; limits are justified analytically, not by finite tests.

## originality

PASS

Grange directly studies the same local-reset fitness mean-field equations and identifies the first-moment density/condensation boundary at nu=1. Kapodistria–Phung-Duc–Resing cover the pointwise catastrophe moment recurrence. Neither checked material states fitness-integrated second factorial-moment singularity at nu=1/2 and its precise constant; this combines known local moment formulas with new endpoint integration. The full Kapodistria primary was inaccessible (Oxford VPN disconnected), so its comparison remains explicitly limited and does not automatically fail originality.

## value

PASS

Diagonal ordered co-occupation is a natural microscopic crowding observable, distinct from average population density. Its sharp transition at ν=1/2 ahead of known ν=1 density condensation is a structurally and physically motivated classification with universal critical exponents, not a trivial substitution or an unmotivated parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
