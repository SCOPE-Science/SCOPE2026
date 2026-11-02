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

Both smooth annular oscillators have ds/dt=−s and on-cycle dθ/dt=1, so share unit-circle trajectory/period 2π and Floquet multiplier e^(−2π). For the second Θ₂=θ+s g_m(θ), direct differentiation yields dΘ₂/dt=1, and its on-cycle phase response is e_θ+g_m e_r. Chebyshev identity gives g_m cosθ=sin((4m−1)θ)+sinθ. Fixed Cartesian kicks (1,0),(0,1) at ratio 1:2 then yield H_m(ψ)=sin((4m−1)ψ)−(1/2)cosψ. Alternating signs at 2k trigonometric test extrema and degree-k zero bound imply exactly 2k simple zeros: k=4m−1 downward and k upward. H_m(0)=−1/2 ensures no simultaneous events; the cited Buescu–Oliveira local full-state impulsive continuation theorem gives k stable and k relative-phase-unstable locked motions for sufficiently small ε depending on m. Effective field (1,0)−0.5cosψ e_θ is within 0.5 of a constant nonzero vector, so winding zero versus tangent winding one, relative winding −1. Independent root/identity checks covered 16 distinct m; finite checks do not replace the all-m construction or cited continuation theorem.

## originality

PASS

The earlier Buescu–Oliveira 2026 paper proves a local continuation theorem at simple phase zeros and a fixed-winding lower bound, which is explicitly used rather than newly claimed. The new construction demonstrates arbitrary high harmonic responses with identical on-cycle geometry, fixed reciprocal Cartesian impulses and a fixed winding of −1; no such explicit family was identified in full available source. Generic arbitrary PRC realization theorems and older multistability literature are residual risks.

## value

PASS

Establishes that a natural integer winding lower bound may be arbitrarily far from actual stable-lock multiplicity even after fixing visible on-cycle geometry, period, Floquet contraction and kick data. This isolates isochron/phase-response freedom and gives a rigorous large-m family, not a single numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
