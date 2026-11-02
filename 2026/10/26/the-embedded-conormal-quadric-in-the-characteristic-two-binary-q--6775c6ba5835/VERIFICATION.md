---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Determinant of the explicit 4x4 Sylvester matrix gives R=(af+cd)^2+(ae+bd)(bf+ce) over F2. Differentiating in six coordinates yields (eU,eV,eW,bU,bV,bW), with R already in this ideal, and U,W in (b,e), so J=I^2+(b,e)I. Segre minors prime; I^2⊂J⊂I proves radical I; a=1 coordinate change gives local V^2+bUV+cU^2 and ideal (U,V)∩(b,U,V)^2. Globally I/J=(I/I^2)|_T, rank-two conormal of P1xP2 restricted to P1xline, whose splitting has bidegrees (-2,-2),(-2,-1). Independently computed modular resultant and derivatives, full symbolic Groebner basis (7 elements), Hilbert coefficients [1,6,21,50,96,162,251,366] for degrees 0..7 matching given rational series. The geometric interpretation follows from the separately checked Segre normal geometry, not solely from code.

## originality

PASS

The discriminantal/residual conormal issue is specific to characteristic two. Choudary’s 1990 resultant hypersurface study and D’Andrea–Chipalkatti 2007 Jacobian-ideal theorem concern characteristic zero; the latter explicitly states all results hold over fields of characteristic zero and treats an F-Jacobian ideal, not the full modular Jacobian thickening. No covering char-2 conormal splitting or Hilbert-series statement was identified in targeted Resultary/published literature; possible older modular invariant work remains a priority risk.

## value

PASS

The singular scheme of an elementary universal resultant is not merely its classical Segre rank-drop support: its square-zero conormal embedded component is a genuine scheme-theoretic invariant in small characteristic. The exact sheaf, supporting quadric, and Hilbert series are structurally meaningful tools for studying modular discriminantal geometry, not a cheap Jacobian vanishing check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
