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

Deck-transform minimization gives A^2=T^2+(Y-Yprime)^2 and B^2=(2s-T)^2+(Y+Yprime)^2 under a common area-coordinate coupling; cylinder=A and Möbius=min(A,B), with T uniform on [0,s]. The linear (u,v) transform has density 1/(8h^2) on |u|+|v|<=2h, so integration of B<=r<A yields the claimed one-dimensional excess CDF and strict interval s<r<R. Opening t=s-w yields sqrt window coefficient 2sqrt(2)/(3h sqrt(s)); near R the event is the cylinder corner tail R^3/(48h^4s^2) eps^3. Independent Simpson/quadrature at s=1,h=.7 and 2 checked onset scaling trend; strict-shortcut probability follows from product of independent uniform magnitudes and has the stated smoothness break. Formula is for intrinsic flat quotient, not embedded ribbon.

## originality

PASS

Best-of-knowledge PASS for the full strict ordering, integral CDF excess, sharp s-onset and matched-coordinate shortcut phase law. Cylinder marginal F_C and cubic cylinder terminal tail are explicitly prior, not independent novelty; no mathematical domination identified from inspected primary works.

## value

PASS

Pairwise intrinsic distances and stochastic comparison for equal-area/equal-boundary flat surfaces are natural geometry-probability invariants. The strict all-aspect CDF ordering, an exact excess formula, onset exponent 3/2, and a non-C3 aspect-ratio shortcut law are nontrivial motivated global descriptors beyond known cylinder data. The coupling is explicitly defined and not misinterpreted as pointwise comparison of independent draws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
