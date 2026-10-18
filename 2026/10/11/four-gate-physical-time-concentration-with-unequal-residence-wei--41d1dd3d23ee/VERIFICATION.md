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

For λ,ω>0, κ>|η|+ω/2, ε>0, differentiated the given cubic equations in polar coordinates: rdot=r(λ−F r²), θdot=r²g, F=κ+η cos2θ+(ω/2)sin4θ is strictly positive, g=ε+ω sin²2θ>0. The radial-square angular equation du/dθ=2(λ−Fu)/g is linear with contracting affine return, yielding a unique positive attracting closed graph. Integrating dlog r around it proves λT=∫F/g and the η cos2θ and sin4θ integrals cancel exactly, yielding T=2πκ/[λ√(ε(ε+ω))]. Near each θ_j=jπ/2, angular damping ∫2F/g diverges as ε→0, forcing u(θ_j+v√(ε/(4ω)))→λ/(κ+(-1)^jη) uniformly for bounded v; g/ε→1+v². Original-time density dθ/[Tug] therefore approaches F_j/[4πκ(1+v²)]dv. Uniform u≥λ/M and g≥ε+c distance² imply O(1/R) tails beyond R√ε windows and ensure full weak convergence, weights F_j/(4κ), and standard conditional Cauchy. This is an infinite ε→0 argument rather than finite sampling.

## originality

PASS

PASS best of knowledge: the original 2024 star-node classification proves qualitative attracting invariant circle, and a separate Resultary theorem establishes the general exact period/Floquet identity (including an anisotropy-independent example with constant angular drift). Neither source supplies the four near-stalled angular gates g_ε=ε+ω sin²2θ, unequal occupation weights (κ±η)/(4κ), nor the joint standard-Cauchy microscopic law. The period identity by itself is prior/method-level, not independently claimed new.

## value

PASS

PASS: transition toward a four-equilibrium polycycle makes residence distribution a mathematically natural dynamical invariant distinct from global period. The exact four unequal weights and universal local Cauchy scale demonstrate physically meaningful time redistribution hidden by an anisotropy-independent period, a motivated parameter-specific boundary layer, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
