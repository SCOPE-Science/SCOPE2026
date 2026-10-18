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

For the gamma=0 interior-interpolation Exner–Pekař quantum chain, the original un-divided secular equation has Bloch sin(theta) and cos(theta) coefficients. At 0<t<1 their prefactors outside cos(k l3)-cos(k l2) and sin(k l2)+sin(k l3) cannot vanish. With l2+l3=2pi their simultaneous zero forces sin(pi k)=0, so k=m>=1 integer. Substituting integer m into original displayed P6,P4,P2 gives respectively -72 ell^6(c-1)^2 S, -48 ell^4(c²-1) S, -8 ell²(c+1)² S where S=sin(m l1)sin²(m l3); hence the constant secular coefficient factors exactly -8 m² ell² S [3m² ell²(c-1)+(c+1)]². Its vanishing is precisely edge commensurability or 3m² ell² tan²(pi t/6)=1. Analytic Bloch direct-integral criterion equates positive-measure zero of fibers with point spectrum and conversely. Independently expanded the multivariate polynomial identity via SymPy; numerical checks cannot substitute for the full secular-equation argument. Endpoint t=1 and negative/zero energies are excluded.

## originality

PASS

Exner and Pekař (2024) give the exact general secular coefficients and identify rational edge-length flat bands in their gamma=0 Section 4, but they do not state the full simultaneous-zero classification or interior length-independent resonant factor in inspected full primary PDF. Earlier Baradaran–Exner–Tater works already prove a related preferred-orientation endpoint resonance m ell=1 at t=1, so the discovery of endpoint resonance is prior. The interior 0<t<1 exact tuning law, irrational-edge witness and complete positive point-spectrum criterion remain distinct. Resultary high-energy Kirchhoff boundary-layer result analyzes bands, not a fixed resonance point eigenvalue.

## value

PASS

A complete positive flat-band classification in a natural interpolation family distinguishes geometric commensurability from coupling-induced point-spectrum localization; it includes explicitly incommensurate-length flat bands and an exact tuning law. This is a nontrivial spectral phenomenon motivated by the original ring-chain model, not just an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
