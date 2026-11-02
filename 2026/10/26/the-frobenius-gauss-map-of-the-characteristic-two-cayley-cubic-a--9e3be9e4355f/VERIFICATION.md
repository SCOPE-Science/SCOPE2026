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

Checked original scheme/field hypotheses, reduced dual, rational rather than global morphism and degree convention. Direct characteristic-two coordinate transform gives F=UVT+W²(U+V+T); Euler polar relation makes o a strange smooth point. On U=1 w²=yz/(1+y+z), nonsquare by prime y=0 valuation. Polar cubics G=(VT(V+T),UT(U+T),UV(U+V)) have exactly seven simple F2-plane basepoints and span cubic equations vanishing at them, confirmed independently by GF2 evaluation rank7. Source rational identities z²=r(r+1)/t(t+1), y²=r(r+t)/(1+t), w²=r/(1+t) force degree2 each stage and k(X)²=k(r,t), since [k(X):k(X)²]=4 by p-basis over perfect k. Independent symbolic checker confirmed coordinate identity and linear-system rank; proof handles infinite-function-field conclusions, and direct valuations are essential. Blowup anticanonical class 3H−ΣE_i has degree2; no assertion of del Pezzo general position.

## originality

PASS

Bounded best-of-knowledge prior-work comparison: None of the inspected primary statements logically dominates the all-map theorem, though a differently named older strange-surface result could.

## value

PASS

The drastic degeneration of the Cayley cubic dual from classical Steiner quartic to a plane in characteristic two, plus exact Frobenius Gauss extension and seven-point net factorization, is a motivated geometric classification of a canonical singular surface. The inseparability degree and factorization explain dual degeneration, beyond a trivial coordinate substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
