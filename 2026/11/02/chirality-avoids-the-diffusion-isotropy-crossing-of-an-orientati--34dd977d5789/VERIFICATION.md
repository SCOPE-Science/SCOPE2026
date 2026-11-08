---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Angular generator L=d∂θ²+ω∂θ+r(f(0)−f) has invariant moments m_k=r/(r+k²d−ikω); first-harmonic conditional relaxation at rate r+d, rotation ω yields the integrable velocity covariance e^{−(r+d)t}R(ωt)S. Symmetric Green–Kubo with 1/(2t) covariance normalization gives Z=v²(m₂−m₁²)/(r+d−iω). Independent SymPy expansion exactly reproduces the stated rational numerator, denominator and two partial derivatives −16v²/(243d²), −16iv²/(243d²) at r=d/2,ω=0. The imaginary numerator −2dω forces ω=0; the remaining d²−2dr forces r=d/2. Ambient D I is isotropic. Local O(h²+ω²) remainder uses analytic denominator. All positive r,d,v, real ω and D≥0 are covered; zero/reset-limit claims are not made.

## originality

PASS

Statement/implication comparisons against published Resultary and primary literature, with genuine full-text material where accessible: no decisive earlier theorem implying the full assigned final claim was found. The exact overlapping special cases are credited; the listed inaccessible sources remain substantive priority risks, not automatic failures.

## value

PASS

The achiral effective diffusivities coincide at an exact r/d ratio, but a nonzero chiral drift changes this from a simple shift of the crossing to strict avoided degeneracy, with an explicit near-critical eigenvalue splitting and principal-axis rotation. This exact anisotropy criterion is a physically natural spectral observable for orientational-reset transport.

The dated certificate retains the supplied scientific assessment, sources and limitations.
