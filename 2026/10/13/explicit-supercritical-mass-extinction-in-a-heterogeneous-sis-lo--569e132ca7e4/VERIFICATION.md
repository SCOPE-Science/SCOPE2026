---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: On (0,1) with Neumann infected flux, β=1−(3/4)cosπx and f=S0−r=1/4+cosπx, V=β f has coefficients (1/4,13/16,−3/4) in c and integral −1/8. For u=m+v, ∫v=0, Neumann π²>9, ∥V∥∞≤2 and 4|m|∥v∥≤m²/16+64∥v∥² prove Rayleigh ≤−∥u∥²/16 for all H¹, hence σ(10,V)≤−1/16. The explicit ℓ=(199+c)/200∈[.99,1], ∥βℓ f−V∥∞≤1/50 yields σ≤−17/400 and trial mass exactly 9/4+1/800. For ψ the positive unit-sup eigenfunction of 10d²+V+β/100, eigenvalue ≤−9/200<−1/25. Exact susceptible identity S−r=f exp(−β∫I) and comparison give I≤10^{-4}exp(−t/25); induced ∥S−S0∥∞≤7/1280<1/100 closes strict first-exit bootstrap. Thus conserved N∈(9/4,9/4+10^{-4}]⊂(max{∫S0,∫r},Nstar), with uniform extinction. Exact independent checker verified all rational margins, but the infinite-dimensional proof uses Poincare, spectral and parabolic comparison.

## originality

PASS

PASS: Salako–Wu explicitly ask in Remark 3.6 whether extinction can occur at total N between max{∫S0,∫r} and their threshold Nstar; their theorem permits but does not realize it. The identified source Corollary 3.5 assumes constant β or fixed-sign risk, both false here. Castellano–Salako analyze equilibria with positive susceptible movement, not the displayed initial-value extinction at zero movement. This is a constructive answer to a published model-specific gap, not a new statement about all masses.

## value

PASS

PASS: An explicit smooth positive-data solution with heterogeneity exhibits a qualitatively counterintuitive supercritical-mass extinction inside a posed open window; all strict spectral/mass margins are analytic and therefore usable by future modeling work. It is a meaningful motivated counterexample, not a trivial zero-infection initial condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
