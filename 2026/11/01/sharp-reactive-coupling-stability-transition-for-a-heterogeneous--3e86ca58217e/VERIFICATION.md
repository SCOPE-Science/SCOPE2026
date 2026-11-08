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

The displayed triangle u has sum zero, squared radii (49,169,289), and βj−3=|uj|², so z=e^(−3iγt)u solves the full nonlinear system for all real γ. In rotating coordinates, the full 6-real Jacobian blocks are [[1,−γ],[γ,1]]−2δjk UjUjᵀ. Independent symbolic computation reconstructs det(λI−J)=λqγ(λ) with the specified quintic, including linear γ² coefficients and positive qγ(0). Its leading Routh–Hurwitz minors Δ1,Δ2,Δ3 are strictly positive, Δ4=12F(γ²), Δ5=341713944(1+γ²)F(γ²); F has positive derivative for X≥0 and opposite signs at 112,113. Two right-half-plane roots below threshold and zero above follow from Routh signs. At F=0 auxiliary quadratic yields simple imaginary pair with remaining Hurwitz cubic; simple Δ4 zero yields transverse crossing. Directly recomputed numerical root counts near both sides corroborate, not prove, the global spectral claim.

## originality

PASS

The 2026 Zhao–Uchida source already establishes polygonal zero-mean relative equilibria and configuration-dependent sampled transverse stability; the exact reactive threshold, unstable index and transversal simple pair for this particular arithmetic-growth triple are additional claims not found in inspected sections.

## value

PASS

Supplies exact analytic stability boundary for a natural but nontrivial configuration family previously treated numerically; distinguishes spectral instability index, transverse imaginary pair and orbital attraction. Coefficient sizes arise from fixed triangle geometry rather than arbitrary slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
